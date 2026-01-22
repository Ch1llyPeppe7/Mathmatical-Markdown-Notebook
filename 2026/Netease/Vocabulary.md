# Vocabulary Induction Structural Analysis – Rectification Plan

## 1. Core Objective (What We Are Actually Studying)

We are **not** studying downstream predictive performance.
We are studying:

> **Vocabulary induction as a structural, combinatorial, and topological process.**

Specifically:

* Tokens are **not sequences**; they are **sets of atoms**.
* Each token corresponds to a **simplex** whose dimension is determined by the number of atoms.
* A vocabulary is a **graded simplicial complex**:

  * 0-simplex: atom
  * 1-simplex: token composed of 2 atoms
  * 2-simplex: token composed of 3 atoms
  * etc.

An item is a **subcomplex**.
The entire dataset is a **union of subcomplexes**, i.e.

$$
\mathcal{K}*{global} = \bigcup*{i=1}^N \mathcal{K}_i
$$

We are analyzing how different vocabulary induction rules shape the **geometry and topology** of this global complex.

---

## 2. Critical Conceptual Fix: What Object Are We Computing Topology On?

There are two fundamentally different options:

### ❌ Wrong (for our goal): Per-item Betti

$$
\beta_k = \mathbb{E}_i[\beta_k(\mathcal{K}_i)]
$$

This only measures the *internal complexity of individual items*.
It says nothing about:

* Global connectivity
* Cross-item structure
* Emergent loops
* Vocabulary-induced geometry

---

### ✅ Correct: Global Union Complex Betti

$$
\beta_k = \beta_k\left( \bigcup_{i=1}^N \mathcal{K}_i \right)
$$

This measures:

* $\beta_0$: Fragmentation vs unification of vocabulary
* $\beta_1$: Cycles induced by combinatorial reuse
* $\beta_2$: Higher-order holes

This is what we actually want.

---

## 3. Vocabulary Data Structure Definition (Must Be Enforced)

Vocabulary must be represented as a **graded structure**:

```
vocab = [
  V0,  # atoms (0-simplex)
  V1,  # tokens made of 2 atoms (1-simplex)
  V2,  # tokens made of 3 atoms (2-simplex)
  ...
]
```

Each token is represented as a **set of atoms**.

---

## 4. Merge Semantics Must Be Disambiguated

We currently use the word "merge" ambiguously.
We must distinguish:

### (A) Constructive merge (expansion)

* Create a new token by combining two tokens
* Old tokens remain
* Vocabulary size increases

### (B) Collapsing merge (compression)

* Identify two redundant tokens
* Replace both with one
* Vocabulary size decreases

These are conceptually different operations.
They must not be mixed.

---

## 5. What We Log Per Step

For each induction step t:

### Structural

* $|V|$ total
* $|V_k|$ per dimension
* Dimension spectrum

### Frequency

* Token frequency distribution
* Atom frequency distribution
* Zipf curves
* Tail mass

### Topological

* Global union complex Betti numbers
* NOT per-item average

---

## 6. Filtration View

Induction defines a filtration:

$$
\mathcal{K}_0 \subset \mathcal{K}_1 \subset \cdots \subset \mathcal{K}_T
$$

This suggests persistent homology in future.

---

## 7. Tooling Direction

This is a **structural analysis engine**, not a recommender model.

It should:

* Accept datasets via an atom-table interface
* Build simplicial complexes
* Log structural metrics
* Visualize evolution

---

## 8. Immediate Corrections Needed

1. Verify what object Betti is currently computed on
2. Enforce graded vocabulary structure
3. Separate constructive vs collapsing merges
4. Fix vocabulary size definition
5. Recompute all topology on the global union complex

---

# Cursor Correction Prompt

You must not create new files. Modify existing logic only.

---

## Prompt

We are correcting conceptual errors in the implementation.

### 1. Vocabulary Representation (Mandatory)

Vocabulary must be a graded structure:

```
vocab = [V0, V1, V2, ...]
```

Where:

* V0 = atoms
* Vk = tokens composed of k+1 atoms

Each token must be stored as a **set of atom IDs**.

---

### 2. Merge Semantics

You must explicitly support only **constructive merges** for now:

* Combine two tokens → create a new token
* Do NOT delete old tokens
* Vocabulary size must monotonically increase

---

### 3. What Defines a Simplex

Each token corresponds to a simplex.
If token has k atoms → it is a $(k-1)$-simplex.

---

### 4. Topology Object Definition (Critical)

Do NOT compute Betti per item.

You must compute Betti on the **global union complex**:

$$
\mathcal{K}_{global} = \bigcup_i \mathcal{K}_i
$$

Where each item contributes a subcomplex.

---

### 5. If Current Code Computes Per-item Betti

You must refactor it to:

* First construct the global complex
* Then compute Betti on that

---

### 6. Vocabulary Size

Vocabulary size means:


$$|V| = sum_k |V_k|$$


NOT the number of tokens used to encode the dataset.

---

### 7. Logging

At each step t, log:

* $|V|, |V_k|$
* Dimension spectrum
* Token frequencies
* Global Betti numbers

---

### 8. Do NOT introduce new models

Only refactor data structures, metrics, and topology logic.

---

If any of the above assumptions contradict current code, you must fix them.
Do not preserve incorrect behavior.
