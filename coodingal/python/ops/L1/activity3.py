class Parrot:

    species = "Bird"

    def __init_(self, name, age):
         self.name = name
         self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("woo", 15)

print("blu is a {}".format(blu.species))
print("woo is also a {}".format(woo.species))

print("{} is {} is years old".format( blu.name, blu.age))
print("{} is {} years old". format(woo.name, woo.age)) 