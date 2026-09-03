from pathlib import Path

import joblib

import nepali_pipeline  

MODEL_PATH = Path(__file__).resolve().parent / "nepali_hmm_pipeline.pkl"

_pipeline = joblib.load(MODEL_PATH)


def lemmatize(sentences: list[str]) -> list[list[str]]:
    """Lemmatize raw Nepali sentences using the pre-trained pipeline."""
    return _pipeline.transform(sentences)


test_data = ["केटाहरुले पोखरामा रातो स्याउ खाए।"]
print("Pipeline Output:", lemmatize(test_data))
