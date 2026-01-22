# 最终推荐的可视化Prompt：复形变化链路图

## 核心要求

**布局**：横向布局，上下两行
- **上面一行**：余极限过程（BPE），从左到右
- **下面一行**：极限过程（推荐系统），从右到左
- **交汇点**：中间位置，两行在此交汇

---

## 完整Prompt（用于图像生成模型）

```
Create a professional mathematical diagram showing the transformation chain of simplicial complexes. The diagram should be HORIZONTAL LAYOUT with TWO ROWS.

=== LAYOUT STRUCTURE ===
- Top row: Colimit process (BPE), flows LEFT TO RIGHT
- Bottom row: Limit process (Recommendation System), flows RIGHT TO LEFT
- Both rows meet at the MIDDLE position (convergence point)

=== TOP ROW: COLIMIT PROCESS (BPE) - LEFT TO RIGHT ===

POSITION 1 (Far left):
- Multiple solid black dots (atoms/characters)
- Arrange 5-7 dots horizontally: a, b, c, d, e, f, g
- Label: "Initial Atoms (0D Simplices)"
- Annotation: "Given atoms (character set)"
- Visual: Simple black dots, clearly separated

POSITION 2 (Left-center):
- Atoms start merging into 1D simplices (line segments)
- Show some atoms connected: a-b, c-d, e-f
- Some atoms remain separate
- Label: "1D Tokens (1D Simplices)"
- Annotation: "Atoms merge into 1D simplices"
- Visual: Line segments connecting pairs of dots, some dots still separate

POSITION 3 (Center-left):
- 1D simplices merge with atoms to form 2D simplices (triangles)
- Show triangles: {a,b,c}, {d,e,f}
- Some 1D simplices and atoms remain
- Label: "2D Tokens (2D Simplices)"
- Annotation: "1D simplices merge into 2D simplices"
- Visual: Filled triangles, some line segments, some dots

POSITION 4 (CENTER - CONVERGENCE POINT):
- Multiple high-dimensional COMPLEXES (not single simplices!)
- Show several different complexes, each containing multiple simplices:
  * Complex 1: Contains simplices {a,b}, {a,b,c}, {a} (a complex with 1D and 2D simplices)
  * Complex 2: Contains simplices {d,e}, {d,e,f}, {d,e,f,g} (a complex with 1D, 2D, 3D simplices)
  * Complex 3: Contains simplices {h,i}, {h,i,j} (a complex with 1D and 2D simplices)
  * Complex 4: Contains simplex {k,l} (a complex with 1D simplex)
- Each simplex within a complex is a TOKEN
- Label: "Multiple High-Dimensional Complexes"
- Annotation: "Each complex contains multiple simplices (tokens)"
- Annotation: "These are COMPLEXES (collections of simplices)"
- Annotation: "This is the CONVERGENCE POINT with bottom row"
- Visual: Multiple complexes, each shown as a collection of simplices grouped together
- Key: Emphasize these are COMPLEXES (collections), not single simplices

POSITION 5 (Center-right):
- All simplices merge into fewer, higher-dimensional complexes
- Show larger complexes containing multiple simplices
- Label: "Consolidated High-Dimensional Complexes"
- Annotation: "Simplices aggregate into larger complexes"
- Visual: Larger structures containing multiple simplices

POSITION 6 (Far right):
- All atoms are in ONE extremely high-dimensional simplex
- Show a single large simplex containing all atoms: {a,b,c,d,e,f,g,h,i,j,k,l,...}
- Label: "One Extremely High-Dimensional Simplex"
- Annotation: "All atoms in one simplex (extreme case)"
- Visual: One large simplex (can be shown as a complex shape with many vertices)

DIRECTION ARROW (Top row):
- Large blue rightward arrow spanning entire top row
- Label: "COLIMIT (Aggregation)"
- Sub-label: "Atoms → Tokens → Complexes → One High-D Simplex"

=== BOTTOM ROW: LIMIT PROCESS (RECOMMENDATION SYSTEM) - RIGHT TO LEFT ===

POSITION 1 (Far right - same as top row Position 6):
- ONE extremely high-dimensional simplex
- Same as top row Position 6
- Label: "One Extremely High-Dimensional Simplex"
- Annotation: "Can also start from here (extreme case)"
- Visual: One large simplex
- Note: This is an ALTERNATIVE starting point, can flow right from Position 2

POSITION 2 (Center-right - CONVERGENCE POINT):
- MULTIPLE high-dimensional SIMPLICES (not complexes!)
- Same position as top row Position 4, but emphasize these are SIMPLICES
- Show several simplices of UNKNOWN dimensions:
  * One simplex (could be 2D, 3D, or higher) - show as ambiguous shape with "?"
  * Another simplex (unknown dimension) - ambiguous shape with "?"
  * Another simplex (unknown dimension) - ambiguous shape with "?"
- Some simplices share FACES (highlight shared faces):
  * Two simplices share a 1D face (edge) - highlight in yellow
  * Two simplices share a 2D face (triangle) - highlight in orange
  * Three simplices share a 0D face (vertex) - highlight in green
- Label: "Multiple High-Dimensional Simplices (Unknown Dimensions)"
- Annotation: "These are SIMPLICES (not complexes), dimensions unknown"
- Annotation: "Some simplices share faces (highlighted)"
- Annotation: "This is the CONVERGENCE POINT with top row"
- Visual: 
  * Ambiguous shapes with question marks (dimensions unknown)
  * Shared faces highlighted in different colors
  * Show connections between simplices via shared faces

POSITION 3 (Center-left):
- Extract SHARED FACES as separate simplices
- Show the shared faces extracted and treated as simplices:
  * One 1D face (edge) extracted - shown as a line segment, colored yellow, labeled "1D Face"
  * One 2D face (triangle) extracted - shown as a triangle, colored orange, labeled "2D Face"
  * One 0D face (vertex) extracted - shown as a dot, colored green, labeled "0D Face"
- Label: "Shared Faces as Simplices"
- Annotation: "Extract shared faces, treat each face as a simplex"
- Visual: Extracted faces shown separately as individual simplices, each colored and labeled with dimension

POSITION 4 (Left-center):
- Continue decomposing into lower-dimensional faces
- Show more shared faces extracted:
  * Multiple 1D faces
  * Multiple 0D faces
- Label: "Lower-Dimensional Shared Faces"
- Annotation: "Continue extracting shared faces"
- Visual: More extracted faces

POSITION 5 (Far left):
- All decomposed into 0D simplices (vertices/atoms)
- Show only 0D simplices (dots)
- Label: "0D Simplices (Atoms)"
- Annotation: "Decomposed to 0D simplices"
- Visual: Only dots (0D simplices)

DIRECTION ARROW (Bottom row):
- Large red leftward arrow spanning entire bottom row
- Label: "LIMIT (Decomposition)"
- Sub-label: "High-D Simplices → Shared Faces → Lower-D Faces → 0D Simplices"

=== CONNECTIONS ===
- Top row Position 4 and Bottom row Position 2 are at the SAME horizontal position (convergence point)
- Draw a vertical dashed line connecting them
- Label at convergence point: "Convergence Point"
- Key distinction:
  * "Top row: COMPLEXES (collections of simplices)"
  * "Bottom row: SIMPLICES (single simplices, unknown dimensions)"
- Note: "Same position, but different structures: Complexes vs Simplices"

=== KEY ANNOTATIONS ===

Top row (Colimit):
- "Atoms are GIVEN (known)"
- "Process: Aggregation (constructive)"
- "Result: Complexes (collections of simplices)"
- "Extreme: All atoms in one high-D simplex"

Bottom row (Limit):
- "Simplices have UNKNOWN dimensions (shown with ?)"
- "Process: Decomposition (discovery)"
- "Simplices share faces (must be discovered, highlighted in colors)"
- "Shared faces are extracted and treated as simplices"
- "Can start from convergence point (multiple simplices) OR from extreme high-D simplex (rightmost)"
- "Decompose to lower-dimensional faces, eventually to 0D simplices"

=== STYLE REQUIREMENTS ===
- Clean, professional mathematical diagram style
- Horizontal layout: two rows, same width
- Color scheme:
  * Top row: Blue tones (blue arrows, blue annotations)
  * Bottom row: Red tones (red arrows, red annotations)
  * Shared faces: Yellow (1D), Orange (2D), Green (0D)
- Dimension labels clearly visible (0D, 1D, 2D, 3D, ...)
- Arrow styles:
  * Top row: Solid blue rightward arrow
  * Bottom row: Solid red leftward arrow
- Text annotations in clear boxes
- Background: White or very light gray
- Font: Clear, readable, mathematical notation style
- Include a legend explaining:
  * Dots = 0D simplices (atoms)
  * Lines = 1D simplices
  * Triangles = 2D simplices
  * Tetrahedra = 3D simplices
  * Ambiguous shapes with "?" = unknown dimension simplices
  * Colored highlights = shared faces
  * Complexes = collections of simplices
  * Simplices = single simplices
- Make it suitable for academic publication
- Ensure clear visual flow: left-to-right (top), right-to-left (bottom)
- Convergence point should be visually clear (same horizontal position)
```

---

## 关键要点说明

### 上面一行（余极限/BPE）
1. **起点**：一堆实心点（原子，0D单纯形）
2. **过程**：逐步聚合
   - 原子 → 1D单纯形（边）
   - 1D单纯形 → 2D单纯形（三角形）
   - 形成多个高维复形（复形 = 单纯形的集合）
3. **中间节点**：多个高维复形（每个复形的子单纯形都是token）
4. **终点**：所有原子都在一个极高维单形里

### 下面一行（极限/推荐系统）
1. **起点（右端）**：可以是两个位置
   - **位置1（最右）**：一个极高维单形（与上面一行终点相同）
   - **位置2（中间）**：多个高维单形（与上面一行中间节点位置相同，但注意：这里是单形不是复形）
2. **关键特征**：
   - 这些单形的维度未知（用问号或模糊形状表示）
   - 它们之间有些有公共面（用颜色高亮）
3. **过程**：从右到左分解
   - 提取公共面作为单形
   - 继续分解到更低维的面
   - 最终分解到全是0维单形（原子）
4. **终点（左端）**：全是0维单形

### 交汇点
- 中间位置：上面一行是"多个高维复形"，下面一行是"多个高维单形"
- 关键区别：上面是复形（complex，单纯形的集合），下面是单形（simplex，单个单纯形）
- 维度：下面的单形维度未知

---

## 使用建议

1. **直接使用上面的完整Prompt**：最详细，最能体现你的要求
2. **强调交汇点**：确保中间位置的两行对齐，视觉上清晰
3. **区分复形和单形**：上面一行强调"复形"（集合），下面一行强调"单形"（单个，维度未知）
4. **共享面的可视化**：用不同颜色高亮不同维度的共享面
