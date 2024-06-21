from textwrap import dedent
from crewai import Task

# create a class that will factory the Research Task and the Habitat Task
class TurtleTasks():
    def research_task(self, 
                      agent, 
                      breed,
                      age):
        return Task(
            description=dedent(f"""\
                Conduct a comprehensive search of the turtle breed and age. Gather 
                information on the habitat, diet, recommended size of tank in gallons, 
                and climate conditions for the turtle to thrive. Accommodate for growth 
                based on the turtles age compared to life expectancy. Compile all the 
                research findings, analysis, and talking points into a concise, comprehensive 
                briefing document for habitat analysis to be performed.

                Turtle Breed: {breed}
                Turtle Age: {age}"""),
            expected_output=dedent("""\
                A comprehensive summary of the findings for the turtle given the breed and age.."""),
            async_execution=False,
            agent=agent
    )

    # Note the Habitat task requires the context from the research task
    def habitat_task(self, agent, context):
        return Task(
                description=dedent(f"""\
                    Examine the comprehensive report for the turtle and create a habitat specification that
                    accomondates the turtle today and provides for growth based on the turtle's breed and age."""),
                expected_output=dedent("""\
                    A specification for the turtle habitat given the breed and age. The specification 
                    should include the following: Recommended Tank Size in gallons, Tank Description, 
                    Substrate , Diet, Temperature and Lighting, and Enrichment.

                    Example Output: 
                         1. Tank Size in Gallons: 80
                         2. Tank Description: Provide an enclosure that is at least 80 gallons to accommodate the size 
                            and activity level of a 15-year-old Diamondback Terrapin. A larger tank or outdoor 
                            pond setup would be even better if space allows.
                         3. Substrate: Use a substrate that is appropriate for both the aquatic and terrestrial areas of the enclosure. 
                            For the aquatic area, you can use aquarium gravel or smooth river rocks. For the terrestrial area, 
                            use a mix of soil, sand, and moss.
                         4. Diet: Diamondback Terrapins are omnivorous and eat a variety of foods, including commercial turtle 
                            pellets, aquatic plants, leafy greens, vegetables, and occasional protein sources like insects or fish.
                         5. Temperature and Lighting: Maintain a temperature gradient in the enclosure with a water temperature of 
                            around 75-80°F (24-27°C) and a cooler area around 70°F (21°C). Provide UVB lighting for at least 10-12 
                            hours a day to help with calcium metabolism and overall health.
                         6. Enrichment: Provide hiding spots, aquatic plants, and objects for exploration to create a stimulating environment. 
                            Diamondback Terrapins enjoy exploring their environment and benefit from enrichment activities.\n\n"""),
                agent=agent,
                context=context
            )
