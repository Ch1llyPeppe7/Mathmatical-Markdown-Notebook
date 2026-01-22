# 插图生成说明

## 快速开始

1. **安装依赖**：
```bash
pip install matplotlib numpy
```

2. **运行脚本**：
```bash
cd 2026/Netease
python generate_figures.py
```

3. **生成结果**：
   - 所有图片将保存在 `images/` 目录下
   - 图片格式：PNG，分辨率：300 DPI

## 生成的插图列表

1. **figure1_simplicial_complex.png** - 单纯复形可视化（超图形式）
2. **figure2_bpe_pushout.png** - BPE的推出构造过程
3. **figure3_inverse_splitting_pullback.png** - 逆向分裂的拉回构造过程
4. **figure4_conjugate_complex.png** - 共轭复形的构造
5. **figure5_weighted_directed_complex.png** - 有向加权复形
6. **figure6_commutative_diagrams.png** - 推出和拉回的交换图

## 自定义修改

如果需要修改插图样式，编辑 `generate_figures.py` 文件中的相应函数：
- `figure1_simplicial_complex()` - 单纯复形
- `figure2_bpe_pushout()` - BPE过程
- `figure3_inverse_splitting_pullback()` - 逆向分裂过程
- `figure4_conjugate_complex()` - 共轭复形
- `figure5_weighted_directed_complex()` - 有向加权复形
- `figure6_commutative_diagrams()` - 交换图

## 注意事项

- 确保 `images/` 目录存在（脚本会自动创建）
- 如果修改了图片文件名，记得同步更新笔记中的图片引用路径
- 图片使用相对路径：`images/figureX_xxx.png`
