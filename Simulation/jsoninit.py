import json
jsonFile = {"lucke": [], "transfer": [], "Adsorbtionsenergie": []}

with open("results/results.txt", "w") as file:
    json.dump(jsonFile, file)
