# generate_test_cases.py
import openai
from config import LLM_API_KEY, LLM_MODEL, PROMPT_TEMPLATE

# Set up API key
openai.api_key = LLM_API_KEY

def generate_test_cases(description):
    prompt = PROMPT_TEMPLATE.format(description=description)

    try:
        response = openai.Completion.create(
            engine=LLM_MODEL,
            prompt=prompt,
            max_tokens=500, 
            temperature=0.5,
            n=1
        )
        
        test_cases = response.choices[0].text.strip()
        return test_cases
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    description = input("Enter a feature or requirement description for test cases: ")
    test_cases = generate_test_cases(description)
    
    if test_cases:
        print("\nGenerated Test Cases:\n")
        print(test_cases)
    else:
        print("Failed to generate test cases. Check your configuration and API key.")

