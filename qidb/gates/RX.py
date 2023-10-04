from .gate import Gate, OperandType
import sympy as sp

signature = [OperandType.FLOAT]

theta = sp.symbols("theta")

matrix = sp.Matrix([
    [sp.cos(theta / 2), -sp.I * sp.sin(theta / 2)],
    [-sp.I * sp.sin(theta / 2), sp.cos(theta / 2)],
])

RX = Gate("RX", "Arbitrary x-axis rotation gate around the Bloch sphere", 1, signature, (theta,), matrix)