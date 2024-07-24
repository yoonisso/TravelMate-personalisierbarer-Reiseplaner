from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

import openaiAPI

# Laden der Umgebungsvariablen
load_dotenv()

# Flask App initialisieren
app = Flask(__name__)

# OpenAI API-Schlüssel laden
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    # Reisedaten aus dem Formular erhalten
    age = request.form['age']
    origin = request.form['origin']
    amount = request.form['amount']
    travel_period_start = request.form['travel_period_start']
    travel_period_end = request.form['travel_period_end']
    budget = request.form['budget']
    interests = request.form['interests']
    accommodation = request.form['accommodation']
    temperature = request.form['temperature']
    destination = request.form['destination']

    # Generiere Reisevorschläge mit OpenAI GPT
    prompt = f"""Erstelle mögliche Reiseziele für eine Person mit folgenden Daten: takte hierbei bitte jeden Tag durch und \n
                    zeige deine Ergebnisse verständlich auf""" \
             f"Alter: {age}\n" \
             f"Herkunft: {origin}\n" \
             f"Anzahl von Personen: {amount}\n" \
             f"Reisezeitraum: {travel_period_start} bis {travel_period_end}\n" \
             f"Budget: {budget}\n" \
             f"Persönliche Interessen: {interests}\n" \
             f"Unterkunftspräferenzen: {accommodation}\n" \
             f"Bevorzugte Temperatur: {temperature}\n" \
             f"Reiseziel: {destination}\n"



    plans = openaiAPI.chatCompletion(prompt)

    return render_template('plan.html', plan=plans)

if __name__ == '__main__':
    app.run(debug=False)
