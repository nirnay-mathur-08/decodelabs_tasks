import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run_tech_stack_recommender():
    print("=== DecodeLabs Personalization Engine v3.0 ===")
    print("Task: Active Career Path Prediction & Digital Matchmaking\n")
    
    # SIMULATING DATASET: Simulates the underlying structured raw_skills.csv [Specification Page 22]
    # Career profiles serve as the primary item rows with structured vocabularies
    mock_csv_data = {
        'Job Role': [
            'Data Scientist', 
            'DevOps Engineer', 
            'Backend Developer', 
            'Cloud Architect', 
            'Frontend Engineer'
        ],
        'Required Skills': [
            'python sql machine learning data analysis pandas git data structures',
            'aws docker kubernetes linux ci/cd automation git cloud computing',
            'java python sql apis databases object oriented programming data structures git',
            'aws cloud computing azure enterprise security microservices software architecture linux',
            'html css javascript react web design frontend development user interface typescript'
        ]
    }
    df = pd.DataFrame(mock_csv_data)
    
    # 1. COLD START ENGINE ROUTING: Vector & Model Ingestion setup
    # Instantiating professional-grade TF-IDF Vector extraction layer [Page 11-12]
    # This automatically runs linear normalization, term calculations, and log dampening
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['Required Skills'])
    
    # 2. STEP 1 INGESTION PIPELINE: Gathering data density inputs
    print("[*] Entering Step 1: User Feature Ingestion Layer...")
    print("    Please input a minimum of 3 technical skills or career tags to bootstrap your profile.")
    
    user_skills = []
    input_count = 1
    while len(user_skills) < 3:
        skill = input(f"    - Enter Skill/Tag #{input_count}: ").strip()
        if skill:
            user_skills.append(skill)
            input_count += 1
        else:
            print("    [!] Input cannot be empty. Please specify a qualitative tag.")
            
    # Combine choices into a single token string query vector space
    user_profile_string = " ".join(user_skills)
    print(f"\n[+] Baseline profile compiled: ['{user_profile_string}']")
    
    # Transform qualitative user state into a weighted spatial vector matching item vocabulary spaces
    user_vector = vectorizer.transform([user_profile_string])
    
    # 3. STEP 2 SCORING PIPELINE: Angular distance metrics execution
    print("\n[*] Entering Step 2: Spatial Scoring Computation Layer...")
    # Computes mathematical angle similarities between user profile and job vectors, invariant to vector text length magnitudes
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    print("    -> Cosine similarities mapped successfully across database space rows.")
    
    # Attach scores onto data frame structure
    df['Similarity Score'] = similarity_scores
    
    # 4. STEP 3 SORTING PIPELINE: Descending sequence logic
    print("[*] Entering Step 3: Descending Structural Sorting Core...")
    # Pushes highest scoring percentage angular matches directly to the top
    sorted_df = df.sort_values(by='Similarity Score', ascending=False).reset_index(drop=True)
    
    # 5. STEP 4 FILTERING PIPELINE: Truncated Top-N List protection
    print("[*] Entering Step 4: Truncated Feature Selection Filtering...")
    # Truncating output to exactly the Top 3 items to completely bypass user choice overload bounds
    top_3_recommendations = sorted_df.head(3)
    print("    -> Target Top-3 recommendations extracted successfully.\n")
    
    # DISPLAY FINAL HIGH-FIDELITY commercial OUTPUT
    print("======= RECO ENGINE RANKED REWARDS (TOP-3 MATCHES) =======")
    for index, row in top_3_recommendations.iterrows():
        rank = index + 1
        percentage_match = row['Similarity Score'] * 100
        
        # Identify absolute user cold start tracking failure (vector multiplication returns 0)
        if percentage_match == 0:
            print(f"\n[!] Rank #{rank} Defaulting to System Trending Fallback Protocols:")
            print("    -> Match Vector Empty. Current query shares 0 common dimensions with item structures.")
            print("    -> Recommendation: Triggering Popular Standard Track: [Full-Stack Developer Route]")
            break
            
        print(f"\n[+] MATCH RANK #{rank} : {row['Job Role']}")
        print(f"    - Mathematical Cosine Angular Match: {percentage_match:.2f}%")
        print(f"    - Base Target Attribute Footprint: {row['Required Skills']}")
    print("\n==========================================================")

if __name__ == "__main__":
    run_tech_stack_recommender()