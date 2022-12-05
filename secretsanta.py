import random

DIRECTORY = "assignments/"
NEWLINES = "\n"*8
NAMES = [ 
    "Spencer", "Jimmy", "Justin", "AJ", "Sam", "Brendan", "Tyler", "Xander", "Zac", 
    "Carter", "Adam", "Jack", "Brian", "Drew", "Damien", "Griffin", "Brandon" 
]

def main():
    # add names to list if not predefined above
    if len(NAMES) == 0:
        name = " "
        while(name != ""):
            name = input("Name of person to be added:\n").lower()
            NAMES.append(name)
    
    print(NAMES)

    if len(NAMES) < 3: # we want at least 3 names to in order for it to be unknown
        print("not enough names in list. Exiting now.")
        return
    
    # shuffle the list to avoid any particular order.
    random.shuffle(NAMES)
    
    # create files with assignments in each
    createFiles(NAMES)

def createFiles(names):
    namesRemaining = names.copy()

    index = 0
    for i in names:
        # change directory name to your desired location
        filename = f"{DIRECTORY}{i}.txt"
        f = open(filename, "w")

        if len(namesRemaining) > 3:
            while(True):
                # find a random location to assign someone to and don't allow them to get themselves
                randomNum = random.randint(0, len(namesRemaining)-1)
                name = namesRemaining[randomNum]
                if name == i: continue # will repeat if they got themselves
            
                f.write(f"{NEWLINES}{i}, your assignment is:\n\t{name}")
                f.close()
                namesRemaining.remove(name)
                break
        
        else:
            print("Last 3")
            name = namesRemaining[(index + 1) % 3]
            f.write(f"{NEWLINES}{i}, your assignment is:\n\t{name}")
            f.close()
            index += 1

if "__main__" == __name__:
    main()
