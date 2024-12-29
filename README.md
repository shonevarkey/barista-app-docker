# ☕ Coffee Shop Reservation System

This is a Flask-based web application for a coffee shop that allows users to view a homepage and make reservations. It includes functionality for storing reservation details in a MySQL database and uses Docker for containerization.

---

## 📁 Directory Structure

```
barista-app-docker/
│
├── app.py
├── .env
├── Dockerfile
├── screenshots/
│   ├── homepage.jpg
│   ├── reservation.jpg
├── templates/
│   ├── index.html
│   ├── reservation.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   ├── coffee1.jpg
│   │   ├── coffee2.jpg
│   │   ├── reservation-bg.jpg
└── requirements.txt
```
---

## ✨ Features

- 🏠 **Homepage**: Displays an elegant image gallery for the coffee shop.
- 📝 **Reservation Page**: Allows users to fill out a form to make reservations.
- 🗄️ **Database Integration**: Stores reservation details in a MySQL database.
- 📱 **Responsive Design**: Mobile-friendly and optimized for various screen sizes.
- 🐳 **Docker Support**: Containerized application for easy deployment.

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Styling Framework**: Custom CSS
- **Containerization**: Docker

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```yaml
# Clone the repository
git clone <repository-url>
cd <repository-folder>
```
### 2️⃣ Set Up Virtual Environment

```yaml
# Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### 3️⃣ Install Requirements

```yaml
# Install dependencies
pip install -r requirements.txt
```

### 4️⃣ Set Up the MySQL Database

```yaml
-- Create a database
CREATE DATABASE coffee_shop;

-- Use the database
USE coffee_shop;

-- Create the reservations table
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(15),
    date DATE,
    time TIME,
    people INT
);
```

### 5️⃣ Configure Environment Variables

Create a .env file in the project root:

```yaml
DB_HOST: your-database-host
DB_USER: your-database-user
DB_PASSWORD: your-database-password
DB_NAME: coffee_shop
SECRET_KEY: your-secret-key
```

### 6️⃣ Run the Application

```yaml
# Start the Flask application
python app.py
```
+ Access the application at http://127.0.0.1:5000.

---

## 🖥️ Environment Variables

---

## 🐳 Docker Deployment

### 1️⃣ Build the Docker Image

```yaml
# Build the Docker image
docker build -t coffee-shop .
```

### 2️⃣ Run the Docker Container

```yaml
# Run the Docker container
docker run -d -p 5000:5000 --env-file .env coffee-shop
```

+ Access the application at http://127.0.0.1:5000.

---

## 📚 Usage

+ Visit the **Homepage** to explore the coffee shop’s gallery.
  
+ Navigate to the **Reservation Page** to book a table.
  
+ On successful reservation, you will see a confirmation message.

---

## 📸 Screenshots

### Homepage

![Home Page](./screenshots/homepage.jpg)

### Reservation Page

![Reservation Page](./screenshots/reservation.jpg)

---

### 👨‍💻 Author

**Shone Varkey**

Feel free to reach out with suggestions or improvements! 😊

---
