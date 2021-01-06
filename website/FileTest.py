import time
a = time.time()
for x in range(1000):
    file = "testFile.txt"
    f = open(file, "w")
    fread = f.write("OKkk\nOKkkk\nOKass\nOKdfas\nOKokmibi\nOKasdvrfa\nOKasfrg\nOKasdads\nOKasdad\nOKasdsad\nOK")
    f.close()
b = time.time()
print (b-a)
