# Interval Arithmetic - Python Class
This is a module for Interval Arithmetic based operations to be used in Python.
<hr>

## About
Interval arithmetic, developed since 1950s and 1960s have been used as an approach to deal with rounding error problems. The basic arithmetic operations: addition (+), subtraction (-), multiplication (x) and division (/) are defined for intervals.

## Code Analysis
The python code provided above performs all basic arithmetic operations.  It has been made of binary operations involving two Intervals or an Interval and Real Number.
> R operator Interval Object
> Interval Object operator R
> Interval Object operator Interval Object

## Usage 

1. Import class
```
from InterArith import Ia
```
2. Object Initialization
`obj = Ia(a,b)` where a,b are Real Number representing interval `[a, b]`
3. Operations
`obj1 operator obj2`
`obj1 operator R`
`R operator obj1`

> operator is +,  -,  x,  /
> R is real number
> `[a, b ]`  interval a to b.

[Wikipedia on Interval Arithmetic - ](https://en.wikipedia.org/wiki/Interval_arithmetic)
<hr>
*If you find any mistakes or imporvements, feel free to contact me.*