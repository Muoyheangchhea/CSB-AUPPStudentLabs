import csv
import pandas as pd
from urllib.request import urlopen
import ssl

class SchoolAssessmentSystem:
  def __init__(self):
    self.data = pd.DataFrame()
    self.summary_data = []

  def process_file(self, file_path):
    if file_path.endswith('.csv'):
      self.data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
      self.data = pd.read_excel(file_path)
    elif file_path.endswith('.txt'):
      with open(file_path, 'r') as file:
        pass

  def transfer_data(self, criteria, source_file, destination_file):
    filtered_data = self.data.query(criteria)
    filtered_data.to_csv(destination_file, index=False)

  def fetch_web_data(self, url):
    context = ssl._create_unverified_context() 
    with urlopen(url, context=context) as response:
      pass

  def _determine_grade(self, avg_score):
    if avg_score > 89:
      return 'A'
    elif avg_score > 79:
        return 'B'
    elif avg_score > 69:
        return 'C'
    elif avg_score > 59:
        return 'D'
    elif avg_score > 49:
        return 'F'
    else:
        return 'F'

  def analyze_content(self, student_name):
    self.summary_data = []
    subject_list = ['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']
    student_data = self.data[self.data['Name'] == student_name]
    if not student_data.empty:
      semester = student_data['Semester'].iloc[0]
      id = student_data['Id'].iloc[0]
      email = student_data['URL'].iloc[0]
      avg_score = student_data[subject_list].mean(axis=1).mean()
      highest_scoring_subject = student_data[subject_list].idxmax(axis=1).iloc[0]
      highest_score = student_data[highest_scoring_subject].iloc[0]
      grade = self._determine_grade(avg_score)
      lowest_class = student_data[subject_list].mean().idxmin() 
      lowest_score = student_data[subject_list].min().min()
      notable_observations = student_data[subject_list].idxmax(axis=1).value_counts().idxmax()
      web_data_time = student_data['Time Spent'].str.extract(r'(\d+)m').astype(int).sum().values[0]
 
      student_summary = {
        'Name': student_data['Name'].iloc[0],
        'id': id,
        'email': email,
        'Semester': semester,
        'Average Score': avg_score,
        'Grade': grade,
        'Highest Score': highest_score,
        'Lowest Score': lowest_score,
        'Lowest Class': lowest_class,
        'Notable Observation': notable_observations,
        'Online Participation': web_data_time
      }
      self.summary_data.append(student_summary)
    else:
      print(f"Student '{student_name}' not found in data.")

  def subject_analysis(self):
    student_data = self.data[self.data['Name'] == student_name]
    subject_list = ['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']
    subject_grade = []
    for subject in subject_list:
      score = student_data[subject].iloc[0]
      sub_grade = self._determine_grade(score)
      subject_grade.append(f"   - {subject}: Score: {score}, Grade: {sub_grade}")
    result = '\n'.join(subject_grade)  
    
    return result
  
  
    

  def generate_summary(self):
    if not self.summary_data:
      return "No student data analyzed yet. Please run analyze_content first."
    summary_report = "\n\nSchool Assessment Summary Report:\n"
    for student in self.summary_data:
        summary_report += f'====================================\n'
        summary_report += f'Student name: {student['Name']}\n'
        summary_report += f'Student ID: {student['id']}\n'
        summary_report += f'Enroll in: {student['Semester']}\n\n'
        summary_report += f"1. Overall Performance:\n"
        summary_report += f"   - Average score: {student['Average Score']:.1f}\n"
        summary_report += f"   - Overall Grade: {student['Grade']}\n"
        summary_report += f"2. Subject-wise Analysis:\n"
        summary_report += f'   + Subject grades:\n{self.subject_analysis()}\n'
        summary_report += f"   * {student['Notable Observation']}: Highest scoring subject of {student['Highest Score']}.\n"
        summary_report += f"   * {student['Lowest Class']}: Lowest scoring subject of {student['Lowest Score']}.\n"
        summary_report += f"3. Notable Observations:\n"
        summary_report += f"   - {student['Notable Observation']} course shows a great accomplishment.\n"
        summary_report += f"4. Web Data Insights:\n"
        summary_report += f'   - Student email: {student['email']}\n'
        summary_report += f"   - Online class participation duration: {student['Online Participation']} minutes\n"
        summary_report += f"5. Recommendations:\n"
        summary_report += f"   - Try to improve your performance in {student['Lowest Class']} course.\n\n"

    summary_report += f"Report generated on: {pd.Timestamp.now().strftime('%Y-%m-%d')}\n"
    return summary_report

analyzer = SchoolAssessmentSystem()
file = 'all_semester.csv'
analyzer.process_file('all_semester.csv')

if __name__ == "__main__":
   student_name = input("Enter student name: ")
   analyzer.analyze_content(student_name)
   summary = analyzer.generate_summary()
   print(summary)
