from textwrap import dedent
from crewai import Agent

from tools.exa_search import ExaSearchTool

# define a class that will create the Turtle Researcher and the Turtle Habitat Specialist.
class TurtleAgents():

    # The Turtle Researcher requires the ExaSearchTool to search the internet for content
    # related to the Turtle given the breed and age. 
    def research_agent(self, verbose=True):
      return Agent(
        role="Turtle Researcher",
        goal='Conduct comprehensive research on turtles.',
        tools=ExaSearchTool.tools(),
        backstory=dedent("""\
          As a Turtle Researcher, you are driven by a strong desire to understand a large variety of 
          turtles including their breed, size, living habits, diet, mating habits and environmental 
          requirements. Your insights will provide the groundwork for the design of turtle habitats 
          such as tank size in gallons, diet, and environmental conditions based on breed and age."""),
        verbose=verbose
      )
      
    # The Turtle Habitat Agent does not require any tools as it will take the context of 
    # what the Turtle Researcher provides and summarize it for a recommendation on the specification  
    def habitat_agent(self, verbose=True): 
      return Agent(
        role='Turtle Habitat Specialist',
        goal='Create a habitat specification for a turtle given breed and age.',
        backstory=dedent("""\
            As the Turtle Habitat Specialist, your role is to produce a habitat specification
            from the comprehensive analysis information provided."""),
        verbose=verbose
      )