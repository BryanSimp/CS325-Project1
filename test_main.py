from main import stock_checker

def test_length():
    with open("webPrompts.txt", "r", encoding="utf-8") as prompts_file:
        prompt_lines = prompts_file.readlines()

    with open("responseP3.txt", "r", encoding="utf-8") as response_file:
        response_lines = response_file.readlines()

    assert len(prompt_lines) == len(response_lines), (
        f"Expected {len(prompt_lines)} responses, but got {len(response_lines)}"
    )

def test_heading():
    with open("webPrompts.txt", "r", encoding="utf-8") as prompts_file:
        prompt_lines = prompts_file.readlines()

    assert len(prompt_lines) >= 10, (
        f"Expected at least 10 responses, but got less than ten"
    )