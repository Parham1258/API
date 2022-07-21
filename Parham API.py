# Parham API
import os
from flask import Flask, render_template, request, abort, send_file, redirect
import random
import time
#from waitress import serve
#import sys

def change_title(title: str): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("title "+title)
        except: pass
    return

def clear_console(): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("cls")
        except: pass
    else:
        try: os.system("clear")
        except: pass
    return

class color: #Credits: Doci Team
    Red = "\033[91m"
    Green = "\033[92m"
    Blue = "\033[94m"
    Cyan = "\033[96m"
    White = "\033[97m"
    Yellow = "\033[93m"
    Magenta = "\033[95m"
    Grey = "\033[90m"
    Black = "\033[90m"
    Default = "\033[99m"

change_title("Parham API")
clear_console()

Rate_Limits = {}

app = Flask("Parham API", template_folder="Templates")

@app.errorhandler(404) 
def Handler_404(error):
    if random.randint(0, 12) == 0: return render_template("Secret 404.html"), 404
    else: return render_template("404.html"), 404
@app.errorhandler(429)
def Handler_429(error): return "", 429
@app.before_request
def Rate_Limit():
    if not request.path.startswith("/Assets/"):
        global Rate_Limits
        if request.remote_addr in Rate_Limits:
            if Rate_Limits[request.remote_addr] > time.time(): abort(429)
            Rate_Limits[request.remote_addr] += 4
        else: Rate_Limits[request.remote_addr] = time.time() + 4
@app.route("/")
def Home(): return render_template("Home.html"), 200
@app.route("/API")
def API(): return render_template("API.html"), 200
@app.route("/API/Password-Generator", methods=["GET", "POST"])
def API_Password_Generator():
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    generated_password = ""
    if "Characters" in request.args:
        try:
            length = int(request.args["Characters"])
            if length > 100: length = 20
        except: length = 20
    else: length = 20
    for i in range(length): generated_password += random.choice(characters)
    return "{ \"Generated Password\": \""+generated_password+"\" }", 200
@app.route("/API/8ball", methods=["GET", "POST"])
def API_8ball():
    words = ["Yes", "no", "maybe", "not now", "never", "100%", "nope", "idk", "Yeah", "no u", "ye", "No"]
    word = random.choice(words)
    return "{ \"8ball\": \""+word+"\" }", 200
@app.route("/API/UNIX", methods=["GET", "POST"])
def API_UNIX(): return "{ \"UNIX\": \""+str(time.time())+"\" }", 200
@app.route("/API/Reverse-Text")
def API_Reverse_Text():
    if "Text" in request.args and request.args["Text"] != "": Text = request.args["Text"]
    else: Text = "Hello"
    Text.replace("\"", "\\\"")
    Reversed_Text = Text[::-1]
    return "{ \"Reversed Text\": \""+Reversed_Text+"\" }", 200
@app.route("/API/Random-Number", methods=["GET", "POST"])
def API_Random_Number():
    if "From" in request.args and "To" in request.args:
        try:
            From = int(request.args["From"])
            To = int(request.args["To"])
            if From >= To:
                From = 1
                To = 10
        except:
            From = 1
            To = 10
    else:
        From = 1
        To = 10
    number = random.randint(From, To)
    return "{ \"Random Number\": \""+str(number)+"\" }", 200
@app.route("/API/Random-Floating-Number", methods=["GET", "POST"])
def API_Floating_Random_Number():
    if "From" in request.args and "To" in request.args:
        try:
            From = float(request.args["From"])
            To = float(request.args["To"])
            if From >= To:
                From = 1
                To = 10
        except:
            From = 1
            To = 10
    else:
        From = 1
        To = 10
    number = random.uniform(From, To)
    return "{ \"Random Floating Number\": \""+str(number)+"\" }", 200
@app.route("/Assets/<string:File>")
def Assets(File):
  if os.path.exists("Assets/"+File): return send_file("Assets/"+File), 200
  else: return "File Doesn't Exists", 404
@app.route("/favicon.ico")
def Icon(): return redirect("/Assets/API.png"), 301

print(color.Green+"Starting Server...")
#app.run(host="0.0.0.0", port=80, debug=True)
#serve(app, host="0.0.0.0", port=80)
#sys.exit(2)