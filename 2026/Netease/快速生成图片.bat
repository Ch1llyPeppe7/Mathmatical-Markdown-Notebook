@echo off
chcp 65001 >nul
echo ========================================
echo 复形范畴笔记插图生成
echo ========================================
echo.
echo Please ensure conda environment Pytorch is activated
echo If not, run: conda activate Pytorch
echo.
echo Required packages: plotly, kaleido, numpy
echo Install: pip install plotly kaleido numpy
echo.
pause
echo.
echo Starting to generate figures...
python generate_figures.py
echo.
echo ========================================
if %ERRORLEVEL% EQU 0 (
    echo 图片生成成功！
    echo 图片保存在: images\ 目录
) else (
    echo 生成失败，请检查：
    echo 1. 是否已激活conda环境 Pytorch
    echo 2. 环境中是否安装了matplotlib和numpy
)
echo ========================================
pause
