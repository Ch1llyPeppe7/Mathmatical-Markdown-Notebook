# Installation Instructions

## Required Packages

The figure generation script requires:
- `plotly` - for visualization
- `kaleido` - for PNG export (required by plotly)
- `numpy` - for calculations

## Installation

### In conda environment (Pytorch):

```bash
conda activate Pytorch
pip install plotly kaleido numpy
```

Or using conda:

```bash
conda activate Pytorch
conda install -c conda-forge plotly python-kaleido numpy
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
- Figures are generated as high-resolution PNG (scale=2)
- All figures use plotly for better visual quality
