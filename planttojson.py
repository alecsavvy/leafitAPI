import plantsort

tasks = []


def run():
    main()
    return None


def main():
    plantsort.run()
    plants = plantsort.plants
    counter = 1
    for plant in plants:
        info = plants[0].get_sorted()
        d = {"id": counter,
             "name": plant.get_name(),
             "info": info
             }
        tasks.append(d)
        counter += 1

    return None

