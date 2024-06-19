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

<strong>Step 5: Setting up the .env file</strong>

<p>You are now ready to run the agents but before you do, you must setup the <strong>.env</strong> file to hold your access tokens for OpenAI and ExaSearch. Create a free account on OpenAI (openai.com) and ExaSearch (exa.ai) and acquire API Keys from both of these services. Although the API keys are free, they will limit you to the number of calls you can make per month and also impact your priority execution. Once you have the API Key open the file called <strong>example.env</strong> and enter your API Keys into the appropriate values. You should see something like this:</p>

`OPENAI_API_KEY="your OpenAI API key here"`
`EXA_API_KEY="your Exa API key here"`

<p>Save the file as <strong>.env</strong> so that it is picked up by the agent framework code.</p>

<strong>Step 6: Test the Program</strong>



