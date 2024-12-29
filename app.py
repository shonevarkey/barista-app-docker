from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Set a secret key

# Database connection using environment variables
try:
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

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
        cursor.close()
       # return redirect('/')
        flash("Reservation completed successfully!", "success")
        return redirect('/reservation')

    return render_template('reservation.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

