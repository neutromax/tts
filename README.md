# PDF to Speech (TTS)

This project converts text from a PDF file into speech using Google Text-to-Speech (gTTS) and NLTK for text processing. The script extracts the text, processes it into sentences, and converts it to an MP3 file for easy listening.

 Features
- PDF to Speech: Converts PDF text to speech.
- Text Tokenization: Breaks the text into sentences for clear speech output using **NLTK**.
- MP3 Output: The speech is saved as an MP3 file.

 Requirements

- Python 3.x
- gTTS library
- PyPDF2 library
- NLTK library

 Installation

1. Clone the repository:

	git clone https://github.com/neutromax/tts.git


2. Navigate to the project directory:

	cd tts

3.Install the required dependencies:

	pip install gTTS PyPDF2 nltk


4.Download necessary NLTK data:


	import nltk
	nltk.download('punkt')


After completing these steps, you should have all the necessary libraries and data installed to run the project.
