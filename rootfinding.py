#!/usr/bin/python3

import numpy as np

def bisection(f,a,b,tol=1e-7,N=1000,verb=1):
    c=0;
    if (f(a)*f(b)<0):
        for i in range(N):

            c=a+(b-a)/2.0;

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

def regulafalsi(f,a,b,tol=1e-7,N=1000,verb=1):
    c=0;
    if (f(a)*f(b)<0):
        for i in range(N):

            c=(a*f(b)-b*f(a))/(f(b)-f(a));

            if (np.abs(f(c))<tol):
                break;

            if (f(a)*f(c)<0):
                b=c;
            else:
                a=c;

        if (i+1==N):
            print("Error: Regula Falsi cannot converge within the prescribed tolerance (Nmax="+str(N)+").");
        else:
            if (verb==1):
                print("Regula Falsi converged in "+str(i+1)+" iteration.");
                print("The root is: ", "%.15f" % c);
    else:
        print("Error: f(a)*f(b)>0.");

    return c;

def regulafalsi_Illinois(f,a,b,tol=1e-7,N=1000,verb=1):
    c=0;
    if (f(a)*f(b)<0):
        m1=1;
        m2=1;
        d=0;
        for i in range(N):

            c=(a*f(b)*m1-b*f(a)*m2)/(f(b)*m1-f(a)*m2);
            m1=1;
            m2=1;

            if (np.abs(f(c))<tol):
                break;

            if (f(a)*f(c)<0):
                b=c;
                if ((d*f(c)>0) and (i>0)):
                    m2=1/2;
            else:
                a=c;
                if ((d*f(c)>0) and (i>0)):
                    m1=1/2;
            d=f(c);

        if (i+1==N):
            print("Error: Regula Falsi (Illinois) cannot converge within the prescribed tolerance (Nmax="+str(N)+").");
        else:
            if (verb==1):
                print("Regula Falsi (Illinois) converged in "+str(i+1)+" iteration.");
                print("The root is: ", "%.15f" % c);
    else:
        print("Error: f(a)*f(b)>0.");

    return c;

def regulafalsi_AndersonBjork(f,a,b,tol=1e-7,N=1000,verb=1):
    c=0;
    if (f(a)*f(b)<0):
        m1=1;
        m2=1;
        d=0;
        for i in range(N):
            c=(a*f(b)*m2-b*f(a)*m1)/(f(b)*m2-f(a)*m1);
            m1=1;
            m2=1;

            if (np.abs(f(c))<tol):
                break;

            if (f(a)*f(c)<0):
                if ((d*f(c)>0) and (i>0)):
                    m1=1-f(c)/f(b);
                    if (m1<0):
                        m1=1/2;
                b=c;
            else:
                if ((d*f(c)>0) and (i>0)):
                    m2=1-f(c)/f(a);
                    if (m2<0):
                        m2=1/2;
                a=c;
            d=f(c);

        if (i+1==N):
            print("Error: Regula Falsi (Anderson-Bjork) cannot converge within the prescribed tolerance (Nmax="+str(N)+").");
        else:
            if (verb==1):
                print("Regula Falsi (Anderson-Bjork) converged in "+str(i+1)+" iteration.");
                print("The root is: ", "%.15f" % c);
    else:
        print("Error: f(a)*f(b)>0.");

    return c;

# end python
