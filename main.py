from Bio.Seq import Seq
from fastapi import FastAPI

app = FastAPI()

# Complementary Sequence
@app.get("/complementary_sequence/{input_sequence}")
def complement_sequence(input_sequence: str):
    initial_sequence = Seq(input_sequence)
    complementary_sequence = initial_sequence.complement()
    return { 
        "output_sequence": str(complementary_sequence) 
        }

# Reverse Complementary Sequence
@app.get("/reverse_complementary_sequence/{input_sequence}")
def reverse_complement_sequence(input_sequence: str):
    initial_sequence = Seq(input_sequence)
    reverse_complementary_sequence = initial_sequence.reverse_complement()
    return { 
        "output_sequence": str(reverse_complementary_sequence) 
        }

# Transcribed Sequence
@app.get("/transcribed_sequence/{input_sequence}")
def transcribe_sequence(input_sequence: str):
    initial_sequence = Seq(input_sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { 
        "output_sequence": str(transcribed_sequence)
        }

# Back-Transcribed Sequence
@app.get("/back_transcribed_sequence/{input_sequence}")
def back_transcribe_sequence(input_sequence: str):
    initial_sequence = Seq(input_sequence)
    back_transcribed_sequence = initial_sequence.back_transcribe()
    return { 
        "output_sequence": str(back_transcribed_sequence)
        }

# Translated Sequence
@app.get("/translated_sequence/{input_sequence}")
def translate_sequence(input_sequence: str):
    initial_sequence = Seq(input_sequence)
    translated_sequence = initial_sequence.translate()
    return {
        "output_sequence": str(translated_sequence)
        }
