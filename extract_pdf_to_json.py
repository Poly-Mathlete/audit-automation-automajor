import boto3  # Import the boto3 library for AWS services
import botocore  # Import the botocore library for AWS low-level service operations
import json  # Import the json library for working with JSON data
import streamlit as st  # Import the Streamlit library for building web apps
import pdfplumber  # Import the pdfplumber library for PDF extraction
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv library
import os  # Import the os module for interacting with the operating system

from prompt import system_prompt  # Import the system_prompt variable from the prompt module

# Loading environment variables from the .env file
load_dotenv()

# Setting up the default AWS session using the profile name from the environment variable
boto3.setup_default_session(profile_name=os.getenv("hackathon"))

# Setting up the Bedrock client with a custom timeout configuration
config = botocore.config.Config(connect_timeout=300, read_timeout=300)
bedrock = boto3.client('bedrock-runtime', 'us-west-2', config=config)

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
    

def pdf_extraction(content):
    """
    Function to extract financial details from the given PDF content.
    """
#     system_prompt = f"""
# You are a Data Processor. You will be provided the text of a Earnings Call or Financial Report from a company
# Extract the following items and information from the provided content and output them into a valid json array
#     Title (shorten the title to 6 words or less)
#     The Published Date (in the format of mm/dd/yyyy)
#     The Company of focus (ex. Amazon, Apple etc.)
#     Earnings Per Share (EPS) of the Company ("Not Provided" if not provided)
#     Net Income of the Company ("Not Provided" if not provided) - include the number-word expression ie. Million or Billion
#     Free Cash Flow ("Not Provided" if not provided) include the number-word expression ie. Million or Billion
#     a brief summary of the financial report based on the information provided and the outlook of the financial performance - make sure this value is valid json (be sure to use escape characters to handle quotation marks if they exist in your summary (ie. \\"SampleQuotes\\""))
#     A key quote from the Company leader (include citation and speaker name/title) - be sure to use escape characters to handle quotation marks (ie. \\"SampleQuotes\\")


# Return your response in valid JSON, using the provided output format
# <example_format>
# {{"Title": "(title)", "Date": "(article_date - in mm/dd/yyy)", "Company": "(company)", "Earnings_Per_Share": "(earnings per share)", "Net_Income": "(net income)", "Free_Cash_Flow": "(Free Cash Flow)", "Outlook": "(outlook)", "Quote": "(quote)"}}
# </example_format>

# When creating the summary and the key quotes, be sure to escape quotation marks in string values so that the output is valid json

# Think through each step of your thought process and write your thoughts down in <scratchpad> xml tags

# return the valid json array with the extracted details in <output> xml tags, only including the valid json

# """

    d_stockage = {}
    for key in system_prompt.keys():
        for i in range(len(system_prompt[key])):
            print(f"Prompt {i} ------------------------------------------------------")
        
            # Prepare the content for the prompt
            content = [{
                "type": "text",
                "text": content
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
        
    print("{")
    for key in d_stockage.keys():
        print(f'"{key}":')
        print(d_stockage, ',')
    print("}")
    

    # Parse the scratchpad and output from the LLM response
    # scratch = parse_xml(llmOutput, "scratchpad")

    # output = parse_xml(llmOutput, "output")

    return llmOutput #scratch, output

def pdf_processing(pdf):
    """
    Function to process a PDF file and extract financial details.
    """
    text = ""
    with st.status("Processing PDF", expanded=False, state="running") as status:
        with pdfplumber.open(pdf) as pdf:
            # Loop through each page in the PDF
            for page in pdf.pages:
                # Extract the text from the page
                text = text + page.extract_text()
        
                # Print the extracted text
                #print(text)
        status.update(label=":heavy_check_mark: PDF Processing Complete", state="running", expanded=False)
        st.write(":heavy_check_mark: PDF Processing Complete")

        status.update(label="Extracting Details from PDF", state="running", expanded=False)
        output = pdf_extraction(text) #scratch, output = pdf_extraction(text)
        print(type(output))
        output_clean = json_clean(output)
        print(output_clean)
        output_json = json.loads(output_clean)
        # json.dumps({
        #         "Text": output
        #     })  

        status.update(label=":heavy_check_mark: Details Extracted", state="complete", expanded=False)
        st.write(":heavy_check_mark: Details Extracted")

    # Display the extracted details in text input fields
    for key in output_json:
        value = output_json[key]
        st.text_input(key, value)

    # Display the full JSON payload in an expander
    with st.expander("Full JSON Payload"):
        st.json(output)
