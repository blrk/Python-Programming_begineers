#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program: Lecture-2.py
Author: blrk
Compute a person’s income tax.
1. Significant constants
tax rate
standard deduction
deduction per dependent
2. The inputs are
gross income
number of dependents
3. Computations:
taxable income = gross income - the standard
deduction - a­ deduction for each dependent
income tax = is a fixed percentage of the taxable income
4. The outputs are the income tax
"""

# initialize the constants
TAX_RATE = 0.20
STANDARED_DEDUCTION = 10000
DEPENDENT_EDUCATION = 3000

# Get the inputs
grossIncome = float(input("enter the gross income: "))
numDependents = int(input("enter the number of dependents: "))

# compute the income tax
taxableIncome = grossIncome - STANDARED_DEDUCTION - \
DEPENDENT_EDUCATION * numDependents * TAX_RATE

# print the income tax
print("Thje income tax is :", taxableIncome)



