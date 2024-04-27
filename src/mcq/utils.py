# helper file/ helping function and all hear


import os
# from PyPDF2 import PdfReader
from PyPDF2 import PdfReader
import json
import traceback

#data

#First helper function
def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PdfReader(file)
            text=""

            for page in pdf_reader.pages:
                text+=page.extract_text()

            return text
        
        except Exception as e:
            raise Exception(f"Error reading the PDF file: {e}")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported file format. Only .pdf and .txt files are supported")
    

#Second Helper Function for converting mcq output in dataframe
def get_table_data(quiz_str):
    try:
        # convert the quiz string to a dictionary
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        # iterate over the quiz dictionary and extract the required information
        for Key, value in quiz_dict.items():
            mcq=value["mcq"]
            options= " | ".join(
                [f"{options}->{option_value}" 
                for options, option_value in value["options"].items()
                ]

            )

            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

#go through StreamlitAPP from here