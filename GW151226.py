"""
GW151226 analysis using GWPy.

This script:
- Fetches open LIGO strain data for H1 and L1
- Applies whitening, bandpass, and notch filtering
- Visualizes raw vs whitened strain around the event
- Computes Q-transform spectrograms to highlight the chirp signal

Author: Mert ACAR
"""

from gwpy.timeseries import TimeSeries  
from gwosc.datasets import event_gps
from gwpy.signal import filter_design
from gwpy.plot import Plot
from gwpy.plot import colors

gps = event_gps("GW151226")
start = int(gps) -16
end = int(gps) +16
detectors = ["H1","L1"]
ifo_color_map = {"H1": colors.GWPY_COLORS["ligo-hanford"],"L1": colors.GWPY_COLORS["ligo-livingston"]}
sample_rate = TimeSeries.fetch_open_data("H1",gps,gps+1,cache=True).sample_rate

# Design bandpass and notch filters for BBH signal band

bp = filter_design.bandpass(40,500,sample_rate)
notchfs = [60,120,180]    
notches = [filter_design.notch(f,sample_rate) for f in notchfs]
zpk = filter_design.concatenate_zpks(bp,*notches)

data = {}

for ifo in detectors:
    raw = TimeSeries.fetch_open_data(ifo,start,end,cache = True)
    # Whiten the data and apply zero-phase filtering
    # (Whitening is used for noise normalization, not visualization)
    filt = raw.whiten(fftlength = 4).filter(zpk,filtfilt = True)
    # Crop edges to remove filter and whitening transients
    raw_cropped = raw.crop(*raw.span.contract(1))
    filt_cropped = filt.crop(*filt.span.contract(1))

    data[ifo] = {"raw" : raw_cropped, "filt": filt_cropped, "color": ifo_color_map[ifo]}

for ifo in data:
    fig = Plot(data[ifo]['raw'],data[ifo]['filt'],figsize =[12,6],separate = True ,sharex = True, color = data[ifo]["color"])
    ax1,ax2 = fig.axes
    ax1.set_title(f"LIGO-{ifo} Strain Data around GW151226")
    ax1.set_ylabel("Raw Amplitude")
    ax2.set_ylabel("Whitened Amplitude")
    ax2.set_ylim(-10,10)
    ax1.set_xlim(gps-1.0,gps +0.2)
    ax2.set_xlim(gps-1.0 , gps+0.2)
    ax2.set_xscale("seconds",epoch = int(gps))
    fig.show()
    # Compute Q-transform on band-limited (not whitened) data
    # for time-frequency visualization of the GW signal
    ts = data[ifo]["raw"].bandpass(30,500)
    q = ts.q_transform(outseg=(int(gps)+0.3 , int(gps)+0.9),frange=(30,1000),qrange=(8,64))
    plot = q.plot(figsize=[10, 5])
    ax = plot.gca()
    ax.set_title(f"LIGO-{ifo} Strain")
    ax.set_xscale('seconds', epoch=int(gps))
    ax.set_xlim(int(gps) +0.3, int(gps)+0.9)
    ax.set_yscale('log')
    ax.set_ylabel('Frequency [Hz]')
    ax.colorbar(label='Normalized Energy')
    plot.show()