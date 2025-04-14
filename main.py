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


import psycopg






app = Flask(__name__)

app.secret_key = os.environ['FLASK_SECRET_KEY']
user_data = []
# pdfmetrics.registerFont(TTFont('Vera','Vera.ttf'))

# with psycopg.connect(host=os.environ['PGHOST'],
#      dbname=os.environ['PGDATABASE'],
#      user=os.environ['PGUSER'],
#      password=os.environ['PGPASSWORD']) as conn:
#     with conn.cursor() as cur:
    
#         cur.execute(
#             """
#             ALTER TABLE student_scores 
#             ALTER COLUMN timestamp TYPE TEXT;
#             """
#         )

#         cur.execute(
#             """
#             CREATE TABLE student_scores (
#                 id SERIAL PRIMARY KEY,
#                 testName TEXT NOT NULL,
#                 testId TEXT NOT NULL,
#                 studentName TEXT NOT NULL,
#                 studentId TEXT NOT NULL,
#                 studentScore NUMERIC NOT NULL,
#                 timestamp TIMESTAMP
#             )
#             """
#         )


# def get_python_loops_data():
#     url="https://api.npoint.io/22d05fa3ee9f0da4f95e"
#     res = requests.get(url).json()
#     return res

# def get_links_and_buttons_data():
#     url="https://api.npoint.io/c30e4cf9a778a1b9a622"
#     res = requests.get(url).json()
#     return res


# def get_basic_html_data():
#     url="https://api.npoint.io/0b9ddad402449729126c"
#     res = requests.get(url).json()
#     return res

# def get_borders_and_padding_data():
#     url="https://api.npoint.io/3aeeef8301d2e5df077a"
#     res = requests.get(url).json()
#     return res

# def get_css_box_model_data():
#     url="https://api.npoint.io/8be0c96872a500564ec1"
#     res = requests.get(url).json()
#     return res

# def get_file_handling_data():
#     url="https://api.npoint.io/beadacc26a1b6b32bbf2"
#     res = requests.get(url).json()
#     return res

# def get_p5play_basics_data():
#     url="https://api.npoint.io/81392477ca243d99e34b"
#     res = requests.get(url).json()
#     return res


# def get_links_buttons_two_data():
#     url="https://api.npoint.io/9cbe6a8116e569a99093"
#     res = requests.get(url).json()
#     return res

# def get_css_box_model_two_data():
#     url="https://api.npoint.io/e30127563f9d1cd04228"
#     res = requests.get(url).json()
#     return res

# def get_kaplay_basics_data():
#     url="https://api.npoint.io/ff09c70f8b4968120f16"
#     res = requests.get(url).json()
#     return res

# def get_jinja_basics_data():
#     url="https://api.npoint.io/f108b722ac27b52908f1"
#     res = requests.get(url).json()
#     return res

# def get_display_positioning_data():
#     url="https://api.npoint.io/e47e5c603cd55c6a906e"
#     res = requests.get(url).json()
#     return res

# def get_python_practice_data():
#     url="https://api.npoint.io/c9ea8b8a00d6b67199ab"
#     res = requests.get(url).json()
#     return res


# def get_css_color_data():
#     url="https://api.npoint.io/d9427e68eedea8cce2b0"
#     res = requests.get(url).json()
#     return res

# def get_css_color_two_data():
#     url="https://api.npoint.io/f725f8119cb45565728d"
#     res = requests.get(url).json()
#     return res

# def get_typography_sizing_one_data():
#     url="https://api.npoint.io/11a3edabb7f3899a2935"
#     res = requests.get(url).json()
#     return res

# def get_typography_sizing_two_data():
#     url="https://api.npoint.io/28ffe6a010734a799ced"
#     res = requests.get(url).json()
#     return res


# def get_cat_photo_one_data():
#     url="https://api.npoint.io/b5f004d362eef8bc1035"
#     res = requests.get(url).json()
#     return res


# def get_rpg_adventure_one_data():
#     url="https://api.npoint.io/d875ec63da9f735648b7"
#     res = requests.get(url).json()
#     return res
# def get_rpg_adventure_two_data():
#     url="https://api.npoint.io/0585a0ed1fc515a8c741"
#     res = requests.get(url).json()
#     return res

# def get_cat_part_two_data():
#     url="https://api.npoint.io/c09f6c4cc19c98883cad"
#     res = requests.get(url).json()
#     return res
DATA_ENDPOINTS = {
    "python_loops": "https://api.npoint.io/22d05fa3ee9f0da4f95e",
    "links_and_buttons": "https://api.npoint.io/c30e4cf9a778a1b9a622",
    "basic_html": "https://api.npoint.io/0b9ddad402449729126c",
    "borders_and_padding": "https://api.npoint.io/3aeeef8301d2e5df077a",
    "css_box_model": "https://api.npoint.io/8be0c96872a500564ec1",
    "file_handling": "https://api.npoint.io/beadacc26a1b6b32bbf2",
    "p5play_basics": "https://api.npoint.io/81392477ca243d99e34b",
    "links_buttons_two": "https://api.npoint.io/9cbe6a8116e569a99093",
    "css_box_model_two": "https://api.npoint.io/e30127563f9d1cd04228",
    "kaplay_basics": "https://api.npoint.io/ff09c70f8b4968120f16",
    "jinja_basics": "https://api.npoint.io/f108b722ac27b52908f1",
    "display_positioning": "https://api.npoint.io/e47e5c603cd55c6a906e",
    "python_practice": "https://api.npoint.io/c9ea8b8a00d6b67199ab",
    "css_color": "https://api.npoint.io/d9427e68eedea8cce2b0",
    "css_color_two": "https://api.npoint.io/f725f8119cb45565728d",
    "typography_sizing_one": "https://api.npoint.io/11a3edabb7f3899a2935",
    "typography_sizing_two": "https://api.npoint.io/28ffe6a010734a799ced",
    "cat_photo_one": "https://api.npoint.io/b5f004d362eef8bc1035",
    "rpg_adventure_one": "https://api.npoint.io/d875ec63da9f735648b7",
    "rpg_adventure_two": "https://api.npoint.io/0585a0ed1fc515a8c741",
    "cat_part_two": "https://api.npoint.io/c09f6c4cc19c98883cad",
    "cat_part_31-45":"https://api.npoint.io/71b75ef4ccfd8559f51e"
}
LESSON_CONFIG = {
    "links_and_buttons": ("links_and_buttons", "Links and Buttons"),
    "basic_html": ("basic_html", "Basic HTML"),
    "python_loops": ("python_loops", "Python Loops"),
    "css_borders_padding": ("borders_and_padding", "CSS Borders and Padding"),
    "css_box_model": ("css_box_model", "CSS Box Model"),
    "file_handling": ("file_handling", "Python Files"),
    "p5play_basics": ("p5play_basics", "p5 Play Basics"),
    "links_buttons_two": ("links_buttons_two", "Links Buttons Part 2"),
    "css_box_model_two": ("css_box_model_two", "CSS Box Model Two"),
    "kaplay_basics": ("kaplay_basics", "Kaplay Basics"),
    "jinja_basics": ("jinja_basics", "Jinja Basics"),
    "css_display_positioning": ("display_positioning", "CSS Display and Positioning"),
    "python_practice": ("python_practice", "Python Practice"),
    "css_color": ("css_color", "CSS Color One"),
    "css_color_two": ("css_color_two", "CSS Color Two"),
    "typography_sizing_one": ("typography_sizing_one", "Typography and Sizing One"),
    "typography_sizing_two": ("typography_sizing_two", "Typography and Sizing Two"),
    "cat_photo_1-15": ("cat_photo_one", "Cat Photo App Steps 1-15"),
    "rpg_adventure_one": ("rpg_adventure_one", "RPG Adventure One"),
    "rpg_adventure_two": ("rpg_adventure_two", "RPG Adventure Two"),
    "cat_part_two": ("cat_part_two", "Cat Photo App Steps 16–30"),
    "cat_part_31-45":("cat_part_31-45", "Cat Photo App Steps 31–45")
}

def get_lesson_data(key):
    url = DATA_ENDPOINTS.get(key)
    if not url:
        raise ValueError(f"No endpoint found for key: {key}")
    return requests.get(url).json()


# List of questions with answers
questions = []

@app.route("/lessons")
def lessons():
    return render_template("lessons.html")

@app.route("/games")
def games():
    return render_template("games.html")




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
    session.pop("notes", None)
    session.pop("wrong_count", None)


    return render_template("index.html")

@app.route("/sign_in/<key>/<title>", methods=["POST", "GET"])
def sign_in(key, title):
    if key == "not-ready":
        return redirect(url_for("home"))
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
        session["wrong_count"] = 0


    # get_lesson_data
    
    # if key == "links_and_buttons":
    #     questions = get_lesson_data("links_and_buttons")
    #     title = "Links and Buttons"

    # if key == "basic_html":
    #     questions = get_basic_html_data()
    #     title = "Basic HTML"

    # if key == "python_loops":
    #     questions = get_python_loops_data()
    #     title = "Python Loops"

    # if key == "css_borders_padding":
    #     questions = get_borders_and_padding_data()
    #     title = "css_borders and padding"

    # if key == "css_box_model":
    #     questions = get_css_box_model_data()
    #     title = "css box model"

    # if key == "file_handling":
    #     questions = get_file_handling_data()
    #     title = "Python Files"
        
    # if key == "p5play_basics":
    #     questions = get_p5play_basics_data()
    #     title = "p5 Play Basics"

    # if key == "links_buttons_two":
    #     questions = get_links_buttons_two_data()
    #     title = "links buttons part 2"

    # if key == "css_box_model_two":
    #     questions = get_css_box_model_two_data()
    #     title = "css box model two"
    
    # if key == "kaplay_basics":
    #     questions = get_kaplay_basics_data()
    #     title = "Kaplay Basics"

    # if key == "jinja_basics":
    #     questions = get_jinja_basics_data()
    #     title = "Jinja Basics"

    # if key == "css_display_positioning":
    #     questions = get_display_positioning_data()
    #     title = "CSS Display and Positioning"

    
    # if key == "python_practice":
    #     questions = get_python_practice_data()
    #     title = "Python Practice"
    
    # if key == "css_color":
    #     questions = get_css_color_data()
    #     title = "CSS Color One"

    # if key == "css_color_two":
    #     questions = get_css_color_two_data()
    #     title = "CSS Color Two"

    # if key == "typography_sizing_one":
    #     questions = get_typography_sizing_one_data()
    #     title = "Typography and Sizing One"

    # if key == "typography_sizing_two":
    #     questions = get_typography_sizing_two_data()
    #     title = "Typography and Sizing Two"

    # if key == "cat_photo_1-15":
    #     questions = get_cat_photo_one_data()
    #     title = "Cat Photo App Steps 1-15"

    # if key == "rpg_adventure_one":
    #     questions = get_rpg_adventure_one_data()
    #     title = "RPG Adventure One"

    # if key == "rpg_adventure_two":
    #     questions = get_rpg_adventure_two_data()
    #     title = "RPG Adventure Two"
    
    # if key == "cat_part_two":
    #     questions = get_cat_part_two_data()
    #     title = "Cat Photo App Steps 16-30"

    if key in LESSON_CONFIG:
        endpoint_key, title = LESSON_CONFIG[key]
        questions = get_lesson_data(endpoint_key)
    else:
        questions = []
        title = "Unknown Lesson"
    
    
    question_data = questions[session["current_index"]]
    session["total_questions"] = len(questions)
    notes = question_data["notes"]
    session["notes"] = notes
    
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
                session["wrong_count"] = 0
                return redirect(url_for("finish", grade = grade))
            else:
                session["userA"] = ""
                session["starter"] = ""
                session.pop("starter", None)
                session.pop("userA", None)
                session.pop('_flashes', None)
                session["wrong_count"] = 0
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
                    session["wrong_count"] = 0
                    session["current_index"] += 1  # Move to next question
                    session["number_correct"] += 1
                    session["userA"] = ""
                    session.pop("starter", None)
                    session.pop('_flashes', None)
                    flash("Correct!", "success")
                    correct = True
                    break
                  
            if not correct:
                session["wrong_count"] += 1
                if session["wrong_count"] >= 3:
                    #do same stuff as skip code
                    session["current_index"] += 1
                    if session["current_index"] >= len(questions):
                        grade =  session["number_correct"] / session["total_questions"] 
                        grade = grade * 100
                        grade = int(grade)
                        session["wrong_count"] = 0
                        return redirect(url_for("finish", grade = grade))
                    else:
                        session["userA"] = ""
                        session["starter"] = ""
                        session.pop("starter", None)
                        session.pop("userA", None)
                        session.pop('_flashes', None)
                        session["wrong_count"] = 0
                        return redirect(url_for("quiz", key=key, title=title, token=token))

                session["starter"] = ""  # Explicitly reset starter
                session.pop('_flashes', None)
                if question_data['feedback'] == "":
                    flash("Attempt {session['wrong_count']}/3 <br>Incorrect! Try again","danger")
                else:
                    flash(f"Attempt {session['wrong_count']}/3 <br>Incorrect! Here is a partial solution to help you out.<br><br><pre style='margin-left:20px; font-family:monospace;'>{question_data['feedback']}</pre>", "danger")  
                  

            if session["current_index"] >= len(questions):
                session["wrong_count"] = 0
                grade =  session["number_correct"] / session["total_questions"] 
                grade = grade * 100
                grade = int(grade)
                return redirect(url_for("finish", grade = grade))

        

        else:
            correct = False
            for answer in question_data["answer"]:
                check_answer = answer.strip().replace(" ", "").replace("\n", "").replace('\r\n', '').replace('\r', '').replace('\"', '\'').lower().replace('\t','')
                if user_answer.lower() == check_answer:
                    session["wrong_count"] = 0
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
                session["wrong_count"] += 1
                if session["wrong_count"] >= 3:
                    #do same stuff as skip code
                    session["current_index"] += 1
                    if session["current_index"] >= len(questions):
                        grade =  session["number_correct"] / session["total_questions"] 
                        grade = grade * 100
                        grade = int(grade)
                        session["wrong_count"] = 0
                        return redirect(url_for("finish", grade = grade))
                    else:
                        session["userA"] = ""
                        session["starter"] = ""
                        session.pop("starter", None)
                        session.pop("userA", None)
                        session.pop('_flashes', None)
                        session["wrong_count"] = 0
                        return redirect(url_for("quiz", key=key, title=title, token=token))

                
                session["starter"] = ""  # Explicitly reset starter
                session.pop('_flashes', None)
                if question_data['feedback'] == "":
                    flash(f"Attempt {session['wrong_count']}/3 <br> Incorrect! Try again","danger")
                else:
                    flash(f"Attempt {session['wrong_count']}/3 <br>Incorrect! Here is a partial solution to help you out.<br><br><pre style='margin-left:20px; font-family:monospace;'>{question_data['feedback']}</pre>", "danger")   

                
        
        
            if session["current_index"] >= len(questions):
                session["wrong_count"] = 0
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
    
    return render_template("quiz.html", question=question_data["question"],image=image,webimage=webimage, key=key, title=title, userA = session.get("userA",""), token=token, starter=session.get("starter", "") , total_questions=total_questions,current_index=session["current_index"],notes=notes, wrong_count = session["wrong_count"])

    



@app.route("/finish/<int:grade>", methods=['POST', 'GET'])
def finish(grade):
    if request.method == 'POST':
        # Retrieve user input from the form
        name = request.form.get('name', "")
        grade = request.form.get('grade', "")
        # using now() to get current time
        current_time = datetime.datetime.now()
        id = session["student_id"]
        testname = session['title']
        testid = " "
        #save to database
        with psycopg.connect(host=os.environ['PGHOST'],
             dbname=os.environ['PGDATABASE'],
             user=os.environ['PGUSER'],
             password=os.environ['PGPASSWORD']) as conn:
            with conn.cursor() as cur:
            # cur.execute(f"INSERT INTO users (email, password,subscribed, key, tfa, thedate, ip, phone) VALUES ('{email}', '{password}', '{subscribed}','{key}','{tfa}','{now}','{ip}','{phone}')")
    
                SQL = "INSERT INTO student_scores (testname,testid, studentname,studentid, studentscore, timestamp) VALUES (%s, %s, %s,%s,%s,%s)"
                data = (
                testname,
                testid,
                name,
                id,
                grade,
                current_time,
                )
        
                cur.execute(SQL, data)

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

@app.route("/coinDash/<path:name>")
def serveCoinDashFiles(name):
    response = send_from_directory(f'./coinDash', name)
    response.headers.add('Cross-Origin-Opener-Policy', 'same-origin')
    response.headers.add('Cross-Origin-Embedder-Policy', 'require-corp')
    return response

@app.route('/coinDash')
def coinDash():
    response = make_response(
        render_template('coinDash.html'))
    response.headers.add('Cross-Origin-Opener-Policy', 'same-origin')
    response.headers.add('Cross-Origin-Embedder-Policy', 'require-corp')
    return response

@app.route('/ads.txt')
def ads():
       return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)



