import os
from crewai import Crew, Process
from agents import blood_test_analyst, article_researcher, health_advisor
from tasks import create_tasks
import PyPDF2  # Ensure you have this installed

# Function to extract text from the first two pages of a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Read only the first two pages or less if not available
        for page in range(min(2, len(reader.pages))):  
            text += reader.pages[page].extract_text()
    return text

# Function to get the blood test PDF report from user
def get_blood_test_report():
    pdf_path = input("Enter the path to the blood test report PDF: ")
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    return pdf_path

# Function to save output to a text file
def save_output_to_txt(output, file_path='output.txt'):
    with open(file_path, 'w') as file:
        file.write(output)

# Getting the blood test report from the user
pdf_report_path = get_blood_test_report()

# Extracting the text from the first two pages of the PDF report
raw_text = extract_text_from_pdf(pdf_report_path)

# Create tasks with the extracted raw text
tasks = create_tasks(raw_text)

# Forming the tech-focused crew with enhanced configuration
crew = Crew(
    agents=[blood_test_analyst, article_researcher, health_advisor],
    tasks=tasks,
    process=Process.sequential,
)

# Starting the task execution process with the blood test data
result = crew.kickoff(inputs={'blood_test_data': raw_text})

# Save the result to a text file
save_output_to_txt(str(result), 'blood_test_analysis_output.txt')

print("Analysis saved to 'blood_test_analysis_output.txt'.")
