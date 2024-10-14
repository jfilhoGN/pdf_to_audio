import pdfplumber as pp
from gtts import gTTS

pdf_text = ""

with pp.open("cortico.pdf") as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text()

tts = gTTS(pdf_text, lang="pt")
tts.save("cortico.mp3")