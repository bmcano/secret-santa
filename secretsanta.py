import random

def main():
    # add names to list or use second method below
    names = ["Name1","Name2","Name3"]
    random.shuffle(names)
    
    # use if you want to add names as an input rather than predefined
    # names = list()
    # while(True):
    #     name = input("Name of person to be added:\n").lower()
    #     if name == "": 
    #         break
    # 
    #     names.append(name)
    # 
    # if len(names) < 2:
    #     print("not enough names in list")
    #     return
    
    # print(names)
    createFiles(names)


def createFiles(names):
    stringbuilder = str()
    namesLeft = names.copy()

    for i in names:
        # change directory name to your desired location
        stringbuilder = f"directory name/{i}.txt"
        f = open(stringbuilder, "w")

        while(True):
            randomNum = random.randint(0, len(namesLeft)-1)
            name = namesLeft[randomNum]

            # cant let someone get themselves
            if name == i:
                continue
        
            # print(f"{i}, your assignment is:\n\t{name}")
            f.write(f"{i}, your assignment is:\n\t{name}")
            f.close()
            namesLeft.remove(name)
            break

if "__main__" == __name__:
    main()