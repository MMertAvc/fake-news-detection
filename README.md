# Fake & Real News Detection — AutoML Classification

A PyCaret AutoML project that classifies news articles as fake or real using TF-IDF text features and an automatically selected best classifier, served through a Streamlit web application.

> **Note:** `train.csv` (87.85 MB), `Fake.csv` (59.88 MB), and `True.csv` (51.10 MB) are large files that approach GitHub's 100 MB per-file limit. They are included in this repo but may trigger a GitHub large-file warning.

---

## English

### About

This project builds a binary text classifier to detect fake news using the PyCaret AutoML library. Raw news article text is vectorized with TF-IDF and fed into PyCaret's model comparison pipeline, which automatically selects the best-performing algorithm. A saved model and vectorizer are then served through a Streamlit web app where users can paste any news article and receive an instant real/fake prediction.

### Features

- Binary classification: Fake (0) vs. Real (1)
- TF-IDF vectorization (`tfidf_vectorizer.pkl`)
- PyCaret AutoML model selection and training
- Streamlit web app for live predictions from pasted news text
- Saved model: `fake_news_model.pkl` (0.85 MB)

### Dataset

**Source:** Kaggle — Fake and Real News Dataset

| File | Size | Status |
|---|---|---|
| `train.csv` | 87.85 MB | ⚠️ Included (large, near GitHub limit) |
| `test.csv` | 21.97 MB | ✅ Included |
| `Fake.csv` | 59.88 MB | ⚠️ Included (large) |
| `True.csv` | 51.10 MB | ⚠️ Included (large) |

Each row contains a news article with a `label` column: `0 = Fake`, `1 = Real`.

### Model Architecture / Tech Stack

```
Raw News Text
→ TF-IDF Vectorization (tfidf_vectorizer.pkl)
→ PyCaret AutoML (model comparison + selection)
→ Binary Label: Fake (0) / Real (1)
```

**Tech Stack:** Python · PyCaret · scikit-learn · pandas · joblib · Streamlit

### How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Paste any news article into the Streamlit app to receive an instant fake/real prediction.

### Requirements

```
pycaret
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## Türkçe

### Hakkında

Bu proje, PyCaret AutoML kütüphanesini kullanarak sahte haberleri tespit eden bir ikili metin sınıflandırıcı oluşturur. Ham haber metni TF-IDF ile vektörleştirilir ve PyCaret'in model karşılaştırma hattına beslenerek en iyi performans gösteren algoritma otomatik olarak seçilir. Kaydedilen model ve vektörleştirici, kullanıcıların herhangi bir haber metni yapıştırarak anında gerçek/sahte tahmini alabildiği bir Streamlit web uygulamasıyla sunulur.

> **Not:** `train.csv` (87,85 MB), `Fake.csv` (59,88 MB) ve `True.csv` (51,10 MB) büyük dosyalardır ve GitHub'ın dosya başına 100 MB sınırına yaklaşmaktadır. Repoya dahil edilmişlerdir ancak GitHub büyük dosya uyarısı verebilir.

### Özellikler

- İkili sınıflandırma: Sahte (0) / Gerçek (1)
- TF-IDF metin vektörleştirme (`tfidf_vectorizer.pkl`)
- PyCaret AutoML model seçimi ve eğitimi
- Yapıştırılan haber metninden canlı tahmin için Streamlit web uygulaması
- Kaydedilen model: `fake_news_model.pkl` (0,85 MB)

### Veri Seti

**Kaynak:** Kaggle — Sahte ve Gerçek Haberler Veri Seti

| Dosya | Boyut | Durum |
|---|---|---|
| `train.csv` | 87,85 MB | ⚠️ Dahil (büyük, limite yakın) |
| `test.csv` | 21,97 MB | ✅ Dahil |
| `Fake.csv` | 59,88 MB | ⚠️ Dahil (büyük) |
| `True.csv` | 51,10 MB | ⚠️ Dahil (büyük) |

Her satır bir haber makalesi içerir ve `label` sütunu: `0 = Sahte`, `1 = Gerçek` şeklindedir.

### Model Mimarisi / Teknoloji Yığını

```
Ham Haber Metni
→ TF-IDF Vektörleştirme (tfidf_vectorizer.pkl)
→ PyCaret AutoML (model karşılaştırma + seçim)
→ İkili Etiket: Sahte (0) / Gerçek (1)
```

**Teknoloji Yığını:** Python · PyCaret · scikit-learn · pandas · joblib · Streamlit

### Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
streamlit run app.py
```

Herhangi bir haber makalesini Streamlit uygulamasına yapıştırarak anında sahte/gerçek tahmini alın.

### Gereksinimler

```
pycaret
pandas
numpy
scikit-learn
streamlit
joblib
```
