import json
import os
from ase.io import read, write
with open("defectdir/xtbout.json")as file:
    dataDefect = json.load(file)
with open("gasdir/xtbout.json")as file:
    dataGas = json.load(file)
with open("interactiondir/xtbout.json")as file:
    dataInteraction = json.load(file)

with open("./../results.txt", "a") as file:
    currentpath = str(os.getcwd())
    currentdir = currentpath.split("/")[-1]
    file.write("The Interaction Energy of " + currentdir + " is: " +
               str(dataInteraction["total energy"] - dataGas["total energy"] - dataDefect["total energy"]) + " \n")


partial_chargesDefect = dataDefect["partial charges"]
atomsDefect = read("defectdir/xtbopt.coord")
positionsDefect = atomsDefect.get_positions()
typesDefect = atomsDefect.get_chemical_formula("all")
typesDefect = list(typesDefect)
transfer = 0

atomsGas = len(dataGas["partial charges"])
atomsInteraction = read("interactiondir/xtbopt.coord")
for i in range(0, len(atomsInteraction)):
    pos = atomsInteraction.get_positions()[i]
    typ = atomsInteraction.get_chemical_formula("all")[i]
    charge = dataInteraction["partial charges"][i]
    if i < len(atomsDefect) - atomsGas:
        transfer = transfer + charge
print("the total charge tranfer is: " + str(transfer))
with open("./../results.txt", "a") as file:
    currentpath = str(os.getcwd())
    currentdir = currentpath.split("/")[-1]
    file.write("The Charge Transfer of " + currentdir + " is: " +
               str(transfer) + " \n")


print("statistics done")
