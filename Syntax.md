---
Created: [[2022-06-05]]
Modified: None
Types: Guide
Tags: 
- syntax
- markdown
- obsidian
---
![[Markdown.webp]]
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

*italic*
**bold**
***bold and italic***
~~Strikethrough~~
==highlight==

$x < y$
$x \le y$
$H_{2}O$
$e^{iπ}$
$\overline{x}$, $\hat{x}$, $\displaystyle\frac{a}{b}$, $\displaystyle\frac{\partial f}{\partial x}$, $\displaystyle\binom{n}{k}$
$x_{1} + x_{2} + \cdots + x_{n}$
$x_{1}, x_{2}, \dots, x_{n}$
$\mathbf{X} = \langle x_{1}, x_{2}, \dots, x_{n}\rangle$
$x_{i} \in \mathbf{X}$
$x \subset B$
$x \subseteq B$
$A \cup B$
$A \cap B$
$\mathrm{P}(A \mid B)$
$\{1, 2, 3\}$
$\left[\int_{-\infty}^{\infty} f(x) \; dx\right]$
$\left. F(x) \right|_{a}^{b}$
$\sum_{x = a}^{b} f(x)$
$\prod_{x = a}^{b} f(x)$
$\displaystyle \lim_{x \to \infty} f(x)$
$\theta, \epsilon, \eta$

>Blockquotes
>>Nested Blockquotes
># with other elements

1. Ordered
2. Lists
	1. Indented
	2. Items

- Unordered
- Lists
	- Indented
	- Items

- [x] Task
- [ ] lists

Link to heading [[#Heading level 1]]

| English | Chinese |
|:------- | -------:|
| Chen    |      陳 |
| Chun    |      俊 |
| Hung    |      鴻 |

---
```python
if True:
	print("Hello World!")
```
```mermaid
gitGraph
	commit
	commit
	branch develop
	commit
	commit
	checkout main
	commit
	commit
	merge develop
	commit
```
``type `class class_name:` to define a class``
type `def function_name(variables):` to set a function
More Markdown syntax in [this website](https://www.markdownguide.org). 
Reference style: Markdown [1]
[1]: https://www.markdownguide.org

Appendix
- cmd+Shift+. → Show .obsidian file
- ctr+Y →YAML
- ctr+P → Plan table
- ctr+E → Elongation of plan table