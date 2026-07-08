# DecodeLabs AI Intern Projects

[cite_start]This repository contains my completed technical milestones for the foundational AI training tracks at DecodeLabs[cite: 4, 241, 501].

---

## 🏗️ Project 1: Rule-Based Chatbot
* [cite_start]**Objective:** Built a deterministic control flow interface using pure programmatic decision-making logic[cite: 7, 10].
* [cite_start]**Architecture:** Implemented an Input-Process-Output (IPO) framework[cite: 75]. [cite_start]Bypassed linear $O(n)$ `if-elif` ladders by pivoting to Python dictionary hash maps to guarantee optimal constant time $O(1)$ direct access lookups[cite: 128, 144, 154].
* [cite_start]**Key Skills:** Input sanitization (`.lower().strip()`), atomic `.get()` fallback routing, and infinite control cycles[cite: 110, 114, 181].

## 📊 Project 2: Supervised Data Classification
* [cite_start]**Objective:** Transitioned from heuristic rules to supervised pattern recognition using the classic Iris benchmark dataset[cite: 244, 280, 281, 322].
* [cite_start]**Architecture:** Formulated a complete machine learning pipeline consisting of data scaling (`StandardScaler` to force $\text{Mean} = 0, \text{Variance} = 1$), an 80/20 train-test data partition split, and a K-Nearest Neighbors classifier model[cite: 311, 316, 319, 369].
* [cite_start]**Validation:** Refused the standard "accuracy mirage"[cite: 402]. [cite_start]Verified model integrity beyond basic metrics by measuring true spatial boundaries using a Confusion Matrix and Macro F1 Score evaluations[cite: 317, 320, 405, 421].

## 🚀 Project 3: Tech Stack Recommender (Active Prediction)
* [cite_start]**Objective:** Developed a content-based filtering matchmaker engine designed to evaluate user interests and predict specific, optimized technical track suggestions to eliminate choice overload[cite: 503, 553, 583].
* [cite_start]**Architecture:** Mapped text tags into matching vector profiles via a shared vocabulary space[cite: 587, 591]. [cite_start]Extracted nuanced feature weights using a Term Frequency-Inverse Document Frequency (TF-IDF) extraction model to logarithmically penalize common words[cite: 615, 616, 636].
* [cite_start]**Similarity Core:** Implemented magnitude-invariant Cosine Similarity to calculate vector orientation angles, generating a clean truncated Top-3 ranking pipeline list while detailing bypass protocols for User Cold Start situations[cite: 660, 661, 686, 736, 759].