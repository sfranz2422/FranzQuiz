from flask import Flask, render_template, send_from_directory, url_for, redirect, render_template, request, flash, send_from_directory, send_file, jsonify, make_response, session, make_response
import uuid
import csv
import json
import os
import random
import io
import requests
import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


app = Flask(__name__)

app.secret_key = os.environ['FLASK_SECRET_KEY']
user_data = []
pdfmetrics.registerFont(TTFont('Vera','Vera.ttf'))

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
    userA =""
    
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
   
    
    question_data = questions[session["current_index"]]
    session["total_questions"] = len(questions)
        
    starter=question_data["starter"]

    
    if request.method == "POST" and 'token' in request.form:
        starter = ""
        if "skip" in request.form:
            session["current_index"] += 1
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            else:
                return redirect(url_for("quiz", key=key, title=title, token=token))

        userA = request.form.get("answer", "")
        user_answer = request.form.get("answer", "").strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '')
        user_answer = user_answer.replace(" ", "")
        user_answer = user_answer.replace("\n", "").replace('\r\n', '').replace('\"', '\'')
        answerKey = question_data["answer"].strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').replace('\"', '\'').lower()
        if user_answer.lower() == answerKey:
            session["current_index"] += 1  # Move to next question
            session["number_correct"] += 1
            flash("Correct!", "success")

            
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            
            
            
            return redirect(url_for("quiz", key=key, title=title, token=token))
        else:
            starter = ""
            flash("Incorrect! Try again.", "danger")

    if question_data["image"].startswith("http"):
        webimage = question_data["image"]
        image = ""
    else:
        image = question_data["image"]
        webimage = ""
        
    return render_template("quiz.html", question=question_data["question"],image=image,webimage=webimage, key=key, title=title, userA = userA, token=token, starter=starter)

    



@app.route("/finish/<int:grade>", methods=['POST', 'GET'])
def finish(grade):
    if request.method == 'POST':
        # Retrieve user input from the form
        name = request.form.get('name', "")
        grade = request.form.get('grade', "")
        # using now() to get current time
        current_time = datetime.datetime.now()

        if name and grade:
            user_data.append({
                'name': name,
                'grade': grade,
                'time' : current_time,
            })

            pdf_file = generate_pdf_file()
            return send_file(pdf_file, as_attachment=True, download_name=f"{name}-{session['title']}.pdf")
   
    
    return render_template("finish.html", grade = grade)



def generate_pdf_file():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Create a PDF document
    p.setFont('Vera', 32)
    p.drawString(100, 750, session["title"])
 
    y = 700
    for data in user_data:
        p.drawString(100, y, f"Name: {data['name']}")
        p.drawString(100, y - 40, f"Grade: {data['grade']}")
        p.setFont('Vera', 16)
        p.drawString(100, y - 80, f"Time: {data['time']}")
        y -= 60

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
