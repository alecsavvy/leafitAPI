import plantsort

tasks = []


def run():
    main()
    return None


def main():
    title = ["General Botanical Characteristics",
             "Distribution/Habitat",
             "Seasonal Development",
             "Interesting Facts",
             "References"
             ]
    plantsort.run()
    plants = plantsort.plants
    counter = 1
    for plant in plants:
        info = plants[0].get_sorted()
        d = {"id": counter,
             "Name": plant.get_name(),
             "General Botanical Characteristics": info[title[0]][0],
             "Distribution/Habitat": info[title[1]][0],
             "Seasonal Development": info[title[2]][0],
             "Interesting Facts": info[title[3]][0],
             "References": info[title[4]][0]
             }
        tasks.append(d)
        counter += 1

    return None

