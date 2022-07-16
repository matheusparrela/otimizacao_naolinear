# Non Linear Optimization - SearchResult
from __future__ import annotations
import sympy
import utils
from dataclasses import dataclass

@dataclass
class SearchResult:
    """
    Class to store all result infos of search methods.
    """

    # Fields (variables of class)

    function: str               #  >> Expression, in text format, informed by the user
    path: list[list[float]]     #  >> List of x1 and x2 of each iteration, like: [[0, 0], [1, 1.5], ...]. Put the start point at first.
    converged: bool             #  >> True if found the result, False if not
    precision_decimals: float   #  >> Precision decimals of the method, like "4" to set the precision 0.0001

    # Predefined fields (variables of class that is automatically initialized)

    path_results: list[float] = None   #  >> The result of f(x1, x2) in each point in path. So, the len(path) == len(path_results). This field is automaticcaly set after the object creation. 
    symbols: str = 'x1 x2'

    # Functions of the class

    def minimum_found(self) -> list[float]:
        return self.path[-1]

    def start_point(self) -> list[float]:
        return self.path[0]

    def iterations(self) -> int:
        return len(self.path) - 1

    def objective_function(self) -> list[float]:
        """
        Objective function is the f(x1, x2) in minimum point, that is, the Z value in minimum point found
        """
        if self.converged:
            return self.path_results[-1]
        else:
            return None

    # Magic functions

    def __post_init__(self):
        """
        Magic function that is called internally in python when the object is creating. 
        This can be used to initialize or change the values of fields (variables) of the class.
        """
        if self.path_results is None:
            symbols_list = sympy.symbols(self.symbols)
            expression = utils.make_expression(self.function)
            self.path_results = []
            for point in self.path:
                self.path_results.append(float(utils.symbols_eval(expression, symbols_list, point)))

    def __str__(self) -> str:
        """
        Magic function that is called when the code call "print(<this object>)"
        """
        result = 'Search result:'
        result += f'\n  function: {self.function}'
        result += f'\n  symbols: {self.symbols}'
        result += f'\n  precision_decimals: {self.precision_decimals}\n  --'
        for k in range(len(self.path)):
            result += f'\n  iteration {k} point {self.path[k]} -> f() = {self.path_results[k]}'
        result += f'\n  --\n  start point: {self.start_point()}'
        result += f'\n  minimum found: {self.minimum_found()}'
        result += f'\n  objective function: {self.objective_function()}'
        result += f'\n  iterations: {self.iterations()}'
        result += f'\n  converged: {self.converged}'
        return result
