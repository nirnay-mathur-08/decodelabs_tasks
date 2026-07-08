import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score

def run_classification_pipeline():
    print("=== DecodeLabs AI Predictive Engine v2.0 ===")
    print("Task: Supervised Flower Classification via Proximity Principles\n")
    
    # 1. INPUT LAYER: Load and explore the classic Iris benchmark [cite: 53, 58, 59]
    iris = load_iris()
    X = iris.data  # 4 dimensions: Sepal Length, Sepal Width, Petal Length, Petal Width 
    y = iris.target  # 3 target classes: Setosa, Versicolor, Virginica 
    
    print(f"[*] Dataset successfully loaded.")
    print(f"    - Total Samples: {X.shape[0]} (Balanced across 3 classes) ")
    print(f"    - Features per sample: {X.shape[1]} dimensional measurements ")
    
    # 2. THE GATEKEEPER RULE: Feature Scaling [cite: 58, 60]
    # Standardizes raw data to have a Mean = 0 and Variance = 1 to balance feature weights 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("[*] Feature scaling applied via StandardScaler.")
    
    # 3. STRUCTURAL INTEGRITY: Shuffle & Train-Test Split [cite: 58, 62]
    # Shuffles data to remove order bias and splits into an 80% training set and 20% validation set [cite: 62, 69]
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"[*] Data partitioned safely:")
    print(f"    - Training Matrix shape: {X_train.shape} (80% Pattern Recognition Core) [cite: 62, 69]")
    print(f"    - Testing Matrix shape:  {X_test.shape} (20% Validation Set) [cite: 62, 69]\n")
    
    # 4. PROCESS LAYER: Instantiate, Fit, and Predict via KNN [cite: 58, 65]
    # Using an optimal K=5 to locate 'The Elbow' and avoid over/underfitting bounds [cite: 64, 65]
    print("[*] Instantiating K-Nearest Neighbors Classifier (K=5)... [cite: 63, 65]")
    model = KNeighborsClassifier(n_neighbors=5)  # Instantiate 
    
    print("[*] Training model (Mapping geometric target proximity maps)... [cite: 63, 65]")
    model.fit(X_train, y_train)  # Fit 
    
    print("[*] Model execution phase: Generating predictive classes for unseen data... [cite: 47, 65]")
    predictions = model.predict(X_test)  # Predict 
    print("    -> Generation complete.\n")
    
    # 5. OUTPUT LAYER: Verification beyond the "Accuracy Mirage" [cite: 58, 66]
    print("=== PERFORMANCE VALIDATION MATRIX ===")
    
    # Generate the Diagnostic Tool: Confusion Matrix [cite: 58, 67]
    conf_mat = confusion_matrix(y_test, predictions)
    print("\n[+] Confusion Matrix Grid Map[cite: 67]:")
    print(conf_mat)
    
    # Calculate macro F1 Score (Harmonic Mean balancing Precision & Recall) [cite: 58, 68]
    macro_f1 = f1_score(y_test, predictions, average='macro')
    print(f"\n[+] Evaluated System Macro F1 Score: {macro_f1:.4f} [cite: 58, 68]")
    
    # Complete text report mapping precision, recall, and boundaries per class
    print("\n[+] Full Classification Integrity Briefing:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

if __name__ == "__main__":
    run_classification_pipeline()