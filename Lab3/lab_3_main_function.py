# lab_3_main_function.py
# Example telling the python interpreter that if the variable __name__ is equal to "__main__" then call the main function
# The main() function sets the entry point for a python program.

import boto3
import json

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'
    print(json.dumps(response, ensure_ascii=False, indent=4)) # Print formatted output

def main():
    translate_text()

if __name__=="__main__":
    main()
