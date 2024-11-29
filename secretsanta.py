import random
import hashlib

PUBLIC_LINK = "https://bmcano.github.io/secret-santa/"
PUBLIC_DIR = "public/"

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

    # Generate assignments
    assignments = createAssignments(names)
    links = generateHTML(assignments)

    print("\nLinks for participants:")
    for name, link in links.items():
        print(f"{name}: {link}")

def createAssignments(names):
    namesRemaining = names.copy()
    assignments = {}

    file = open("assignments.txt", "w")
    index = 0
    for i in names: 
        if len(namesRemaining) > 3:
            while(True):
                name = random.choice(namesRemaining)
                if name == i: continue # will repeat if they got themselves
                file.write(f"{i} -> {name}\n")
                assignments[i] = name
                namesRemaining.remove(name)
                break
        else:
            print("Last 3")
            name = namesRemaining[(index + 1) % 3]
            file.write(f"{i} -> {name}\n")
            index += 1
    file.close()
    return assignments

def generateHTML(assignments):
    links = {}
    print(assignments)
    for giver, receiver in assignments.items():
        unique_id = hashlib.sha256(giver.encode()).hexdigest()[:8]
        filename = f"{PUBLIC_DIR}{unique_id}.html"
        links[giver] = f"{PUBLIC_LINK}{unique_id}.html"

        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Secret Santa Assignment</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                         background-color: red;
                        margin-top: 50px;
                    }}
                    .card {{
                        border: 2px solid #ccc;
                        border-radius: 10px;
                        padding: 20px;
                        max-width: 500px;
                        background-color: white;
                        margin: auto;
                    }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>Merry Cringemas Assignment</h1>
                    <p><strong>{giver}</strong>, your assignment is:</p>
                    <h2>{receiver}</h2>
                </div>
            </body>
            </html>
        """

        # Write to an HTML file
        with open(filename, "w") as f:
            f.write(html_content)

    return links

if "__main__" == __name__:
    main()
