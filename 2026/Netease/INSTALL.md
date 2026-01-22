# Installation Instructions

## Required Packages

The figure generation script requires:
- `matplotlib` - for visualization and PNG export
- `numpy` - for calculations

## Installation

### In conda environment (Pytorch):

```bash
conda activate Pytorch
pip install matplotlib numpy
```

Or using conda:

```bash
conda activate Pytorch
conda install matplotlib numpy
```

## Run Script

After installation:

```bash
conda activate Pytorch
cd "D:\Document\Mathmatical-Markdown-Notebook\2026\Netease"
python generate_figures.py
```

## Notes

- All text in figures is in English to avoid font issues
- Figures are generated as high-resolution PNG (300 DPI)
- All figures use matplotlib for direct PNG export (no external dependencies needed)
