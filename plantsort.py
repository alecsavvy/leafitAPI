# file will create JSONs from text file, extracted from PDF

# list of plant objects
plants = []


class Plant:
    def __init__(self, name, description):
        self.name = name  # type=string
        self.description = description  # type=list of strings
        self.sorted_des = None

    def __str__(self):
        return "plant: " + self.name

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_sorted(self):
        return self.sorted_des

    def sort_description(self, des):
        # des type=list of strings
        varlist = [
            "General Botanical Characteristics",
            "Seasonal Development",
            "Distribution/Habitat",
            "Interesting Facts",
            "References"
        ]

        self.sorted_des = {
            "General Botanical Characteristics": [],
            "Seasonal Development": [],
            "Distribution/Habitat": [],
            "Interesting Facts": [],
            "References": []
        }

        index = 0
        for line in self.description:
            if index <= 4 and line == varlist[index]:
                index += 1
            else:
                self.sorted_des[varlist[index-1]].append(line)


def main():
    with open("plantGuide.txt", "r", encoding='utf-8') as inp:
        data = []
        for line in inp:
            line = line.strip()
            data.append(line)

    plant_dict = listParse(data)
    makeobjs(plant_dict)
    return None


def run():
    main()
    return None


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


def makeobjs(plant_dict):
    for key in plant_dict:
        if key == 0:
            print()
        else:
            # print("key: " + str(key))
            name = plant_dict[key][0]
            plist = plant_dict[key]
            plant = Plant(name, plist[1:])
            plant.sort_description(plant.description)
            plants.append(plant)
    return None
