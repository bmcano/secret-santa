import random
import uuid

PUBLIC_LINK = "https://bmcano.github.io/secret-santa/public/"
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
            assignments[i] = name
            file.write(f"{i} -> {name}\n")
            index += 1
    file.close()
    return assignments

def generateHTML(assignments):
    links = {}
    print(assignments)
    for giver, receiver in assignments.items():
        unique_id = uuid.uuid4().hex[:8]
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
                        margin-top: 50px;
                        background-color: red;
                        background-image: 
                            radial-gradient(white 1px, transparent 1px),
                            radial-gradient(white 1px, transparent 1px);
                        background-size: 20px 20px;
                        background-position: 0 0, 10px 10px; /* Offset the dots to create a snowy effect */
                        color: white; /* Ensures text is readable on the red background */
                    }}
                    .card {{
                        border: 2px solid #ccc;
                        border-radius: 10px;
                        padding: 20px;
                        max-width: 500px;
                        margin: auto;
                        background-color: white; /* Optional: White card background for contrast */
                        color: black; /* Optional: Black text inside the card */
                    }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>Secret Santa Assignment</h1>
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
