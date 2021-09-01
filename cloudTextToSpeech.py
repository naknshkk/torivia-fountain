# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone
from google.cloud import texttospeech
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')
client = texttospeech.TextToSpeechClient(credentials=credentials)

synthesis_input = texttospeech.types.SynthesisInput(
  text='目的地は、秋葉原です。')

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
