"""
Simplicial Complex Category Notes - Figure Generation Script
Using plotly for better visualization
Requires: plotly, kaleido (for PNG export)
Install: pip install plotly kaleido
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import os

# Check for kaleido
try:
    import kaleido
except ImportError:
    print("Warning: kaleido not found. Installing...")
    print("Please run: pip install kaleido")
    print("Or: conda install -c conda-forge python-kaleido")

# Create images directory
os.makedirs('images', exist_ok=True)

# ==================== Figure 1: Simplicial Complex (Hypergraph) ====================

def figure1_simplicial_complex():
    """Generate simplicial complex visualization as hypergraph"""
    fig = go.Figure()
    
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
        x_coords = [vertices[i][0] for i in face] + [vertices[face[0]][0]]
        y_coords = [vertices[i][1] for i in face] + [vertices[face[0]][1]]
        fig.add_trace(go.Scatter(
            x=x_coords, y=y_coords,
            fill='toself',
            fillcolor='rgba(100, 150, 255, 0.1)',
            line=dict(color='rgba(100, 150, 255, 0.3)', width=1),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Draw 2-simplex (triangles) - more visible
    triangles = [
        [0, 1, 2], [0, 1, 3]
    ]
    for tri in triangles:
        x_coords = [vertices[i][0] for i in tri] + [vertices[tri[0]][0]]
        y_coords = [vertices[i][1] for i in tri] + [vertices[tri[0]][1]]
        fig.add_trace(go.Scatter(
            x=x_coords, y=y_coords,
            fill='toself',
            fillcolor='rgba(100, 150, 255, 0.3)',
            line=dict(color='rgba(50, 100, 200, 0.8)', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Draw 1-simplex (edges)
    edges = [
        (0, 1), (1, 2), (2, 0),
        (0, 3), (1, 3), (2, 3)
    ]
    for i, j in edges:
        fig.add_trace(go.Scatter(
            x=[vertices[i][0], vertices[j][0]],
            y=[vertices[i][1], vertices[j][1]],
            mode='lines',
            line=dict(color='black', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Draw 0-simplex (vertices)
    fig.add_trace(go.Scatter(
        x=vertices[:, 0],
        y=vertices[:, 1],
        mode='markers+text',
        marker=dict(size=20, color='black'),
        text=labels,
        textposition='bottom center',
        textfont=dict(size=14, color='black', family='Arial Black'),
        showlegend=False,
        hoverinfo='text',
        hovertext=[f'Vertex {l}' for l in labels]
    ))
    
    # Add dimension labels
    fig.add_annotation(x=0.5, y=0.3, text="0-dim: vertices", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    fig.add_annotation(x=0.5, y=0.5, text="1-dim: edges", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    fig.add_annotation(x=0.5, y=0.7, text="2-dim: triangles", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    fig.add_annotation(x=0.5, y=0.9, text="3-dim: tetrahedron", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    
    fig.update_layout(
        title=dict(
            text='Simplicial Complex (Hypergraph Visualization)',
            x=0.5,
            font=dict(size=16, family='Arial')
        ),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        width=800,
        height=700,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    fig.write_image('images/figure1_simplicial_complex.png', width=800, height=700, scale=2)
    print("✓ Generated Figure 1: Simplicial Complex")

# ==================== Figure 2: BPE Pushout Process (Hypergraph Iteration) ====================

def figure2_bpe_pushout():
    """Generate BPE pushout process: showing hypergraph step-by-step aggregation"""
    fig = make_subplots(
        rows=1, cols=4,
        subplot_titles=('Step 1: Atoms<br>(0-simplices)', 
                       'Step 2: Add Edges<br>(1-simplices)',
                       'Step 3: Pushout<br>(Merge to Tokens)',
                       'Step 4: Higher Dim<br>(2-simplices)'),
        horizontal_spacing=0.1
    )
    
    atoms = ['a', 'b', 'c', 'd']
    positions = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])
    
    # Step 1: Atoms only
    for i, (pos, atom) in enumerate(zip(positions, atoms)):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=30, color='blue'),
            text=atom,
            textposition='middle center',
            textfont=dict(size=12, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=1
        ))
    
    # Step 2: Add edges
    for i, (pos, atom) in enumerate(zip(positions, atoms)):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=30, color='blue'),
            text=atom,
            textposition='middle center',
            textfont=dict(size=12, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=2
        ))
    # Draw edges
    for i in range(len(positions) - 1):
        fig.add_trace(go.Scatter(
            x=[positions[i][0], positions[i+1][0]],
            y=[positions[i][1], positions[i+1][1]],
            mode='lines',
            line=dict(color='green', width=4),
            showlegend=False,
            row=1, col=2
        ))
    
    # Step 3: Merge to tokens
    token_positions = np.array([[0.5, 0], [1.5, 0], [2.5, 0]])
    token_labels = ['ab', 'bc', 'cd']
    for pos, label in zip(token_positions, token_labels):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=50, color='purple', symbol='ellipse', 
                        line=dict(width=2, color='purple')),
            text=label,
            textposition='middle center',
            textfont=dict(size=12, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=3
        ))
    # Show original atoms (faded)
    for pos, atom in zip(positions, atoms):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers',
            marker=dict(size=20, color='blue', opacity=0.3),
            showlegend=False,
            row=1, col=3
        ))
    
    # Step 4: Higher dimension aggregation
    big_token_pos = np.array([1.5, 0])
    # Draw triangle (2-simplex)
    triangle_vertices = np.array([[0.5, -0.3], [2.5, -0.3], [1.5, 0.3]])
    fig.add_trace(go.Scatter(
        x=list(triangle_vertices[:, 0]) + [triangle_vertices[0, 0]],
        y=list(triangle_vertices[:, 1]) + [triangle_vertices[0, 1]],
        fill='toself',
        fillcolor='rgba(255, 165, 0, 0.5)',
        line=dict(color='orange', width=2),
        showlegend=False,
        row=1, col=4
    ))
    fig.add_trace(go.Scatter(
        x=[big_token_pos[0]], y=[big_token_pos[1]],
        mode='markers+text',
        marker=dict(size=40, color='orange'),
        text='abc',
        textposition='middle center',
        textfont=dict(size=12, color='white', family='Arial Black'),
        showlegend=False,
        row=1, col=4
    ))
    
    # Update layout
    for i in range(1, 5):
        fig.update_xaxes(range=[-0.5, 3.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
        fig.update_yaxes(range=[-0.5, 0.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
    
    fig.update_layout(
        title=dict(
            text='BPE Colimit Process: Hypergraph Step-by-Step Aggregation',
            x=0.5,
            font=dict(size=14, family='Arial')
        ),
        plot_bgcolor='white',
        width=1600,
        height=400,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    fig.write_image('images/figure2_bpe_pushout.png', width=1600, height=400, scale=2)
    print("✓ Generated Figure 2: BPE Pushout Process")

# ==================== Figure 3: Inverse Splitting Pullback Process ====================

def figure3_inverse_splitting_pullback():
    """Generate inverse splitting pullback process: showing hypergraph step-by-step decomposition"""
    fig = make_subplots(
        rows=1, cols=4,
        subplot_titles=('Step 1: Global Complex<br>(2-simplex)', 
                       'Step 2: Decompose to Edges<br>(1-simplices)',
                       'Step 3: Pullback<br>(Filter Clusters)',
                       'Step 4: Minimal Clusters<br>(Limit Object)'),
        horizontal_spacing=0.1
    )
    
    # Step 1: 2-simplex (triangle)
    triangle_vertices = np.array([[0.5, 0], [2, 0], [1.25, 1.2]])
    labels = ['A', 'B', 'C']
    
    fig.add_trace(go.Scatter(
        x=list(triangle_vertices[:, 0]) + [triangle_vertices[0, 0]],
        y=list(triangle_vertices[:, 1]) + [triangle_vertices[0, 1]],
        fill='toself',
        fillcolor='rgba(255, 165, 0, 0.4)',
        line=dict(color='orange', width=2),
        showlegend=False,
        row=1, col=1
    ))
    for i, (v, label) in enumerate(zip(triangle_vertices, labels)):
        fig.add_trace(go.Scatter(
            x=[v[0]], y=[v[1]],
            mode='markers+text',
            marker=dict(size=30, color='orange'),
            text=label,
            textposition='middle center',
            textfont=dict(size=12, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=1
        ))
    
    # Step 2: Decompose to edges
    edges = [
        (triangle_vertices[0], triangle_vertices[1], 'AB'),
        (triangle_vertices[1], triangle_vertices[2], 'BC'),
        (triangle_vertices[2], triangle_vertices[0], 'CA')
    ]
    for start, end, label in edges:
        fig.add_trace(go.Scatter(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            mode='lines+text',
            line=dict(color='green', width=3),
            text=[None, label],
            textposition='top center',
            textfont=dict(size=10, color='green', family='Arial'),
            showlegend=False,
            row=1, col=2
        ))
    for v, label in zip(triangle_vertices, labels):
        fig.add_trace(go.Scatter(
            x=[v[0]], y=[v[1]],
            mode='markers+text',
            marker=dict(size=25, color='orange', opacity=0.6),
            text=label,
            textposition='middle center',
            textfont=dict(size=11, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=2
        ))
    
    # Step 3: Pullback (filter clusters)
    clusters = [
        (np.array([0.5, 0.3]), '{A,B}'),
        (np.array([1.25, 0.6]), '{B,C}')
    ]
    for pos, label in clusters:
        # Draw rectangle for cluster
        rect_x = [pos[0]-0.3, pos[0]+0.3, pos[0]+0.3, pos[0]-0.3, pos[0]-0.3]
        rect_y = [pos[1]-0.15, pos[1]-0.15, pos[1]+0.15, pos[1]+0.15, pos[1]-0.15]
        fig.add_trace(go.Scatter(
            x=rect_x, y=rect_y,
            fill='toself',
            fillcolor='rgba(144, 238, 144, 0.6)',
            line=dict(color='green', width=2),
            showlegend=False,
            row=1, col=3
        ))
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='text',
            text=label,
            textposition='middle center',
            textfont=dict(size=10, color='black', family='Arial Black'),
            showlegend=False,
            row=1, col=3
        ))
    
    # Step 4: Minimal clusters
    final_clusters = [
        (np.array([0.5, 0.2]), '{A,B}'),
        (np.array([1.25, 0.4]), '{B,C}'),
        (np.array([0.875, 0.8]), '{A}')
    ]
    for pos, label in final_clusters:
        rect_x = [pos[0]-0.25, pos[0]+0.25, pos[0]+0.25, pos[0]-0.25, pos[0]-0.25]
        rect_y = [pos[1]-0.12, pos[1]-0.12, pos[1]+0.12, pos[1]+0.12, pos[1]-0.12]
        fig.add_trace(go.Scatter(
            x=rect_x, y=rect_y,
            fill='toself',
            fillcolor='rgba(173, 216, 230, 0.7)',
            line=dict(color='blue', width=2),
            showlegend=False,
            row=1, col=4
        ))
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='text',
            text=label,
            textposition='middle center',
            textfont=dict(size=9, color='black', family='Arial Black'),
            showlegend=False,
            row=1, col=4
        ))
    
    # Update layout
    for i in range(1, 5):
        fig.update_xaxes(range=[-0.5, 2.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
        fig.update_yaxes(range=[-0.5, 1.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
    
    fig.update_layout(
        title=dict(
            text='Inverse Splitting Limit Process: Hypergraph Step-by-Step Decomposition',
            x=0.5,
            font=dict(size=14, family='Arial')
        ),
        plot_bgcolor='white',
        width=1600,
        height=400,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    fig.write_image('images/figure3_inverse_splitting_pullback.png', width=1600, height=400, scale=2)
    print("✓ Generated Figure 3: Inverse Splitting Pullback Process")

# ==================== Figure 4: Conjugate Complex Construction ====================

def figure4_conjugate_complex():
    """Generate conjugate complex construction visualization"""
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Original Complex $K$<br>Vertices=Atoms, Simplices=Tokens',
                       'Conjugate Complex $K^*$<br>Vertices=Tokens, Simplices=Atom Clusters'),
        horizontal_spacing=0.15
    )
    
    # Left: Original complex K
    vertices_k = np.array([[0.5, 0], [1.5, 0], [1, 0.866]])
    labels_k = ['a', 'b', 'c']
    
    # Draw triangle
    fig.add_trace(go.Scatter(
        x=list(vertices_k[:, 0]) + [vertices_k[0, 0]],
        y=list(vertices_k[:, 1]) + [vertices_k[0, 1]],
        fill='toself',
        fillcolor='rgba(100, 150, 255, 0.3)',
        line=dict(color='blue', width=2),
        showlegend=False,
        row=1, col=1
    ))
    # Draw edges
    for i in range(3):
        fig.add_trace(go.Scatter(
            x=[vertices_k[i, 0], vertices_k[(i+1)%3, 0]],
            y=[vertices_k[i, 1], vertices_k[(i+1)%3, 1]],
            mode='lines',
            line=dict(color='blue', width=2),
            showlegend=False,
            row=1, col=1
        ))
    # Draw vertices
    for v, label in zip(vertices_k, labels_k):
        fig.add_trace(go.Scatter(
            x=[v[0]], y=[v[1]],
            mode='markers+text',
            marker=dict(size=25, color='blue'),
            text=label,
            textposition='bottom center',
            textfont=dict(size=11, color='blue', family='Arial Black'),
            showlegend=False,
            row=1, col=1
        ))
    fig.add_annotation(x=1, y=0.5, text="{a,b,c}", 
                      showarrow=False, font=dict(size=10, color='blue', style='italic'),
                      row=1, col=1)
    
    # Right: Conjugate complex K*
    kstar_vertices = [
        (np.array([0.5, 0.2]), '{a,b}'),
        (np.array([1.5, 0.2]), '{b,c}'),
        (np.array([1, 0.866]), '{a,b,c}')
    ]
    
    for pos, label in kstar_vertices:
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=30, color='purple'),
            text=label,
            textposition='middle center',
            textfont=dict(size=10, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=2
        ))
    
    # Draw edges in K*
    edges_kstar = [
        (kstar_vertices[0][0], kstar_vertices[2][0]),
        (kstar_vertices[1][0], kstar_vertices[2][0])
    ]
    for start, end in edges_kstar:
        fig.add_trace(go.Scatter(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            mode='lines',
            line=dict(color='purple', width=2, dash='dash'),
            showlegend=False,
            row=1, col=2
        ))
    
    fig.add_annotation(x=1, y=0.5, text="Atom Clusters", 
                      showarrow=False, font=dict(size=10, color='purple', style='italic'),
                      row=1, col=2)
    
    # Add transformation arrow
    fig.add_annotation(
        x=1.5, y=0.5,
        text="Vertex↔Simplex<br>Reversal",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='red',
        ax=0, ay=0,
        font=dict(size=11, color='red', family='Arial Black'),
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='red',
        borderwidth=2
    )
    
    # Update layout
    for i in range(1, 3):
        fig.update_xaxes(range=[-0.3, 2.3], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
        fig.update_yaxes(range=[-0.5, 1.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
    
    fig.update_layout(
        title=dict(
            text='Conjugate Complex Construction: Vertex-Simplex Reversal',
            x=0.5,
            font=dict(size=14, family='Arial')
        ),
        plot_bgcolor='white',
        width=1200,
        height=500,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    fig.write_image('images/figure4_conjugate_complex.png', width=1200, height=500, scale=2)
    print("✓ Generated Figure 4: Conjugate Complex Construction")

# ==================== Figure 5: Weighted Directed Complex ====================

def figure5_weighted_directed_complex():
    """Generate weighted directed complex visualization"""
    fig = go.Figure()
    
    # Define node positions (items)
    nodes = {
        '1': np.array([0, 0]),
        '2': np.array([2, 0]),
        '3': np.array([1, 1.732]),
        '4': np.array([3, 1.732])
    }
    
    # Draw nodes
    for node_id, pos in nodes.items():
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=40, color='orange', line=dict(width=2, color='darkorange')),
            text=f'Item {node_id}',
            textposition='middle center',
            textfont=dict(size=11, color='white', family='Arial Black'),
            showlegend=False,
            name=node_id
        ))
    
    # Define directed edges with weights
    edges = [
        (('1', '2'), 0.8),
        (('2', '3'), 0.6),
        (('3', '1'), 0.4),
        (('2', '4'), 0.7),
        (('4', '3'), 0.5)
    ]
    
    # Draw directed edges with arrows using annotations
    for (start, end), weight in edges:
        start_pos = nodes[start]
        end_pos = nodes[end]
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length
        dy_norm = dy / length
        
        # Calculate arrow start and end (avoiding node overlap)
        arrow_start_x = start_pos[0] + 0.3 * dx_norm
        arrow_start_y = start_pos[1] + 0.3 * dy_norm
        arrow_end_x = end_pos[0] - 0.3 * dx_norm
        arrow_end_y = end_pos[1] - 0.3 * dy_norm
        
        # Add arrow annotation (plotly handles arrow drawing)
        fig.add_annotation(
            x=arrow_end_x,
            y=arrow_end_y,
            ax=arrow_start_x,
            ay=arrow_start_y,
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=3,
            arrowcolor='red',
            showarrow=True,
            axref='x',
            ayref='y',
            xref='x',
            yref='y'
        )
        
        # Label weight
        mid_x = (start_pos[0] + end_pos[0]) / 2
        mid_y = (start_pos[1] + end_pos[1]) / 2
        offset_x = -0.15 * dy_norm
        offset_y = 0.15 * dx_norm
        fig.add_annotation(
            x=mid_x + offset_x,
            y=mid_y + offset_y,
            text=f'w={weight}',
            showarrow=False,
            font=dict(size=10, color='red', family='Arial Black'),
            bgcolor='rgba(255, 255, 255, 0.9)',
            bordercolor='red',
            borderwidth=1,
            borderpad=3
        )
    
    # Draw 2-simplex (directed triangle)
    triangle_vertices = np.array([nodes['1'], nodes['2'], nodes['3']])
    fig.add_trace(go.Scatter(
        x=list(triangle_vertices[:, 0]) + [triangle_vertices[0, 0]],
        y=list(triangle_vertices[:, 1]) + [triangle_vertices[0, 1]],
        fill='toself',
        fillcolor='rgba(0, 255, 0, 0.2)',
        line=dict(color='green', width=2, dash='dash'),
        showlegend=False,
        hoverinfo='skip'
    ))
    fig.add_annotation(x=1, y=0.6, text="Directed Triangle<br>(2-simplex)", 
                      showarrow=False, font=dict(size=9, color='green', style='italic'))
    
    fig.add_annotation(x=1.5, y=-0.8, text="Directed edges show temporal relations: Item i → Item j", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    fig.add_annotation(x=1.5, y=-1.1, text="Weights w represent co-occurrence frequency (AEP convergence)", 
                      showarrow=False, font=dict(size=10, color='gray', style='italic'))
    
    fig.update_layout(
        title=dict(
            text='Weighted Directed Complex: From Interaction Sequences to Global Complex',
            x=0.5,
            font=dict(size=14, family='Arial')
        ),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 3.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 2.5]),
        plot_bgcolor='white',
        width=1000,
        height=800,
        margin=dict(l=20, r=20, t=80, b=100)
    )
    
    fig.write_image('images/figure5_weighted_directed_complex.png', width=1000, height=800, scale=2)
    print("✓ Generated Figure 5: Weighted Directed Complex")

# ==================== Figure 6: Conjugate Transformation ====================

def figure6_conjugate_transformation():
    """Generate conjugate complex hypergraph transformation"""
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=('Original Complex $K$<br>Vertices=Atoms, Simplices=Tokens',
                       'Transformation',
                       'Conjugate Complex $K^*$<br>Vertices=Tokens, Simplices=Atom Clusters'),
        horizontal_spacing=0.1
    )
    
    # Left: Original complex K
    vertices_k = np.array([[0.5, 0], [1.5, 0], [1, 0.866]])
    labels_k = ['a', 'b', 'c']
    
    fig.add_trace(go.Scatter(
        x=list(vertices_k[:, 0]) + [vertices_k[0, 0]],
        y=list(vertices_k[:, 1]) + [vertices_k[0, 1]],
        fill='toself',
        fillcolor='rgba(100, 150, 255, 0.3)',
        line=dict(color='blue', width=2),
        showlegend=False,
        row=1, col=1
    ))
    for i in range(3):
        fig.add_trace(go.Scatter(
            x=[vertices_k[i, 0], vertices_k[(i+1)%3, 0]],
            y=[vertices_k[i, 1], vertices_k[(i+1)%3, 1]],
            mode='lines',
            line=dict(color='blue', width=2),
            showlegend=False,
            row=1, col=1
        ))
    for v, label in zip(vertices_k, labels_k):
        fig.add_trace(go.Scatter(
            x=[v[0]], y=[v[1]],
            mode='markers+text',
            marker=dict(size=25, color='blue'),
            text=label,
            textposition='bottom center',
            textfont=dict(size=11, color='blue', family='Arial Black'),
            showlegend=False,
            row=1, col=1
        ))
    
    # Middle: Transformation arrow (bidirectional)
    fig.add_annotation(
        x=1.5, y=0.5,
        text="Vertex↔Simplex<br>Reversal",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='red',
        ax=-0.3, ay=0,
        font=dict(size=11, color='red', family='Arial Black'),
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='red',
        borderwidth=2,
        row=1, col=2
    )
    # Add reverse arrow
    fig.add_annotation(
        x=0.5, y=0.5,
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='red',
        ax=0.3, ay=0,
        row=1, col=2
    )
    
    # Right: Conjugate complex K*
    kstar_vertices = [
        (np.array([0.5, 0.2]), '{a,b}'),
        (np.array([1.5, 0.2]), '{b,c}'),
        (np.array([1, 0.866]), '{a,b,c}')
    ]
    
    for pos, label in kstar_vertices:
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            marker=dict(size=30, color='purple'),
            text=label,
            textposition='middle center',
            textfont=dict(size=10, color='white', family='Arial Black'),
            showlegend=False,
            row=1, col=3
        ))
    
    edges_kstar = [
        (kstar_vertices[0][0], kstar_vertices[2][0]),
        (kstar_vertices[1][0], kstar_vertices[2][0])
    ]
    for start, end in edges_kstar:
        fig.add_trace(go.Scatter(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            mode='lines',
            line=dict(color='purple', width=2, dash='dash'),
            showlegend=False,
            row=1, col=3
        ))
    
    # Update layout
    for i in range(1, 4):
        fig.update_xaxes(range=[-0.3, 2.3], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
        fig.update_yaxes(range=[-0.5, 1.5], showgrid=False, zeroline=False, 
                         showticklabels=False, row=1, col=i)
    
    fig.update_layout(
        title=dict(
            text='Conjugate Complex Construction: Hypergraph Vertex-Simplex Reversal',
            x=0.5,
            font=dict(size=14, family='Arial')
        ),
        plot_bgcolor='white',
        width=1500,
        height=500,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    fig.write_image('images/figure6_conjugate_transformation.png', width=1500, height=500, scale=2)
    print("✓ Generated Figure 6: Conjugate Transformation")

# ==================== Main Function ====================

def main():
    """Generate all figures"""
    print("Starting to generate Simplicial Complex Category figures...")
    print("=" * 60)
    
    # Check for kaleido
    try:
        import kaleido
    except ImportError:
        print("ERROR: kaleido is required for PNG export!")
        print("Please install: pip install kaleido")
        print("Or: conda install -c conda-forge python-kaleido")
        return
    
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
        print("\nIf you see 'kaleido' related errors, please install:")
        print("  pip install kaleido")
        print("Or: conda install -c conda-forge python-kaleido")

if __name__ == '__main__':
    main()
