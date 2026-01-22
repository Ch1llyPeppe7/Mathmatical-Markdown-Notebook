"""
复形范畴笔记插图生成脚本
使用matplotlib和networkx生成静态PNG图片
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# 创建images目录
os.makedirs('images', exist_ok=True)

# 设置中文字体（如果需要）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ==================== 插图1：单纯复形（Hypergraph）示例 ====================

def figure1_simplicial_complex():
    """生成包含0-3维单纯形的复形可视化"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 定义顶点坐标
    v0 = np.array([0, 0])
    v1 = np.array([2, 0])
    v2 = np.array([1, 1.732])
    v3 = np.array([1, 0.577])
    
    vertices = [v0, v1, v2, v3]
    labels = ['a', 'b', 'c', 'd']
    
    # 绘制3维单纯形（四面体）- 用半透明填充
    tetrahedron = [
        [v0, v1, v2],
        [v0, v1, v3],
        [v0, v2, v3],
        [v1, v2, v3]
    ]
    for face in tetrahedron:
        triangle = Polygon(face, alpha=0.15, color='blue', edgecolor='none')
        ax.add_patch(triangle)
    
    # 绘制2维单纯形（三角形）- 用较深颜色填充
    triangles = [
        [v0, v1, v2],
        [v0, v1, v3]
    ]
    for tri in triangles:
        triangle = Polygon(tri, alpha=0.3, color='blue', edgecolor='blue', linewidth=1.5)
        ax.add_patch(triangle)
    
    # 绘制1维单纯形（边）
    edges = [
        (v0, v1), (v1, v2), (v2, v0),
        (v0, v3), (v1, v3), (v2, v3)
    ]
    for v_start, v_end in edges:
        ax.plot([v_start[0], v_end[0]], [v_start[1], v_end[1]], 
                'k-', linewidth=2, zorder=2)
    
    # 绘制0维单纯形（顶点）
    for i, (v, label) in enumerate(zip(vertices, labels)):
        ax.scatter(v[0], v[1], s=200, c='black', zorder=5)
        ax.text(v[0], v[1] - 0.2, label, fontsize=14, ha='center', weight='bold')
    
    # 添加维度标注
    ax.text(0.5, 0.3, '0维: 顶点', fontsize=10, style='italic', color='gray')
    ax.text(0.5, 0.5, '1维: 边', fontsize=10, style='italic', color='gray')
    ax.text(0.5, 0.7, '2维: 三角形', fontsize=10, style='italic', color='gray')
    ax.text(0.5, 0.9, '3维: 四面体', fontsize=10, style='italic', color='gray')
    
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('单纯复形（Simplicial Complex）\n作为超图（Hypergraph）的可视化', 
                 fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('images/figure1_simplicial_complex.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图1: 单纯复形可视化")

# ==================== 插图2：BPE的推出构造过程 ====================

def figure2_bpe_pushout():
    """生成BPE的推出构造过程（序列图）"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 阶段1：初始状态（原子复形）
    ax1 = axes[0]
    # 绘制原子顶点
    atoms = ['a', 'b', 'c']
    positions = [(0, 0), (1, 0), (2, 0)]
    for pos, atom in zip(positions, atoms):
        circle = plt.Circle(pos, 0.15, color='blue', zorder=3)
        ax1.add_patch(circle)
        ax1.text(pos[0], pos[1], atom, ha='center', va='center', 
                fontsize=12, weight='bold', color='white', zorder=4)
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('阶段1: 原子复形\n（0维单纯形）', fontsize=11, pad=10)
    
    # 阶段2：中间状态（推出构造）
    ax2 = axes[1]
    # 绘制原子
    for pos, atom in zip(positions, atoms):
        circle = plt.Circle(pos, 0.15, color='blue', zorder=3)
        ax2.add_patch(circle)
        ax2.text(pos[0], pos[1], atom, ha='center', va='center', 
                fontsize=12, weight='bold', color='white', zorder=4)
    # 绘制边（1维单纯形）
    ax2.plot([0, 1], [0, 0], 'g-', linewidth=3, zorder=2, label='合并')
    ax2.plot([1, 2], [0, 0], 'g-', linewidth=3, zorder=2)
    # 添加箭头表示推出
    arrow = FancyArrowPatch((0.5, 0.2), (1.5, 0.2), 
                           arrowstyle='->', mutation_scale=20, 
                           color='red', linewidth=2, zorder=5)
    ax2.add_patch(arrow)
    ax2.text(1, 0.35, '推出构造', ha='center', fontsize=10, 
            color='red', weight='bold')
    ax2.set_xlim(-0.5, 2.5)
    ax2.set_ylim(-0.5, 0.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('阶段2: 推出构造\n（聚合过程）', fontsize=11, pad=10)
    
    # 阶段3：最终状态（高维Token）
    ax3 = axes[2]
    # 绘制Token（高维单纯形）
    token_positions = [(0.5, 0), (1.5, 0)]
    token_labels = ['ab', 'bc']
    for pos, label in zip(token_positions, token_labels):
        # 绘制更大的圆表示Token
        circle = plt.Circle(pos, 0.25, color='purple', zorder=3)
        ax3.add_patch(circle)
        ax3.text(pos[0], pos[1], label, ha='center', va='center', 
                fontsize=12, weight='bold', color='white', zorder=4)
    # 绘制连接
    ax3.plot([0.5, 1.5], [0, 0], 'purple', linewidth=2, zorder=2)
    ax3.set_xlim(-0.5, 2.5)
    ax3.set_ylim(-0.5, 0.5)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('阶段3: 高维Token复形\n（1-3维单纯形）', fontsize=11, pad=10)
    
    plt.suptitle('BPE的余极限过程：从原子复形到Token复形', 
                fontsize=14, weight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure2_bpe_pushout.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图2: BPE的推出构造过程")

# ==================== 插图3：逆向分裂的拉回构造过程 ====================

def figure3_inverse_splitting_pullback():
    """生成逆向分裂的拉回构造过程"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 阶段1：初始状态（全局交互复形）
    ax1 = axes[0]
    # 绘制有向加权复形
    nodes = {'A': (0, 0), 'B': (1.5, 0), 'C': (0.75, 1.3)}
    for node, pos in nodes.items():
        circle = plt.Circle(pos, 0.2, color='orange', zorder=3)
        ax1.add_patch(circle)
        ax1.text(pos[0], pos[1], node, ha='center', va='center', 
                fontsize=12, weight='bold', color='white', zorder=4)
    # 绘制有向边（带权重）
    edges = [
        (('A', 'B'), 0.8), (('B', 'C'), 0.6), (('C', 'A'), 0.4)
    ]
    for (start, end), weight in edges:
        start_pos = nodes[start]
        end_pos = nodes[end]
        # 绘制箭头
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        ax1.arrow(start_pos[0] + 0.15*dx, start_pos[1] + 0.15*dy,
                 dx*0.7, dy*0.7, head_width=0.1, head_length=0.1,
                 fc='red', ec='red', linewidth=2, zorder=2)
        # 标注权重
        mid_x, mid_y = (start_pos[0] + end_pos[0])/2, (start_pos[1] + end_pos[1])/2
        ax1.text(mid_x + 0.1, mid_y + 0.1, f'w={weight}', 
                fontsize=9, color='red', weight='bold')
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-0.5, 2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('阶段1: 全局交互复形\n（有向加权）', fontsize=11, pad=10)
    
    # 阶段2：中间状态（拉回构造）
    ax2 = axes[1]
    # 绘制分解过程
    for node, pos in nodes.items():
        circle = plt.Circle(pos, 0.2, color='orange', alpha=0.5, zorder=3)
        ax2.add_patch(circle)
        ax2.text(pos[0], pos[1], node, ha='center', va='center', 
                fontsize=12, weight='bold', color='gray', zorder=4)
    # 绘制分解箭头
    ax2.arrow(0.75, 0.65, 0, -0.3, head_width=0.15, head_length=0.1,
             fc='blue', ec='blue', linewidth=2, zorder=5)
    ax2.text(0.9, 0.5, '拉回构造', ha='left', fontsize=10, 
            color='blue', weight='bold')
    # 绘制分解后的原子簇
    cluster_positions = [(0.2, -0.5), (1.3, -0.5)]
    cluster_labels = ['{A,B}', '{B,C}']
    for pos, label in zip(cluster_positions, cluster_labels):
        rect = FancyBboxPatch((pos[0]-0.3, pos[1]-0.2), 0.6, 0.4,
                             boxstyle="round,pad=0.1", 
                             facecolor='lightgreen', edgecolor='green',
                             linewidth=2, zorder=3)
        ax2.add_patch(rect)
        ax2.text(pos[0], pos[1], label, ha='center', va='center', 
                fontsize=10, weight='bold', zorder=4)
    ax2.set_xlim(-0.5, 2.5)
    ax2.set_ylim(-1, 2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('阶段2: 拉回构造\n（分解过程）', fontsize=11, pad=10)
    
    # 阶段3：最终状态（极小原子簇）
    ax3 = axes[2]
    # 绘制极小原子簇
    final_clusters = [
        ((0.5, 0), '{A,B}'),
        ((1.5, 0), '{B,C}'),
        ((1, 0.8), '{A}')
    ]
    for pos, label in final_clusters:
        rect = FancyBboxPatch((pos[0]-0.25, pos[1]-0.15), 0.5, 0.3,
                             boxstyle="round,pad=0.05", 
                             facecolor='lightblue', edgecolor='blue',
                             linewidth=2, zorder=3)
        ax3.add_patch(rect)
        ax3.text(pos[0], pos[1], label, ha='center', va='center', 
                fontsize=10, weight='bold', zorder=4)
    ax3.set_xlim(-0.5, 2.5)
    ax3.set_ylim(-0.5, 1.5)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('阶段3: 极小原子簇\n（极限对象）', fontsize=11, pad=10)
    
    plt.suptitle('逆向分裂的极限过程：从全局交互复形到极小原子簇', 
                fontsize=14, weight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure3_inverse_splitting_pullback.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图3: 逆向分裂的拉回构造过程")

# ==================== 插图4：共轭复形的构造 ====================

def figure4_conjugate_complex():
    """生成共轭复形的构造可视化"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左图：原复形 K
    # 绘制原复形（简单的三角形）
    vertices_k = np.array([[0, 0], [2, 0], [1, 1.732]])
    triangle_k = Polygon(vertices_k, alpha=0.3, color='blue', 
                        edgecolor='blue', linewidth=2)
    ax1.add_patch(triangle_k)
    
    # 绘制边
    for i in range(3):
        ax1.plot([vertices_k[i, 0], vertices_k[(i+1)%3, 0]], 
                [vertices_k[i, 1], vertices_k[(i+1)%3, 1]], 
                'b-', linewidth=2)
    
    # 绘制顶点并标注
    labels_k = ['{a}', '{b}', '{c}']
    for i, (v, label) in enumerate(zip(vertices_k, labels_k)):
        ax1.scatter(v[0], v[1], s=200, c='blue', zorder=5)
        ax1.text(v[0], v[1] - 0.3, label, ha='center', fontsize=11, weight='bold')
    
    # 标注单纯形
    ax1.text(1, 0.6, '{a,b,c}', fontsize=10, ha='center', 
            style='italic', color='blue', weight='bold')
    ax1.text(1, -0.5, '{a,b}', fontsize=9, ha='center', style='italic', color='blue')
    ax1.text(0.3, 0.3, '{a,c}', fontsize=9, ha='center', style='italic', color='blue')
    ax1.text(1.7, 0.3, '{b,c}', fontsize=9, ha='center', style='italic', color='blue')
    
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-0.8, 2.2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('原复形 $K$\n顶点=原子，单纯形=Token', fontsize=12, pad=15)
    
    # 右图：共轭复形 K*
    # 绘制共轭复形的顶点（原复形的单纯形）
    vertices_kstar = [
        ((0.5, 0), '{a,b}'),
        ((1.5, 0), '{b,c}'),
        ((0.5, 1.2), '{a,c}'),
        ((1, 0.6), '{a,b,c}')
    ]
    
    for pos, label in vertices_kstar:
        circle = plt.Circle(pos, 0.25, color='purple', zorder=3)
        ax2.add_patch(circle)
        ax2.text(pos[0], pos[1], label, ha='center', va='center', 
                fontsize=10, weight='bold', color='white', zorder=4)
    
    # 绘制共轭复形的边（表示闭覆盖关系）
    edges_kstar = [
        ((0.5, 0), (1, 0.6)),
        ((1.5, 0), (1, 0.6)),
        ((0.5, 1.2), (1, 0.6))
    ]
    for (start, end) in edges_kstar:
        ax2.plot([start[0], end[0]], [start[1], end[1]], 
                'purple', linewidth=2, zorder=2, alpha=0.6)
    
    # 添加箭头表示转换
    arrow = FancyArrowPatch((2.7, 1), (3.3, 1), 
                           arrowstyle='<->', mutation_scale=25, 
                           color='red', linewidth=3, zorder=10)
    ax2.add_patch(arrow)
    ax2.text(3, 1.3, '顶点-单纯形\n反转', ha='center', fontsize=10, 
            color='red', weight='bold')
    
    ax2.set_xlim(-0.5, 4)
    ax2.set_ylim(-0.5, 1.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('共轭复形 $K^*$\n顶点=Token，单纯形=原子簇', fontsize=12, pad=15)
    
    plt.suptitle('共轭复形的构造：顶点-单纯形反转', 
                fontsize=14, weight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure4_conjugate_complex.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图4: 共轭复形的构造")

# ==================== 插图5：有向加权复形 ====================

def figure5_weighted_directed_complex():
    """生成有向加权复形的可视化"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 定义节点位置（物品）
    nodes = {
        '1': (0, 0),
        '2': (2, 0),
        '3': (1, 1.732),
        '4': (3, 1.732)
    }
    
    # 绘制节点
    for node, pos in nodes.items():
        circle = plt.Circle(pos, 0.3, color='orange', zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], f'物品{node}', ha='center', va='center', 
                fontsize=11, weight='bold', color='white', zorder=4)
    
    # 定义有向边和权重
    edges = [
        (('1', '2'), 0.8, 'black'),
        (('2', '3'), 0.6, 'black'),
        (('3', '1'), 0.4, 'black'),
        (('2', '4'), 0.7, 'black'),
        (('4', '3'), 0.5, 'black')
    ]
    
    # 绘制有向边
    for (start, end), weight, color in edges:
        start_pos = nodes[start]
        end_pos = nodes[end]
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length
        dy_norm = dy / length
        
        # 绘制箭头
        ax.arrow(start_pos[0] + 0.3*dx_norm, start_pos[1] + 0.3*dy_norm,
                dx*0.4, dy*0.4, head_width=0.15, head_length=0.15,
                fc=color, ec=color, linewidth=2.5, zorder=2)
        
        # 标注权重
        mid_x = start_pos[0] + 0.5*dx
        mid_y = start_pos[1] + 0.5*dy
        # 偏移标注位置避免重叠
        offset_x = -0.15*dy_norm
        offset_y = 0.15*dx_norm
        ax.text(mid_x + offset_x, mid_y + offset_y, f'w={weight}', 
               fontsize=9, color='red', weight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor='red', alpha=0.8), zorder=5)
    
    # 绘制2维单纯形（有向三角形）
    triangle_vertices = [nodes['1'], nodes['2'], nodes['3']]
    triangle = Polygon(triangle_vertices, alpha=0.2, color='green', 
                      edgecolor='green', linewidth=2, linestyle='--', zorder=1)
    ax.add_patch(triangle)
    ax.text(1, 0.6, '有向三角形\n(2维单纯形)', ha='center', fontsize=9, 
           style='italic', color='green', weight='bold')
    
    # 添加说明
    ax.text(1.5, -0.8, '有向边表示时序关系：物品i → 物品j', 
           fontsize=10, ha='center', style='italic')
    ax.text(1.5, -1.1, '权重w表示共现频率（基于AEP收敛）', 
           fontsize=10, ha='center', style='italic')
    
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-1.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('有向加权复形\n从交互序列构造全局交互复形', 
                fontsize=14, pad=20, weight='bold')
    plt.tight_layout()
    plt.savefig('images/figure5_weighted_directed_complex.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图5: 有向加权复形")

# ==================== 插图6：推出和拉回的交换图 ====================

def figure6_commutative_diagrams():
    """生成推出和拉回的交换图"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左图：推出（Pushout）
    # 绘制对象
    objects_pushout = {
        'M': (1, 2),
        'K': (0, 0),
        'L': (2, 0),
        'K⊔_M L': (1, -1.5)
    }
    
    for obj, pos in objects_pushout.items():
        rect = FancyBboxPatch((pos[0]-0.4, pos[1]-0.3), 0.8, 0.6,
                             boxstyle="round,pad=0.1", 
                             facecolor='lightblue', edgecolor='blue',
                             linewidth=2, zorder=3)
        ax1.add_patch(rect)
        ax1.text(pos[0], pos[1], obj, ha='center', va='center', 
                fontsize=10, weight='bold', zorder=4)
    
    # 绘制态射（箭头）
    arrows_pushout = [
        (objects_pushout['M'], objects_pushout['K'], 'f', 'blue'),
        (objects_pushout['M'], objects_pushout['L'], 'g', 'blue'),
        (objects_pushout['K'], objects_pushout['K⊔_M L'], 'ι₁', 'green'),
        (objects_pushout['L'], objects_pushout['K⊔_M L'], 'ι₂', 'green')
    ]
    
    for start, end, label, color in arrows_pushout:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        ax1.arrow(start[0] + 0.1*dx, start[1] + 0.1*dy,
                 dx*0.8, dy*0.8, head_width=0.15, head_length=0.15,
                 fc=color, ec=color, linewidth=2, zorder=2)
        mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
        offset = 0.2 if 'ι' in label else 0.15
        ax1.text(mid_x + offset, mid_y + offset, label, 
                fontsize=9, color=color, weight='bold', zorder=5)
    
    ax1.set_xlim(-1, 3)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('推出（Pushout）\n$K \sqcup_M L$', fontsize=12, pad=15, weight='bold')
    
    # 右图：拉回（Pullback）
    objects_pullback = {
        'K': (0, 0),
        'L': (2, 0),
        'M': (1, 2),
        'K×_M L': (1, -1.5)
    }
    
    for obj, pos in objects_pullback.items():
        rect = FancyBboxPatch((pos[0]-0.4, pos[1]-0.3), 0.8, 0.6,
                             boxstyle="round,pad=0.1", 
                             facecolor='lightcoral', edgecolor='red',
                             linewidth=2, zorder=3)
        ax2.add_patch(rect)
        ax2.text(pos[0], pos[1], obj, ha='center', va='center', 
                fontsize=10, weight='bold', zorder=4)
    
    # 绘制态射（箭头）
    arrows_pullback = [
        (objects_pullback['K'], objects_pullback['M'], 'f', 'red'),
        (objects_pullback['L'], objects_pullback['M'], 'g', 'red'),
        (objects_pullback['K×_M L'], objects_pullback['K'], 'π₁', 'green'),
        (objects_pullback['K×_M L'], objects_pullback['L'], 'π₂', 'green')
    ]
    
    for start, end, label, color in arrows_pullback:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        ax2.arrow(start[0] + 0.1*dx, start[1] + 0.1*dy,
                 dx*0.8, dy*0.8, head_width=0.15, head_length=0.15,
                 fc=color, ec=color, linewidth=2, zorder=2)
        mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
        offset = 0.2 if 'π' in label else 0.15
        ax2.text(mid_x + offset, mid_y + offset, label, 
                fontsize=9, color=color, weight='bold', zorder=5)
    
    ax2.set_xlim(-1, 3)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('拉回（Pullback）\n$K \times_M L$', fontsize=12, pad=15, weight='bold')
    
    plt.suptitle('范畴论交换图：推出与拉回', fontsize=14, weight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure6_commutative_diagrams.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 生成插图6: 推出和拉回的交换图")

# ==================== 主函数 ====================

def main():
    """生成所有插图"""
    print("开始生成复形范畴笔记插图...")
    print("=" * 50)
    
    figure1_simplicial_complex()
    figure2_bpe_pushout()
    figure3_inverse_splitting_pullback()
    figure4_conjugate_complex()
    figure5_weighted_directed_complex()
    figure6_commutative_diagrams()
    
    print("=" * 50)
    print("✓ 所有插图生成完成！")
    print(f"图片保存在: {os.path.abspath('images')}")

if __name__ == '__main__':
    main()
