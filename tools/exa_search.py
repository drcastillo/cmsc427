import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchTool:
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		return ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=5)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		return ExaSearchTool._exa().find_similar(url, num_results=5)

	@tool
	def get_contents(ids: list):
		"""Get the contents of a webpage.
		The ids must be passed in as a list, a list of ids returned from `search`.
		"""
		print("Ids: \n")
		print(ids)
		contents = str(ExaSearchTool._exa().get_contents(ids))
		print(contents)
		contents = contents.split("URL:")
		contents = [content[:1000] for content in contents]
		return "\n\n".join(contents)

    # returns an array of ExSearch tools that the agents can use 
	def tools():
		return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]

	def _exa():
		return Exa(api_key=os.environ["EXA_API_KEY"])