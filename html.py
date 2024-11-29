def get_html_content(giver, receiver):
    return f"""<!DOCTYPE html>
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
            background-position: 0 0, 10px 10px;
            color: white;
        }}
        .card {{
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            max-width: 500px;
            margin: auto;
            background-color: white;
            color: black;
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
</html>"""