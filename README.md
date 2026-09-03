# CLD 400 & TECH 400 — Combined Course Materials

Course materials for **Westcliff University's** combined intensive studio pairing **CLD 400 (Virtualization & Storage)** with **TECH 400 (Introduction to Information Retrieval)**, delivered in partnership with **Presidential Graduate School (Nepal)**.

Both courses are taught as a single 8-week, 6-hour/week studio in which two collaborating student teams build one shared system: a real-time, distributed **Nepali news crawler**, a **hybrid lexical/neural cross-lingual search engine**, and an interactive **GIS spatial news platform** covering Nepal's provinces, districts, and municipalities.

- CLD 400 (Systems/DevOps) owns bare-metal hypervisors, distributed storage, Linux HA, container orchestration, queues/databases, and observability.
- TECH 400 (Information Retrieval) owns crawlers, the Devanagari NLP pipeline, geo-entity resolution, hybrid search, and the GIS frontend.

See [syllabus.tex](syllabus.tex) / [syllabus.pdf](syllabus.pdf) for the full combined syllabus (learning outcomes, weekly schedule, team roles, and the capstone architecture/interface contract between the two teams).

## Repository Layout

```
.
├── syllabus.tex / syllabus.pdf       # Combined CLD 400 & TECH 400 syllabus (source + built PDF)
├── original-syllabus/                # The original, separate Westcliff catalog syllabi (source PDFs)
├── images/                           # Logos and diagrams used by the LaTeX documents
├── requirements.txt                  # Python deps for the TECH 400 notebooks/scripts
└── TECH-400/                         # TECH 400 (Information Retrieval) lecture notes, labs, and code
    ├── tech400-lecture-notes.tex/.pdf   # Full IR lecture notes (Boolean retrieval through language models)
    ├── week-1-2.ipynb                   # Week 1-2 lab: Boolean retrieval, inverted indexing, TF-IDF/BM25
    ├── nepali-lemmatization.ipynb       # Notebook building/training the Nepali lemmatizer below
    ├── nepali_pipeline.py               # scikit-learn pipeline: tokenizer, HMM lemmatizer, stop-word remover
    ├── lemmatization.py                 # Loads the trained pipeline and exposes lemmatize()
    ├── nepali_hmm_pipeline.pkl          # Trained/pickled HMM lemmatization pipeline
    └── data/                            # Corpus data for the notebooks
```

## Getting Started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the labs via Jupyter:

```bash
jupyter notebook TECH-400/week-1-2.ipynb
# or
jupyter notebook TECH-400/nepali-lemmatization.ipynb
```

### Nepali lemmatization pipeline

`TECH-400/nepali_pipeline.py` implements a from-scratch scikit-learn pipeline for Devanagari text: tokenization, a heuristic-labeled training set, and an HMM (Viterbi) lemmatizer, plus a Nepali stop-word remover. `TECH-400/lemmatization.py` loads the trained `nepali_hmm_pipeline.pkl` and exposes a simple API:

```bash
python3 TECH-400/lemmatization.py
```

```python
from lemmatization import lemmatize

lemmatize(["केटाहरुले पोखरामा रातो स्याउ खाए।"])
```

### Building the LaTeX documents

```bash
latexmk -pdf syllabus.tex
latexmk -pdf TECH-400/tech400-lecture-notes.tex
```

## Course Structure at a Glance

| Phase | Weeks | CLD 400 | TECH 400 |
|---|---|---|---|
| Independent Foundations | 1–4 | Bare-metal hypervisors, storage, Linux HA | Full IR theory + algorithm prototypes on a sample corpus |
| Joint Integration & Deployment | 5–6 | Container orchestration, queues, observability | GIS map, gazetteer, distributed crawling, hybrid search |
| Cloud Migration & Defense | 7–8 | Mentors AWS migration, defends on-prem resilience | Migrates search engine to AWS, live benchmarks/defense |

Full week-by-week breakdown, learning outcomes, the shared resource contract between the two teams, and grading/AI-usage policy are in [syllabus.tex](syllabus.tex).
