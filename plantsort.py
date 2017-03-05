# file will create JSONs from text file, extracted from PDF


class Entry:
    def __init__(self, name, chars, seasonDev, habitat, facts, ref):
        self.name = name
        self.chars = chars
        self.seasonDev = seasonDev
        self.habitat = habitat
        self.facts = facts
        self.ref = ref

    def getName(self):
        return self.name

    def getChar(self):
        return self.chars

    def getSeasonDev(self):
        return self.seasonDev

    def getHabitat(self):
        return self.habitat

    def getFacts(self):
        return self.facts

    def getRef(self):
        return self.ref


def listParse(ulist):
    pagenum = 1
    slist = []
    sdict = {}
    for line in ulist:
        try:
            int(line)
            if int(line) == pagenum:
                sdict[pagenum-1] = slist
                slist = []
                pagenum += 1

        except:
            slist.append(line)

    return sdict


def createObj(sdict):
    chars = []
    seasonDev = []
    habitat = []
    facts = []
    ref = []

    ends = ["Seasonal Development",
            "Distribution/Habitat",
            "Interesting Facts",
            "References"
    ]
    for plant in sdict:
        curLine = sdict[plant]
        if curLine == []:
            continue
        else:
            name = curLine[0]
            curLine.remove(name)
            for line in curLine:
                if line != "Seasonal Development":
                    chars.append(line)
                    curLine.remove(line)
                elif line != "Distribution/Habitat":
                    seasonDev.append(line)
                    curLine.remove(line)
                elif line != "Interesting Facts":
                    habitat.append(line)
                    curLine.remove(line)
                elif line != "References":
                    facts.append(line)
                    curLine.remove(line)
                else:
                    ref.append(line)
                    curLine.remove(line)

        plant = Entry(name, chars, seasonDev, habitat, facts, ref)
        return plant

def printPlant(obj):
    print(obj.getName())
    print(obj.getChar())
    print(obj.getSeasonDev())
    print(obj.getHabitat())
    print(obj.getFacts())
    print(obj.getRef())
    return None


with open("plantGuide.txt", "r", encoding='utf-8') as inp:
    data = []
    for line in inp:
        line = line.strip()
        data.append(line)

print()
plantDict = listParse(data)


for key in plantDict:
    print("key: " + str(key))
    for line in plantDict[key]:
        print(line)
    print()



