![GitHub last commit](https://img.shields.io/github/last-commit/1nolysk/Interval-Arithmetic)   ![GitHub](https://img.shields.io/github/license/1nolysk/Interval-Arithmetic)
# Interval Arithmetic - Python Class
This is a module for Interval Arithmetic based operations to be used in Python.


## About
Interval arithmetic, developed since 1950s and 1960s have been used as an approach to deal with rounding error problems. The basic arithmetic operations: addition (+), subtraction (-), multiplication (x) and division (/) are defined for intervals.

## Code Analysis
The python code provided above performs all basic arithmetic operations.  It has been made of binary operations involving two Intervals or an Interval and Real Number.
- R operator Interval Object
- Interval Object operator R
- Interval Object operator Interval Object

## Usage 

1. Import class
```python
from InterArith import Ia
```
2. Object Initialization<br>
`obj = Ia(a,b)` <br/> where a,b are Real Number representing interval `[a, b]` <br/>

3. Operations

```
obj1 operator obj2
obj1 operator R
R operator obj1
```
<br/>

> operator is **+,  -,  x,  /**<br/>
> R is real number<br/>
> `[a, b ]`  interval a to b.<br/>

<hr>

[Wikipedia on Interval Arithmetic](https://en.wikipedia.org/wiki/Interval_arithmetic)

<br/>

*If you find any mistakes or imporvements, feel free to contact me.*

