from Bio.Seq import Seq
from fastapi import FastAPI

app = FastAPI()

# Complementary Sequence
@app.get("/complementary_sequence/{input_sequence}")
def complement_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    complementary_sequence = initial_sequence.complement()
    return { 
        "output_sequence": str(complementary_sequence) 
        }

# Transcribed Sequence
@app.get("/transcribed_sequence/{input_sequence}")
def transcribe_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { 
        "output_sequence": str(transcribed_sequence)
        }

# Translated Sequence
@app.get("/translated_sequence/{input_sequence}")
def translate_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    translated_sequence = initial_sequence.translate()
    return {
        "output_sequence": str(translated_sequence)
        }
