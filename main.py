import sys
import os

# Append tools subdirectory 
sub_dirs = ['./tools']
for sub_dir in sub_dirs:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), sub_dir)))

# load up the environment file with openAI and ExaSearch access tokens
from dotenv import load_dotenv
load_dotenv()

# Import Crew
from crewai import Crew


# Import OpenAI 
from langchain_openai import ChatOpenAI

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
llm = ChatOpenAI(
    model = model,
    api_key = api_key
)
max_rpm = 100


# import the classes that create the Agents and Tasks
from tasks import TurtleTasks
from agents import TurtleAgents

# instantiate the agents and tasks
agents = TurtleAgents(llm, verbose=True, max_rpm=max_rpm)
tasks = TurtleTasks()


# Prompt the user for the turtle breed and age

print("## Welcome to the Turtle Habitat Information System ##")
breed = input("What is the name of the Turtle breed? Chose one of 'Box Turtle', 'Eastern Box Turtle', 'Diamondback Turtle', or 'Pennisula Cooter Turtle'\n")
age = input(f"What is the age of the {breed} turtle?\n")

# Create Agents
researcher_agent = agents.research_agent()
habitat_agent = agents.habitat_agent()

# Create Tasks - Note that these tasks are simple sequential tasks and research_task provides the context for the habitat_task
research_task = tasks.research_task(researcher_agent, breed, age)
habitat_task = tasks.habitat_task(habitat_agent, [research_task])


# Create Crew responsible for generating the habitat research and specification
crew = Crew(
	agents=[
		researcher_agent,
		habitat_agent
	],
	tasks=[
		research_task,
		habitat_task
	]
)

# Run the crew
result = crew.kickoff()


# Print results
print("\n")
print("----------------------------------------------------------------------------------\n")
print("Final Turtle Habitat Specification for " + breed + " that is " + str(age) + " years old.")
print(result)
print("\n")
print("----------------------------------------------------------------------------------\n")


