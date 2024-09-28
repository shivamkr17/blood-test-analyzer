import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# call gemini model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature=0.5,
                            google_api_key=os.getenv('GOOGLE_API_KEY'))               


blood_test_analyst = Agent(
    role='Blood Test Analyst',
    goal='Analyze the blood test report and summarize the findings.',
    backstory='A medical expert specializing in blood test analysis.',
    memory=True,
    verbose=True,
    llm=llm,
    allow_delegation=False
)

article_researcher = Agent(
    role='Article Researcher',
    goal='Search for health articles based on blood test results.',
    backstory='An expert researcher proficient in finding health-related articles.',
    tools=[tool],
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation = False,
)

health_advisor = Agent(
    role='Health Advisor',
    goal='Provide health recommendations based on the articles found.',
    backstory='A health advisor with extensive knowledge in providing health advice.',
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation = False,
)
