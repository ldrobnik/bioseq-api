from Bio.Seq import Seq

from fastapi import FastAPI

app = FastAPI()

@app.get("/complement/{sequence}")
def complement_sequence(sequence: str):
    initial_sequence = Seq(sequence)
    complementary_sequence = initial_sequence.complement()
    return { str(complementary_sequence)}
