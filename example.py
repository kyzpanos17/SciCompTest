#!/usr/bin/python3

import numpy as np
import sympy as sym
from rootfinding import *

# define iterative method parameters
Nmax=100;
tol=1e-12;

# define an interval [a,b]
a=0.0;
b=2.5;

# define a test function (f=x^3+2x-8)
x=sym.Symbol('x');
expr=x**3+2*x-8;
f = sym.lambdify((x), expr, "numpy");

#compute root using bisection method
rt1=bisection(f,a,b,tol=tol,N=Nmax);

#compute root using Regula Falsi method
rt2=regulafalsi(f,a,b,tol=tol,N=Nmax);
rt3=regulafalsi_Illinois(f,a,b,tol=tol,N=Nmax);
rt4=regulafalsi_AndersonBjork(f,a,b,tol=tol,N=Nmax);

#compute root using Newton Raphson method
x0=2.5;
dexpr=sym.diff(expr,x);
df = sym.lambdify((x), dexpr, "numpy");
rt6=newtonraphson(f,df,x0,tol=tol,N=Nmax);

# end python
