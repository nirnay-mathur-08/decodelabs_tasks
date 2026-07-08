def run_chatbot():
    # 1. KNOWLEDGE BASE: Dictionary with 5+ unique intents [Specification #3]
    # Provides O(1) constant time direct access lookup
    knowledge_base = {
        "hello": "Hi there! Welcome to DecodeLabs. How can I help your engineering journey today?",
        "hi": "Hello! Ready to build some deterministic logic architectures?",
        "help": "I can assist you with understanding Project 1 specifications, IPO models, or AI guardrails.",
        "project 1": "Project 1 is the Rule-Based Chatbot phase focusing on Control Flow and Logic Engine basics.",
        "system 1": "System 1 is the Probabilistic Engine (The Artist)—flexible, but risks hallucinations.",
        "system 2": "System 2 is the Deterministic Engine (The Engineer)—100% hard-coded, white-box safety.",
        "guardrails": "AI Guardrails act as a rule-based filter around LLMs to filter, redact, or block outputs."
    }

    print("=== DecodeLabs Logic Engine v1.0 ===")
    print("Type 'exit' or 'quit' at any time to close the program.\n")

    # 2. INPUT LOOP: Continuous 'while' cycle to keep interaction alive [Specification #1]
    while True:
        # Capture raw user input
        raw_input = input("You: ")

        # 3. SANITIZATION: Explicitly handle casing and trailing/leading whitespace [Specification #2]
        clean_input = raw_input.lower().strip()

        # 4. EXIT STRATEGY: Clean break command to terminate loop safely [Specification #5]
        if clean_input in ['exit', 'quit']:
            print("Bot: Terminating continuous loop. Goodbye, Engineer!")
            break

        # 5. FALLBACK & OUTPUT: The Professional atomic .get() approach [Specification #4]
        # Handles rule lookup and default fallback string in one operation
        fallback_msg = "I do not understand. Please try asking about 'Project 1', 'System 1', or 'Guardrails'."
        reply = knowledge_base.get(clean_input, fallback_msg)
        
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()