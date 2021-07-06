import json, random

easyObjsFile = open("easy_objectives.txt", "r")
easyObjsArr = easyObjsFile.read().strip().split("\n")
easyObjsFile.close()

mediumObjsFile = open("medium_objectives.txt", "r")
mediumObjsArr = mediumObjsFile.read().strip().split("\n")
mediumObjsFile.close()

hardObjsFile = open("hard_objectives.txt", "r")
hardObjsArr = hardObjsFile.read().strip().split("\n")
hardObjsFile.close()

settingsJson = open("settings.json", "r")
parsedSettings = json.loads(settingsJson.read())
settingsJson.close()

easyObjs = random.sample(easyObjsArr, parsedSettings['numEasyObjectives'])
mediumObjs = random.sample(mediumObjsArr, parsedSettings['numMediumObjectives'])
hardObjs = random.sample(hardObjsArr, parsedSettings['numHardObjectives'])

objsArr = []

for obj in easyObjs:
    objsArr.append({"name": obj})

for obj in mediumObjs:
    objsArr.append({"name": obj})

for obj in hardObjs:
    objsArr.append({"name": obj})

with open('output.json', 'w') as json_file:
    json.dump(objsArr, json_file)
