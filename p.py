from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
import os
import uuid

app = Flask(__name__, template_folder='somethingnew')

# Set the output directory for audio files
OUTPUT_DIR = 'audio_output'


@app.route('/', methods=['GET', 'POST'])
def text_to_speech():
    if request.method == 'POST':
        text = request.form['text']

        # Generate a unique filename for the audio file
        unique_filename = str(uuid.uuid4()) + '.mp3'
        output_file = os.path.join(OUTPUT_DIR, unique_filename)

        # Initialize gTTS and generate the speech
        tts = gTTS(text)
        tts.save(output_file)

        return render_template('p.html', text=text, output_file=unique_filename)

    return render_template('p.html')


@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(OUTPUT_DIR, filename)


if __name__ == '__main__':
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    app.run(debug=True)
