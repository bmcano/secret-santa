# Secret Santa Assignment Generator
A Python script that generates personalized Secret Santa assignments and creates a unique webpage for each participant. 
Each participant receives a random assignment via a custom link, which they can use to view their assignment. 
The script also ensures no participant is assigned to themselves.

## How It Works
1. **Input**: A text file, `names.txt`, containing the names of all participants, each on a new line.
2. **Shuffle and Assign**: Randomly assigns Secret Santa partners while ensuring no one gets themselves.
3. **Webpage Generation**: Creates a unique HTML file for each participant with a festive design.
4. **Links**: Outputs the unique links to send out to each participant to access their assignment. 

## Links

Each link follows this structure:
```
https://bmcano.github.io/secret-santa/public/{random-string}.html
```
