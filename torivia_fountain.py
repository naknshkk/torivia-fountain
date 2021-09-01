# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone
from google.cloud import texttospeech
from google.oauth2 import service_account
import MySQLdb
import pygame.mixer
import time
import os

#---------
# 接続
#---------
cnct = MySQLdb.connect(
    host = "localhost",
    user = "root",
    password = "root",
    db = "triviadata",
    charset = "utf8"
    )
TABLE = "tribia"

cur = cnct.cursor()

while True:
    cur.execute("SELECT tribia FROM " + TABLE + " ORDER BY rand() limit 1" + ";")
    results = cur.fetchone()
    print(results[0])
    
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    
    synthesis_input = texttospeech.types.SynthesisInput(
      text=results[0])
    
    voice = texttospeech.types.VoiceSelectionParams(
      language_code='ja-JP',
      name='ja-JP-Wavenet-D',
      ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    
    audio_config = texttospeech.types.AudioConfig(
      audio_encoding=texttospeech.enums.AudioEncoding.MP3,
      pitch = -2.0
      )
    
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    now = datetime.now(timezone('Asia/Tokyo'))
    filename = now.strftime('%Y-%m-%d_%H%M%S.mp3')
    with open(filename, 'wb') as out:
      out.write(response.audio_content)
      print(f'Audio content written to file {filename}')
    
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load("./" + filename)
    pygame.mixer.music.play(1)
    time.sleep(30)
    pygame.mixer.music.stop()
    
    os.remove(filename)

cur.close()
cnct.close()