# config.py
import os

# Configuration for LLM API
LLM_API_KEY = os.getenv("LLM_API_KEY", "your-api-key-here")
LLM_MODEL = "gpt-4"  # or another model name as per API

# Prompt settings
PROMPT_TEMPLATE = """
You are an intelligent assistant designed to generate automated test cases based on the following requirements provided by the user.

### User Requirements:
{user_input}

### Your Task:
Create comprehensive and clear automated test cases that effectively validate the specified functionality. Ensure that the test cases cover various scenarios, including edge cases, and are structured in a way that is easy to understand and implement.

### Example Test Cases:
1. 
2. 
3. 
...
"""


