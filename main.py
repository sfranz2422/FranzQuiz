from flask import Flask, render_template, send_from_directory, url_for, redirect, render_template, request, flash, send_from_directory, send_file, jsonify, make_response, session, make_response
from csv import DictReader
import uuid
import pdfkit
import csv
import json
import os
import random
import io
import pathlib
import hashlib
import requests
import re
import datetime
import html
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from questions import quiz1, quiz2, links_and_buttons, basic_html


app = Flask(__name__)
# app.secret_key = os.environ['FLASK_SECRET_KEY']
app.secret_key = "kasdjhfalsdkfhjadfls"
user_data = []
pdfmetrics.registerFont(TTFont('Vera','Vera.ttf'))

# List of questions with answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
]

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
    if request.method == "POST":
        name = request.form.get("name", "")
        id = request.form.get("id", "")
        session["name"] = name
        session["student_id"] = id
        session["title"] = title
        
        
        return redirect(url_for("quiz", key=key, title=title))
    return render_template("sign_in.html", key=key, title=title)


@app.route("/quiz/<key>/<title>",methods=["GET", "POST"])
def quiz(key, title):
   
    userA =""
    # Initialize session variables
    if "current_index" not in session:
        session["current_index"] = 0
        session["number_correct"] = 0
        session["total_questions"] = 0
    # index = session["current_index"]

    if key == "quiz1":
        questions = quiz1
        title = "Quiz 1"
        question_data = questions[session["current_index"]]
        session["total_questions"] = len(questions)
    if key == "quiz2":
        questions = quiz2
        title = "Quiz 2"
        question_data = questions[session["current_index"]]
        session["total_questions"] = len(questions)
    if key == "links_and_buttons":
        questions = links_and_buttons
        title = "Links and Buttons"
        question_data = questions[session["current_index"]]
        session["total_questions"] = len(questions)
    if key == "basic_html":
        questions = basic_html
        title = "Basic HTML"
        question_data = questions[session["current_index"]]
        session["total_questions"] = len(questions)
    

    if request.method == "POST":

        if "skip" in request.form:
            session["current_index"] += 1
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            else:
                return redirect(url_for("quiz", key=key, title=title))

        userA = request.form.get("answer", "")
        user_answer = request.form.get("answer", "").strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '')
        user_answer = user_answer.replace(" ", "")
        user_answer = user_answer.replace("\n", "").replace('\r\n', '').replace('\r', '')
        answerKey = question_data["answer"].strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').lower()
        if user_answer.lower() == answerKey:
            session["current_index"] += 1  # Move to next question
            session["number_correct"] += 1
            flash("Correct!", "success")

            
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            
            
            
            return redirect(url_for("quiz", key=key, title=title))
        else:
            flash("Incorrect! Try again.", "danger")

    if question_data["image"].startswith("http"):
        webimage = question_data["image"]
        image = ""
    else:
        image = question_data["image"]
        webimage = ""
        
    return render_template("quiz.html", question=question_data["question"],image=image,webimage=webimage, key=key, title=title, userA = userA)

    



@app.route("/finish/<int:grade>", methods=['POST', 'GET'])
def finish(grade):
    # session.pop("current_index", None)  # Reset session
    # session.pop("number_correct", None)
    # session.pop("total_questions", None)
    # return "Quiz complete! <a href='/'>Restart</a>"
    if request.method == 'POST':
        # Retrieve user input from the form
        name = request.form.get('name', "")
        grade = request.form.get('grade', "")
        # using now() to get current time
        current_time = datetime.datetime.now()

        # Printing value of now.
        # print("Time:", current_time)
        # Validate and store the user input
        if name and grade:
            user_data.append({
                'name': name,
                'grade': grade,
                'time' : current_time,
            })

            pdf_file = generate_pdf_file()
            return send_file(pdf_file, as_attachment=True, download_name=f"{name}-{session['title']}.pdf")
   
    
    return render_template("finish.html", grade = grade)



def scramble_question_set():
    pass


# @app.route('/generate-pdf', methods=['GET', 'POST'])
# def generate_pdf():
#     if request.method == 'POST':
#         # Retrieve user input from the form
#         name = request.form.get('name', "")
#         grade = request.form.get('grade', "")

#         # Validate and store the user input
#         if title and author and publication_year:
#             user_data.append({
#                 'name': name,
#                 'grade': grade,
#             })

#     pdf_file = generate_pdf_file()
#     return send_file(pdf_file, as_attachment=True, download_name='book_catalog.pdf')


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
