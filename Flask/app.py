from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = secret_key

client = MongoClient(mongo_uri)
db = client.sample_mflix
userCollection = db.users

@app.route('/api', methods=['GET'])
def get_users():
    users = userCollection.find()
    return render_template('users.html', users=users)

@app.route('/simple_form', methods=['GET', 'POST'])
def simple_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Basic validation
        if not name or not email or not password:
            flash("All fields (Name, Email, Password) are required.")
            return render_template('simpleForm.html')

        try:
            # Insert data into MongoDB
            userCollection.insert_one({
                'name': name,
                'email': email,
                'password': password
            })
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return render_template('simpleForm.html')

    # GET request
    return render_template('simpleForm.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)