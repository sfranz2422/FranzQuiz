from flask import Flask, render_template, send_from_directory, url_for, redirect, render_template, request, flash, send_from_directory, send_file, jsonify, make_response, session
from csv import DictReader
import uuid
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
from questions import quiz1, quiz2
app = Flask(__name__)
# app.secret_key = os.environ['FLASK_SECRET_KEY']
app.secret_key = "kasdjhfalsdkfhjadfls"


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
    return render_template("index.html")


@app.route("/quiz/<key>/<title>",methods=["GET", "POST"])
def quiz(key, title):
        
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

        
        user_answer = request.form.get("answer", "").strip()
        if user_answer.lower() == question_data["answer"].lower():
            session["current_index"] += 1  # Move to next question
            session["number_correct"] += 1
            flash("Correct! Moving to the next question.", "success")

            
            if session["current_index"] >= len(questions):
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))
            
            
            
            return redirect(url_for("quiz", key=key, title=title))
        else:
            flash("Incorrect! Try again.", "danger")

    return render_template("quiz.html", question=question_data["question"], key=key, title=title)

    



@app.route("/finish/<int:grade>", methods=['POST', 'GET'])
def finish(grade):
    # session.pop("current_index", None)  # Reset session
    # session.pop("number_correct", None)
    # session.pop("total_questions", None)
    # return "Quiz complete! <a href='/'>Restart</a>"
    if request.method == "POST":
        return "submitted to teacher"

    


    
    return render_template("finish.html", grade = grade)



def scramble_question_set():
    pass






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
