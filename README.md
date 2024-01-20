# BioSeq API

BioSeq API uses [Biopython](https://biopython.org/) to handle nucleotide sequences.

## Endpoints

### Complementary Sequence
Accepts a nucleotide sequence and returns a complementary nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/complementary_sequence/{input_sequence}
```
#### Example request
> https://bioseq.onrender.com/complementary_sequence/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "output_sequence": "tcgggaggtcctgtccgacgtagtcttctccggtagttc"
}
```

### Reverse Complementary Sequence
Accepts a nucleotide sequence and returns a reverse complementary nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/reverse_complementary_sequence/{input_sequence}
```
#### Example request
> https://bioseq.onrender.com/reverse_complementary_sequence/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "output_sequence": "cttgatggcctcttctgatgcagcctgtcctggagggct"
}
```

### Transcribed Sequence
Accepts a nucleotide sequence and returns a transcribed nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/transcribed_sequence/{input_sequence}
```
#### Example request
> https://bioseq.onrender.com/transcribed_sequence/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "output_sequence": "agcccuccaggacaggcugcaucagaagaggccaucaag"
}
```

### Back-Transcribed Sequence
Accepts a nucleotide sequence and returns a back-transcribed nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/back_transcribed_sequence/{input_sequence}
```
#### Example request
> https://bioseq.onrender.com/back_transcribed_sequence/agcccuccaggacaggcugcaucagaagaggccaucaag

#### Example response
```json
{
    "output_sequence": "agccctccaggacaggctgcatcagaagaggccatcaag"
}
```

### Translated Sequence
Accepts a nucleotide sequence and returns a translated amino acid sequence.

#### Request syntax
```
https://bioseq.onrender.com/translated_sequence/{input_sequence}
```
#### Example request
> https://bioseq.onrender.com/translated_sequence/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "output_sequence": "SPPGQAASEEAIK"
}
```