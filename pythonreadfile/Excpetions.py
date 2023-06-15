ItemCart = 0
if ItemCart != 2:#raise Exception("Product Cart Count Not Matched")
    pass
assert(ItemCart == 0)

try:
    file = open("readtexte.txt")
    for line in file.readlines():
        print(line)

except Exception as e:
    print(e)

finally:
    print("cleaning the memory")

