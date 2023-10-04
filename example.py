# Example usage of the QIDB

import qidb

import sympy as sp
import math

# Pretty-print X as Sympy matrix
print(qidb.gates.X)
print()

# Returns X as Numpy array
print(qidb.gates.X())
print()

# Query numpy RX with symbolic argument
# Should fail if not all arguments are provided.
print(qidb.gates.RX(sp.pi))
print()

# Query numpy RX with concrete float argument
# Should fail if not all arguments are provided.
print(f"RX(π) =\n{qidb.gates.RX(math.pi)}")
print()

print(f"RX(π/2) =\n{qidb.gates.RX(math.pi / 2)}")
print()

# Pretty-print CNOT as Sympy matrix
print(qidb.gates.CNOT)
print()

# Numpy CNOT
print(qidb.gates.CNOT())
print()