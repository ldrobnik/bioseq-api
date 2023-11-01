from Bio.Seq import Seq

from fastapi import FastAPI

app = FastAPI()

@app.get("/complement/{sequence}")
def complement_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    complementary_sequence = initial_sequence.complement()
    return { str(complementary_sequence) }

@app.get("/transcribe/{sequence}")
def transcribe_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { str(transcribed_sequence) }

