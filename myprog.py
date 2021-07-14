def fileIo(file):  
    f = open(file, "r")
    print("\nThe content of the file is as follow :\n")
    print(f.read())

file = input("Input the name of the file please :")
fileIo(file)