class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = [] 
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name_species)
        elif species == "fish":
            self.fishes.append(name_species)
        elif species == "bird":
            self.birds.append(name_species)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            self.mammals = ", ".join(self.mammals)
            return f"Mammals in {self.name}: {self.mammals} \nTotal animals: {Zoo.__animals}" 
        elif species == "fish":
            self.fishes = ", ".join(self.fishes)
            return f"Fishes in {self.name}: {self.fishes} \nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            self.birds = ", ".join(self.birds)
            return f'Birds in {self.name}: {self.birds} \nTotal animals: {Zoo.__animals}'

name = input()
number = int(input())
zoo = Zoo(name)


for i in range(number):
    anima_info = input()

    anima_info = anima_info.split(" ")

    species = anima_info[0]
    name_species = anima_info[1]

    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
