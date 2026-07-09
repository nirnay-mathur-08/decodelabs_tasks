import cv2
import pytesseract
import numpy as np

# Double-check that this explicit mapping matches your installation location!
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def run_ocr_perception_pipeline(image_path):
    print("=== DecodeLabs AI Perception Engine v4.0 ===")
    print("Task: Optical Character Recognition (OCR) Sequencing\n")
    
    # 1. INPUT LAYER: Load the raw unstructured 3D image matrix
    raw_img = cv2.imread(image_path)
    if raw_img is None:
        print(f"[!] Error: Unable to locate or load image at target path: '{image_path}'")
        return

    print(f"[*] Raw Image Loaded. Dimensions: {raw_img.shape} (Height x Width x Channels)")
    
    # 2. PRE-PROCESSING LAYER: Breaking down data noise
    print("[*] Initiating image pre-processing matrix operations...")
    
    # Step A: Grayscale conversion to strip chromatic channel bias
    gray_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
    print("    -> Grayscale flattening complete.")
    
    # Step B: Gaussian Blur to soften pixel frequency jumps and filter out noise
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    print("    -> Gaussian smoothing complete.")
    
    # Step C: Adaptive Thresholding (Otsu's Binarization) to isolate clear foreground text
    _, binary_threshold_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print("    -> Adaptive thresholding binarization complete.\n")
    
    # 3. PROCESS LAYER: Tesseract OCR Ingestion
    print("[*] Passing pre-processed binary image to Tesseract configuration engine...")
    
    # Custom configuration flag: Fully automatic layout segmentation mode (PSM 3)
    custom_config = r'--psm 3'
    
    # Extract detailed data dictionary containing words and their corresponding confidence scores
    ocr_data = pytesseract.image_to_data(binary_threshold_img, config=custom_config, output_type=pytesseract.Output.DICT)
    
    # 4. OUTPUT & VALIDATION LAYER: Enforcing the strict 80% Confidence Gate
    print("[*] Evaluating extracted text structures against compliance safety thresholds...")
    
    validated_words = []
    total_confidence = 0
    word_count = 0
    
    # Loop through all detected text entries
    for i in range(len(ocr_data['text'])):
        word = ocr_data['text'][i].strip()
        confidence = float(ocr_data['conf'][i])
        
        # Filter out empty string artifacts
        if word != "":
            # Convert confidence percentage out of 100 to a decimal fraction score
            confidence_score = confidence / 100.0
            
            # CRITICAL: Validate against the mandatory 80% baseline filter gate
            if confidence_score >= 0.80:
                validated_words.append(word)
                total_confidence += confidence_score
                word_count += 1
            else:
                print(f"    [!] Dropped low-probability hallucination: '{word}' (Confidence: {confidence:.2f}%)")
                
    print("\n======= EXTRACTION PERCEPTION BRIEFING =======")
    if word_count > 0:
        final_text = " ".join(validated_words)
        avg_system_confidence = (total_confidence / word_count) * 100
        
        print(f"[+] Final Validated OCR Output String:\n\n    \"{final_text}\"\n")
        print(f"[+] Pipeline System Average Confidence: {avg_system_confidence:.2f}%")
        print("[+] Status: VERIFICATION COMPLIANT")
    else:
        print("[!] Result: System failure. No extracted elements passed the 80% confidence criteria thresholds.")
        print("[!] Status: VERIFICATION NON-COMPLIANT")
    print("==============================================")

import os

if __name__ == "__main__":
    # This automatically finds the exact folder path where your script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change 'sample_document.png' below to match your file's exact extension (.jpg, .png, etc.)
    sample_image = os.path.join(script_dir, "sample_document.png") 
    
    run_ocr_perception_pipeline(sample_image)