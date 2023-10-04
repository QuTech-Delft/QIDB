# QIDB
Quantum Inspire gate DataBase

# Expected usage

``python
import qidb

print(qidb.gates.X.name)
print(qidb.gates.X.matrix) # Numpy ndarray?
print(qidb.gates.RX.matrix) # Sympy matrix
print(qidb.gates.RX.matrix(3.1415)) # Numpy ndarray
print(qidb.gates.RX.picture) # Binary data? Python bytes object
print(qidb.gates.RX.signature)
```