#!/usr/bin/env python
import sys
from crew import AutomatedAiCrewForExtractingRecruiterContactInformationCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'company_name': 'Microsoft Hyderabad'
#     }
#     AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().kickoff(inputs=inputs)


# run()
# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         'company_name': 'sample_value'
#     }
#     try:
#         AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         'company_name': 'sample_value'
#     }
#     try:
#         AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: main.py <command> [<args>]")
#         sys.exit(1)

#     command = sys.argv[1]
#     if command == "run":
#         run()
#     elif command == "train":
#         train()
#     elif command == "replay":
#         replay()
#     elif command == "test":
#         test()
#     else:
#         print(f"Unknown command: {command}")
#         sys.exit(1)


# def run_for_all_companies(file_path='companies.txt'):
#     """
#     Run the crew for each company listed in the text file.
#     """
#     with open(file_path, 'r') as f:
#         companies = [line.strip() for line in f if line.strip()]

#     for company in companies:
#         print(f"\n🔍 Running crew for: {company}")
#         inputs = {
#             'company_name': company
#         }
#         AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().kickoff(inputs=inputs)

# run_for_all_companies('companies.txt')




# ####NEW

# import sys
# import csv
# from crew import AutomatedAiCrewForExtractingRecruiterContactInformationCrew
# from typing import List, Dict

# def run_for_companies(company_names: List[str], output_file: str = "recruiter_results.csv"):
#     """
#     Run the crew for multiple companies and save results to a CSV file.
    
#     Args:
#         company_names: List of company names to process
#         output_file: Path to the output CSV file
#     """
#     all_results = []
    
#     # Process each company
#     for company_name in company_names:
#         print(f"Processing company: {company_name}")
        
#         inputs = {
#             'company_name': company_name
#         }
        
#         # Run the crew for this company
#         result = AutomatedAiCrewForExtractingRecruiterContactInformationCrew().crew().kickoff(inputs=inputs)
        
#         # Add company name to the result
#         result['company_name'] = company_name
#         all_results.append(result)
        
#         print(f"Completed processing: {company_name}")
    
#     # Save all results to CSV
#     export_results_to_csv(all_results, output_file)
#     print(f"Results saved to {output_file}")

# def export_results_to_csv(results: List[Dict], output_file: str):
#     """
#     Export the results to a CSV file.
    
#     Args:
#         results: List of result dictionaries
#         output_file: Path to the output CSV file
#     """
#     if not results:
#         print("No results to export")
#         return
    
#     # Get all possible headers from all results
#     headers = set()
#     for result in results:
#         headers.update(result.keys())
    
#     headers = sorted(list(headers))
    
#     # Write to CSV
#     with open(output_file, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(results)

# if __name__ == "__main__":
#     # List of 10 companies to process
#     companies = [
#         "Careerfit.ai",
#         "Fluiidmask Studios Pvt. Ltd.",
#         "Flutter Jobs",
#         "Sapphire Software Solutions",
#         "Welspun Transformation Services Limited",
#         "iTechNotion Private Limited",
#         "Microsoft",
        
#     ]
    
#     # You can modify this list or pass it as a command-line argument
#     if len(sys.argv) > 1:
#         companies = sys.argv[1:]
    
#     # Run the crew for all companies
#     run_for_companies(companies)



