#!/usr/bin/python3

import numpy as np
import sympy as sym
from rootfinding import *

# define iterative method parameters
Nmax=100;
tol=1e-10;

# define an interval [a,b]
a=0.5;
b=2.5;

# define an test function (f=x^3-6x^2+11x-6)
x=sym.Symbol('x');
f = sym.lambdify((x), x**3+2*x-8, "numpy");

#compute root using bisection method
rt=bisection(f,a,b,tol=tol,N=Nmax);

# end python
