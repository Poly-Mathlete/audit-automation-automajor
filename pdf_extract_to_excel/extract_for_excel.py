import boto3  # Import the boto3 library for AWS services
import botocore  # Import the botocore library for AWS low-level service operations
import json  # Import the json library for working with JSON data
import streamlit as st  # Import the Streamlit library for building web apps
import pdfplumber  # Import the pdfplumber library for PDF extraction
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv library
import os  # Import the os module for interacting with the operating system  # Import the pdf_processing function from the extract_pdf_to_json module
from excel_prompt_page_duree import excel_extraction_page_duree
from excel_promp_page_divers import excel_extraction_page_divers
from excel_prompt_page_charge import excel_extraction_page_charge

# Loading environment variables from the .env file
load_dotenv()

# Setting up the default AWS session using the profile name from the environment variable
boto3.setup_default_session(profile_name=os.getenv("hackathon"))

# Setting up the Bedrock client with a custom timeout configuration
config = botocore.config.Config(connect_timeout=300, read_timeout=300)
bedrock = boto3.client('bedrock-runtime', 'us-west-2', config=config)

test_pdf_path = "C:\\Users\\mateo\\Documents\\ecole\\CS-1A\\assos\\automatant\\hackathon-GenIA-31-01-2025\\data\\Bail_Harmonie.pdf"

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

def extract_from_pdf(pdf_file, to_do):
    text = ""
    print("pocessing pdf...")
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    print("pdf processed !")

    result = {}

    print("processing tags one by one")
    for thing in to_do:
        print("processing", thing[0]["tag"])
        input = [{
        "type": "text",
        "text": text
        }]
        for call in thing:
            prompt = {
                "temperature": 0.0,
                "messages": [  
                    {
                        "role": "system",
                        "content": call["sys_prompt"]
                    },
                    {
                        "role": "user",
                        "content": f"<legal_call_content> {input} </legal_call_content>"
                    }
                ]
            }
            prompt = json.dumps(prompt)
            response = bedrock.invoke_model(body=prompt, modelId="mistral.mistral-large-2407-v1:0", accept="application/json", contentType="application/json")
            response_body = json.loads(response.get('body').read())
            llmOutput = response_body['choices'][0]['message']['content']
            print("llmOutput", llmOutput)
            output = parse_xml(llmOutput, "output")
            input = [{"type": "text", "text": output}]
        result[thing[0]["tag"]] = input[0]["text"]
    return result



if __name__ == "__main__":
    with open(test_pdf_path, 'rb') as file:
        print(extract_from_pdf(file, excel_extraction_page_divers))