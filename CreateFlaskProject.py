import os

# Create a flask project folder system. 


def first_steps(projectName):
    if len(projectName) < 1:
        return first_steps(input("Project name cannot be blank!\nNew Project Name: "))
    try:
        os.mkdir(projectName)
    except FileExistsError:
        return first_steps(input('Project name you suppleid already exists!\nNew Project Name:'))
    os.mkdir(f'{projectName}/Templates')
    os.mkdir(f'{projectName}/Static') 
    with open(f'{projectName}/main.py','w',encoding='UTF-8') as mainpy:
        mainpy.write("""
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('layout.html')


app.run(debug=True)""")

    with open(f'{projectName}/layout.html','w',encoding="UTF-8") as layouthtml:
        layouthtml.write(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block title %}
    <title>Document</title>
    {% endblock %}
    {% block css %}
    <link rel="stylesheet" href="#">
    {% endblock %}
    
    
</head>
<body>
    {% block body %}
    {% endblock %}
    
</body>
</html>""")
    return f"Successfully created your project: {projectName}"

print(first_steps(input('Project Name: ')))