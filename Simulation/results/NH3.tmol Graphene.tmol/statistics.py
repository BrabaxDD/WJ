import json
from ase.io import read, write
with open("defectdir/xtbout.json")as file:
    data = json.load(file)

partial_charges = data["partial charges"]
atoms = read("defectdir/xtbopt.coord")
positions = atoms.get_positions()
types = atoms.get_chemical_formula("all")
types = list(types)
transfer = 0
for i in range(0, len(atoms)):
    pos = positions[i]
    typ = types[i]
    charge = partial_charges[i]
#   print("The Atom is:" + str(typ) + "it is at: " +
#         str(pos) + "and has partial charge" + str(charge))
    if i < len(atoms) - 2:
        transfer = transfer + charge
print("the total charge tranfer is: " + str(transfer))

print("statistics done")
