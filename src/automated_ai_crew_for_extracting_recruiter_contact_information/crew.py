from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class AutomatedAiCrewForExtractingRecruiterContactInformationCrew():
    """AutomatedAiCrewForExtractingRecruiterContactInformation crew"""

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['search_agent'],
            tools=[SerperDevTool()],
        )

    @agent
    def scrape_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['scrape_agent'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @agent
    def validation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['validation_agent'],
            
        )

    @agent
    def compilation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['compilation_agent'],
            
        )


    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_task'],
            tools=[SerperDevTool()],
        )

    @task
    def scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_task'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @task
    def validate_task(self) -> Task:
        return Task(
            config=self.tasks_config['validate_task'],
            
        )

    @task
    def compile_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_task'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomatedAiCrewForExtractingRecruiterContactInformation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )



###NEWWWWW


# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
# from dotenv import load_dotenv

# load_dotenv()


# @CrewBase
# class AutomatedAiCrewForExtractingRecruiterContactInformationCrew():
#     """AutomatedAiCrewForExtractingRecruiterContactInformation crew"""

#     @agent
#     def search_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['search_agent'],
#             tools=[SerperDevTool()],
#         )

#     @agent
#     def scrape_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['scrape_agent'],
#             tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
#         )

#     @agent
#     def validation_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['validation_agent'],
#         )

#     @agent
#     def compilation_agent(self) -> Agent:
#         return Agent(
#             config=self.agents_config['compilation_agent'],
#         )

#     @task
#     def search_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['search_task'],
#             tools=[SerperDevTool()],
#         )

#     @task
#     def scrape_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['scrape_task'],
#             tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
#         )

#     @task
#     def validate_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['validate_task'],
#         )

#     @task
#     def compile_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['compile_task'],
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the AutomatedAiCrewForExtractingRecruiterContactInformation crew"""
#         return Crew(
#             agents=self.agents,  # Automatically created by the @agent decorator
#             tasks=self.tasks,    # Automatically created by the @task decorator
#             process=Process.sequential,
#             verbose=True,
#             # Make sure crew returns structured data that can be saved to CSV
#             output_parser=lambda output: parse_crew_output(output),
#         )

# def parse_crew_output(output):
#     """
#     Parse the crew output to ensure it's in a structured format.
#     This could be extended based on your specific output format.
#     """
#     # If output is already a dict, return it
#     if isinstance(output, dict):
#         return output
    
#     # If it's a string, try to extract structured data
#     # This is a placeholder - modify to match your actual output format
#     try:
#         # Extract data based on your expected format
#         # For example, parsing a structured text output into a dictionary
#         result = {}
#         lines = output.strip().split('\n')
#         for line in lines:
#             if ':' in line:
#                 key, value = line.split(':', 1)
#                 result[key.strip()] = value.strip()
#         return result
#     except Exception as e:
#         # Fallback to returning the whole output as a single field
#         return {"raw_output": output}