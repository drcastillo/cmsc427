<h1>CMSC427</h1>
<h2>Simple Agent example that leverages LLMs and Agents</h2>

<p>In the Turtle example in CMSC427 we depend on the logic of Genetic Algorithms to recommend the size of the turtle tank, given the breed and age of the turtle. 

This example demonstrates an alternative approch that leverages LLMs and Agent to effectively recommend a habitat specification for a given turtle given the breed and age. 

We leverage an open source Agent framework called CrewAI to create the Agents, Tasks, Tools, and Crew to provide a comprehensive habitat specification for a specific breed and age of turtle.

This example can be generalized for any reptile or animal but is intentionally focused on turtles so that it aligns with the Genetic Algorithm Agent assignment in CMSC427.</p>

<strong>Step 1: Setting up the environment</strong>

<p>Download MiniConda 32/64 bit version for Windows or Mac or Linux. Choose the appropriate installer for your operating system and architecture (Windows, macOS, or Linux, 64-bit or 32-bit) </p>

<strong>Step 2: Clone this repository. Find a location on your computer and enter the following:</strong>

`git clone https://github.com/drcastillo/cmsc427.git`

<strong>Step 3: Configuring the environment for running CrewAI Agents</strong>

Once the environment is cloned change directories to the "cmsc427" directory and type in the following:

`conda env create -f environment.yml`

<p>This will automatically build the virtual conda environment called <strong>cmsc427</strong> which is configured to run CrewAI.</p>

<strong>Step 4: Activate the cmsc427 environment by typing in the following:</strong>

`conda activate cmsc427`

<p>You should see something like the following appear in the command line.</p>

`(cmsc427)`




