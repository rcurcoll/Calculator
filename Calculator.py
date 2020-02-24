#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:31:06 2020

@author: rcurcoll
"""
class Calculator:
    
    urbag_constant = 12.4
    
    def sum(a,b):
        return a+b
    
    def applyUrbag(a,b):
        urbag_constant = 12.4

        result = a*urbag_constant+b
        #self: pq miri en la 'class' Calculator. De fet, podríem escriure Calculator
        return result