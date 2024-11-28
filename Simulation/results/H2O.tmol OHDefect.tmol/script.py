from ase.io import read, write
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
gas = read("gas")
defect = read("defect")
print("------------------------------------------------------------------------------------------------------")
print("calculating: " + dir_path)
print(gas.get_positions())
interaction = gas + defect
interaction.write("interaction", format="turbomole")
