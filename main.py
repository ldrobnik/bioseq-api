from Bio.Seq import Seq

from fastapi import FastAPI

app = FastAPI()

# Complement a Sequence
@app.get("/complement/{sequence}")
def complement_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    complementary_sequence = initial_sequence.complement()
    return { 
        "sequence": str(complementary_sequence) 
        }

# Transcribe a Sequence
@app.get("/transcribe/{sequence}")
def transcribe_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { 
        "sequence": str(transcribed_sequence)
        }

# Translate a Sequence
@app.get("/translate/{sequence}")
def translate_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    translated_sequence = initial_sequence.translate()
    return {
        "sequence": str(translated_sequence)
        }
