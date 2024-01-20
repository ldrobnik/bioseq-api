# BioSeq API

BioSeq API uses [Biopython](https://biopython.org/) to [complement](#complementary-sequence), [transcribe](#transcribed-sequence), and [translate](#translated-sequence) nucleotide sequences.

## Endpoints

### Complementary Sequence
Returns a [complementary](https://en.wikipedia.org/wiki/Complementary_sequences) nucleotide sequence based on a nucleotide sequence.

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

### Transcribd Sequence
Returns a [transcribed](https://en.wikipedia.org/wiki/Transcription_(biology)) RNA sequence based on a nucleotide sequence.

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

### Translated Sequence
This endpoint returns a [translated](https://en.wikipedia.org/wiki/Translation_(biology)) amino acid sequence based on a nucleotide sequence.

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