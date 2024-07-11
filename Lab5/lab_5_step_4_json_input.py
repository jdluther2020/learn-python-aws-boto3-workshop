# lab_5_step_4_json_input.py 
# Simple example of using JSON data

import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string)
    print(json_input)
    print(json.dumps(json_input, ensure_ascii=False, indent=4)) # Print formatted output

if __name__=="__main__":
    main()
