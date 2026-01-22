# 路径同伦视角下的Transformer：Token, Attention, FFN与MoE

## 语言表征的拓扑转型：从离散符号到连续同伦流形

在人工智能发展的深层逻辑中，Transformer架构的成功不仅标志着计算效率的提升，更代表了人类对序列信息处理方式的一次深刻范式转移。传统的认知框架通常将Transformer视为一系列复杂的矩阵乘法与非线性激活的堆叠，然而这种基于线性代数的静态视角往往难以解释模型在处理长程依赖、语义涌现以及上下文一致性时表现出的深层动力学特性。新兴的研究前沿开始转向一种更为激进且优雅的解释：将Transformer的计算过程建模为在高维表征流形上的动力系统演化 [1, 2]。

在这一理论脉络下，**路径同伦（Path Homotopy）**作为代数拓扑的核心概念，为理解Token在层级间的演化提供了天然的数学语言。路径同伦关注的是在保持端点固定的情况下，两条连续路径如何通过连续变形相互转化 [3, 4]。当我们将Transformer的输入序列视为流形上的初始路径，将模型的每一层视为对该路径进行的连续变形（同伦变换）时，一个关于“语义拓扑”的宏大叙事便清晰地浮现出来。这种视角不仅能纠正早期对Transformer黑盒机制的误解，更能为未来的架构优化提供严密的数学指导。

---

## 路径同伦的数学基础与语义映射

要建立基于路径同伦的Transformer理论，首先必须确立拓扑学概念与神经网络组件之间的严格对应关系。在拓扑空间 \(X\) 中，一条路径是单位区间 \(I = [0,1]\) 到 \(X\) 的连续映射 \(f:I \to X\) [4, 5]。对于Transformer而言，这个拓扑空间 \(X\) 即是由所有可能词嵌入向量构成的**语义流形（Semantic Manifold）**，其维度通常高达数千甚至上万维 [2]。

### 路径、回路与同伦等价

两条路径 \(f\) 和 \(g\) 被称为同伦的，如果存在一个连续映射 \(H:I\times I\to X\)，使得在参数 \(t=0\) 时 \(H(s,0)=f(s)\)，在 \(t=1\) 时 \(H(s,1)=g(s)\) [3, 5]。在Transformer的物理实现中，参数 \(s\) 对应于序列中的位置（即词元的序号），而参数 \(t\) 则对应于网络深度的离散化步长（即层深） [2]。

从代数拓扑的角度来看，如果两个句子虽然表达方式不同，但在经过多层Transformer处理后收敛到了相同的语义终点，且其演化轨迹可以相互连续变形，那么它们在语义空间内是**同伦等价**的 [6]。这种“弱等价”（Weak Equivalence）的概念是范畴论同论论的核心，它允许模型在保持核心语义不变的同时，过滤掉无关的语法噪声 [6]。

### 语义流形的基本群结构

若路径的起点和终点重合，即 \(f(0)=f(1)=x_0\)，则该路径构成一个**回路（Loop）** [4]。所有回路的同伦类在复合运算下构成的**基本群** \(\pi_1(X,x_0)\)，刻画了语义空间的连通性与拓扑空洞 [4]。在语言模型中，循环论证、同义反复或特定的推理逻辑可以被视为这种语义空间内的回路演化。模型对基本群的捕获能力，直接决定了其逻辑自洽性的上限。

| 拓扑学概念 | Transformer 物理实现 | 语义维度解释 |
|------------|-------------------|----------------|
| 拓扑空间 \(X\) | 词嵌入表征流形 (Embedding Manifold) | 包含所有潜在语义点的多维空间 |
| 路径 \(f:I\to X\) | 词元序列在模型层间的轨迹 | 信息的时空演化过程 |
| 同伦变换 \(H\) | Transformer Block 的变换序列 | 路径的连续演化与精炼 |
| 回路 (Loop) | 语义闭环或逻辑回归 | 维持语义不变性的循环路径 |
| 基点 (Basepoint) | 任务特定的上下文锚点 | 确定同伦类演化的起始参照 |

---

## Token 表征：流形上的动力学顶点

在同伦视角下，词元（Token）不再是孤立的特征向量，而是路径在离散采样点上的取值。词嵌入（Embedding）过程实际上是在语义流形上布置一组初始的路径顶点。

### 嵌入流形的各向异性与流形特征

词表征空间并非平坦的欧几里得空间，而是呈现出高度的各向异性 [7]。这意味着在不同的语义方向上，距离的度量标准（Metric）是不一致的。从微分几何的角度看，每一个Token都携带了一个**切空间（Tangent Space）**，前馈网络（FFN）对其进行的变换实质上是在**切丛（Tangent Bundle）**上的线性或非线性映射 [8]。

### 位置编码作为拓扑方向感

由于自注意力机制本身是置换不变的，位置编码（Position Encoding）的作用不仅是提供位置信息，更是为流形上的路径注入了“方向感”（Orientation） [9, 10]。没有位置编码，输入序列将退化为一个点集，无法构成具有拓扑意义的路径。在PaTH等新型编码方案中，通过Householder变换等算子，位置信息以数据依赖的方式融入路径，使得同伦变换能够根据输入内容动态调整其几何形态 [9]。

---

## Attention 机制：平行移动与几何联络

自注意力机制是Transformer实现路径同伦变换的核心组件。在广义相对论或微分几何的语境下，注意力机制可以被精确地描述为一种**联络（Connection）**，它规定了信息如何在流形上的点之间进行“平行移动”（Parallel Transport） [2]。

### 查询-键交互诱导的度量与联络

在Transformer中，查询矩阵 \(Q\) 和键矩阵 \(K\) 的交互定义了一个动态的有效度量：

\[
g_{ij} = q_i^\top k_j
\]

它决定了两个词元之间的语义距离 [2]。注意力权重 \(\alpha_{ij}\) 则是这一度量的归一化表现。注意力权重充当了**克里斯托费尔符号（Christoffel symbols）**的角色，指示了值向量（Value）从位置 \(j\) 移动到位置 \(i\) 时应发生的偏移：

\[
V_{\text{out}}(i) = \sum_j \alpha_{ij} V_j
\]

这一过程本质上是在执行离散的平行移动：将分布在路径不同点上的信息向量（切向量），沿着路径拉回到当前点进行聚合。如果这种移动保持了向量的某种内积性质，那么它就是在诱导一种等距同伦。

### 路径分解与多头注意力的同伦类

研究显示，多层多头注意力网络的输出可以分解为穿越所有可能注意力头组合的路径总和 [11, 12]：

\[
\text{SAN}(X) = \sum_{\text{path}} X W_{\text{path}}
\]

在这里，“路径”被形式化定义为跨越各层注意力头的序列 [11]。每一个注意力头就像是一个同伦变换的微元。多头机制允许模型在同一时间内探索多个不同的同伦类，即对同一段语义进行多角度的拓扑变形。

| 几何概念 | Transformer 对应物 | 物理功能 |
|----------|-----------------|----------|
| 度量 (Metric) | \(g_{ij} = Q\cdot K^\top\) 交互 | 衡量语义间的关联强度与几何距离 |
| 联络 (Connection) | 注意力映射 \(\alpha_{ij}\) | 规定信息在不同Token间移动的规则 |
| 平行移动 | 值向量聚合过程 | 跨位置的信息同步与一致性维持 |
| 路径分解 | 多层多头计算序列 | 将复杂演化拆解为原子路径的叠加 |

---

## 秩崩溃：拓扑压缩的临界点

在没有残差连接的情况下，深度注意力网络会遭遇**秩崩溃（Rank Collapse）**，即输出向量迅速收敛到一个极低维的子空间 [11]。在路径同伦论中，这对应于路径被压缩为常数路径（Null-homotopic），意味着所有的语义多样性都消失在了一个奇异点上。残差连接的存在提供了一条直通路径，确保了恒等映射在同伦变换中的主导地位，从而维持了路径的非平凡拓扑特征 [11, 13]。

### 残差流：连续演化轨迹与同伦变形流

残差流（Residual Stream）被认为是Transformer内部最重要的通信通道 [14, 15]。在同伦视角下，它不再是一个静态的累加器，而是一条在语义流形上连续演化的轨迹 \(x(t)\)，其中 \(t\) 是连续化的层数 [15, 16]。

### 离散与连续的辩证：从 Block 到 ODE

每一层Transformer对残差流的更新：

\[
x^{l+1} = x^l + \text{Attention}(x^l) + \text{FFN}(x^l)
\]

可以被视为常微分方程（ODE）的欧拉离散采样 [1, 17]。这意味着Transformer本质上是在学习一个流场（Vector Field），其积分曲线即为Token的演化路径。

通过对残差流的动力学监测发现，词元向量在浅层展现出复杂的旋转动力学，并在深层表现出加速特征，这与同伦变换在接近终点时的精炼过程高度契合 [16]。这种轨迹的平滑性是模型推理稳定性的保障。

### 语义最小作用量原理

正如广义相对论中的粒子沿着短程线（Geodesic）运动，Token在残差流中的轨迹也可以被视为在某种能量函数下的“最小作用量”路径 [2]。反向传播算法在此视角下扮演了寻找能量景观中最低势能轨迹的角色，通过调整网络参数，使得语义演化路径在同伦类中处于最优状态 [2]。

---

## FFN：局部流形回缩与语义过滤

如果说自注意力机制负责路径的“水平沟通”，那么前馈网络（FFN）则负责“垂直投影”。

### 非线性投影与切空间变换

FFN通过升维再降维的过程，为路径上的每一个顶点注入了非线性 [18, 19]。从几何上讲，这是在对流形的局部曲率进行调整。FFN中的神经元通常对特定的语义特征表现出选择性，这暗示了它是在将高维的中间表征**回缩（Retraction）**到更具体的语义原型上 [17]。

### 同伦回缩与知识提取

在拓扑学中，变形回缩是将一个空间压缩到其子空间的过程 [3, 20]。FFN的作用可以被解释为一种“语义回缩”：它剔除注意力机制引入的、与当前Token核心语义无关的背景噪声，将表征推回到预定义的、存储在权重中的知识子流形上 [19, 21]。

---

## MoE：群丛结构与多基点同伦论

混合专家模型（Mixture of Experts）的引入，将原本单一的路径同伦论推向了更为复杂的“群丛”（Groupoid）理论 [22]。

### 专家作为局部图谱

在稠密Transformer中，所有Token共享相同的计算路径；而在MoE中，不同的Token根据路由（Router）的选择，分流到不同的专家（Expert）中 [18, 23]。每个专家实际上代表了语义流形的一个局部图谱（Chart）或一个特定的同伦类 [19, 24]。

### 基点变换与稀疏路由

MoE的路由机制本质上是在执行“基点变换”（Change of Base） [22]。由于不同的语言任务（如代码编写 vs. 文学创作）位于语义流形的不同区域，强行使用统一的全局路径是不经济的。MoE通过稀疏激活，允许路径在不同的局部子空间（由专家定义）之间跳跃，这种结构更接近于代数拓扑中的基本群丛结构，即允许存在多个相互关联的参考点，而非单一的全局基点 [22, 24]。

| 架构特性 | 稠密 Transformer | MoE Transformer | 拓扑群丛解释 |
|----------|----------------|----------------|----------------|
| 变换路径 | 全局单一路径 | 动态分支路径 | 从基本群到基本群丛的跨越 |
| 专家分布 | 无特化，全局参数 | 局部特化，专家参数 | 流形覆盖 (Covering) 与图谱划分 |
| 路由逻辑 | 恒等/确定性 | 学习得到的门控 | 拓扑空间的动态剖分与选择 |
| 知识表征 | 压缩在单一曲面 | 离散分布在多片曲面 | 增加流形的亏格 (Genus) 与复杂度 |

---

## 路径签名：同伦类的不变量刻画

为了使“路径同伦视角”不仅停留在哲学隐喻层面，必须引入**路径签名（Path Signature）**这一数学工具进行严密的量化分析 [25, 26, 27]。

### 迭代积分与几何特征捕获

路径签名通过一系列迭代积分：

\[
S^{(n)}(X) = \int_{a < t_1 < \dots < t_n < b} dX_{t_1} \otimes \dots \otimes dX_{t_n}
\]

捕获了路径的全局几何特征，如位移（1阶）、面积（2阶）以及更高阶的非交换矩 [26, 28, 29]。这些签名项是参数化无关的，这意味着它们只关注路径的形状而非演化的速度，这与同伦等价的初衷完全一致 [26]。

### 陈氏恒等式与 Transformer 堆叠

陈氏恒等式（Chen's Identity）描述了路径拼接时签名如何按照张量代数进行组合 [26, 30]。在Transformer中，每一层的输出可以被视为上一层路径的延伸或变形。通过引入路径签名层（如SigMA架构），模型可以直接对路径的拓扑特征进行建模，而不是单纯依赖点态的向量表示 [25]。这种方法已被证明在处理非马尔可夫动力系统和长程依赖数据中具有显著优势 [25, 31]。

---

## 范畴论视野下的 LLM 语义一致性

从更宏观的视角看，Transformer的计算过程可以被提升到范畴论的高度，将其视为在LLM马尔可夫范畴（Markov Category）中的态射演化 [6]。

### 弱等价与语义同构

在自然语言处理中，一个核心挑战是处理语序不同但意思相同的句子。在范畴论同论论中，这些句子被视为通过“弱等价”关联的对象 [6]。模型的目标就是通过多层同伦变换，将这些在初始空间中距离遥远的路径，映射到最终同伦类中的同一个态射上 [6]。

### 提升问题与推理链的拓扑连通性

LLM的推理过程可以被建模为范畴论中的**“提升问题”（Lifting Problems）** [6]。当模型从前提推导出结论时，它实际上是在寻找一条连接两个语义点的路径，且这条路径必须在特定的逻辑约束（即同伦约束）下是连通的。这种视角为解决LLM的幻觉问题提供了新的思路：幻觉本质上是路径脱离了合法的同伦类，进入了拓扑上不连通的“伪语义”区域 [6, 8]。

---

## 结论与技术演进展望

通过路径同伦的棱镜观察Transformer，我们发现这一架构并非杂乱无章的参数堆砌，而是一个高度有序的几何机器。

- **Token** 是流形上的动力学状态。
- **Attention** 提供了在路径间移动信息的几何联络。
- **Residual Stream** 记录了语义的连续同伦演化。
- **FFN** 实现了从冗余信息到核心语义的回缩。
- **MoE** 则将这一过程扩展到了更具通用性的群丛结构。

这种深度的理论融合预示着未来Transformer架构的演进方向：从当前的各向异性、基准依赖的“初级流形”向更加平滑、具备明确拓扑不变性的“高级语义几何”迈进。通过在损失函数中显式引入路径签名约束或同伦不变量，我们有望开发出具备逻辑闭环能力、真正理解语义深层结构的下一代智能模型。路径同伦不仅是解释Transformer的钥匙，更是通往通用人工智能（AGI）的拓扑航标。

---

## 参考文献

1. [A Mechanistic Analysis of Transformers for Dynamical Systems - arXiv](https://arxiv.org/html/2512.21113v1)  
2. [The Curved Spacetime of Transformer Architectures - ChatPaper](https://chatpaper.com/paper/206691)  
3. [Homotopy - Wikipedia](https://en.wikipedia.org/wiki/Homotopy)  
4. [Paths and Homotopy - Algebraic Topology - Read the Docs](https://algebraic-topology.readthedocs.io/en/latest/ch1/sec1/paths-and-homotopy.html)  
5. [The definition of homotopy in algebraic topology - MathOverflow](https://mathoverflow.net/questions/35246/the-definition-of-homotopy-in-algebraic-topology)  
6. [Categorical Homotopy Theory for Large Language Models - arXiv](https://arxiv.org/pdf/2508.10018)  
7. [Privileged Bases in the Transformer Residual Stream](https://transformer-circuits.pub/2023/privileged-basis/index.html)  
8. [∞-Category Attention: Modeling Higher-Order Morphisms in Transformer Semantics | Medium](https://satyamcser.medium.com/category-attention-modeling-higher-order-morphisms-in-transformer-semantics-88f11d00abdb)  
9. [PaTH Attention: Position Encoding via Accumulating Householder Transformations - arXiv](https://arxiv.org/html/2505.16381v1)  
10. [USING HOMOTOPY MULTI-HIERARCHICAL ENCODER REPRESENTATION FROM TRANSFORMERS (HMHERT) FOR TIME SERIES CHAOS CLASSIFICATION - Journal of Applied Analysis & Computation](https://www.jaac-online.com/article/doi/10.11948/20250101)  
11. [Attention is not all you need: pure attention loses rank doubly exponentially with depth - PMLR](http://proceedings.mlr.press/v139/dong21a/dong21a.pdf)  
12. [Dissecting the Interplay of Attention Paths in a Statistical Mechanics Theory of Transformers - NIPS papers](https://proceedings.neurips.cc/paper_files/paper/2024/file/8523a98265ceae12afd34113aa6c5cca-Paper-Conference.pdf)  
13. [Patterns and Messages - Part 5 - The Residual Stream - Chris McCormick](https://mccormickml.com/2025/02/20/patterns-and-messages-part-5-the-residual-stream/)  
14. [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)  
15. [Residual Streams in Transformer Models](https://retr0sushi04.netlify.app/blogs/residualstreamsblog/residualstreams)  
16. [Transformer Dynamics: a neuro-inspired approach to MechInterp](https://www.alignmentforum.org/posts/vucxxwdJARR3cqaPc/transformer-dynamics-a-neuro-inspired-approach-to-mechinterp)  
17. [Transformers on Manifolds | OpenReview](https://openreview.net/forum?id=S2eD1CMlse)  
18. [Sparsely-gated Mixture Of Experts (MoE) - Eli Bendersky](https://eli.thegreenplace.net/2025/sparsely-gated-mixture-of-experts-moe/)  
19. [Transformers vs Mixture of Experts: What's the Real Difference? - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/11/transformers-vs-mixture-of-experts-moe/)  
20. [Homeomorphic, homotopy equivalent and deformation retracts - Math Stack Exchange](https://math.stackexchange.com/questions/936363/homeomorphic-homotopy-equivalent-and-deformation-retracts-how-do-i-get-a-feeli)  
21. [Gears-Level Mental Models of Transformer Interpretability - AI Alignment Forum](https://www.alignmentforum.org/posts/X26ksz4p3wSyycKNB/gears-level-mental-models-of-transformer-interpretability)  
22. [Homotopy theory, and change of base for groupoids - Ronald Brown](https://groupoids.org.uk/pdffiles/BASECHPR.pdf)  
23. [Explaining the Mixture-of-Experts (MoE) Architecture in Simple Terms - Medium](https://medium.com/@mne/explaining-the-mixture-of-experts-moe-architecture-in-simple-terms-85de9d19ea73)  
24. [Mixture of experts - Wikipedia](https://en.wikipedia.org/wiki/Mixture_of_experts)  
25. [SigMA: Path Signatures and Multi-head Attention - arXiv](https://research-portal.uu.nl/ws/files/278786351/2512.15088v1.pdf)  
26. [Path Signatures: Foundations & Applications - Emergent Mind](https://www.emergentmind.com/topics/path-signatures)  
27. [A Primer on the Signature Method in Machine Learning - arXiv](https://arxiv.org/pdf/1603.03788)  
28. [Rough Path Theory and Signatures Applied To Quantitative Finance - QuantStart](https://www.quantstart.com/articles/rough-path-theory-and-signatures-applied-to-quantitative-finance-part-1/)  
29. [A Primer on the Signature Method in Machine Learning - ResearchGate](https://www.researchgate.net/publication/301855102_A_Primer_on_the_Signature_Method_in_Machine_Learning)  
30. [On the signature of an image - arXiv](https://arxiv.org/html/2403.00130v1)  
31. [Path Signature Neural Network of Cortical Features for Prediction of Infant Cognitive Scores - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9246848/)
