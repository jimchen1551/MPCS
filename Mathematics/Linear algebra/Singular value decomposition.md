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
- $U$: left singular vectors, $V$: right singular vectors, $\Sigma$: singular values
- $U,V$: unitary matrix with orgonormal columns; $\Sigma$: diagonal matrix
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
$$XX^T=U\Sigma V^TV\Sigma U^T=U\Sigma^2U^T$$
$$XX^TU=U\Sigma^2$$
$$X^TX=V\Sigma U^TU\Sigma V^T=V\Sigma^2V^T$$
$$X^TXV=V\Sigma^2$$
de ja vu? Exactlt, $U$ or $V$ is the eigen vectors of $XX^T$ or $X^TX$ and $\Sigma^2$ is the corresponding eigen values. 
$$(XX^T)u_i=\sigma_i^2u_i=\lambda_iu_i\Rightarrow\sigma_i^2=\lambda_i$$
$$(X^TX)v_i=\sigma_i^2v_i=\lambda_iv_i\Rightarrow\sigma_i^2=\lambda_i$$

## Economy SVD
$$X=U\Sigma V^T=\begin{bmatrix}
\hat U&\hat U^\perp\end{bmatrix}
\begin{bmatrix}\hat\Sigma\\0\end{bmatrix}V^T
=\hat U\hat\Sigma V^T$$
- After truncating $U$ and $\Sigma$ at rank r, we have $\hat U$ and $\hat \Sigma$
- $span(\hat U^\perp)$ is complementary and orthogonal to $span(\hat U)$

## Eckart-Young theorem
$$X\approx \tilde U\tilde \Sigma \tilde V^T=\tilde X$$
$$\arg\min_{\tilde X,\text{ st } rank(\tilde X)=r}\|X-\tilde X\|_F=\tilde U\tilde \Sigma \tilde V^T$$
- $\tilde U\tilde \Sigma\tilde V^T$ is pretty approximate to $X$
- $\tilde U^T\tilde U=I_{r\times r}$ ;  $\tilde U\tilde U^T\neq I$
Ps. Frobenius norm: $\|A\|_F=\sqrt{\sum_{i,j}(A_{ij})^2}$

## Method of Snapshots
$$X=\tilde U\tilde\Sigma \tilde V^T$$
$$U=X\tilde V\tilde\Sigma^{-1}$$

## Unitary transformation
$$Y=CX\text{, where C is a left unitary transformation}$$
$$Y=XP^T\text{, where P is a right unitary transformation}$$
$$X=U_X\Sigma_XV_X^T; Y=U_Y\Sigma_YV_Y^T$$
$$V_Y\Sigma_Y^2V_Y^T=Y^TY=X^TC^TCX=X^TX=V_X\Sigma_X^2V_X^T$$
$$U_Y=YV_X\Sigma_x^{-1}=CXV_X\Sigma_x^{-1}=CU_X$$
$$\Rightarrow U_Y=CU_X; \Sigma_X=\Sigma_Y;V_Y=V_X$$
$$\Rightarrow Y=CX=CU_X\Sigma_XV_X^T$$
Similarly, 
$$Y^TY=PX^TXP^T=PV_X\Sigma_X^2V_X^TP^T$$
$$Y^TYPV_X=PV_X\Sigma_X^2$$
$$\Rightarrow V_Y=PV_X; \Sigma_X=\Sigma_Y$$
$$\Rightarrow U_Y=YPV_X\Sigma_X^{-1}=XV_X\Sigma_X^{-1}=U_X$$
$$\Rightarrow Y=XP^T=U_X\Sigma_XV_X^TP^T$$

## Reference
[this website](https://www.youtube.com/playlist?list=PLMrJAkhIeNNRpsRhXTMt8uJdIGz9-X_1-)
