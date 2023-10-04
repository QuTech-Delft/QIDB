from .gate import Gate, OperandType
import sympy as sp

signature = []

matrix = sp.Matrix([
    [0, 1],
    [1, 0],
])

X = Gate("X", "The Pauli-X gate, or σₓ", 1, signature, (), matrix)