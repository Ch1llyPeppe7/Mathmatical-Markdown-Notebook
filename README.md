# Markdown 学术笔记系统

基于 Markdown Preview Enhanced 和 Crossnote 的 LaTeX 风格学术笔记系统，支持自动编号、丰富的定理环境、优雅的排版和 PDF 导出。

## ✨ 主要特性

- 📚 **LaTeX 风格排版**：接近 LaTeX 论文的视觉效果
- 🔢 **自动编号系统**：Chapter、Section、Subsection 及各类定理环境自动编号
- 🎨 **丰富的块类型**：支持 17+ 种不同类型的学术块（定义、定理、引理、命题等）
- 📄 **扉页系统**：专业的封面页设计
- 🔬 **数学公式优化**：块内公式自动放大，CD 环境自适应
- 🖨️ **Prince PDF 导出**：支持高质量 PDF 导出，保留所有背景色
- ⚡ **代码片段补全**：快速插入各类块结构
- 📐 **响应式布局**：充分利用页面空间

## 📁 项目结构

```
.
├── .crossnote/              # Crossnote 配置目录
│   ├── style.less          # 主样式文件（LESS）
│   ├── config.js           # Crossnote 配置
│   ├── parser.js           # Markdown 解析器扩展
│   └── head.html           # HTML 头部注入
├── .MPE/                    # Markdown Preview Enhanced 配置
│   └── markdown.json       # MPE 代码片段配置
├── .vscode/                 # VSCode 配置
│   ├── settings.json       # 编辑器设置
│   └── markdown.code-snippets  # 代码片段（自动补全）
└── 2026/                    # 笔记内容目录
    ├── Medical/            # 医学相关笔记
    ├── Netease/            # 网易相关笔记
    └── ...
```

## 🚀 快速开始

### 1. 安装依赖

确保已安装以下 VSCode 扩展：
- **Markdown Preview Enhanced** (shd101wyy.markdown-preview-enhanced)
- **Crossnote** (推荐，用于更好的预览体验)

### 2. 使用代码片段

在 Markdown 文件中输入 `blk` 然后按 `Tab`，选择块类型即可快速插入。

### 3. 创建扉页

```markdown
<blockquote class="cover-page">
  <div class="cover-title">文档标题</div>
  <blockquote class="cover-subtitle">
  副标题
  </blockquote>
  <div class="cover-meta-group">
    <div class="cover-author">作者姓名</div>
    <div class="cover-date">2026.1.15</div>
  </div>
</blockquote>
```

## 📐 支持的块类型

### 书籍结构

| 块类型 | 自动标题格式 | 说明 |
|--------|------------|------|
| `chapter` | Chapter X | 章节 |
| `section` | Section X.Y | 节 |
| `subsection` | Subsection X.Y.Z | 小节 |

### 定理环境

| 块类型 | 自动标题格式 | 颜色 | 用途 |
|--------|------------|------|------|
| `definition` | Definition X.Y | 🟢 绿色 | 定义 |
| `theorem` | Theorem X.Y | 🔵 蓝色 | 定理 |
| `lemma` | Lemma X.Y | 🟢 绿色 | 引理 |
| `proposition` | Proposition X.Y | 🔵 浅蓝 | 命题 |
| `property` | Property X.Y | 🟣 紫色 | 性质 |
| `assumption` | Assumption X.Y | 🟣 紫色 | 假设 |
| `proposal` | Proposal X.Y | 🔵 青色 | 提议 |
| `proof` | Proof. | 🟣 紫色 | 证明 |
| `example` | Example X.Y | 🔵 青色 | 例子 |
| `counterexample` | Counterexample X.Y | 🔴 橙红 | 反例 |
| `remark` | Remark X.Y | 🟠 橙色 | 备注 |
| `discussion` | Discussion X.Y | ⚫ 灰色 | 讨论 |
| `algorithm` | Algorithm X.Y | 🔵 蓝色 | 算法 |
| `objective` | Objective X.Y | 🟠 橙色 | 目标 |

### 信息提示块

| 块类型 | 颜色 | 用途 |
|--------|------|------|
| `info` | 🔵 蓝色 | 信息提示 |
| `warning` | 🔴 红色 | 警告 |
| `tip` | 🟢 绿色 | 提示 |

## 💡 使用示例

### 基本块结构

```markdown
<blockquote class="chapter">

# 章节标题

<blockquote class="section">

## 节标题

<blockquote class="definition">

这是定义内容，可以包含数学公式 $E = mc^2$。

$$
\begin{align}
x &= a + b \\
y &= c + d
\end{align}
$$

</blockquote>

</blockquote>
</blockquote>
```

### 数学公式

- **行内公式**：`$...$` - 在 Chapter/Section/Subsection 中保持正常大小
- **块级公式**：`$$...$$` - 在定理环境中自动放大
- **CD 环境**：`\begin{CD}...\end{CD}` - 自动适应容器宽度

### 扉页示例

```markdown
<blockquote class="cover-page">
  <div class="cover-title">残差网络系列研究</div>
  <blockquote class="cover-subtitle">
  深度残差、宽度残差与超残差
  </blockquote>
  <div class="cover-meta-group">
    <div class="cover-author">Jin.Qian</div>
    <div class="cover-date">2026.1.15</div>
  </div>
</blockquote>
```

## 🎨 样式定制

所有样式定义在 `.crossnote/style.less` 文件中，使用 CSS 变量进行统一管理：

### 字体大小

```less
--font-size-body: 12.5px;           // 正文大小
--font-size-block-title: 20px;      // 块标题大小
--font-size-chapter-title: 22px;    // Chapter 标题大小
--font-size-section-title: 18px;     // Section 标题大小
--font-size-h1: 19px;               // Markdown # 标题大小
```

### 颜色定制

```less
--color-def: #2e7d32;        // Definition 颜色
--color-thm: #1565c0;        // Theorem 颜色
--color-lemma: #4caf50;      // Lemma 颜色
// ... 更多颜色变量
```

修改这些变量即可全局调整样式。

## 🖨️ PDF 导出

### 使用 Prince 导出

1. 在 Markdown Preview Enhanced 中打开预览
2. 右键 → `Chrome (Puppeteer)` → `PDF`
3. 或使用 Prince XML 进行高质量导出

### PDF 导出特性

- ✅ 保留所有背景色
- ✅ 自动分页（Chapter 自动新页）
- ✅ 优化的页面布局
- ✅ 数学公式正确渲染
- ✅ CD 环境自适应容器

## ⌨️ 代码片段

### 快速插入块

输入 `blk` + `Tab`，然后选择块类型：

```
blk → <blockquote class="[选择类型]">
```

### 支持的块类型

所有块类型都在代码片段的下拉菜单中，按逻辑顺序排列。

## 📝 标题大小关系

自动生成的标题大小遵循以下层级关系：

```
Chapter 块标题 (22px) 
  > # Markdown 标题 (19px)
    > Section 块标题 (18px)
      > ## Markdown 标题 (17px)
        > Subsection 块标题 (16px)
          > ### Markdown 标题 (15px)
```

其他块标题（Definition、Theorem 等）：20px

## 🔧 配置说明

### VSCode 设置

`.vscode/settings.json` 中已配置：
- Markdown 文件的代码片段自动补全
- Markdown Preview Enhanced 的自定义样式路径
- 快速建议和 Tab 补全

### Crossnote 配置

`.crossnote/config.js` - Crossnote 主配置
`.crossnote/style.less` - 样式文件（LESS 格式）
`.crossnote/parser.js` - Markdown 解析器扩展

## ⚠️ 注意事项

1. **块类型命名**：使用小写字母，如 `definition` 而不是 `Definition`
2. **数学公式**：在 Chapter/Section/Subsection 中保持正常大小，在定理环境中自动放大
3. **CD 环境**：会自动缩小以适应容器，避免超出边界
4. **Prince 导出**：确保使用最新版本的 Prince XML 以获得最佳效果
5. **代码片段**：如果自动补全不工作，重启 VSCode 或重新加载窗口

## 🐛 故障排除

### 代码片段不工作？

1. 检查 `.vscode/markdown.code-snippets` 文件是否存在
2. 确认 VSCode 设置中 `editor.snippetSuggestions` 为 `"top"`
3. 重启 VSCode 或重新加载窗口（`Ctrl+Shift+P` → "Reload Window"）

### 样式不显示？

1. 检查 `.crossnote/style.less` 文件路径是否正确
2. 确认 Markdown Preview Enhanced 的自定义样式配置
3. 重启预览窗口

### PDF 导出背景色丢失？

1. 检查 Prince 版本（建议使用最新版）
2. 确认样式文件中使用了 `print-color-adjust: exact !important`
3. 检查是否使用了 `color-mix()`（已改为直接颜色值）

## 📚 更多资源

- [Markdown Preview Enhanced 文档](https://shd101wyy.github.io/markdown-preview-enhanced/)
- [Crossnote 文档](https://crossnote.app/)
- [Prince XML 文档](https://www.princexml.com/doc/)

## 📄 许可证

本项目为个人学术笔记系统，可自由使用和修改。

---

**最后更新**：2026年1月
