"""
Simplicial Complex Category Notes - Figure Generation Script
Using matplotlib for PNG export (no external dependencies needed)
All text in English to avoid font issues
Requires: matplotlib, numpy
Install: pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
from matplotlib.patches import FancyArrow
import numpy as np
import os

# Create images directory
os.makedirs('images', exist_ok=True)

# Set matplotlib style for better quality
plt.style.use('default')
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# ==================== Figure 1: Simplicial Complex (Hypergraph) ====================

def figure1_simplicial_complex():
    """Generate simplicial complex visualization as hypergraph"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define vertices (0-simplices)
    vertices = np.array([
        [0, 0],      # a
        [2, 0],      # b
        [1, 1.732],  # c
        [1, 0.577]   # d
    ])
    labels = ['a', 'b', 'c', 'd']
    
    # Draw 3-simplex (tetrahedron) faces with transparency
    tetra_faces = [
        [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]
    ]
    for face in tetra_faces:
        triangle = Polygon(vertices[face], closed=True, 
                          facecolor='lightblue', alpha=0.1,
                          edgecolor='lightblue', linewidth=1)
        ax.add_patch(triangle)
    
    # Draw 2-simplex (triangles) - more visible
    triangles = [
        [0, 1, 2], [0, 1, 3]
    ]
    for tri in triangles:
        triangle = Polygon(vertices[tri], closed=True,
                          facecolor='lightblue', alpha=0.3,
                          edgecolor='blue', linewidth=2)
        ax.add_patch(triangle)
    
    # Draw 1-simplex (edges)
    edges = [
        (0, 1), (1, 2), (2, 0),
        (0, 3), (1, 3), (2, 3)
    ]
    for i, j in edges:
        ax.plot([vertices[i][0], vertices[j][0]], 
                [vertices[i][1], vertices[j][1]], 
                'k-', linewidth=2)
    
    # Draw 0-simplex (vertices)
    for i, (v, label) in enumerate(zip(vertices, labels)):
        ax.plot(v[0], v[1], 'ko', markersize=15)
        ax.text(v[0], v[1]-0.15, label, ha='center', va='top',
                fontsize=14, fontweight='bold')
    
    # Add dimension labels
    ax.text(0.5, 0.3, "0-dim: vertices", fontsize=10, 
            color='gray', style='italic')
    ax.text(0.5, 0.5, "1-dim: edges", fontsize=10, 
            color='gray', style='italic')
    ax.text(0.5, 0.7, "2-dim: triangles", fontsize=10, 
            color='gray', style='italic')
    ax.text(0.5, 0.9, "3-dim: tetrahedron", fontsize=10, 
            color='gray', style='italic')
    
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Simplicial Complex (Hypergraph Visualization)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('images/figure1_simplicial_complex.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 1: Simplicial Complex")

# ==================== Figure 2: BPE Pushout Process (Hypergraph Iteration) ====================

def figure2_bpe_pushout():
    """Generate BPE pushout process: showing hypergraph step-by-step aggregation"""
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    
    atoms = ['a', 'b', 'c', 'd']
    positions = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])
    
    # Step 1: Atoms only
    ax = axes[0]
    for pos, atom in zip(positions, atoms):
        circle = Circle(pos, 0.3, color='blue', zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], atom, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=4)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 1: Atoms\n(0-simplices)', fontsize=11, fontweight='bold')
    
    # Step 2: Add edges
    ax = axes[1]
    for pos, atom in zip(positions, atoms):
        circle = Circle(pos, 0.3, color='blue', zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], atom, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=4)
    for i in range(len(positions) - 1):
        ax.plot([positions[i][0], positions[i+1][0]], 
                [positions[i][1], positions[i+1][1]], 
                'g-', linewidth=4, zorder=1)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 2: Add Edges\n(1-simplices)', fontsize=11, fontweight='bold')
    
    # Step 3: Merge to tokens
    ax = axes[2]
    token_positions = np.array([[0.5, 0], [1.5, 0], [2.5, 0]])
    token_labels = ['ab', 'bc', 'cd']
    for pos, label in zip(token_positions, token_labels):
        ellipse = Ellipse(pos, 0.8, 0.4, color='purple', zorder=3)
        ax.add_patch(ellipse)
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=4)
    # Show original atoms (faded)
    for pos, atom in zip(positions, atoms):
        circle = Circle(pos, 0.2, color='blue', alpha=0.3, zorder=2)
        ax.add_patch(circle)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 3: Pushout\n(Merge to Tokens)', fontsize=11, fontweight='bold')
    
    # Step 4: Higher dimension aggregation
    ax = axes[3]
    big_token_pos = np.array([1.5, 0])
    # Draw triangle (2-simplex)
    triangle_vertices = np.array([[0.5, -0.3], [2.5, -0.3], [1.5, 0.3]])
    triangle = Polygon(triangle_vertices, closed=True,
                      facecolor='orange', alpha=0.5,
                      edgecolor='orange', linewidth=2, zorder=1)
    ax.add_patch(triangle)
    circle = Circle(big_token_pos, 0.4, color='orange', zorder=3)
    ax.add_patch(circle)
    ax.text(big_token_pos[0], big_token_pos[1], 'abc', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white', zorder=4)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 4: Higher Dim\n(2-simplices)', fontsize=11, fontweight='bold')
    
    plt.suptitle('BPE Colimit Process: Hypergraph Step-by-Step Aggregation',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure2_bpe_pushout.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 2: BPE Pushout Process")

# ==================== Figure 3: Inverse Splitting Pullback Process ====================

def figure3_inverse_splitting_pullback():
    """Generate inverse splitting pullback process: showing hypergraph step-by-step decomposition"""
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    
    # Step 1: 2-simplex (triangle)
    ax = axes[0]
    triangle_vertices = np.array([[0.5, 0], [2, 0], [1.25, 1.2]])
    labels = ['A', 'B', 'C']
    triangle = Polygon(triangle_vertices, closed=True,
                      facecolor='orange', alpha=0.4,
                      edgecolor='orange', linewidth=2)
    ax.add_patch(triangle)
    for v, label in zip(triangle_vertices, labels):
        circle = Circle(v, 0.15, color='orange', zorder=3)
        ax.add_patch(circle)
        ax.text(v[0], v[1], label, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white', zorder=4)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 1: Global Complex\n(2-simplex)', fontsize=11, fontweight='bold')
    
    # Step 2: Decompose to edges
    ax = axes[1]
    edges = [
        (triangle_vertices[0], triangle_vertices[1], 'AB'),
        (triangle_vertices[1], triangle_vertices[2], 'BC'),
        (triangle_vertices[2], triangle_vertices[0], 'CA')
    ]
    for start, end, label in edges:
        ax.plot([start[0], end[0]], [start[1], end[1]], 
                'g-', linewidth=3, zorder=1)
        mid = (start + end) / 2
        ax.text(mid[0], mid[1]+0.1, label, ha='center', va='bottom',
                fontsize=10, color='green', fontweight='bold')
    for v, label in zip(triangle_vertices, labels):
        circle = Circle(v, 0.12, color='orange', alpha=0.6, zorder=2)
        ax.add_patch(circle)
        ax.text(v[0], v[1], label, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white', zorder=3)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 2: Decompose to Edges\n(1-simplices)', fontsize=11, fontweight='bold')
    
    # Step 3: Pullback (filter clusters)
    ax = axes[2]
    clusters = [
        (np.array([0.5, 0.3]), '{A,B}'),
        (np.array([1.25, 0.6]), '{B,C}')
    ]
    for pos, label in clusters:
        rect = FancyBboxPatch((pos[0]-0.3, pos[1]-0.15), 0.6, 0.3,
                              boxstyle="round,pad=0.05",
                              facecolor='lightgreen', alpha=0.6,
                              edgecolor='green', linewidth=2)
        ax.add_patch(rect)
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=10, fontweight='bold', color='black')
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 3: Pullback\n(Filter Clusters)', fontsize=11, fontweight='bold')
    
    # Step 4: Minimal clusters
    ax = axes[3]
    final_clusters = [
        (np.array([0.5, 0.2]), '{A,B}'),
        (np.array([1.25, 0.4]), '{B,C}'),
        (np.array([0.875, 0.8]), '{A}')
    ]
    for pos, label in final_clusters:
        rect = FancyBboxPatch((pos[0]-0.25, pos[1]-0.12), 0.5, 0.24,
                              boxstyle="round,pad=0.05",
                              facecolor='lightblue', alpha=0.7,
                              edgecolor='blue', linewidth=2)
        ax.add_patch(rect)
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=9, fontweight='bold', color='black')
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Step 4: Minimal Clusters\n(Limit Object)', fontsize=11, fontweight='bold')
    
    plt.suptitle('Inverse Splitting Limit Process: Hypergraph Step-by-Step Decomposition',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/figure3_inverse_splitting_pullback.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 3: Inverse Splitting Pullback Process")

# ==================== Figure 4: Conjugate Complex Construction ====================

def figure4_conjugate_complex():
    """Generate conjugate complex construction visualization"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: Original complex K
    ax = axes[0]
    vertices_k = np.array([[0.5, 0], [1.5, 0], [1, 0.866]])
    labels_k = ['a', 'b', 'c']
    
    # Draw triangle
    triangle = Polygon(vertices_k, closed=True,
                      facecolor='lightblue', alpha=0.3,
                      edgecolor='blue', linewidth=2)
    ax.add_patch(triangle)
    # Draw edges
    for i in range(3):
        ax.plot([vertices_k[i, 0], vertices_k[(i+1)%3, 0]],
                [vertices_k[i, 1], vertices_k[(i+1)%3, 1]],
                'b-', linewidth=2)
    # Draw vertices
    for v, label in zip(vertices_k, labels_k):
        circle = Circle(v, 0.12, color='blue', zorder=3)
        ax.add_patch(circle)
        ax.text(v[0], v[1]-0.15, label, ha='center', va='top',
                fontsize=11, fontweight='bold', color='blue')
    ax.text(1, 0.5, "{a,b,c}", ha='center', va='center',
            fontsize=10, color='blue', style='italic')
    ax.set_xlim(-0.3, 2.3)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Original Complex $K$\nVertices=Atoms, Simplices=Tokens',
                 fontsize=11, fontweight='bold')
    
    # Right: Conjugate complex K*
    ax = axes[1]
    kstar_vertices = [
        (np.array([0.5, 0.2]), '{a,b}'),
        (np.array([1.5, 0.2]), '{b,c}'),
        (np.array([1, 0.866]), '{a,b,c}')
    ]
    
    for pos, label in kstar_vertices:
        circle = Circle(pos, 0.15, color='purple', zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=4)
    
    # Draw edges in K*
    edges_kstar = [
        (kstar_vertices[0][0], kstar_vertices[2][0]),
        (kstar_vertices[1][0], kstar_vertices[2][0])
    ]
    for start, end in edges_kstar:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                'purple', linewidth=2, linestyle='--', zorder=1)
    
    ax.text(1, 0.5, "Atom Clusters", ha='center', va='center',
            fontsize=10, color='purple', style='italic')
    ax.set_xlim(-0.3, 2.3)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Conjugate Complex $K^*$\nVertices=Tokens, Simplices=Atom Clusters',
                 fontsize=11, fontweight='bold')
    
    # Add transformation arrow
    fig.text(0.5, 0.5, "Vertex↔Simplex\nReversal", 
             ha='center', va='center', fontsize=12, 
             fontweight='bold', color='red',
             bbox=dict(boxstyle='round', facecolor='white', 
                      edgecolor='red', linewidth=2))
    
    plt.suptitle('Conjugate Complex Construction: Vertex-Simplex Reversal',
                 fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/figure4_conjugate_complex.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 4: Conjugate Complex Construction")

# ==================== Figure 5: Weighted Directed Complex ====================

def figure5_weighted_directed_complex():
    """Generate weighted directed complex visualization"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define node positions (items)
    nodes = {
        '1': np.array([0, 0]),
        '2': np.array([2, 0]),
        '3': np.array([1, 1.732]),
        '4': np.array([3, 1.732])
    }
    
    # Draw nodes
    for node_id, pos in nodes.items():
        circle = Circle(pos, 0.2, color='orange', 
                       edgecolor='darkorange', linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], f'Item {node_id}', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white', zorder=4)
    
    # Define directed edges with weights
    edges = [
        (('1', '2'), 0.8),
        (('2', '3'), 0.6),
        (('3', '1'), 0.4),
        (('2', '4'), 0.7),
        (('4', '3'), 0.5)
    ]
    
    # Draw directed edges with arrows
    for (start, end), weight in edges:
        start_pos = nodes[start]
        end_pos = nodes[end]
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length
        dy_norm = dy / length
        
        # Calculate arrow start and end (avoiding node overlap)
        arrow_start_x = start_pos[0] + 0.2 * dx_norm
        arrow_start_y = start_pos[1] + 0.2 * dy_norm
        arrow_end_x = end_pos[0] - 0.2 * dx_norm
        arrow_end_y = end_pos[1] - 0.2 * dy_norm
        
        # Draw arrow
        arrow = FancyArrowPatch((arrow_start_x, arrow_start_y),
                                (arrow_end_x, arrow_end_y),
                                arrowstyle='->', mutation_scale=20,
                                color='red', linewidth=3, zorder=1)
        ax.add_patch(arrow)
        
        # Label weight
        mid_x = (start_pos[0] + end_pos[0]) / 2
        mid_y = (start_pos[1] + end_pos[1]) / 2
        offset_x = -0.15 * dy_norm
        offset_y = 0.15 * dx_norm
        ax.text(mid_x + offset_x, mid_y + offset_y, f'w={weight}',
                ha='center', va='center', fontsize=10, 
                fontweight='bold', color='red',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor='red', linewidth=1))
    
    # Draw 2-simplex (directed triangle)
    triangle_vertices = np.array([nodes['1'], nodes['2'], nodes['3']])
    triangle = Polygon(triangle_vertices, closed=True,
                      facecolor='lightgreen', alpha=0.2,
                      edgecolor='green', linewidth=2, linestyle='--', zorder=0)
    ax.add_patch(triangle)
    ax.text(1, 0.6, "Directed Triangle\n(2-simplex)", ha='center', va='center',
            fontsize=9, color='green', style='italic')
    
    ax.text(1.5, -0.8, "Directed edges show temporal relations: Item i → Item j",
            ha='center', va='center', fontsize=10, color='gray', style='italic')
    ax.text(1.5, -1.1, "Weights w represent co-occurrence frequency (AEP convergence)",
            ha='center', va='center', fontsize=10, color='gray', style='italic')
    
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-1.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Weighted Directed Complex: From Interaction Sequences to Global Complex',
                 fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('images/figure5_weighted_directed_complex.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 5: Weighted Directed Complex")

# ==================== Figure 6: Conjugate Transformation ====================

def figure6_conjugate_transformation():
    """Generate conjugate complex hypergraph transformation"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Left: Original complex K
    ax = axes[0]
    vertices_k = np.array([[0.5, 0], [1.5, 0], [1, 0.866]])
    labels_k = ['a', 'b', 'c']
    
    triangle = Polygon(vertices_k, closed=True,
                      facecolor='lightblue', alpha=0.3,
                      edgecolor='blue', linewidth=2)
    ax.add_patch(triangle)
    for i in range(3):
        ax.plot([vertices_k[i, 0], vertices_k[(i+1)%3, 0]],
                [vertices_k[i, 1], vertices_k[(i+1)%3, 1]],
                'b-', linewidth=2)
    for v, label in zip(vertices_k, labels_k):
        circle = Circle(v, 0.12, color='blue', zorder=3)
        ax.add_patch(circle)
        ax.text(v[0], v[1]-0.15, label, ha='center', va='top',
                fontsize=11, fontweight='bold', color='blue')
    ax.set_xlim(-0.3, 2.3)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Original Complex $K$\nVertices=Atoms, Simplices=Tokens',
                 fontsize=11, fontweight='bold')
    
    # Middle: Transformation arrow
    ax = axes[1]
    ax.arrow(0.3, 0.5, 0.4, 0, head_width=0.1, head_length=0.1,
             fc='red', ec='red', linewidth=3, zorder=2)
    ax.arrow(0.7, 0.5, -0.4, 0, head_width=0.1, head_length=0.1,
             fc='red', ec='red', linewidth=3, zorder=2)
    ax.text(0.5, 0.5, "Vertex↔Simplex\nReversal", ha='center', va='center',
            fontsize=12, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='white',
                     edgecolor='red', linewidth=2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Right: Conjugate complex K*
    ax = axes[2]
    kstar_vertices = [
        (np.array([0.5, 0.2]), '{a,b}'),
        (np.array([1.5, 0.2]), '{b,c}'),
        (np.array([1, 0.866]), '{a,b,c}')
    ]
    
    for pos, label in kstar_vertices:
        circle = Circle(pos, 0.15, color='purple', zorder=3)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=4)
    
    edges_kstar = [
        (kstar_vertices[0][0], kstar_vertices[2][0]),
        (kstar_vertices[1][0], kstar_vertices[2][0])
    ]
    for start, end in edges_kstar:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                'purple', linewidth=2, linestyle='--', zorder=1)
    
    ax.set_xlim(-0.3, 2.3)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Conjugate Complex $K^*$\nVertices=Tokens, Simplices=Atom Clusters',
                 fontsize=11, fontweight='bold')
    
    plt.suptitle('Conjugate Complex Construction: Hypergraph Vertex-Simplex Reversal',
                 fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/figure6_conjugate_transformation.png', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated Figure 6: Conjugate Transformation")

# ==================== Main Function ====================

def main():
    """Generate all figures"""
    print("Starting to generate Simplicial Complex Category figures...")
    print("=" * 60)
    
    try:
        figure1_simplicial_complex()
        figure2_bpe_pushout()
        figure3_inverse_splitting_pullback()
        figure4_conjugate_complex()
        figure5_weighted_directed_complex()
        figure6_conjugate_transformation()
        
        print("=" * 60)
        print("✓ All figures generated successfully!")
        print(f"Images saved in: {os.path.abspath('images')}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
