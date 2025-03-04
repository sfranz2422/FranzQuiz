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
from questions import quiz1
app = Flask(__name__)
# app.secret_key = os.environ['FLASK_SECRET_KEY']
app.secret_key = "kasdjhfalsdkfhjadfls"



question_set = []
number_correct = 0
number_given = 0
current_question_number = 0




@app.route('/', methods=['POST', 'GET'])
def index():
    global number_correct
    global number_given
    global current_question_number
    question_set = quiz1
    current_question = question_set[current_question_number]
    

    if request.method == 'POST':
        if request.form['answer'] == current_question['answer']:
            flash("Correct")
            return redirect(url_for("index"))
        else:
            flash("Incorrect, Try again")
    
    else:
        
        
        return render_template("index.html", question_set = question_set, current_question=current_question)
    



def scramble_question_set():
    pass






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
