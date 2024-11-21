from ase.io import read,write

gas = read("gas")
defect = read("defect")
print(gas.get_positions())
