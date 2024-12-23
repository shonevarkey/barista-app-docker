from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if used)
load_dotenv()

app = Flask(__name__)

# Database connection using environment variables
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        people = request.form['people']

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO reservations (name, phone, date, time, people) VALUES (%s, %s, %s, %s, %s)",
            (name, phone, date, time, people)
        )
        db.commit()
        return redirect('/')

    return render_template('reservation.html')

if __name__ == "__main__":
    app.run(debug=True)
