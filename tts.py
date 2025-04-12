import PyPDF2
from gtts import gTTS
import nltk
from nltk.tokenize import sent_tokenize
import os

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# --- Step 1: Extract text from PDF ---
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

# --- Step 2: Convert to single MP3 and show sentences ---
def save_pdf_as_mp3(pdf_path, output_filename):
    text = extract_text_from_pdf(pdf_path)

    if not text.strip():
        print("❌ No readable text found in the PDF.")
        return

    sentences = sent_tokenize(text)
    full_text = ""

    print("\n📃 Extracted Sentences:\n------------------------")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")
        full_text += sentence + " "

    print("\n🔊 Generating MP3...")
    tts = gTTS(text=full_text.strip(), lang='en')
    tts.save(output_filename)
    print(f"✅ MP3 file saved as: {output_filename}")

# --- Main Execution ---
pdf_file_path = "test.pdf"  # Use full path if needed
output_mp3 = "output_audio.mp3"

save_pdf_as_mp3(pdf_file_path, output_mp3)
