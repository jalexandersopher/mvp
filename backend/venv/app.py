from flask import Flask, request, Response, redirect, url_for
from flask_cors import CORS
import mariadb
import json
import dbcreds
import string
import random
from werkzeug.utils import secure_filename
from flask import send_from_directory, render_template
import os

app = Flask(__name__)
CORS(app)

def get_random_alphanumeric_string():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(30)))
    return result_str

@app.route('/api/login', methods=['POST',])
def login():
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")
        loginToken = get_random_alphanumeric_string()
        loginSuccess = False

        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=? AND password=?", [username, password])
            user_list = cursor.fetchall()
            if(len(user_list) == 1):
                cursor.execute("INSERT INTO user_session(userId, loginToken) VALUES(?, ?)", [user_list[0][0], loginToken])
                conn.commit()
                loginSuccess = True

        except Exception as error:
            print("Something went wrong: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(loginSuccess):
                return Response(json.dumps({"loginToken": loginToken}, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)

@app.route("/api/card", methods=['POST'])
def postCard():
    if request.method == "POST":
        title = request.json.get("title")
        price = request.json.get("price")
        picture = request.json.get("picture")
        description = request.json.get("description")
        category = request.json.get("category")
        loginToken = request.json.get("loginToken")
        cardSuccess = False

        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_session WHERE loginToken =?", [loginToken,])
            user_list = cursor.fetchall()
            if(len(user_list) == 1):
                cursor.execute("INSERT INTO cards(title, price, description, category, picture) VALUES(?, ?, ?, ?, ?)", [title, price, description, category, picture])
                conn.commit()
                cardSuccess = True

        except Exception as error:
            print("Something went wrong: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(cardSuccess):
                return Response(json.dumps({"Message": "Your product was inserted"}, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)


@app.route("/api/card", methods=['DELETE'])
def deleteCard():
    if request.method == "DELETE":
        title = request.json.get("title")
        loginToken = request.json.get("loginToken")
        cardSuccess = False

        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_session WHERE loginToken =?", [loginToken,])
            card_list = cursor.fetchall()
            cursor.execute("DELETE FROM cards WHERE title =?", [title,])
            conn.commit()
            cardSuccess = True

        except Exception as error:
            print("Something went wrong: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(cardSuccess):
                return Response(json.dumps({"Message": "Your product was deleted!"}, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)


@app.route('/api/contact', methods=['POST',])
def contact():
    if request.method == 'POST':
        email = request.json.get("email")
        description = request.json.get("description")
        item_name = request.json.get("item_name")
        name = request.json.get("name")

        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contact(email, description, item_name, name) VALUES(?, ?, ?, name)", [email, description, item_name, name])
            conn.commit()

        except Exception as error:
            print("Something went wrong: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
                return Response(json.dumps({"Message": "Your message was sent!"}, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)

@app.route("/api/contact", methods=['DELETE'])
def deleteContact():
    if request.method == "DELETE":
        email = request.json.get("email")
        loginToken = request.json.get("loginToken")
        cardSuccess = False

        try:
            conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_session WHERE loginToken =?", [loginToken,])
            card_list = cursor.fetchall()
            cursor.execute("DELETE FROM contact WHERE email =?", [email,])
            conn.commit()
            cardSuccess = True

        except Exception as error:
            print("Something went wrong: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(cardSuccess):
                return Response(json.dumps({"Message": "Your product was deleted!"}, default=str), mimetype="application/json", status=200)
            else:
                return Response("Something went wrong!", mimetype="text/html", status=500)



