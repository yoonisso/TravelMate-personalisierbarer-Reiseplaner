import os
from openai import OpenAI
import logging
from dotenv import load_dotenv
import json

def loadAPIKey():
    # Laden der Umgebungsvariablen
    dotenv_path = '.env'
    load_dotenv(dotenv_path)
    # Logging konfigurieren
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # Überprüfen, ob die .env-Datei geladen wurde
    if os.path.exists(dotenv_path):
        logging.debug(f"{dotenv_path} Datei gefunden und geladen.")
    else:
        logging.error(f"{dotenv_path} Datei nicht gefunden.")
    # API-Schlüssel von OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    # Überprüfen, ob der API-Schlüssel geladen wurde
    if api_key:
        logging.debug("API-Schlüssel erfolgreich geladen.")
    else:
        logging.error("Fehler: API-Schlüssel konnte nicht geladen werden.")

    return api_key

def chatCompletion(prompt):
    OpenAI().api_key = loadAPIKey()
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for travel planner. You output your findings in a nice looking list. The list must be detailed and every input must be taken into account"},
            {"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content