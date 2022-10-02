---
Created: [[2022-10-02]]
Aliases: SVD
Types: Note
Tags: 
- 
---
# Singular value decomposition
- a useful **data reduction** tool
- data-driven generalization of Fourier transform (FFT)
- tailored to specific problem
$$X=\begin{bmatrix}
x_1&x_2&\dots&x_m
\end{bmatrix}
=U\Sigma V^T$$
$$=\begin{bmatrix}
u_1&u_2&\dots&u_n
\end{bmatrix}
\begin{bmatrix}
\sigma_1\\
&\sigma_2\\
&&\ddots\\
&&&\sigma_m\\
0&0&\cdots&0\\
\vdots&\vdots&\vdots&\vdots
\end{bmatrix}
\begin{bmatrix}
v_1&v_2&\dots&v_m
\end{bmatrix}^T$$
$U,V$: unitary matrix (orthogonal); $\Sigma$: diagonal matrix
