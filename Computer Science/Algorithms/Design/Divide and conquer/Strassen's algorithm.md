---
Created: [[2022-10-25]]
Aliases: 
Types: Card
Tags: 
- 
---
# Strassen's algorithm
$$\begin{bmatrix}
C_{11}&C_{12}\\
C_{21}&C_{22}
\end{bmatrix}
=\begin{bmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{bmatrix}
\begin{bmatrix}
B_{11}&B_{12}\\
B_{21}&B_{22}
\end{bmatrix}$$
$M_1=(A_{11}+A_{22})(B_{11}+B_{22})$
$M_2=(A_{21}+A_{22})B_{11}$
$M_3=A_{11}(B_{12}-B_{22})$
$M_4=A_{22}(B_{21}-B_{11})$
$M_5=(A_{11}+A_{12})B_{22}$
$M_6=(A_{21}-A_{11})(B_{11}+B_{12})$
$M_7=$
$$\begin{bmatrix}
C_{11}&C_{12}\\
C_{21}&C_{22}
\end{bmatrix}
=\begin{bmatrix}
M_1+M_4-M_5+M_7&M_3+M_5\\
M_2+M_4&M_1-M_2+M_3+M_6
\end{bmatrix}$$
- an efficient recursive algorithm for matrix multiplication
- using [[Divide and conquer]] strategy
- performing only 7 recursive multiplication
- running in $\Theta (n^{\log 7})$ < $\Theta (n^3)$