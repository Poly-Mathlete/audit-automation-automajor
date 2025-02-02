import boto3  # Import the boto3 library for AWS services
import botocore  # Import the botocore library for AWS low-level service operations
import json  # Import the json library for working with JSON data
import streamlit as st  # Import the Streamlit library for building web apps
import pdfplumber  # Import the pdfplumber library for PDF extraction
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv library
import os  # Import the os module for interacting with the operating system

from concurrent.futures import ThreadPoolExecutor

from prompts import system_prompt  # Import the system_prompt variable from the prompt module

load_dotenv()

# Setting up the default AWS session using the profile name from the environment variable
boto3.setup_default_session(profile_name=os.getenv("hackathon"))

# Setting up the Bedrock client with a custom timeout configuration
config = botocore.config.Config(connect_timeout=300, read_timeout=300)
bedrock = boto3.client('bedrock-runtime', 'us-west-2', config=config)

test_pdf_path = "C:\\Users\\mateo\\Documents\\ecole\\CS-1A\\assos\\automatant\\hackathon-GenIA-31-01-2025\\data\\Bail_HABIDOM.pdf"

def parse_xml(xml, tag):
    """
    Helper function to extract the value between XML tags from a given string.
    """
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    
    start_index = xml.find(start_tag)
    if start_index == -1:
        return ""

    end_index = xml.find(end_tag)
    if end_index == -1:
        return ""

    value = xml[start_index+len(start_tag):end_index]
    return value

def json_clean(json_str):
    first_ind = json_str.find('{')
    last_ind = json_str.rfind('}')
    return json_str[first_ind:last_ind+1]

def handle_key(key, text, system_prompt, d_stockage):
    for i in range(len(system_prompt[key])):
        print(f"Prompt {i} ------------------------------------------------------")
        
            # Prepare the content for the prompt
        content = [{
                "type": "text",
                "text": text
            }]
            
            #prompt dictionary
        prompt = {
                "temperature": 0.2,
                "messages": [  
                    {
                        "role": "system",
                        "content": system_prompt[key][i]
                    },  
                    {
                        "role": "user",
                        "content": f"{content}"
                    }
                ],
            }

            # Convert the prompt to a JSON string
        prompt = json.dumps(prompt)

            # Invoke the Bedrock model with the prompt
        response = bedrock.invoke_model(
                body=prompt, 
                modelId="mistral.mistral-large-2407-v1:0", 
                accept="application/json", 
                contentType="application/json" )
            
        response_body = json.loads(response.get('body').read())
        llmOutput = response_body['choices'][0]['message']['content'].strip()

        print("beginning of llmOutput")
        print(llmOutput)
        print("end of llmOutput")
        content = llmOutput
    output_clean = json_clean(llmOutput)
    d_stockage[key] = output_clean
    return "ok"

def extract_from_pdf_fast(file, max_simult=10):
    text = ""
    print("processing pdf...")
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    print("pdf processed !")

    d_stockage = {}

    with ThreadPoolExecutor(max_workers=max_simult) as executor:
        futs = []
        for key in system_prompt.keys():
            futs.append(
                executor.submit(handle_key, key, text, system_prompt, d_stockage)
            )    
        r = [fut.result() for fut in futs]

    return d_stockage

def extract_from_pdf(file):

    text = ""
    print("processing pdf...")
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    print("pdf processed !")

    d_stockage = {}
    for key in system_prompt.keys():
        for i in range(len(system_prompt[key])):
            print(f"Prompt {i} ------------------------------------------------------")
        
            # Prepare the content for the prompt
            content = [{
                "type": "text",
                "text": text
            }]
            
            #prompt dictionary
            prompt = {
                "temperature": 0.2,
                "messages": [  
                    {
                        "role": "system",
                        "content": system_prompt[key][i]
                    },  
                    {
                        "role": "user",
                        "content": f"{content}"
                    }
                ],
            }

            # Convert the prompt to a JSON string
            prompt = json.dumps(prompt)

            # Invoke the Bedrock model with the prompt
            response = bedrock.invoke_model(
                body=prompt, 
                modelId="mistral.mistral-large-2407-v1:0", 
                accept="application/json", 
                contentType="application/json" )
            
            response_body = json.loads(response.get('body').read())
            llmOutput = response_body['choices'][0]['message']['content'].strip()

            print("beginning of llmOutput")
            print(llmOutput)
            print("end of llmOutput")
            content = llmOutput
        output_clean = json.loads(json_clean(llmOutput))
        d_stockage[key] = output_clean
        
    print("{")
    for key in d_stockage.keys():
        print(f'"{key}":')
        print(d_stockage, ',')
    print("}")
    

    # Parse the scratchpad and output from the LLM response
    # scratch = parse_xml(llmOutput, "scratchpad")

    # output = parse_xml(llmOutput, "output")

    return d_stockage #scratch, output

if __name__=="__main__":
    with open(test_pdf_path, 'rb') as f:
        dict = extract_from_pdf_fast(f,2)
    str = json.dumps(dict)
    with open("data.json", "w") as f:
        f.write(str)