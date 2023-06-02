# Propositional Logic in Artificial Intelligence
<img src="media_files/cover.webp" style="align:center;">

## Learning Outcome:
<i>At the end of the class, students should be able to:</i>

* Define primitive statements <br>
* Form a compound statements <br>
* define negation, conjunction, disjunction, conditional, biconditional, tautology, contradiction and contingency statements. <br>
* construct truth table. <br>

## LOGICAL CONNECTIVES
<i>Main components of symbolic logic are:</i> <br>

- Proposition/Statements
- Connectives

## PROPOSITION/STATEMENTS

- A proposition is a declarative sentence that is either true or false.
- The truth or falsify of a statement is called truth value.
- Usually denoted by letters p, q, r, s and so on.
<i>Example:</i> <br>

✔ You will be late to school if you miss the bus; <br>
✔ Ms. Nina will have a broader audience next month;<br>
✔ I did not join the competition;<br>
✔ Today is Monday;<br>
✔ I love reading thriller books;<br>
✔ The number 3 is an odd integer;<br>

## Logical connectives and compound statements

| <b>Logical Connective</b> | <b>Compound statement</b> | <b>Symbolic compound statement</b> |
| ------------- | ------------- | ------------- |
| ∧  | p and q (conjunction)  | p ∧ q  |
| ∨ | p or q (disjunction)  | p ∨ q  |
| →  | if p then q (conditional/implication)  | p → q  |
| ↔ | p if and only if q (biconditional)  | p ↔ q  |

* If the compound statement has two variables (p and q) the truth table must be constructed with 4 rows.
* If 3 variables (p, q and r), then 8 rows.

Two primitive statements are defined as follows,

    s: Your handbag is stylish
    c: I like its colour.

Connectives join primitives statements into more complex statement: <br>

Your handbag is stylish and I like its colour.

    In symbolic: s ∧ c

Connective “but” has an identical role as “and”, thus, use same symbol ∧ <br>

Your handbag is stylish but I like its colour <br>

    In symbolic: s ∧ c

## EXERCISE
Answer : <br>

1. Boston is the capital of Massachusetts. Truth value: True.
2. Miami is the capital of Florida. Truth value: False. (The capital of Florida is Tallahassee)
3. 2 + 3 = 5. Truth value: True.
4. 5 + 7 = 10. Truth value: False.
5. x + 2 = 11
> x + 2 = 11" not a proposition because it contains a variable (x) and is not a statement that can be determined as true or false without additional information about the value of x.

## TRUTH VALUES AND TRUTH TABLES(NOT)
| p | ¬q |
| -- | -- |
| True | False |
| False | True |

- The operation “not” or ¬ turns single statement into negation and it is not a connective.

For example, the negation of *I like you is I don’t like you.*

    p: I like you.
    ¬q: I don't like you.
## TRUTH VALUES AND TRUTH TABLES(CONJUNCTION /AND)
Combine primary statements by the word “and”denoted by p ∧ q (if 2 statements)

If p is true and q is true, then p ∧ q is true. Otherwise, p ∧ q is false.

| p | q | p ∧ q |
| -- | -- | -- |
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

    p: I play the piano (false)
    q: I study logic (true)
Thus,

    p ∧ q: I play the piano and study logic is a false statement
## TRUTH VALUES AND TRUTH TABLES(DISJUNCTION/OR)
Combine primary statements by the word “or”. Denoted by p ∨ q (if 2 statements)

If p is true or q is true or both p and q are true, then p ∨ q is true. Otherwise, p ∨ q is false.

| p | q | p ∨ q |
| -- | -- | -- |
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

    p: 2+3=6 (false)
    q: 3>2 (true)
Thus,

    p ∨ q: (2+3=6) or (3>2) is a true statement

## TRUTH VALUES AND TRUTH TABLES (CONDITIONAL STATEMENTS)
A compound statement of the form “If p then q”, p → q
In p → q, p is the hypothesis (antecedent or premise) and q is the conclusion (or consequence).

If p is true and q is false, then the conditional p → q (*p implies q*) is false. Otherwise, p → q is true.

| p | q | p → q |
| -- | -- | -- |
| False | False | True |
| False | True | True |
| True | False | False |
| True | True | True |

If Amy is a human being, then Amy has feeling.
Defined primitive statement:

    p : Amy is a human being (is the antecedent/hypothesis).
    q : Amy has feeling (is the consequent).

Thus, the only way the statement is false , that is:

    p → q: If Amy is a human being and she doesn’t have feeling.

## TRUTH VALUES AND TRUTH TABLES (BICONDITIONAL STATEMENTS)
If p and q have the same truth value, then p ↔ q is true.
If p and q have opposite truth value, then p ↔ q is false.

| p | q | p ↔ q |
| -- | -- | -- |
| False | False | True |
| False | True | False |
| True | False | False |
| True | True | True |

