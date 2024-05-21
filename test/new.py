import csv
import pandas as pd
from urllib.request import urlopen

def process_file(filepath):
    my_list = []
    with open('test.txt') as f:
        lines = f.readlines()
    for line in lines:
        my_list.append(line.strip())
    # filepath = b,

def transfer_data(self, criteria, destination_file):
    filtered_data = self.data[self.data[criteria[0]] == criteria[1]]
    filtered_data.to_csv(destination_file, index=False)

def analyze_data(data):
    averages = data.mean()
    outstanding_students = data[data['Score'] >= 90] 
    return {"averages": averages.to_dict(), "outstanding_students": outstanding_students.to_dict()}
  
def generate_summary(analysis_results):
  summary = f"""
  **Assessment Summary**

  * Average Scores: {analysis_results['averages']}
  * Outstanding Students (>90%): {len(analysis_results['outstanding_students'])}
  * (Optional: Include insights on trends or outliers)

  This report highlights the key findings from the recent assessment activities. The average scores provide a general overview of student performance, while identifying outstanding students allows for further recognition. 
  """
  return summary


filepath = "all_semester.csv"
data = process_file(filepath)
analysis_results = analyze_data(data)
summary = generate_summary(analysis_results)

print(summary)


