from main import stock_checker  # Import the stock_checker function from main.py

def test_length():
    stock_checker() # Run stock checker function
    with open("webPrompts.txt", "r", encoding="utf-8") as prompts_file:  # Open the prompts file for reading
        prompt_lines = prompts_file.readlines()  # Read all lines from the prompts file

    with open("responseP3.txt", "r", encoding="utf-8") as response_file:  # Open the responses file for reading
        response_lines = response_file.readlines()  # Read all lines from the response file

    assert len(prompt_lines) == len(response_lines), (  # Check if the number of prompts matches number of responses
        f"Expected {len(prompt_lines)} responses, but got {len(response_lines)}"  # Error message if they don't match
    )

def test_heading():
    stock_checker() # Run stock checker function
    with open("webPrompts.txt", "r", encoding="utf-8") as prompts_file:  # Open the prompts file for reading
        prompt_lines = prompts_file.readlines()  # Read all lines from the prompts file

    assert len(prompt_lines) >= 10, (  # Check if there are at least 10 prompts
        f"Expected at least 10 responses, but got less than ten"  # Error message if there are fewer than 10
    )