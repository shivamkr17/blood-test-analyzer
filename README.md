# Blood Test Report Analyzer

## Overview

This project is designed to automate the analysis of a blood test report provided in PDF format. It utilizes a multi-agent system to extract the relevant information from the blood test report, summarize the data, find related health articles, and provide personalized health advice. This automation helps in assisting both medical professionals and patients by giving them instant insights from blood test results.

## Approach

### Task Breakdown

I approached this task by breaking it down into several components:

1. **PDF Data Extraction**: The first step was to extract text from the blood test report (PDF format). I used the `PyPDF2` library to extract text from the first two pages of the PDF report, assuming that the key data would generally be on the first couple of pages.
   
2. **Multi-Agent System**: I used the CrewAI framework to create a multi-agent system that handles the analysis:
   - **Blood Test Analyst**: Parses the extracted text to identify key health metrics (e.g., hemoglobin, platelet count, etc.).
   - **Article Researcher**: Uses health metrics as keywords to search the internet for articles related to the extracted blood data.
   - **Health Advisor**: Based on the blood test data, this agent provides suggestions for improving health.
   
3. **Task Creation and Orchestration**: Tasks were generated using the extracted PDF data and then distributed to the relevant agents. The execution flow was set up in a sequential process to ensure that each agent works in harmony with the previous one.

4. **Result Output**: Finally, the results from the multi-agent analysis were saved into a text file (`blood_test_analysis_output.txt`), making it easy for users to view the summary, related articles, and health suggestions.

## Features

- **Extracts Data from PDF**: Handles the extraction of blood test information from the first two pages of a PDF.
- **Multi-Agent System**: Utilizes multiple AI agents to handle different tasks (blood test analysis, article research, and health advice).
- **Health Suggestions**: Provides health-related suggestions based on the blood test results.
- **Relevant Article Lookup**: Searches for related articles on the internet based on blood test results.

---

## Installation

To run this project, you need to have Python installed, along with the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.10 or above
- Required Python packages:
  - PyPDF2
  - crewai (custom agent system)

### Install the Dependencies

First, make sure that you have all the required Python libraries. You can install them using `pip`.

1. Clone this repository:

```bash
git clone https://github.com/shivamkr17/blood-test-analyzer.git
cd blood-test-analyzer

2. Install Dependencies
```
    pip install -r requirements.txt


3. Set Up API Keys

Create a .env file in the project root and add your API keys:

    GOOGLE_API_KEY=<your-google-api-key>
    SERPER_API_KEY=<your-serper-api-key>


- Step 4: Run the Script

    python crew.py