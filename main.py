from flask import Flask, render_template, send_from_directory, url_for, redirect, render_template, request, flash, send_from_directory, send_file, jsonify, make_response, session, make_response,after_this_request,get_flashed_messages
import uuid
import csv
import json
import os
import random
import io
import requests
import datetime
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image, ImageDraw, ImageFont



app = Flask(__name__)

app.secret_key = os.environ['FLASK_SECRET_KEY']
user_data = []
# pdfmetrics.registerFont(TTFont('Vera','Vera.ttf'))

def get_python_loops_data():
    url="https://api.npoint.io/22d05fa3ee9f0da4f95e"
    res = requests.get(url).json()
    return res

def get_links_and_buttons_data():
    url="https://api.npoint.io/c30e4cf9a778a1b9a622"
    res = requests.get(url).json()
    return res


def get_basic_html_data():
    url="https://api.npoint.io/0b9ddad402449729126c"
    res = requests.get(url).json()
    return res

def get_borders_and_padding_data():
    url="https://api.npoint.io/3aeeef8301d2e5df077a"
    res = requests.get(url).json()
    return res

def get_css_box_model_data():
    url="https://api.npoint.io/8be0c96872a500564ec1"
    res = requests.get(url).json()
    return res

def get_file_handling_data():
    url="https://api.npoint.io/beadacc26a1b6b32bbf2"
    res = requests.get(url).json()
    return res

def get_p5play_basics_data():
    url="https://api.npoint.io/81392477ca243d99e34b"
    res = requests.get(url).json()
    return res


def get_links_buttons_two_data():
    url="https://api.npoint.io/9cbe6a8116e569a99093"
    res = requests.get(url).json()
    return res
# List of questions with answers
questions = []

@app.route("/")
def home():
    # Initialize session variables
    session.pop("current_index", None)
    session.pop("number_correct", None) 
    session.pop('_flashes', None)
    session.pop("total_questions", None)
    session.pop("name", None)
    session.pop("student_id", None)
    session.pop("title", None)
    session.pop("userA", None)
    session.pop("starter", None)
    return render_template("index.html")

@app.route("/sign_in/<key>/<title>", methods=["POST", "GET"])
def sign_in(key, title):
    token = uuid.uuid4()
    
    if request.method == "POST" and 'token' in request.form:
        name = request.form.get("name", "")
        id = request.form.get("id", "")
        session["name"] = name
        session["student_id"] = id
        session["title"] = title
        
        
        return redirect(url_for("quiz", key=key, title=title))
    return render_template("sign_in.html", key=key, title=title, token=token)


@app.route("/quiz/<key>/<title>",methods=["GET", "POST"])
def quiz(key, title):
    token = uuid.uuid4()
    
    # Initialize session variables
    if "current_index" not in session:
        session["current_index"] = 0
        session["number_correct"] = 0
        session["total_questions"] = 0
 

    if key == "links_and_buttons":
        questions = get_links_and_buttons_data()
        title = "Links and Buttons"

    if key == "basic_html":
        questions = get_basic_html_data()
        title = "Basic HTML"

    if key == "python_loops":
        questions = get_python_loops_data()
        title = "Python Loops"

    if key == "css_borders_padding":
        questions = get_borders_and_padding_data()
        title = "css_borders and padding"

    if key == "css_box_model":
        questions = get_css_box_model_data()
        title = "css box model"

    if key == "file_handling":
        questions = get_file_handling_data()
        title = "Python Files"
        
    if key == "p5play_basics":
        questions = get_p5play_basics_data()
        title = "p5 Play Basics"

    if key == "links_buttons_two":
        questions = get_links_buttons_two_data()
        title = "links buttons part 2"
        
     
    question_data = questions[session["current_index"]]
    session["total_questions"] = len(questions)
        
    
    if request.method == "POST" and 'token' in request.form:
        session.pop("starter", "")

        session["userA"]  = request.form.get("answer", "")
        userA =  request.form.get("answer", "")
        session["userA"] = userA

        
        if "skip" in request.form:
            session["current_index"] += 1
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            else:
                session["userA"] = ""
                session["starter"] = ""
                session.pop("starter", None)
                session.pop("userA", None)
                session.pop('_flashes', None)
                
                return redirect(url_for("quiz", key=key, title=title, token=token))

    
        

        
        if questions[0]["type"] == 'python':
            user_answer = request.form.get("answer", "").strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '')
            user_answer = user_answer.replace(" ", "")
            user_answer = user_answer.replace("\n", "").replace('\r\n', '').replace('\"', '\'')
           
        
        else:
            user_answer = request.form.get("answer", "").strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').replace('\t','')
            user_answer = user_answer.replace(" ", "")
            user_answer = user_answer.replace("\n", "").replace('\r\n', '').replace('\"', '\'')
           

            
            
       
        if questions[0]["type"] == 'python':
            correct = False
            for answer in question_data["answer"]:
                check_answer = answer.strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').replace('\"', '\'').lower()
                if user_answer.lower() == check_answer:
                    session["current_index"] += 1  # Move to next question
                    session["number_correct"] += 1
                    session["userA"] = ""
                    session.pop("starter", None)
                    session.pop('_flashes', None)
                    flash("Correct!", "success")
                    correct = True
                    break
                  
            if not correct:
                session["starter"] = ""  # Explicitly reset starter
                session.pop('_flashes', None)
                if question_data['feedback'] == "":
                    flash("Incorrect! Try again","danger")
                else:
                    flash(f"Incorrect! Here is a partial solution to help you out.<br><br><pre style='margin-left:20px; font-family:monospace;'>{question_data['feedback']}</pre>", "danger")  
                  

            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))

        

        else:
            correct = False
            for answer in question_data["answer"]:
                check_answer = answer.strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').replace('\"', '\'').lower().replace('\t','')
                if user_answer.lower() == check_answer:
                    session["current_index"] += 1  # Move to next question
                    session["number_correct"] += 1
                    session["userA"] = ""
                    session.pop("userA", None)
                    session.pop("starter", None)
                    session.pop('_flashes', None)
                    flash("Correct!", "success")
                    correct = True
                    break
                   
            if not correct:
                session["starter"] = ""  # Explicitly reset starter
                session.pop('_flashes', None)
                if question_data['feedback'] == "":
                    flash("Incorrect! Try again","danger")
                else:
                    flash(f"Incorrect! Here is a partial solution to help you out.<br><br><pre style='margin-left:20px; font-family:monospace;'>{question_data['feedback']}</pre>", "danger")               
        
        
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
        
        
        
        return redirect(url_for("quiz", key=key, title=title, token=token))
    
        
    
    if "starter" not in session or session["starter"] != "":
        session["starter"] = question_data["starter"]
        
    if "userA" not in session:
        session["userA"] = ""
    
    if question_data["image"].startswith("http"):
        webimage = question_data["image"]
        image = ""
    else:
        image = question_data["image"]
        webimage = ""

    total_questions = len(questions)
    
    return render_template("quiz.html", question=question_data["question"],image=image,webimage=webimage, key=key, title=title, userA = session.get("userA",""), token=token, starter=session.get("starter", "") , total_questions=total_questions,current_index=session["current_index"])

    



@app.route("/finish/<int:grade>", methods=['POST', 'GET'])
def finish(grade):
    if request.method == 'POST':
        # Retrieve user input from the form
        name = request.form.get('name', "")
        grade = request.form.get('grade', "")
        # using now() to get current time
        current_time = datetime.datetime.now()



        return redirect(url_for('generate_text_file',name=name, grade=grade, current_time=current_time ))
       
   
    
    return render_template("finish.html", grade = grade)



@app.route('/download/<name>/<grade>/<current_time>')
def generate_text_file(name, grade, current_time):
    file_name = f"{name}-{session['title']}.png"
    
    id = session["student_id"]
    


    img = Image.new('RGB', (1000, 800), color=(255, 255, 255))  # White background
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("Vera.ttf", 36)  # Ensure the font file exists
    except:
        font = ImageFont.load_default()  # Fallback if font is missing

    text = f"Name: {name}\nStudent id: {id}\nGrade: {grade}\nTime: {current_time}"
    draw.multiline_text((20, 50), text, fill=(0, 0, 0), font=font)  # Black text

    img.save(file_name)
    
    

    # Delete the file
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
        return response



    
    return send_file(file_name, as_attachment=True, mimetype="image/png", download_name=f"{name}-{session['title']}.png")




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
