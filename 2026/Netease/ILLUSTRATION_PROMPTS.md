# 插图生成提示词（Image Generation Prompts）

本文档列出了笔记中需要的高质量插图及其生成提示词。所有插图应为学术风格，清晰、专业，适合数学笔记使用。

## 1. 单纯形的维度示意图

**位置**: 基础概念章节 - 单纯形定义后

**提示词**:
```
Mathematical diagram showing dimensions of simplices: 
- 0-simplex: a single point labeled "vertex"
- 1-simplex: a line segment with two endpoints labeled "edge"
- 2-simplex: a filled triangle with three vertices labeled "triangle"
- 3-simplex: a tetrahedron with four vertices labeled "tetrahedron"
All simplices should be clearly labeled with their dimensions (0-dim, 1-dim, 2-dim, 3-dim). 
Academic style, clean white background, black lines, professional mathematical illustration.
```

## 2. 单纯复形的闭包公理示意图

**位置**: 单纯复形定义后

**提示词**:
```
Mathematical diagram illustrating the closure axiom of simplicial complexes:
Show a triangle (2-simplex) with its three edges (1-simplices) and three vertices (0-simplices).
All faces of the triangle must be included in the complex.
Use arrows or annotations to show that "if a simplex is in the complex, all its faces must also be in the complex".
Clean academic style, white background, labeled vertices (a, b, c), professional mathematical illustration.
```

## 3. 共轭复形的顶点-单纯形反转示意图

**位置**: 共轭复形定义后

**提示词**:
```
Mathematical diagram showing conjugate complex construction with vertex-simplex reversal:
Left side: Original complex K with vertices {a, b, c} forming a triangle, labeled "Vertices = Atoms, Simplices = Tokens"
Right side: Conjugate complex K* where the triangle becomes a vertex and vertices become simplices, labeled "Vertices = Tokens, Simplices = Atom Clusters"
Show a bidirectional arrow between them labeled "Vertex ↔ Simplex Reversal"
Academic style, clean layout, professional mathematical illustration.
```

## 4. 单纯映射的维度降低示意图

**位置**: 单纯映射定义后

**提示词**:
```
Mathematical diagram showing a simplicial map that reduces dimension:
Source complex: a triangle with vertices {a, b, c}
Target complex: a line segment with vertices {x, y}
Show mapping: a→x, b→x, c→y, where the triangle (2-simplex) maps to the edge (1-simplex)
Annotate: "Dimension reduction: 2-simplex → 1-simplex"
Clean academic style, arrows showing the mapping, professional mathematical illustration.
```

## 5. 加权有向复形的详细示意图

**位置**: 加权复形与有向单纯复形章节

**提示词**:
```
Mathematical diagram of a weighted directed simplicial complex:
Show 4 nodes (items) connected by directed edges with arrowheads.
Each edge should be labeled with a weight (e.g., w=0.8, w=0.6).
Show a directed triangle (2-simplex) with arrows indicating temporal order.
Include annotations: "Directed edges show temporal relations: Item i → Item j"
"Weights w represent co-occurrence frequency"
Academic style, clean layout, professional mathematical illustration with clear arrow directions.
```

## 6. 链复形与边界算子的示意图

**位置**: 链复形与边界算子章节

**提示词**:
```
Mathematical diagram showing chain complex and boundary operator:
Show a sequence: C_2 → C_1 → C_0 with boundary operators ∂_2, ∂_1 between them.
Illustrate: a triangle (2-simplex) in C_2, its boundary (three edges) in C_1, and vertices in C_0.
Show the boundary operator ∂_2 applied to the triangle, resulting in the sum of its three edges with alternating signs.
Annotate: "∂_d ∘ ∂_{d+1} = 0" (boundary of boundary is zero)
Academic style, clean mathematical notation, professional illustration.
```

## 7. 同调群的直观解释图

**位置**: 同调群与Betti数章节

**提示词**:
```
Mathematical diagram illustrating homology groups:
Show a torus (donut shape) with:
- β_0 = 1 (one connected component) - label one region
- β_1 = 2 (two holes/loops) - highlight two independent loops on the torus
- β_2 = 1 (one cavity) - show the interior cavity
Alternatively, show a simple example: a circle (β_1 = 1) and a filled disk (β_1 = 0).
Academic style, clear annotations, professional topological illustration.
```

## 8. 极限的泛性质示意图

**位置**: 极限的定义章节

**提示词**:
```
Mathematical commutative diagram showing the universal property of limits:
Show a diagram with objects K, L, M, and the limit object K × L.
Include projection morphisms π_1: K × L → K and π_2: K × L → L.
Show a generic object X with morphisms f_1: X → K and f_2: X → L.
Show the unique morphism f: X → K × L making the diagram commute.
Label: "Universal Property: ∃! f such that π_1 ∘ f = f_1 and π_2 ∘ f = f_2"
Academic style, clean commutative diagram, professional category theory illustration.
```

## 9. 拉回的交换方块图

**位置**: 拉回构造章节

**提示词**:
```
Mathematical commutative square diagram for pullback:
Show a square with:
- Top: K with morphism f: K → M
- Bottom: L with morphism g: L → M  
- Left: K ×_M L with projection π_1: K ×_M L → K
- Right: K ×_M L with projection π_2: K ×_M L → L
All arrows should be clearly labeled.
The square should commute: f ∘ π_1 = g ∘ π_2
Academic style, clean diagram, professional category theory illustration.
```

## 10. 推出的交换方块图

**位置**: 推出构造章节

**提示词**:
```
Mathematical commutative square diagram for pushout:
Show a square with:
- Top left: M with morphism f: M → K
- Top right: K with inclusion ι_1: K → K ⊔_M L
- Bottom left: L with inclusion ι_2: L → K ⊔_M L
- Bottom right: K ⊔_M L (the pushout)
All arrows should be clearly labeled.
The square should commute: ι_1 ∘ f = ι_2 ∘ g
Academic style, clean diagram, professional category theory illustration.
```

## 11. BPE的推出构造过程（详细版）

**位置**: BPE作为余极限过程章节

**提示词**:
```
Mathematical diagram showing BPE pushout construction in detail:
Step 1: Two atomic complexes A_1 and A_2 (each with single vertices)
Step 2: Constraint complex M showing the "continuous substring" constraint
Step 3: Morphisms f: M → A_1 and g: M → A_2
Step 4: The pushout A_1 ⊔_M A_2 showing the merged token
Show the commutative square and annotate: "BPE merge operation = Pushout construction"
Academic style, step-by-step illustration, professional category theory diagram.
```

## 12. 逆向分裂的拉回构造过程（详细版）

**位置**: 逆向分裂作为极限过程章节

**提示词**:
```
Mathematical diagram showing inverse splitting pullback construction in detail:
Step 1: Global interaction complex G (a 2-simplex/triangle)
Step 2: Constraint complex M with frequency and minimality constraints
Step 3: Sub-complexes G_1 and G_2 with morphisms to M
Step 4: The pullback G_1 ×_M G_2 showing the minimal atomic clusters
Show the commutative square and annotate: "Inverse splitting = Pullback construction"
Academic style, step-by-step illustration, professional category theory diagram.
```

## 13. 函子与伴随对的示意图

**位置**: 函子与伴随对章节

**提示词**:
```
Mathematical diagram showing the adjunction between forgetful and free functors:
Left side: Category of Sets (Set) with a set S
Right side: Category of Complexes (Comp) with complex K
Show:
- Free functor F: Set → Comp, F(S) = free complex on S
- Forgetful functor U: Comp → Set, U(K) = vertex set of K
- Natural isomorphism: Hom_Comp(F(S), K) ≅ Hom_Set(S, U(K))
Show bidirectional arrows and label the adjunction F ⊣ U
Academic style, clean category theory diagram, professional illustration.
```

## 14. 共轭复形关系的对偶性示意图

**位置**: 共轭复形关系的核心体现章节

**提示词**:
```
Mathematical diagram showing the duality between original and conjugate complexes:
Left: Original complex K showing "Vertices = Atoms, Simplices = Tokens"
Right: Conjugate complex K* showing "Vertices = Tokens, Simplices = Atom Clusters"
Show the reversal relationship with bidirectional arrows.
Annotate: "K's simplices = K*'s vertices" and "K's vertices = K*'s simplex components"
Show how BPE operates on K (colimit) and inverse splitting operates on K* (limit)
Academic style, clear duality illustration, professional mathematical diagram.
```

## 15. 信息论AEP的典型集示意图

**位置**: 信息论基础章节

**提示词**:
```
Mathematical diagram illustrating Asymptotic Equipartition Property (AEP):
Show a probability distribution with:
- A region labeled "Typical Set A_ε^(n)" containing most of the probability mass
- A small region labeled "Atypical sequences" with low probability
- Annotations: "P(A_ε^(n)) > 1 - ε" and "|A_ε^(n)| ≈ 2^(nH(X))"
- Show convergence as n → ∞
Academic style, probability distribution plot, professional information theory illustration.
```

## 插图生成建议

1. **风格统一**: 所有插图应使用统一的学术风格，白色背景，黑色线条，清晰的标注
2. **字体**: 使用数学字体（如LaTeX风格）标注数学符号
3. **颜色**: 可以使用少量颜色来区分不同的对象（如原复形用蓝色，共轭复形用紫色）
4. **布局**: 保持清晰的布局，避免拥挤，留出足够的边距
5. **分辨率**: 建议生成高分辨率图像（至少1200x800像素），以便在PDF中清晰显示

## 使用说明

将这些提示词输入到图像生成模型（如DALL-E、Midjourney、Stable Diffusion等）中，可以生成高质量的数学插图。如果模型支持，可以添加以下通用后缀：

```
, academic mathematical illustration, clean white background, professional diagram, high resolution, detailed annotations
```
