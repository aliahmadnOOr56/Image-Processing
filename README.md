# Image-Processing
# Automated Rice Grain Phenotyping & Dataset Pipeline

An automated computer vision and data engineering pipeline developed in Python to segment, extract, normalize, and extract morphological features from macro-level agricultural imagery without relying on OpenCV abstractions.

---

## Overview

In computer vision and agricultural data analytics, training high-precision classification models requires standardized, noise-free, and calibrated datasets. This project automates the transition from raw batch photography to structured granular datasets and engineered tabular features ready for downstream machine learning tasks.

### Key Capabilities
- **Non-OpenCV Implementation:** Engineered using pure `scikit-image`, `numpy`, and mathematical image processing fundamentals.
- **Adaptive Segmentation & Morphological Operations:** Cleans noise, handles non-uniform illumination, and removes border artefacts.
- **Orientation Normalization:** Automatically identifies grain major axes and applies geometric alignment for uniform vertical cropping.
- **Feature Extraction & Metadata Generation:** Automatically measures height, width, aspect ratio, orientation, and mean color metrics per instance, serializing the results into `metadata.csv`.
- **High-Throughput Processing:** Scaled from raw inputs to generate over 3,000+ segmented individual grain instances.

---

## Pipeline Architecture

The pipeline processes raw input images through the following consecutive stages:

1. **Preprocessing:** Grayscale conversion and intensity normalization.
2. **Segmentation:** Global/adaptive thresholding to isolate foreground matter from the backdrop.
3. **Morphological Filtering:** Hole filling, opening/closing passes, and border-clearing to discard partial boundary objects.
4. **Scale Calibration:** Reference object detection for pixel-to-metric spatial calibration.
5. **Component Extraction & Rotation:** Individual connected-component analysis, calculating orientation angles, and applying vertical rotation.
6. **Feature Quantification:** Measuring geometric dimensions (length, width, aspect ratio) and localized RGB color profiles.
7. **Dataset Serialization:** Exporting single-grain cropped images and logging extracted measurements to `metadata.csv`.

---

## Directory Structure

```text
Rice-Grain-Pipeline/
│
├── RawImages/
│   ├── PK386/
│   │   ├── L1F23BSCS0778_PK386_Raw_001.jpg
│   │   └── ...
│   └── SuperKernel/
│       └── ...
│
├── GrainImages/
│   ├── L1F23BSCS0778_PK386_Raw_001_Grain_0001.jpg
│   ├── L1F23BSCS0778_PK386_Raw_001_Grain_0002.jpg
│   └── ...
│
├── scripts/
│   └── main.py
│
├── metadata.csv
├── requirements.txt
└── README.md
