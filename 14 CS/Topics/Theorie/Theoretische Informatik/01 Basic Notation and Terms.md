## Basic
- Bracketing mathematical expressions: $\lparen \rparen$, $\brack$
- Function Arguments: $\lparen \rparen$
- Bracketing [[#Sets]]: $\brace$


>[!Note]
>0 is a **natural** number $0 \in \N$
>
## Sets
### Notation
$\mathbb{N}$ := $\{0, 1, 2, \dots\}$ (Set of natural numbers)

$\mathbb{N}^+$ := $\{1, 2, \dots\}$ (Set of positive natural numbers)
<!--SR:!2024-10-07,4,274-->

$\mathbb{P}$ := $\{2, 3, 5, 7, 11, \dots\}$ (Set of primes)

$\mathbb{Z}$ := $\{\dots, -2, -1, 0, 1, 2, \dots\}$ (Set of integers)
<!--SR:!2024-10-07,4,274-->

$\emptyset$ := Empty set
<!--SR:!2024-10-07,4,274-->

### Operations

$(x \mod y)$ := $x - zy$ (Rest of the division $x/y$), where $z \in \mathbb{N}$ and $zy \leq x$

$\{n \in \mathbb{N} \mid n \geq 5\}$ := $\{5, 6, 7, \dots\}$

$a \in M$ := $a$ is an element of set $M$

$a \notin M$ := $a$ is not an element of set $M$
<!--SR:!2024-10-07,4,274-->

$M \subseteq N$ := For all $a$, if $a \in M$, then $a \in N$ (Subset of $N$)
<!--SR:!2024-10-07,4,274-->

$M \not\subseteq N$ := $M$ is not a subset of $N$

$M \subsetneq N$ := $M \subseteq N$ and $M \neq N$ (Proper subset of $N$)

### Set Operations

$A \cap B$ := $\{a \mid a \in A \text{ and } a \in B\}$ (Intersection of $A$ and $B$)

$A \cup B$ := $\{a \mid a \in A \text{ or } a \in B\}$ (Union of $A$ and $B$)

$A \setminus B$ := $\{a \mid a \in A \text{ and } a \notin B\}$ (Difference of $A$ and $B$)

$\bar{A}$ := $M \setminus A$ (Complement of $A$ relative to base set $M$)

$P(A)$ := $\{B \mid B \subseteq A\}$ (Power set of $A$)

$\#A = |A|$ := Number of elements of a finite set $A$

## Tuple(Vector)

$(a_1, a_2, \dots, a_n)$ := Sequence of elements $a_1, a_2, \dots, a_n$ (n-tuple)
### Cartesian Product

$A_1 \times A_2 \times \dots \times A_n$ := $\{(a_1, a_2, \dots, a_n) \mid a_i \in A_i \text{ for all } i\}$ (Cartesian product)

$A^n$ := $A \times A \times \dots \times A$ (n-dimensional Cartesian product)

## Quantifiers
$\exists$ := "There exist(s)"
<!--SR:!2024-10-07,4,270-->

$\forall$ := "For all"
<!--SR:!2024-10-07,4,270-->

## Functions
$f : A \to B$ := A function $f$ from set $A$ (domain) to set $B$ (codomain)

$f(a)$ := $b$ where $(a, b) \in G_f$ (Function value at $a$)

Domain of $f$ := $D_f := \{a \in A \mid \exists b \in B \text{ such that } f(a) = b\}$

Range of $f$ := $R_f := \{b \in B \mid \exists a \in A \text{ such that } f(a) = b\}$
<!--SR:!2024-10-06,3,254-->

$f$ is total := $D_f = A$
<!--SR:!2024-10-07,4,274-->

$f$ is surjective := $R_f = B$

$f$ is injective := $f(a_1) \neq f(a_2)$ for all distinct $a_1, a_2 \in D_f$

$f$ is bijective := $f$ is total, surjective, and injective
<!--SR:!2024-10-07,4,274-->

$(g \circ f)(x)$ := $g(f(x))$ (Composition of functions)

- Bild: Pfeile zwischen Mengen 
- inverse Funktion nur von injekive Funktionen zu bilden( da sonst ein x zwei y abbildet)

## Complete Induction
### Concept
Prove $BC$(Base Case) and $IS$(Induction Step) => $A_0 \Rightarrow A_1 \Rightarrow$ all other statements

### Example
Statement: "For all natural numbers $n$ the following statement $A_n$ is true"
$$
\sum\limits_{i = 1}^ki = \frac{n^2+n}{n}
$$

## Flashcards

Functions: Whats the domain and the codomain? := $f : A(\text{Domain}) \rightarrow B(\text{Codomain})$
