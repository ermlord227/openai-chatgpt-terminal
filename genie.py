import openai
import sys
import random
import string
import colorama
import shutil
import argparse
from extras import greeting, lamp
from prompts import prompts
from colorama import Fore, Back, Style

openai.api_key = "API_KEY"

def parse_args():
    parser = argparse.ArgumentParser(description="Genie: Interact with ChatGPT")
    parser.add_argument("--model", default="gpt-3.5-turbo", choices=["gpt-4", "gpt-3.5-turbo","code-davinci-002","text-davinci-003"], help="Choose the API model to use")
    parser.add_argument("question", nargs="*", help="Optional question for non-interactive mode")
    return parser.parse_args()

def display_prompt_menu():
    term_width = shutil.get_terminal_size((80, 20)).columns
    num_columns = 3
    column_width = term_width // num_columns
    formatted_prompts = []

    for i, prompt in enumerate(prompts):
        formatted_prompt = f"{i + 1} - {prompt.split(':')[0]}"
        padded_prompt = formatted_prompt.center(column_width)
        formatted_prompts.append(padded_prompt)

    print(Fore.YELLOW + "Choose a prompt, type your question, or 'q' to quit:\n".center(term_width))
    for i, formatted_prompt in enumerate(formatted_prompts):
        print(Fore.YELLOW + formatted_prompt, end="")
        if (i + 1) % num_columns == 0 and i != len(formatted_prompts) - 1:
            print()
    print("\n")

def center_multiline_string(s):
    term_width = shutil.get_terminal_size((80, 20)).columns
    centered_lines = []

    for line in s.split('\n'):
        padding_left = (term_width - len(line)) // 2
        centered_line = " " * padding_left + line
        centered_lines.append(centered_line)

    return '\n'.join(centered_lines)

args = parse_args()

messages = []

randomgreeting = random.choice(greeting)

if args.question:
    prompt = " ".join(args.question).rstrip(string.punctuation)
else:
    print(Fore.YELLOW + center_multiline_string(lamp))
    print(Fore.YELLOW + center_multiline_string(randomgreeting) + "\n")
    
    display_prompt_menu()
    user_input = input(Fore.BLUE + "Ask me any question, choose '1-9', or 'q': ".center(shutil.get_terminal_size((80, 20)).columns)).strip()
    if user_input.isdigit() and 1 <= int(user_input) <= len(prompts):
        prompt = prompts[int(user_input) - 1]
    else:
        prompt = user_input

while True:
    if prompt.lower() in ["quit", "q", "bye"]:
        print(Fore.YELLOW + "\nGenie: " + "Farewell, master. Until you drag me out of bed again...\n")
        break

    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=args.model,
        messages=messages,
        temperature=0.7)
    reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    print(Fore.YELLOW + "\nGenie: " + reply + "\n")

    if args.question:
        break
    else:
        prompt = input(Fore.BLUE + "Master: ")
        if prompt.lower() == "menu":
            display_prompt_menu()
            user_input = input(Fore.BLUE + "Prompt (1-9), custom question, or 'q': ".center(shutil.get_terminal_size((80, 20)).columns)).strip()
            if user_input.isdigit() and 1 <= int(user_input) <= len(prompts):
                prompt = prompts[int(user_input) - 1]
            else:
                prompt = user_input
