# BioSeq API

BioSeq API uses [Biopython](https://biopython.org/) to handle nucleotide sequences.

## Endpoints

### Complementary Sequence
<details>

<summary><code>GET</code> <code><strong>/complementary-sequence/{nucleotide-sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a complementary nucleotide sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `nucleotide-sequence` |  Required  | String     | Nucleotide sequence to complement              |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/complementary-sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "nucleotide-sequence": "TCGGGAGGTCCTGTCCGACGTAGTCTTCTCCGGTAGTTC"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `nucleotide-sequence` |  Required  | String     | Complementary nucleotide sequence       |
</details>

### Reverse Complementary Sequence

<details>
<summary><code>GET</code> <code><strong>/reverse-complementary-sequence/{nucleotide-sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a reverse complementary nucleotide sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `nucleotide-sequence` |  Required  | String     | Nucleotide sequence to reverse-complement      |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/reverse-complementary-sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "nucleotide-sequence": "CTTGATGGCCTCTTCTGATGCAGCCTGTCCTGGAGGGCT"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `nucleotide-sequence` |  Required  | String     | Reverse complementary nucleotide sequence      |
</details>

### Transcribed Sequence

<details>
<summary><code>GET</code> <code><strong>/transcribed-sequence/{dna-sequence}</strong></code></summary>

Accepts a DNA sequence and returns a transcribed RNA sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `dna-sequence` |  Required  | String     | DNA sequence to transcribe     |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/transcribed-sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "rna-sequence": "AGCCCUCCAGGACAGGCUGCAUCAGAAGAGGCCAUCAAG"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `rna-sequence` |  Required  | String     | Transcribed RNA sequence                 |
</details>

### Back-Transcribed Sequence

<details>
<summary><code>GET</code> <code><strong>/back-transcribed-sequence/{rna-sequence}</strong></code></summary>

Accepts an RNA sequence and returns a back-transcribed DNA sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `rna-sequence` |  Required  | String     | RNA sequence to back-transcribe                |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/back-transcribed-sequence/AGCCCUCCAGGACAGGCUGCAUCAGAAGAGGCCAUCAAG"
> ```

#### Example response
> ```json
> {
>     "dna-sequence": "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `dna-sequence` |  Required  | String     | Back-transcribed DNA sequence            |
</details>

### Translated Sequence

<details>
<summary><code>GET</code> <code><strong>/translated-sequence/{nucleotide-sequence}</strong></code></summary>

Accepts a nucleotide sequence and returns a translated protein sequence.

#### Path parameters

> | Name   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `nucleotide-sequence` |  Required  | String     | Nucleotide sequence to translate          |

#### Example request
> ```js
>  curl -X GET "https://bioseq.xyz/translated-sequence/AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAG"
> ```

#### Example response
> ```json
> {
>     "protein-sequence": "SPPGQAASEEAIK"
> }
> ```

#### Response schema

> | Object   |  Type      | Data type      | Description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `protein-sequence` |  Required  | String     | Translated protein sequence        |

</details>
