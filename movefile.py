import os

source = "C:\\Users\\jcari\\OneDrive\\Documents\\PythonCode\\BroCode\\Day2\\test.txt"
destination = "C:\\Users\\jcari\\OneDrive\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + " was moved")
except: FileNotFoundError: print(source +" was not found")
