#!/usr/bin/python3

import numpy as np

def bisection(f,a,b,tol=1e-7,N=1000,verb=1):
    if (f(a)*f(b)<0):
        for i in range(N):

            c=(a+b)/2.0;

            if (np.abs(f(c))<tol):
                break;

            if (f(a)*f(c)<0):
                b=c;
            else:
                a=c;

        if (i+1==N):
            print("Error: Bisection cannot converge within the prescribed tolerance (Nmax="+str(N)+").");
        else:
            if (verb==1):
                print("Bisection converged in "+str(i+1)+" iteration.");
                print("The root is: ", "%.15f" % c);
    else:
        print("Error: f(a)*f(b)>0.");

    return c;
# end python
