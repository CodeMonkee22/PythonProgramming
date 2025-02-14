
name = "Bro"  # global scope (avaliable inside & outside functions)
 
def display_name():
    name = "Code" # local scope (only avaliable only inside function)
    print(name)

display_name()
print(name)
