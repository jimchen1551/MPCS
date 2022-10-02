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
$$=\sigma_1u_1v_1^T+\sigma_2u_2v_2^T+\dots+\sigma_mu_mv_m^T+0$$
- $U,V$: unitary matrix (orthogonal); $\Sigma$: diagonal matrix
- $U$: left singular vectors, $V$: right singular vectors, $\Sigma$: singular values
- $UU^T=U^TU=I_{n\times n}$ ; $VV^T=V^TV=I_{m\times m}$ ; $\sigma_1\geq\sigma_2\geq\dots\geq\sigma_m\geq0$
- Importance: $u_1\geq u_2\geq\dots$ ; $v_1\geq v_2\geq\dots$

## Correlation matrix
$$X^TX=\begin{bmatrix}
x_1^Tx_1&x_1^Tx_2&\cdots&x_1^Tx_m\\
x_2^Tx_1&x_2^Tx_2&\cdots&x_2^Tx_m\\
\vdots&\vdots&\ddots&\vdots\\
x_m^Tx_1&x_m^Tx_2&\cdots&x_m^Tx_m\\
\end{bmatrix}$$
$$x_i^Tx_j=\langle x_i,x_j\rangle$$
$$\text{if }X=U\Sigma V^T,X^T=V\Sigma U^T$$
$$X^TX=V\Sigma U^TU\Sigma V^T=V\Sigma^2V^T$$
$$X^TXV=V\Sigma^2$$
de ja vu? Yes, V is the eigen vector of $X_TX$ and $\Sigma^2$ is the corresponding eigen value. 

## Eckand-Young theorem
$$X\approx \tilde U\tilde \Sigma\tilde V^T=\tilde X$$
$$\arg\min_{ rank(\tilde X)=r}\|X-\tilde X\|_F$$
- After truncating $U$, $\Sigma$, and $V$ at rank r, we have $\tilde U$, $\tilde \Sigma$, and $\tilde V$ (economy)
- $\tilde U\tilde \Sigma\tilde V^T$ is pretty approximate to $X$
- $\tilde U^T\tilde U=I_{r\times r}$ ;  $\tilde U\tilde U^T\neq I$
