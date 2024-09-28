## https://serper.dev/
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()

SERPER_API_KEY= os.getenv('SERPER_API_KEY')

# inititlaize the tool for internet searching capabilities
tool = SerperDevTool(api_key=SERPER_API_KEY)