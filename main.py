from Bio.Seq import Seq

from fastapi import FastAPI

app = FastAPI()

# Get a Complementary Sequence
@app.get("/complementary-sequence/{sequence}")
def complement_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    complementary_sequence = initial_sequence.complement()
    return { 
        "sequence": str(complementary_sequence) 
        }

# Get a Transcribed Sequence
@app.get("/transcribed-sequence/{sequence}")
def transcribe_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { 
        "sequence": str(transcribed_sequence)
        }

# Get a Translated Sequence
@app.get("/translated-sequence/{sequence}")
def translate_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    translated_sequence = initial_sequence.translate()
    return {
        "sequence": str(translated_sequence)
        }
