# BioSeq API

BioSeq API uses [Biopython](https://biopython.org/) to handle nucleotide sequences.

## Endpoints

### Complementary Sequence
<details>

<summary><code>GET</code> <code><strong>/complementary_sequence/{input_sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a complementary nucleotide sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `input_sequence` |  Required  | String     | Nucleotide sequence to complement              |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/complementary_sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "output_sequence": "TCGGGAGGTCCTGTCCGACGTAGTCTTCTCCGGTAGTTC"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `output_sequence` |  Required  | String     | Complementary nucleotide sequence       |
</details>

### Reverse Complementary Sequence

<details>
<summary><code>GET</code> <code><strong>/reverse_complementary_sequence/{input_sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a reverse complementary nucleotide sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `input_sequence` |  Required  | String     | Nucleotide sequence to reverse-complement      |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/reverse_complementary_sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "output_sequence": "CTTGATGGCCTCTTCTGATGCAGCCTGTCCTGGAGGGCT"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `output_sequence` |  Required  | String     | Reverse complementary nucleotide sequence      |
</details>

### Transcribed Sequence

<details>
<summary><code>GET</code> <code><strong>/transcribed_sequence/{input_sequence}</strong></code></summary>

Accepts a DNA sequence and returns a transcribed RNA sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `input_sequence` |  Required  | String     | DNA sequence to transcribe     |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/transcribed_sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "output_sequence": "AGCCCUCCAGGACAGGCUGCAUCAGAAGAGGCCAUCAAG"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `output_sequence` |  Required  | String     | Transcribed RNA sequence                 |
</details>

### Back-Transcribed Sequence

<details>
<summary><code>GET</code> <code><strong>/back_transcribed_sequence/{input_sequence}</strong></code></summary>

Accepts an RNA sequence and returns a back-transcribed DNA sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `input_sequence` |  Required  | String     | RNA sequence to back-transcribe                |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/back_transcribed_sequence/AGCCCUCCAGGACAGGCUGCAUCAGAAGAGGCCAUCAAG"
> ```

#### Example response
> ```json
> {
>     "output_sequence": "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `output_sequence` |  Required  | String     | Back-transcribed DNA sequence            |
</details>

### Translated Sequence

<details>
<summary><code>GET</code> <code><strong>/translated_sequence/{input_sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a translated protein sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `input_sequence` |  Required  | String     | Nucleotide sequence to translate          |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/translated_sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "output_sequence": "SPPGQAASEEAIK"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `output_sequence` |  Required  | String     | Translated protein sequence        |

</details>