import os
import random
import uuid
from html import get_html_content

YEAR_DIR = "2024/" # update for each year
PUBLIC_LINK = f"https://bmcano.github.io/secret-santa/{YEAR_DIR}" 

def clear_directory(directory):
    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path): os.remove(file_path)


def create_assignments(names):
    namesRemaining = names.copy()
    assignments = {}
    index = 0
    for i in names: 
        if len(namesRemaining) > 3:
            while(True):
                name = random.choice(namesRemaining)
                if name == i: continue # will repeat if they got themselves
                assignments[i] = name
                namesRemaining.remove(name)
                break
        else:
            print("Last 3")
            name = namesRemaining[(index + 1) % 3]
            assignments[i] = name
            index += 1
    return assignments


def generate_html(assignments):
    links = {}
    for giver, receiver in assignments.items():
        unique_id = uuid.uuid4().hex[:8]
        filename = f"{YEAR_DIR}{unique_id}.html"
        links[giver] = f"{PUBLIC_LINK}{unique_id}.html"
        html_content = get_html_content(giver, receiver)
        with open(filename, "w") as f:
            f.write(html_content)
    return links


def main():
    names = []
    with open("names.txt", "r") as file:
        for line in file:
            names.append(line.strip())

    if len(names) < 3:
        print("Not enough names were found in the list, program exited.")
        return

    # shuffle the list to avoid any particular order.
    random.shuffle(names)
    print(names)

    # generate assignments
    clear_directory(YEAR_DIR)
    assignments = create_assignments(names)
    # print(assignments) # for debugging purposes
    links = generate_html(assignments)
    file = open("assignments.txt", "w")
    for name, link in links.items():
        file.write(f"{name}: {link}\n")
    file.close()


if "__main__" == __name__:
    main()
