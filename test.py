#!/usr/bin/python3

import numpy as np
import sympy as sym
from numpy import pi
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt

#universal parameters
tol=1e-7;
Nmax=100;

# Fixed Point
x0 = np.array([0.1,0.1])
x1=sym.Symbol('x1');
x2=sym.Symbol('x2');
G1 = sym.lambdify((x1,x2), (x1**2+x2**2+8)/10, "numpy");
G2 = sym.lambdify((x1,x2), (x1*(x2**2)+x1+8)/10, "numpy");

x1=np.zeros((2));
for i in range(Nmax):
    x1[0]=G1(x0[0],x0[1]);
    x1[1]=G2(x0[0],x0[1]);
    if (np.linalg.norm(x1-x0)<tol):
        print("Solution converged after "+str(i+1)+" iterations");
        break;
    x0=np.copy(x1);

print("Error: "+str(x1-np.ones((2))));
print("Res: "+str(x1));

 # Newton raphson
x0 = np.array([[0.1],[0.1]])
x1=sym.Symbol('x1');
x2=sym.Symbol('x2');

F1 = sym.lambdify((x1,x2), (x1**2-10*x1+x2**2+8), "numpy");
F2 = sym.lambdify((x1,x2), x1*(x2**2)+x1-10*x2+8, "numpy");
DF11 = sym.lambdify((x1,x2), 2*x1-10, "numpy");
DF12 = sym.lambdify((x1,x2), 2*x2, "numpy");
DF21 = sym.lambdify((x1,x2), x2**2+1, "numpy");
DF22 = sym.lambdify((x1,x2), 2*x1*x2-10, "numpy");

res=np.zeros((2,1));
dres=np.zeros((2,2));
x1=np.zeros((2,1));
for i in range(Nmax):
    res[0]=F1(x0[0],x0[1]);
    res[1]=F2(x0[0],x0[1]);
    dres[0,0]=DF11(x0[0],x0[1]);
    dres[0,1]=DF12(x0[0],x0[1]);
    dres[1,0]=DF21(x0[0],x0[1]);
    dres[1,1]=DF22(x0[0],x0[1]);
    x1=x0-np.linalg.solve(dres,res);
    if (np.linalg.norm(x1-x0)<tol):
        print("Solution converged after "+str(i+1)+" iterations");
        break;
    x0=np.copy(x1);

print("Error: "+str(x1-np.ones((2))));
print("Res: "+str(x1[0])+" "+str(x1[1]));

# python end
