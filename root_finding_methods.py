import numpy as np
import random

############################# assistance functions ####################################
#### to do###
#2. create function that check ranges in different sizes - maybe random arrays are better?
#3. think of a better way to run over the array in the bracketing function



def bracketing_func(func):
    #finds 2 values a, b such that f(a)<0 , f(b) > 0
    a = 0
    b = 0
    #we will create arrays for X in range
    x = 0
    while func(a) >= 0 or func(b) <= 0:
        if func(a) == 0:
            return (a, a) #root was found by accident
        if func(b) == 0:
            return (b, b) #root was found by accident
        A = list(range(-(2)**x, 2**x + 1))
        for i in range(len(A)):
            if func(A[i]) == 0:
                return (A[i],A[i])  # root was found by accident
            if func(A[i]) > 0:
                b = A[i]
            else:
                a = A[i]
            if func(a) < 0 and func(b) > 0:
                return (a, b)
        x += 1

    return (a, b)

def root_finding_func(z,input): # function to find the root of input (= num)
    return z**2 - input

def func(z):
    return z**2 - 3


# find the roots of the function using the different methods learned

def find_root_bisection_method(delta, func):
    #bracketing:
    res = bracketing_func(func)  # a tuple
    if res[0] == res[1]:
        return res[0] #root was found using the bracketing method
    else:
        a = res[0]
        b = res[1]

    #a,b being 2 initial guesses bracketing the root (f(a) negative, f(b) positive)
    z = 0.5 * (a + b)
    while abs(b-a) > delta:
        if func(z) * func(a) < 0: #(f(a) negative and f(z) positive,z<b)
            b = z
        else: #(f(a) and f(z) negative, |z|<|a|)
            a = z
        z = 0.5 * (a + b)
    return z


print((find_root_bisection_method(0.0005, func))**2)


def find_root_regula_falsi_method(delta,func):

    #bracketing:
    res = bracketing_func(func)  # a tuple
    if res[0] == res[1]:
        return res[0] #root was found using the bracketing method
    else:
        a = res[0]
        b = res[1]

    #a,b being 2 initial guesses bracketing the root (f(a) negative, f(b) positive)
    c = b - ((func(b) * (b - a)) / (func(b) - func(a)))

    while abs(func(c)) > delta:
        if func(c) * func(b) < 0:  # (f(c) negative and f(b) positive,|c|<|a|)
            a = c
        else:  # (f(b) and f(c) positive, |c|<|b|)
            b = c
        c = b - ((func(b) * (b - a)) / (func(b) - func(a)))
    return c

print((find_root_regula_falsi_method(0.0005,func))**2)


def find_root_secant_method(delta,func):
    # x0,x1 being 2 initial guesses near the root, |f(x1)|<|f(x0)|
    x0 = random.random()
    x1 = random.random()
    if abs(func(x1)) < abs(func(x0)):
        z = x1
    else:
        z = x0
    while abs(func(z)) > delta:
        z = x1 - ((func(x1)*(x1-x0))/(func(x1) - func(x0)))
        x0 = x1
        x1 = z
    return z

print((find_root_secant_method(0.0005,func))**2)


################################ Newton raphson #######################################

