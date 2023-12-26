# BioSeq API

BioSeq API uses [Biopython](https://biopython.org/) to [complement](#complement-a-sequence), [transcribe](#transcribe-a-sequence), and [translate](#translate-a-sequence) nucleotide sequences.

## Endpoints

BioSeq API provides three endpoints using the `GET` method.

### Complement a Sequence
This endpoint returns a [complementary](https://en.wikipedia.org/wiki/Complementary_sequences) nucleotide sequence based on a nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/complement/{sequence}
```
#### Example request
> https://bioseq.onrender.com/complement/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "sequence": "tcgggaggtcctgtccgacgtagtcttctccggtagttc"
}
```

### Transcribe a Sequence
This endpoint returns a [transcribed](https://en.wikipedia.org/wiki/Transcription_(biology)) RNA sequence based on a nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/transcribe/{sequence}
```
#### Example request
> https://bioseq.onrender.com/transcribe/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "sequence": "agcccuccaggacaggcugcaucagaagaggccaucaag"
}
```

### Translate a Sequence
This endpoint returns a [translated](https://en.wikipedia.org/wiki/Translation_(biology)) amino acid sequence based on a nucleotide sequence.

#### Request syntax
```
https://bioseq.onrender.com/translate/{sequence}
```
#### Example request
> https://bioseq.onrender.com/translate/agccctccaggacaggctgcatcagaagaggccatcaag

#### Example response
```json
{
    "sequence": "SPPGQAASEEAIK"
}
```