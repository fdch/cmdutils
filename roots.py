#!/usr/local/bin/python3
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #
# -*- coding: utf-8 -*-
""" Get the roots of a polynomial equation """

from math import sqrt, pow
from numpy import conj
from fractions import Fraction
from decimal import Decimal

ROUND = 3

def rounder(f): 
    return round(Decimal(f), ROUND)

def display(*args):
    for f in args:
        if isinstance(f, float):
            if f.is_integer():
                return f"{int(f)},"
            else:
                r = rounder(f)
                return f"{r} = {Fraction(r)}"
        else: # complex 
            return f"{f},"

def discriminant(a,b,c):
    d = pow(b,2)
    d -= 4 * a * c
    return d

def roots(a,b,c):
    print("-"*80)
    print(f"a = {a}, b = {b}, c = {c}")
    d = discriminant(a,b,c)
    b_op = -b
    
    if d == 0:
        print('--> One root')
        x0 = b_op
        x0 /= 2 * a
        print(f"""
        \u0394 = {d}
        x0 = {display(x0)}
        """)
    else:
        is_real = d > 0
        
        if is_real:
            print('--> 2 Real roots')
            x1 = b_op + sqrt(d) 
            x2 = b_op - sqrt(d)
        else:
            print('--> 2 Complex roots')
            x1 = b_op + sqrt(-d) * 1j
            x2 = b_op - sqrt(-d) * 1j
        
        x1 /= 2 * a
        x2 /= 2 * a
        
        r_sum = b_op / a
        r_mul = c / a
        

        if not is_real:
            try:
                # get the conjucate of the complex number x1
                assert x2 == conj(x1)
            except:
                print(f"Warning: x2 != conj(x1), conj(x1) = {conj(x1)}")
        else: 
            r_sum_1 = rounder(x1 + x2)
            r_mul_1 = rounder(x1 * x2)
            
            try:
                assert r_sum_1 == rounder(-b/a)
            except:
                print(f"Warning: x1 + x2 != -b/a, Sum of roots {r_sum}, {r_sum_1}")
            
            try:
                assert r_mul_1 == rounder(c/a)
            except:
                print(f"Warning: x1 * x2 != c/a, Mul of roots {r_mul}, {r_mul_1}")
        
        print(f"""
        \u0394 = {display(d)}
        x1 = {display(x1)}
        x2 = {display(x2)}
        r_sum = {display(r_sum)}
        r_mul = {display(r_mul)}
        """)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solve quadratic equation')
    parser.add_argument('a', type=float, help='coefficient a')
    parser.add_argument('b', type=float, help='coefficient b')
    parser.add_argument('c', type=float, help='coefficient c')
    # add optional argument for rounding
    parser.add_argument('--round', type=int, default=4, help='rounding')
    args = parser.parse_args()
    ROUND = args.round
    roots(args.a, args.b, args.c)
    # roots(*list(map(lambda x : Decimal(x), (args.a, args.b, args.c))))
