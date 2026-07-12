# DecodeLabs AI Intern Projects

[cite_start]This repository contains my completed technical milestones for the foundational AI training tracks at DecodeLabs[cite: 4].

---

## 🏗️ Project 1: Rule-Based Chatbot
* [cite_start]**Objective:** Built a deterministic control flow interface using pure programmatic decision-making logic[cite: 7, 10].
* [cite_start]**Architecture:** Implemented an Input-Process-Output (IPO) framework[cite: 75]. [cite_start]Bypassed linear $O(n)$ `if-elif` ladders by pivoting to Python dictionary hash maps to guarantee optimal constant time $O(1)$ direct access lookups[cite: 128, 144, 154].
* [cite_start]**Key Skills:** Input sanitization (`.lower().strip()`) [cite: 110][cite_start], atomic `.get()` fallback routing [cite: 181, 182][cite_start], and infinite control cycles[cite: 114].

## 📊 Project 2: Supervised Data Classification
* [cite_start]**Objective:** Transitioned from heuristic rules to supervised pattern recognition using the classic Iris benchmark dataset[cite: 244, 280, 281].
* [cite_start]**Architecture:** Formulated a complete machine learning pipeline consisting of data scaling (`StandardScaler` to force $\text{Mean} = 0, \text{Variance} = 1$) [cite: 320, 371][cite_start], an 80/20 train-test data partition split [cite: 318, 434, 435][cite_start], and a K-Nearest Neighbors classifier model[cite: 321, 380].
* [cite_start]**Validation:** Refused the standard "accuracy mirage"[cite: 404]. [cite_start]Verified model integrity beyond basic metrics by measuring true spatial boundaries using a Confusion Matrix and Macro F1 Score evaluations[cite: 319, 322, 407].

## 🚀 Project 3: Tech Stack Recommender (Active Prediction)
* **Objective:** Developed a content-based filtering matchmaker engine designed to evaluate user interests and predict specific, optimized technical track suggestions to eliminate choice overload.
* **Architecture:** Mapped text tags into matching vector profiles via a shared vocabulary space. Extracted nuanced feature weights using a Term Frequency-Inverse Document Frequency (TF-IDF) extraction model to logarithmically penalize common words.
* **Similarity Core:** Implemented magnitude-invariant Cosine Similarity to calculate vector orientation angles, generating a clean truncated Top-3 ranking pipeline list while detailing bypass protocols for User Cold Start situations.

## 📄 Project 4: Optical Character Recognition (OCR) Engine
* **Objective:** Graduated from structured tabular processing to handling unstructured physical visual data matrices to build an intelligent digital machine perception layer.
* **Preprocessing Pipeline:** Implemented a full pixel-manipulation matrix pipeline using OpenCV. Flattened images to grayscale to remove chromatic channel bias, applied Gaussian Smoothing to eliminate high-frequency noise artifacts, and executed Adaptive Thresholding (Otsu's Binarization) to dynamically isolate clean foreground text borders.
* **Ingestion & Validation:** Linked the binarized visual matrices into a sequence parsing engine configuration wrapper running automatic layout segmentation.
* **Compliance:** Enforced a strict production **80% Confidence Gate** to filter out low-probability character strings and eliminate structural hallucinations, achieving verified verification-compliant outputs.