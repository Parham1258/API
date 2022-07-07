#API
import os
from flask import Flask, render_template, send_file, request
import random
import webbrowser
from waitress import serve
import sys

class color: #Credits: Doci Team
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'


def clear_console(): #Credits: Doci Team
    if os.name in ('nt', 'dos'): #Check OS Name
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

def change_title(title: str): #Credits: Doci Team
    if os.name in ('nt', 'dos'): #Check OS Name
        try:
            os.system("title "+title)
        except:
            pass
    else:
            pass

change_title("API")
clear_console()

app = Flask("app", template_folder="Templates")

@app.errorhandler(404) 
def Handler_404(error):
    if random.randint(0, 12) == 0: return render_template("Secret 404.html")
    else: return render_template("404.html")
@app.route("/")
def Home(): return render_template("Home.html")
@app.route("/API")
def API(): return render_template("API.html")
@app.route("/API/Password-Generator")
def API_Password_Generator():
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    generated_password = ""
    for i in range(20): generated_password += random.choice(characters)
    return "{ \"Generated Password\": \""+generated_password+"\" }", 200
@app.route("/Assets/<file>")
def styles(file):
  try: return send_file("Assets/"+file)
  except IOError: return "File Doesn't Exists"
@app.route("/favicon.ico")
def icon(): return send_file("Assets/API.png")

debug=False
print(color.Green+"Starting Server...")
if debug:
    webbrowser.open("http://localhost:8080/")
    app.run(host='0.0.0.0', port=8080, debug=True)
else:
    webbrowser.open("http://localhost:80/")
    serve(app, host="0.0.0.0", port=80)
sys.exit(2)