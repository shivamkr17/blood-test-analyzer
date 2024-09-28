from crewai import Task
from tools import tool
from agents import blood_test_analyst, article_researcher,health_advisor

def create_tasks(raw_text):
    analyze_blood_test_task = Task(
        description=f'You have to analyze the blood test report from the following text: "{raw_text}"',
        expected_output='A summary of the blood test results.',
        agent=blood_test_analyst,
        async_execution=False,
    )

    find_articles_task = Task(
        description='Search for health articles based on the blood test analysis.',
        expected_output='A list of relevant health articles with links.',
        agent=article_researcher,
        context=[analyze_blood_test_task], 
        async_execution=False,
    )

    provide_recommendations_task = Task(
        description='Provide health recommendations based on the articles found.',
        expected_output='Health recommendations with links to the articles.',
        agent=health_advisor,
        context=[find_articles_task], 
        async_execution=False,
    )
    
    return [analyze_blood_test_task, find_articles_task, provide_recommendations_task]
