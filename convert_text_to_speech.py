from google.cloud import texttospeech


def text_to_wav(voice_name, text):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    client = texttospeech.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )
    # The response's audio_content is binary.
    with open('voice_notes/output.mp3', 'wb') as out:
    # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')