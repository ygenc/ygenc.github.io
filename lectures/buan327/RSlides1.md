<style>
  .reveal pre {font-size: 12px;}
</style>


========================================================
font-family: Garamond
<h1>Introduction to R <br>  Basics of Data</h1>



Yegin Genc  
text here

Agenda
========================================================


- Course overview and mechanics
- Built-in data types
- Built-in functions and operators
- First data structures: Vectors and arrays

Why good statisticians learn to program
========================================================

- _Independence_: Otherwise, you rely on someone else having given you exactly the right tool

- *Honesty*: Otherwise, you end up distorting your problem to match the tools you have

- *Clarity*: Making your method something a machine can do disciplines your thinking and makes it public; that's science



How this class will work
========================================================
- No programming knowledge presumed
- Some stats. knowledge presumed
- General programming mixed with data-manipulation and statistical inference
- Class will be _very_ cumulative



 

Mechanics
========================================================
- Lectures: concepts, methods, examples
- In-class Assignments to try stuff out and get fast feedback
- HW weekly to do longer and more complex things
- Projects:
    + Project 1: Descriptive statistics
    + Project 2: Inferencial Statistics
- Midterm and Final: in class, hands-on 
 

R as statistical programming environment
====
Download and review at https://www.r-project.org/
![alt text](_images/R_intro.png)

The R Console
====

![alt text](_images/R_console.png)

***
Basic interaction with R is by typing in the **console**, a.k.a. **terminal** or **command-line**

You type in commands, R gives back answers (or errors)

Menus and other graphical interfaces are extras built on top of the console


RStudio as the user interface for R
====


<img src="_images/R_studio.png" width="7500">



Statistical programming in a nutshell: Functional programming
========================================================
2 sorts of things (**objects**): **data** and **functions**

- **Data**:  things like 7, "seven", $7.000$, the matrix $\left[ \begin{array}{ccc} 7 & 7 & 7 \\ 7 & 7 & 7\end{array}\right]$

- **Functions**: things like $\log{}$, $+$ (two arguments), $<$ (two), $\mod{}$ (two), `mean` (one)

> A function is a machine which turns input objects (**arguments**) into an output object (**return value**), possibly with **side effects**, according to a definite rule




Before functions, data
====

Different kinds of data object

All data is represented in binary format, by **bits** (TRUE/FALSE, YES/NO, 1/0)

- **Booleans** Direct binary values: `TRUE` or `FALSE` in R
- **Integers**: whole numbers (positive, negative or zero), represented by a fixed-length block of bits
- **Characters** fixed-length blocks of bits, with special coding;
**strings** = sequences of characters
- **Floating point numbers**: a fraction (with a finite number of bits) times an exponent, like $1.87 \times {10}^{6}$, but in binary form
- **Missing or ill-defined values**: `NA`, `NaN`, etc.

R as a calculator - Operators
===


```r
7+5
```

```
[1] 12
```

```r
7-5
```

```
[1] 2
```

```r
7*5
```

```
[1] 35
```

```r
7^5
```

```
[1] 16807
```

====

```r
7/5
```

```
[1] 1.4
```

```r
7 %% 5
```

```
[1] 2
```

```r
7 %/% 5
```

```
[1] 1
```




Operators cont'd.
===
**Comparisons** are also binary operators; they take two objects, like numbers, and give a Boolean

```r
7 > 5
```

```
[1] TRUE
```

```r
7 < 5
```

```
[1] FALSE
```

```r
7 >= 7
```

```
[1] TRUE
```

```r
7 <= 5
```

```
[1] FALSE
```

===

```r
7 == 5
```

```
[1] FALSE
```

```r
7 != 5
```

```
[1] TRUE
```

Boolean operators
===
Basically "and" and "or":

```r
(5 > 7) & (6*7 == 42)
```

```
[1] FALSE
```

```r
(5 > 7) | (6*7 == 42)
```

```
[1] TRUE
```



More types
===

`typeof()` function returns the type

`is.`_foo_`()` functions return Booleans for whether the argument is of type _foo_

`as.`_foo_`()` (tries to) "cast" its argument to type _foo_ --- to translate it sensibly into a _foo_-type value

===

```r
typeof(7)
```

```
[1] "double"
```

```r
is.numeric(7)
```

```
[1] TRUE
```

```r
is.na(7)
```

```
[1] FALSE
```

```r
is.na(7/0)
```

```
[1] FALSE
```

```r
is.na(0/0)
```

```
[1] TRUE
```
<small>Why is 7/0 not NA, but 0/0 is?</small>

===

```r
is.character(7)
```

```
[1] FALSE
```

```r
is.character("7")
```

```
[1] TRUE
```

```r
is.character("seven")
```

```
[1] TRUE
```

```r
is.na("seven")
```

```
[1] FALSE
```

===

```r
as.character(5/6)
```

```
[1] "0.833333333333333"
```

```r
as.numeric(as.character(5/6))
```

```
[1] 0.8333333
```

```r
6*as.numeric(as.character(5/6))
```

```
[1] 5
```

```r
5/6 == as.numeric(as.character(5/6))
```

```
[1] FALSE
```
<small>(why is that last FALSE?)</small>


Data can have names
===

We can give names to data objects; these give us **variables**

A few variables are built in:

```r
pi
```

```
[1] 3.141593
```

Variables can be arguments to functions or operators, just like constants:

```r
pi*10
```

```
[1] 31.41593
```

```r
cos(pi)
```

```
[1] -1
```

===

Most variables are created with the **assignment operator**, `<-` or `=`  

```r
approx.pi <- 22/7
approx.pi
```

```
[1] 3.142857
```

```r
diameter.in.cubits = 10
approx.pi*diameter.in.cubits
```

```
[1] 31.42857
```

===
The assignment operator also changes values:

```r
circumference.in.cubits <- approx.pi*diameter.in.cubits
circumference.in.cubits
```

```
[1] 31.42857
```

```r
circumference.in.cubits <- 30
circumference.in.cubits
```

```
[1] 30
```

===

Using names and variables makes code: easier to design, easier to debug, less prone to bugs, easier to improve,  and easier for others to read

Avoid "magic constants"; use named variables
<small>you will be graded on this!</small>

Named variables are a first step towards **abstraction**


The workspace
===
What names have you defined values for?

```r
ls()
```

```
[1] "approx.pi"               "circumference.in.cubits"
[3] "diameter.in.cubits"     
```

```r
objects()
```

```
[1] "approx.pi"               "circumference.in.cubits"
[3] "diameter.in.cubits"     
```

Getting rid of variables:

```r
rm("circumference.in.cubits")
ls()
```

```
[1] "approx.pi"          "diameter.in.cubits"
```

First data structure: vectors
===

Group related data values into one object, a **data structure**

A **vector** is a sequence of values, all of the same type

```r
x <- c(7, 8, 10, 45)
x
```

```
[1]  7  8 10 45
```

```r
is.vector(x)
```

```
[1] TRUE
```

`c()` function returns a vector containing all its arguments in order

`x[1]` is the first element, `x[4]` is the 4th element  
`x[-4]` is a vector containing all but the fourth element

===
`vector(length=6)` returns an empty vector of length 6; helpful for filling things up later

```r
weekly.hours <- vector(length=5)
weekly.hours[5] <- 8
```

Vector arithmetic
===

Operators apply to vectors "pairwise" or "elementwise":

```r
y <- c(-7, -8, -10, -45)
x+y
```

```
[1] 0 0 0 0
```

```r
x*y
```

```
[1]   -49   -64  -100 -2025
```

Recycling
===
**Recycling** repeats elements in shorter vector when combined with longer

```r
x + c(-7,-8)
```

```
[1]  0  0  3 37
```

```r
x^c(1,0,-1,0.5)
```

```
[1] 7.000000 1.000000 0.100000 6.708204
```

Single numbers are vectors of length 1 for purposes of recycling:

```r
2*x
```

```
[1] 14 16 20 90
```

===
Can also do pairwise comparisons:

```r
x > 9
```

```
[1] FALSE FALSE  TRUE  TRUE
```
Note: returns Boolean vector

Boolean operators work elementwise:

```r
(x > 9) & (x < 20)
```

```
[1] FALSE FALSE  TRUE FALSE
```

===
To compare whole vectors, best to use `identical()` or `all.equal()`:

```r
x == -y
```

```
[1] TRUE TRUE TRUE TRUE
```

```r
identical(x,-y)
```

```
[1] TRUE
```

```r
identical(c(0.5-0.3,0.3-0.1),c(0.3-0.1,0.5-0.3))
```

```
[1] FALSE
```

```r
all.equal(c(0.5-0.3,0.3-0.1),c(0.3-0.1,0.5-0.3))
```

```
[1] TRUE
```

Functions on vectors
===

Lots of functions take vectors as arguments:
- `mean()`, `median()`, `sd()`, `var()`, `max()`, `min()`, `length()`, `sum()`: return single numbers
- `sort()` returns a new vector
- `hist()` takes a vector of numbers and produces a histogram, a highly structured object, with the side-effect of making a plot
- Similarly `ecdf()` produces a cumulative-density-function object
- `summary()` gives a five-number summary of numerical vectors
- `any()` and `all()` are useful on Boolean vectors

Addressing vectors
===

Vector of indices:

```r
x[2];x[4]
```

```
[1] 8
```

```
[1] 45
```

```r
x[c(2,4)]
```

```
[1]  8 45
```

Vector of negative indices

```r
x[c(-1,-3)]
```

```
[1]  8 45
```
<small>(why that, and not  `8 10`?)</small>

===
Boolean vector:

```r
x[x>9]
```

```
[1] 10 45
```

```r
y[x>9]
```

```
[1] -10 -45
```

`which()` turns a Boolean vector in vector of TRUE indices:

```r
places <- which(x > 9)
places
```

```
[1] 3 4
```

```r
y[places]
```

```
[1] -10 -45
```

Named components
===

You can give names to elements or components of vectors

```r
names(x) <- c("v1","v2","v3","fred")
names(x)
```

```
[1] "v1"   "v2"   "v3"   "fred"
```

```r
x[c("fred","v1")]
```

```
fred   v1 
  45    7 
```
note the labels in what R prints; not actually part of the value

===
`names(x)` is just another vector (of characters):

```r
names(y) <- names(x)
sort(names(x))
```

```
[1] "fred" "v1"   "v2"   "v3"  
```

```r
which(names(x)=="fred")
```

```
[1] 4
```




Take-Aways
===
- We write programs by composing functions to manipulate data
- The basic data types let us represent Booleans, numbers, and characters
- Data structure let us group related values together
- Vectors let us group values of the same type
- Use variables rather a profusion of magic constants
- Name components of structures to make data more meaningful




