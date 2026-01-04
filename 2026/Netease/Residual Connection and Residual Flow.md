# Residual Connection and Residual Flow

## 1. Background&Motivation 
### Gradient Propagation in Deep Neural Networks

Consider an $L$-layer deep neural network defined by the forward recursion
$$
x_{l+1} := F_l(x_l, \theta_l), \quad l = 0, 1, \dots, L-1,
$$
where $x_l$ and $\theta_l$ denote the intermediate **feature representation** and  **parameters** respectively. Both $x_l$ and $\theta_l$ are tensors of arbitrary shapes, and the index $l$ refers to the layer depth rather than tensor components.
Let $\mathcal{L}(x_L, \Phi)$ be a loss function applied to the final output $x_L$, with $\Phi$ denoting additional parameters unrelated to the network backbone.

By the chain rule, the gradient of the loss with respect to $\theta_l$ can be expressed in an abstract Jacobian form as

$$
\frac{\partial \mathcal{L}}{\partial \theta_l}=
\frac{\partial \mathcal{L}}{\partial x_L}
\frac{\partial x_{l+1}}{\partial \theta_l}
\prod_{i=l+1}^{L-1}
\frac{\partial x_{i+1}}{\partial x_i}.
$$
All derivatives above are understood as Jacobian operators between appropriate tensor spaces.When expanded element-wise, the chain rule involves tensor-valued Jacobians and contractions, which are omitted for clarity.

Additionally, we can include the activation functions in the chain-rule formulation by representing each layer as a composition of a linear operator and a nonlinear activation, $$x_{l+1} := \sigma_l(W_l x_l + b_l),$$ 
where $W_l$ is a linear map and $\sigma_l$ a pointwise nonlinear operator. 
Then the layerwise Jacobian is $$J_l := \frac{\partial x_{l+1}} { \partial x_l} = \operatorname{diag}(\sigma_l'(h_l))\, W_l,$$ 
and the full backpropagated gradient from the loss $\mathcal{L}$ can be expressed as $$\frac{\partial \mathcal{L}} {\partial x_0} = \left(\prod_{l=0}^{L-1} J_l\right) \frac{\partial \mathcal{L}}{ \partial x_L},$$ where the product is understood as an ordered composition of linear operators. The stability of gradient propagation is determined by the norm of this operator product; specifically, using the operator (spectral) norm $\| \cdot \|_\infty$ (largest singular value), we have $$\|\partial \mathcal{L} / \partial x_0\|_\infty \le \prod_{l=0}^{L-1} \|J_l\|_\infty \|\partial \mathcal{L} / \partial x_L\|_\infty$$. 

Different activation functions manifest their gradient pathologies through the properties of $\operatorname{diag}(\sigma_l'(h_l))$: sigmoids or tanh induce continuous spectral shrinkage ($\|\operatorname{diag}(\sigma_l'(h_l))\|_\infty < 1$) causing vanishing gradients, ReLU introduces a sparse projection that may collapse the gradient rank, leaky ReLU and GELU partially soften this effect but do not eliminate the potential conditioning issues, and residual connections correspond to adding an identity component $I$ to $J_l$, guaranteeing a non-vanishing channel in the Jacobian chain irrespective of the activation or weight norms.

### Vanishing and Exploding Gradients
The gradient expression above reveals a fundamental difficulty in training deep neural networks: the gradient with respect to early-layer parameters is dominated by a product of Jacobian matrices across layers.

If the spectral norms of the intermediate Jacobians satisfy
$$
\left\| \frac{\partial x_{i+1}}{\partial x_i} \right\| < 1
\quad \text{for most } i,
$$
the gradient magnitude decays exponentially with depth, leading to the **vanishing gradient** problem. In this regime, parameters in early layers receive negligible updates and fail to learn meaningful representations.

Conversely, if
$$
\left\| \frac{\partial x_{i+1}}{\partial x_i} \right\| > 1
\quad \text{for most } i,
$$
the gradient norm grows exponentially, resulting in **exploding gradients**. This causes numerical instability and severely hampers optimization.

In practice, even when the expected Jacobian norm is close to one, small perturbations may accumulate through the multiplicative structure, making gradient propagation highly sensitive to depth.

### Motivation for Residual Learning

The analysis above indicates that the root cause of both vanishing and exploding gradients lies in the **multiplicative nature of deep function composition**. As depth increases, the repeated multiplication of Jacobian operators becomes increasingly ill-conditioned.

Residual learning addresses this issue by reformulating deep networks as incremental updates of feature representations, replacing pure function composition with an additive structure. This seemingly simple modification fundamentally changes the geometry of gradient propagation and enables the stable training of very deep models.

From a broader perspective, residual connections suggest interpreting depth not merely as a stack of nonlinear transformations, but as a discretized evolution process. This viewpoint naturally leads to the concept of **residual flows**, where deep networks are understood as approximations of continuous-time dynamical systems.


## 2. Definition
### 2.1 Residual Connection
For simplicity, we omit the parameters $\theta$ and the difference of function $F$ in each layers. The residual connection could be formed as:
$$
 x_{l+1}=x_l+F(x_l),
$$
whose gradient $$\frac{\partial \mathcal{L}}{\partial x_l}=\frac{\partial \mathcal{L}}{\partial x_{l+1}}(I+\frac{\partial F}{\partial x_{l}})$$ avoids the **gradient vanishing** problem
### 2.2 Residual Flow
$$
 x_{l+1}-x_l=f(x_l),
$$
## 3. Mathematical Formulation

## 4. Interpretation (Geometric / Dynamic)

## 5. Remarks / Connections
- **Remark.1**:Residual connections are one particular realization of identity preservation at the level of first-order training dynamics, rather than a necessary architectural constraint. Others like **Straight-Estimation** also realizes training stability.
  
## 6. Appendix: Matrix Norms
Matrix norms can be classified into three main types: induced (operator) norms, Schatten norms, and elementwise norms. Each captures a different aspect of a matrix.

---

### 1. Induced (Operator) Norms

These norms treat a matrix as a linear map and measure how much it can stretch vectors:

\[
\|A\|_p = \sup_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}.
\]

Special cases:

- \(p = 2\): spectral norm (largest singular value) \(\|A\|_2 = \sigma_{\max}(A)\)  
- \(p = 1\): maximum column sum \(\|A\|_1 = \max_j \sum_i |A_{ij}|\)  
- \(p = \infty\): maximum row sum \(\|A\|_\infty = \max_i \sum_j |A_{ij}|\)  

**Focus:** matrix as a transformation on vectors.

---

### 2. Schatten Norms

Schatten norms are defined on the singular values of the matrix:

\[
\|A\|_{\mathcal S_p} = \left( \sum_{i=1}^{r} \sigma_i(A)^p \right)^{1/p}, \quad 1 \le p < \infty,
\]

where \(\sigma_1 \ge \dots \ge \sigma_r\) are the singular values of \(A\).  

Special cases:

- \(p = 2\): Frobenius norm \(\|A\|_F = \sqrt{\sum_i \sigma_i^2}\)  
- \(p = \infty\): maximum singular value \(\|A\|_{\mathcal S_\infty} = \sigma_{\max}(A) = \|A\|_2\)  

**Focus:** matrix as an operator, measured via its singular value spectrum.

---

### 3. Elementwise (Entrywise) Norms

These norms treat a matrix as a collection of numbers, ignoring operator properties:

\[
\|A\|_p = \left( \sum_{i,j} |A_{ij}|^p \right)^{1/p}, \quad
\|A\|_\infty = \max_{i,j} |A_{ij}|.
\]

Special cases:

- \(p = 2\): Frobenius norm (same numeric value as Schatten 2-norm)  
- \(p = 1\): sum of absolute values of all entries  
- \(p = \infty\): maximum absolute element  

**Focus:** intrinsic size of matrix entries.

---

### 4. Relations and Remarks

- Frobenius norm is both a Schatten 2-norm and an elementwise 2-norm.  
- Spectral norm (operator 2-norm) is identical to Schatten ∞-norm (maximum singular value).  
- Elementwise ∞-norm (maximum element) generally does **not** equal spectral norm.  
- Operator and Schatten norms measure **matrix as a linear map**, elementwise norms measure **matrix as a numeric array**; they coincide only in special cases.

---

**In practice:** for analyzing gradient propagation and Jacobian stability in deep networks, the **operator/spectral norm (Schatten ∞)** is most relevant because it quantifies the maximal amplification along any input direction.
