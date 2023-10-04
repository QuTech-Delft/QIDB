import sympy as sp
from enum import Enum
import typing
import numpy as np

class OperandType(Enum):
    FLOAT = 0
    INT = 1


class Gate:
    def __init__(self, name: str, description: str, numberOfQubits: int, signature: [OperandType], arguments: tuple[sp.core.basic.Atom,...], matrix: sp.Matrix):
        self.name = name
        self.description = description
        self.numberOfQubits = numberOfQubits
        self.signature = signature
        self.arguments = arguments
        self._matrix = matrix

        assert(sp.shape(self._matrix) == (1 << numberOfQubits, 1 << numberOfQubits))
    
    def __call__(self, *args):
        assert(len(args) == len(self.arguments))

        result = self._matrix.subs(dict(zip(self.arguments, args)))

        isConcreteCall = all(isinstance(x, int) or isinstance(x, float) for x in args)

        if isConcreteCall:
            result = np.array(result).astype(np.complex128)
        
        return result
    
    def __repr__(self):
        # TODO: LaTeX? Pretty-printing?
        return f"""{self.name} ({self.description}) =\n{self._matrix}\n"""
    
    # TODO: infer angle and axis, or add constructor for providing directly angle and axis representation