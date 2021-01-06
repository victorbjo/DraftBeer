import os
def restore(fileName):
    example = open(fileName+"Skabelon.txt", "r")
    writeTo = open(fileName+".txt", "w")
    example = example.read()
    writeTo.write(example)
    print(example)
    writeTo.close()
    writeTo = open(fileName+".txt", "r")
    print(writeTo.read())
    #example.close()
    
def allFiles():
    restore("toPi")
    restore("toArd")

