# config.py
import os

# Configuration for LLM API
LLM_API_KEY = os.getenv("LLM_API_KEY", "your-api-key-here")
LLM_MODEL = "gpt-4"  # or another model name as per API

# Prompt settings
PROMPT_TEMPLATE = """
Create a set of detailed test cases for the following description:
"{description}"
The test cases should include:
1. A brief test case title.
2. Preconditions, if any.
3. Steps to perform the test.
4. Expected results.

Ensure clarity and usability for QA testing purposes.
"""


