from Bio.Seq import Seq
from fastapi import FastAPI

app = FastAPI()

# Complementary Sequence
@app.get("/complementary-sequence/{nucleotide_sequence}")
def complement_sequence(nucleotide_sequence: str):
    initial_sequence = Seq(nucleotide_sequence)
    complementary_sequence = initial_sequence.complement()
    return { 
        "nucleotide-sequence": str(complementary_sequence) 
        }

# Reverse Complementary Sequence
@app.get("/reverse-complementary-sequence/{nucleotide_sequence}")
def reverse_complement_sequence(nucleotide_sequence: str):
    initial_sequence = Seq(nucleotide_sequence)
    reverse_complementary_sequence = initial_sequence.reverse_complement()
    return { 
        "nucleotide-sequence": str(reverse_complementary_sequence) 
        }

# Transcribed Sequence
@app.get("/transcribed-sequence/{dna_sequence}")
def transcribe_sequence(dna_sequence: str):
    initial_sequence = Seq(dna_sequence)
    transcribed_sequence = initial_sequence.transcribe()
    return { 
        "rna-sequence": str(transcribed_sequence)
        }

# Back-Transcribed Sequence
@app.get("/back-transcribed-sequence/{rna_sequence}")
def back_transcribe_sequence(rna_sequence: str):
    initial_sequence = Seq(rna_sequence)
    back_transcribed_sequence = initial_sequence.back_transcribe()
    return { 
        "dna-sequence": str(back_transcribed_sequence)
        }

# Translated Sequence
@app.get("/translated-sequence/{nucleotide_sequence}")
def translate_sequence(nucleotide_sequence: str):
    initial_sequence = Seq(nucleotide_sequence)
    translated_sequence = initial_sequence.translate()
    return {
        "protein-sequence": str(translated_sequence)
        }
