
animal = "cow"
item = "moon"

# print("The " +animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) #positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}"

print(text.format(animal,item))

name = "Bro"

print("Hello, my name is {}.".format(name))
print("Hello, my name is {:10}. nice to meet you".format(name))
print("Hello, my name is {:<10}. nice to meet you".format(name))
print("Hello, my name is {:>10}. nice to meet you".format(name))
print("Hello, my name is {:^10}. nice to meet you".format(name))

number = 1000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))