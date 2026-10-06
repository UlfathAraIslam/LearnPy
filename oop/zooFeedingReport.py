class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def feeding_cost(self):
        return 0


class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} says: Roar!")

    def feeding_cost(self):
        return 3000


class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} says: Trumpet!")

    def feeding_cost(self):
        return 4000


def main():
    animals = []

    while True:
        animal_type = input("Animal type (lion/elephant, or 'done' to finish): ")
        if animal_type == "done":
            break

        name = input("Animal name: ")

        if animal_type == "lion":
            animals.append(Lion(name))
        elif animal_type == "elephant":
            animals.append(Elephant(name))
        else:
            print("Unknown animal type, skipping.")
            continue

    total_cost = 0
    for a in animals:
        a.make_sound()
        total_cost += a.feeding_cost()

    print(f"Total daily feeding cost: ¥{total_cost}")


if __name__ == "__main__":
    main()