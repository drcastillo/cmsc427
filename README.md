<h1>CMSC427</h1>
<h2>Simple Agent example that leverages LLMs and Agents</h2>

<p>In the Turtle example in CMSC427 we depend on the logic of Genetic Algorithms to recommend the size of the turtle tank, given the breed and age of the turtle. 

This example demonstrates an alternative approch that leverages LLMs and Agent to effectively recommend a habitat specification for a given turtle given the breed and age. 

We leverage an open source Agent framework called CrewAI to create the Agents, Tasks, Tools, and Crew to provide a comprehensive habitat specification for a specific breed and age of turtle.

This example can be generalized for any reptile or animal but is intentionally focused on turtles so that it aligns with the Genetic Algorithm Agent assignment in CMSC427.</p>

<strong>Step 1: Setting up the environment</strong>

<p>Download MiniConda 32/64 bit version for Windows or Mac or Linux. Choose the appropriate installer for your operating system and architecture (Windows, macOS, or Linux, 64-bit or 32-bit) </p>

<strong>Step 2: Once you have Miniconda installed clone this repository. Find a location on your computer and enter the following:</strong>

`git clone https://github.com/drcastillo/cmsc427.git`

<strong>Step 3: Configuring the environment for running CrewAI Agents</strong>

Once the environment is cloned change directories to the "cmsc427" directory and type in the following:

`conda env create -f environment.yml`

<p>This will automatically build the virtual conda environment called <strong>cmsc427</strong> which is configured to run CrewAI.</p>

<strong>Step 4: Activate the cmsc427 environment by typing in the following:</strong>

`conda activate cmsc427`

<p>You should see something like the following appear in the command line.</p>

`(cmsc427)`

<strong>Step 5: Creating your .env file</strong>

<p>You are now ready to run the agents but before you do, you must create the <strong>.env</strong> file to hold your access tokens for OpenAI and ExaSearch. Setup a free account on OpenAI (openai.com) and ExaSearch (exa.ai) and acquire API Keys from both of these services. Although the API keys are free, they will limit he number of API calls you can make per month and also impact your priority execution. Once you have the API Key create a file called <strong>.env</strong> and enter your API Keys into the appropriate values. You should see something like this:</p>

`OPENAI_API_KEY="your OpenAI API key here"`<br>
`EXA_API_KEY="your Exa API key here"`

<p>Save the file as <strong>.env</strong> so that it is picked up by the agent framework code.</p>

<strong>Step 6: Test the Program by typing in the following:</strong>

`(cmsc427): python main.py`<br>

<p>You should see a user prompt asking for the breed of the turtle which you will type in and press return. It will then prompt you for the age of the turtle which you will type in an integer number. The process will resemble the following:</p>

`## Welcome to the Turtle Habitat Information System ##`<br>
`What is the name of the Turtle breed? Chose one of 'Box Turtle', 'Eastern Box Turtle', 'Diamondback Turtle', or 'Pennisula Cooter Turtle'`<br>
`Box Turtle`<br>

`What is the age of the Box Turtle?`<br>
`2`<br>

<p>You will then see the something resembling the following text followed by the Agent Chain of Thought Reasoning process. It will finally finish when the Turtle Research Agent hands off it's comprehensive report to the Turtle Habitat Specialist who delivers the Final Habitat Specification. Here is an example of an output run less some of teh Chain of Thought reasoning.</p>

<strong>>Entering new CrewAgentExecutor chain...</strong><br>
<p>Thought: To create a habitat specification for a 2-year-old Box Turtle, I need detailed information regarding its habitat requirements, diet, tank size, and climate conditions. I will ask the Turtle Researcher for the comprehensive summary of the findings for the care of the 2-year-old Box Turtle....</p><br>
<strong>Finished Chain.</strong><br>
<p>----------------------------------------------------------------------------------</p><br>
<p>Final Turtle Habitat Specification:</p><br>
<p>1. **Tank Size in Gallons:** 40 gallons (minimum for a 2-year-old Box Turtle)</p>
<p>2. **Tank Description:** Provide an indoor enclosure such as a large Rubbermaid tub or a specially built wooden box with opaque sides to prevent the turtle from trying to get through the glass and to reduce stress from outside activities. An outdoor enclosure is highly recommended if you live within the natural range of North American box turtles, which should include access to sunlight, shade, a variety of weeds, and a small pond deep enough for swimming.</p>
<p>3. **Substrate:** Use a substrate that maintains humidity and provides a natural environment. A mix of soil, sand, and coconut coir is ideal for retaining moisture and allowing the turtle to dig.</p>
<p>4. **Diet:** Box turtles are omnivorous and require a varied diet. Provide a mix of animal protein (insects such as crickets and worms, snails, and occasional lean meats) and plant matter (leafy greens, vegetables, and fruits). Avoid iceberg lettuce due to its lack of nutritional value. Supplement their diet with calcium and vitamins to support shell and bone health.</p>
<p>5. **Temperature and Lighting:** Maintain a daytime basking area with a temperature range of 85-90°F and allow nighttime temperatures to drop to 70-75°F. Outdoor setups should offer both sunny and shaded areas for natural temperature regulation. Use a UVB light source to ensure proper calcium metabolism and prevent metabolic bone disease. Provide a day/night cycle with around 12 hours of light and 12 hours of darkness.</p>
<p>6. **Enrichment:** Ensure the enclosure has hiding spots, logs, and plants to create a stimulating environment. Regular misting and a humid hide can help maintain humidity levels between 60-80%.</p><br>
<p>By adhering to these specifications, you can create a suitable and enriching environment for a 2-year-old Box Turtle, promoting its health, growth, and overall well-being.</p><br>
