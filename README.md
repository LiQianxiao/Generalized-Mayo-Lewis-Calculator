# Theory

![alt text](.images/theory-0.png)

Suppose there are $n$ monomers species. Let
$$M = (M_1, M_2,\dots, M_n) \in \mathbb{R}^d$$
denote the vector of monomer concentrations, and
$$M^* = (M_1^*, M_2^*, \dots, M_n^*) \in \mathbb{R}^d$$
denote the vector of concentrations of chains terminating in monomer $(M_1, M_2,\dots, M_n)$ respectively.
Let us also write the rate constant matrix as
$$K \in \mathbb{R}^{n\times n}$$
We shall assume that $K$ is in general position, i.e. $K$ is invertible and diagonalizable (which happens almost surely if this is measured with some random error)

Then, the generalized $n$-monomer Mayo-Lewis reaction is given by
$$
\begin{aligned}
    M_i + M^*_j \overset{K_{ij}}{\longrightarrow} M^*_i,
    \qquad
    i,j = 1,2,\dots,n
\end{aligned}
$$

The rate equations are the following system of ODEs (written in vector form)
$$
\begin{aligned}
    \frac{dM}{dt} &= - (K^T M^*) \circ M \\
    \frac{dM^*}{dt} &= (K^T M^*) \circ M - (K M) \circ M^*
\end{aligned}
$$
where $K^T$ is the transpose of the matrix $K$ amd $\circ$ denotes vector Hadamard product, i.e. for vectors $x$ and $y$, $x\circ y$ is a vector with components $x\circ y = (x_1y_1, x_2y_2, \dots, x_ny_n)$.

Now, let us denote by $\mathbf{1}$ the vector of all $1$'s, i.e. $\mathbf{1} = (1, 1, \dots, 1)$. Then, the monomer mole fraction is a vector
$$f = \frac{M}{\mathbf{1}^T M}$$
Similarly, the fraction of chains terminating in monomers $f$ is
$$f^* = \frac{M^*}{\mathbf{1}^T M^*}$$
Finally, under the steady-state condition the mole fraction of incorporated moonomer is a vector
$$F = \frac{ dM/dt }{ \mathbf{1}^T dM/dt}$$
We shall assume that $M$, $M^*$ and $dM/dt$ are not identically 0 so that the above expressions for $f,f^*,F$ are well-defined.

Using the steady-state approximation, we may set $dM^*/dt = 0$. This allows us to write, using the ODE system, the following equations
$$
\begin{aligned}
    &F = \frac{ f \circ K^T f^* }{ f^T K^T f^*} \\
    &0 = (K^T f^*) \circ f - (K f) \circ f^*
\end{aligned}
$$
The last equation can be rewritten
$$
    (D_f K^T - D_{K f}) f^* = 0
$$
where for any vector $x$, $D_x$ denotes the diagonal matrix formed by having $x$ on the diagonal and $0$ everywhere else. Since $K$ is in general position, the matrix $A(K,f) \equiv (D_f K^T - D_{K f})$ has a one-dimensional null-space, whose basis we denote by the vector $v_0(K,f)$. Then, we immediately have
$$
    f^* = \frac{v_0(K,f)}{\mathbf{1}^T v_0(K, f)}
$$

Therefore, we have the relashionship between $F$ and $f$
$$
    F = \frac{ f \circ K^T v_0(K, f) }{ f^T K^T v_0(K, f)}
$$

Conversely, given $F$ we can also determine $f$, but this is in general no longer a one-to-one mapping, hence we may resort to solving the optimization problem
$$
    f = \mathrm{arg\,min}_{x: x_i\geq 0, \sum_{x_i} = 1}
    \| F - \frac{ x \circ K^T v_0(K, x) }{ x^T K^T v_0(K, x)} \|^2
$$
which can be solved numerically by the L-BFGS-B method.

---

# Program Usage

## 1. Computing product mole fractions from monomer mole fractions

### 1.1 Config files

1. Put the rate constants into ```rate_constants.csv```
    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```
    Example: (3 monomers, 2 different configs):

        f1, f2, f3
        g1, g2, g3

### 1.2 Usage

Run ```compute.py```

        python compute_F.py

The results are saved to ```product_outputs.csv```, in the format

        F1, F2, F3
        G1, G2, G3

## 2. Computing monomer mole fractions from product mole fractions

### 2.1 Config files

1. Put the rate constants into ```rate_constants.csv```
    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```
    Example: (3 products, 2 different configs):

        F1, F2, F3
        G1, G2, G3

### 2.2 Usage

Run ```compute.py```

        python compute_f.py

The results are saved to ```monomer_outputs.csv```, in the format

        f1, f2, f3
        g1, g2, g3
