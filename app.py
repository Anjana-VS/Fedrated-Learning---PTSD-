from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load model data (replace with actual model training)
data = pd.read_csv("data/user_data.csv")
X = data.drop(columns=['recommendation'])
y = data['recommendation']
model = RandomForestClassifier()
model.fit(X, y)

# Generate encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Symptom Tracking
@app.route('/symptom_form')
def symptom_form():
    return render_template('symptom_form.html')

@app.route('/submit_symptom', methods=['POST'])
def submit_symptom():
    symptom_data = request.form
    print(symptom_data)
    return "Symptom data submitted successfully!"

# Personalized Counselling
@app.route('/personalized_counselling')
def personalized_counselling():
    return render_template('personalized_counselling.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = [float(request.form.get(key)) for key in request.form.keys()]
    recommendation = model.predict([user_input])
    return render_template('recommendations.html', recommendation=recommendation[0])

# Therapeutic Music
@app.route('/music')
def music():
    with open("data/music_playlist.json", "r") as file:
        music_playlist = file.read()
    return render_template('music.html', music=music_playlist)

# Encrypt and Decrypt
@app.route('/encrypt_data', methods=['POST'])
def encrypt_data():
    data = request.form['data'].encode()
    encrypted = cipher_suite.encrypt(data)
    return f"Encrypted Data: {encrypted.decode()}"

@app.route('/decrypt_data', methods=['POST'])
def decrypt_data():
    encrypted = request.form['encrypted_data'].encode()
    decrypted = cipher_suite.decrypt(encrypted)
    return f"Decrypted Data: {decrypted.decode()}"

if __name__ == "__main__":
    app.run(debug=True)
