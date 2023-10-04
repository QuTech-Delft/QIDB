from .gate import Gate, OperandType
import sympy as sp

signature = []

matrix = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
])

CNOT = Gate("CNOT", "The CNOT gate", 2, signature, (), matrix)