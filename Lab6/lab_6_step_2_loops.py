# lab_6_step_2_loops.py
# Create a new list out of the data provided
# Run it as:
# python lab_6_step_2_loops.py --file translate_input.json

# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3 

# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print("\nIn function: new_input_text_list()\n")
    print(new_list)

# Another list
def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print("\nIn function: new_list_comprehension()\n")
    print(list_comprehension)

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file""" 
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    print("\nIn function: translate_loop()\n")
    for item in input_text: # Here we iterate over all dictionaries in the Input list
        translate_text(**item)

# Main Function - use to call other functions
def main():
    new_input_text_list()
    new_input_text_list()
    translate_loop()

if __name__ == "__main__":
    main()
