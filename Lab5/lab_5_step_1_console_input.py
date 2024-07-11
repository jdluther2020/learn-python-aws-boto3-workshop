# lab_5_step_1_console_input.py

# Provide the values as user command line prompt input at the time we run the program

import boto3
import json

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 
    print(json.dumps(response, ensure_ascii=False, indent=4)) # Print formatted output

text = input("Provide the text you want translating: ")
source_language_code = input("Provide the two letter source language code (en or fr): ")
target_language_code = input("Provide the two letter target language code (en or fr): ") 

def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()

