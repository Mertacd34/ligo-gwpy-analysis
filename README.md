# LIGO GWPy Analysis

## Overview

This repository holds a collection of Python-based analyses of gravitational-wave data from the LIGO detectors. It uses publicly available open data and the [GWPy](https://gwpy.github.io/) library.

The project highlights standard methods used in gravitational-wave data analysis. This includes time-domain visualization, noise whitening, filtering, and time-frequency methods like the Q-transform. The repository is meant to be expanded with new events and analysis methods over time.

---

## Current Content

### GW151226, Binary Black Hole Merger

The initial analysis reproduces key features of the LIGO binary black hole event **GW151226**, seen by the Hanford (H1) and Livingston (L1) detectors.

For this event, the analysis includes:

* Retrieval of open LIGO strain data (GWOSC)
* Whitening and bandpass/notch filtering
* Time-domain strain comparison (raw vs. whitened)
* Q-transform spectrograms that highlight the chirp signal

Results align with publicly released LIGO visualizations.

---

## Methods

* **Data source:** LIGO Open Science Center (GWOSC)
* **Tools:** Python, GWPy, NumPy, Matplotlib
* **Signal processing:**

  * Noise whitening
  * Bandpass filtering (BBH frequency band)
  * Power-line notch filtering
* **Visualization:**

  * Time-domain strain plots
  * Time-frequency Q-transform spectrograms

---

## Repository Structure

```
ligo-gwpy-analysis/
├── gw151226/
│   ├── GW151226.py
│   ├── figures/
│   └── README.md
├── requirements.txt
└── README.md
```

More events and analysis modules will be added in future updates.

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the analysis

```bash
python gw151226/GW151226.py
```

Generated figures will be found in the `figures/` directory.

---

## Future Extensions

Planned extensions include:

* Analysis of more LIGO/Virgo events
* Noise and PSD studies
* Signal-to-noise ratio (SNR) estimation
* Introduction to matched filtering techniques

---

## Author

**Mert Acar**

---

## References

* LIGO Open Science Center (GWOSC)
* GWPy documentation: [https://gwpy.github.io/](https://gwpy.github.io/)