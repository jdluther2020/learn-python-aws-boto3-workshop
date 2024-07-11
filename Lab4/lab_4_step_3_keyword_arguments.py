# lab_4_step_3_keyword_arguments.py

# Keyword arguments using the **kwargs: helps pass an arbitrary number of keyword arguments (key = value)
# Build the kwargs containing a dictionary of key\:value pairs

import json
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    # print(response) 
    print(json.dumps(response, ensure_ascii=False, indent=4)) # Print formatted output

kwargs_var={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs_var)

if __name__=="__main__":
    main()

