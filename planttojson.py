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
        info = plant.sorted_des
        d = {"id": counter,
             "Name": plant.get_name(),
             "General Botanical Characteristics": info[title[0]],
             "Distribution/Habitat": info[title[1]],
             "Seasonal Development": info[title[2]],
             "Interesting Facts": info[title[3]],
             "References": info[title[4]]
             }
        tasks.append(d)
        counter += 1

    return None

