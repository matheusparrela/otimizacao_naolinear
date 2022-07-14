# Non Linear Optimization - Utils
import numpy
import sympy
from collections.abc import Iterable, Sequence

def isiterable(obj: object) -> bool:
    """
    Check if a variable is a iterable, like a list, or not
    """
    return isinstance(obj, Iterable) or isinstance(obj, Sequence)

def symbols_eval(expression, symbols_list, symbols_values):
    """
    Generic function to make substitutions of symbols for values in expression.
    """
    def substitution(expression, symbol, value):
        if isinstance(symbol, sympy.MatrixSymbol) and not isinstance(value, sympy.Matrix):
            value = sympy.Matrix(value)
        return expression.subs(symbol, value)

    if isiterable(expression):
        is_matrix = isinstance(expression, numpy.matrix)
        if is_matrix:
            expression = expression.A
        result = []
        for item in expression:
            result.append(symbols_eval(item, symbols_list, symbols_values))
        if is_matrix:
            result = numpy.matrix(result)
    else:
        result = expression
        if isinstance(symbols_values, numpy.matrix):
            symbols_values = symbols_values.A1
        if isiterable(symbols_list) and isiterable(symbols_values):
            for (symbol, value) in zip(symbols_list, symbols_values):
                result = substitution(result, symbol, value)
        else:
            result = substitution(result, symbols_list, symbols_values)
    return result