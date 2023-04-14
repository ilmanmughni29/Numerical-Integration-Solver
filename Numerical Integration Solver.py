# Muhammad Ilman Mughni 
# NPM: 2006537324
# f(x) = 2**0 + 0**6 + 5**3 + 7**3 + 2**4
# f(x) = 1 + 12*x**3 + 2*x**4
import numpy as np
import time

st = time.time()

# Define function to integrate
def f(x):
    return 1 + 12*x**3 + 2*x**4

# Implementing trapezoidal method
def trapezoidal (f,a,b,n):
    h = (b-a)/n
    integration = f(a) + f(b)
    for i in range(1,n):
        k = a + i*h
        integration = integration + 2 * f(k)
    integration = integration * h/2
    return integration

#implementing midpoint method
def midpoint (f,a,b,n):
    h = (b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

def trapezoidalVec(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

def midpointVec(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a + h/2, b - h/2, n)
    return h*sum(f(x))

# Input section
a = 1
b = 5
n = 10

# Call integration method and get result
print ("\nresult:")
print ("n   trapezoidal     midpoint      trapVec        midVec")
for i in range (1,n):
    n = 2**i
    trap = trapezoidal (f,a, b, n)
    et1 = time.time()
    ep1 = et1 - st
    mid = midpoint (f,a,b,n)
    et2 = time.time()
    ep2 = et2 - st
    trapVec = trapezoidalVec (f,a,b,n)
    et3 = time.time()
    ep3 = et3 - st
    midVec = midpointVec (f,a,b,n)
    et4 = time.time()
    ep4 = et4 - st
    print ((n),"|", "%0.6f"%(trap),"|", "%0.6f"%(mid),"|", "%0.6f"%(trapVec),"|", "%0.6f"%(midVec))

print("\nnumerical integration execution time:")
print("trap execution time: %0.10f" %(ep1))
print("mid execution time: %0.10f" %(ep2))
print("trapVec execution time: %0.10f" %(ep3))
print("midVec execution time: %0.10f" %(ep4))
print(" ")

# calculate error
# exact value = 3125.6
err_trap = abs(((3125.6 - trap)/3125.6)*100)
err_mid = abs(((3125.6 - mid)/3125.6)*100)
err_trapVec = abs(((3125.6 - trapVec)/3125.6)*100)
err_midVec = abs(((3125.6 - midVec)/3125.6)*100)
print ("error value:")
print("The error of trap result is: %0.4f" % (err_trap), '%')
print("The error of mid result is: %0.4f" % (err_mid), '%')
print("The error of trapVec result is: %0.4f" % (err_trapVec), '%')
print("The error of midVec result is: %0.4f" % (err_midVec), '%')

et = time.time()
elapsed_time = et-st
print ('\nprogram execution time: ', elapsed_time, 'seconds')