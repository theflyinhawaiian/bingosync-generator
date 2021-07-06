easyObjs = open("easy_objectives.txt", "r")
easyObjsArr = easyObjs.read().strip().split("\n")
easyObjs.close()

mediumObjs = open("medium_objectives.txt", "r")
mediumObjsArr = mediumObjs.read().strip().split("\n")
mediumObjs.close()

hardObjs = open("hard_objectives.txt", "r")
hardObjsArr = hardObjs.read().strip().split("\n")
hardObjs.close()

print(easyObjsArr)
print(mediumObjsArr)
print(hardObjsArr)
