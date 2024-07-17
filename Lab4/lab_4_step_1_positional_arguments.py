# lab_4_step_1_positional_arguments.py
# Positional arguments: the order of the argument passed to the function depends on order within the ()

import json
import boto3

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response) 
    print(json.dumps(response, ensure_ascii=False, indent=4)) # Print formatted output

def main():
    translate_text('I am learning to code in AWS','en','fr')

if __name__=="__main__":
    main()
