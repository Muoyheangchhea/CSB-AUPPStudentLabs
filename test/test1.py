
import csv
from types import new_class
import pandas as pd
from urllib.request import urlopen
from datetime import datetime
import os

class SchoolAssessmentAnalyzer:
    def init(self):
        self.data = pd.DataFrame()
        self.web_data = ""

    def process_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"The file {file_path} does not exist.")
            return False
        
        if file_path.endswith('all_semester.csv'):
            self.data = pd.read_csv(file_path)
            # Calculate the 'Average' column after reading the CSV file
            self.data['Average'] = self.data[['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']].mean(axis=1)
        else:
            print("Wrong file format.")
            return False
        return True

    def fetch_web_data(self, url):
        # Simulating fetching web data
        self.web_data = "95% of students accessed assessment resources online."

    def analyze_content(self):
        if self.data.empty:
            print("No data to analyze.")
            return {}

        overall_performance = self._calculate_overall_performance()
        subject_analysis = self._subject_wise_analysis()
        notable_observations = self._notable_observations()
        web_data_insights = self._web_data_insights()
        recommendations = self._generate_recommendations()

        report = {
            'overall_performance': overall_performance,
            'subject_analysis': subject_analysis,
            'notable_observations': notable_observations,
            'web_data_insights': web_data_insights,
            'recommendations': recommendations
        }
        return report
    def analyze_student(self, student_name):
        if self.data.empty:
            print("No data to analyze.")
            return {}

        if student_name not in self.data['Name'].values:
            print(f"No data found for student: {student_name}")
            return {}

        student_data = self.data[self.data['Name'] == student_name]
        student_performance = self._calculate_student_performance(student_data)
        student_subject_analysis = self._student_subject_wise_analysis(student_data)
        student_web_data_insights = self.student_web_data_insights()
        overall_performance = self.calculate_overall_performance()
        top_class = self.determine_top_class()
        notable_observations = self.student_notable_observations()
        recommendations = self.student_generate_recommendations()

        student_report = {
            'student_performance': student_performance,
            'student_subject_analysis': student_subject_analysis,
            'student_web_data_insights': student_web_data_insights,
            'overall_performance': overall_performance,
            'top_class': top_class,
            'student_notable_observations': notable_observations,
            'recommendations': recommendations
        }
        return student_report

    def generate_student_summary(self, student_report, student_name):
        if not student_report:
            print("No report to generate summary from.")
            return
        
        summary = f"""
School Assessment Summary Report for {student_name}:

1. Overall Performance:
   - Average score: {student_report['student_performance']['average_score']}
   - Top-performing class: {student_report['top_class']}

2. Subject-wise Analysis:
   - INF 652: {student_report['student_subject_analysis']['INF 652']}
   - CSC 241: {student_report['student_subject_analysis']['CSC 241']}
   - ITM 101: {student_report['student_subject_analysis']['ITM 101']}
   - ITM 371: {student_report['student_subject_analysis']['ITM 371']}
   - COSC 201: {student_report['student_subject_analysis']['COSC 201']}

3. Notable Observations:
   - {student_report['student_notable_observations']}

4. Web Data Insights:
   - {student_report['student_web_data_insights']}

5. Recommendations:
   - {student_report['recommendations']}

Report generated on: {datetime.now().date()}
"""
        print(summary)

def _calculate_student_performance(self, student_data):
        avg_score = student_data[['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']].mean(axis=1).iloc[0]
        top_class = self.data.groupby('Semester')['Average'].mean().idxmax()
        return {'average_score': round(avg_score, 2), 'top_class': top_class}

def _student_subject_wise_analysis(self, student_data):
        analysis = {}
        for subject in ['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']:
            score = student_data[subject].iloc[0]
            analysis[subject] = f"Score: {score}"
        return analysis
def _subject_wise_analysis(self):
        analysis = {}
        for subject in ['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']:
            avg_improvement = self.data.groupby('Semester')[subject].mean().pct_change().iloc[-1] * 100
            analysis[subject] = f"Improved by {avg_improvement:.2f}%" if not pd.isna(avg_improvement) else "No change"
        return analysis

def student_notable_observations(self):
        notable_students = self.data.loc[self.data['Average'] > 90, 'Name'].tolist()
        return f"Students with average more than 90% of total scores: {', '.join(notable_students)}"

def student_web_data_insights(self):
        return self.web_data

def student_generate_recommendations(self):
        underperforming_students = self.data.loc[self.data['Average'] < 85, 'Name'].tolist()
        if not underperforming_students:
            return "No underperforming students."
        else:
            return f"Consider additional support for students: {', '.join(underperforming_students)}"

def calculate_overall_performance(self):
        # Placeholder for actual implementation
        return {'average_score': self.data['Average'].mean(), 'top_class': 'Summer'}

def determine_top_class(self):
        # Placeholder for actual implementation
        return 'Summer'

# Example usage
if __name__ == "__main__":
    analyzer = SchoolAssessmentAnalyzer()
    file_path = 'all_semester.csv'
    
    if analyzer.process_file(file_path):
        student_name = input("Enter the name of the student: ")
        analyzer.fetch_web_data('http://aupp.com/school-assessment')
        student_report = analyzer.analyze_student(student_name)
        analyzer.generate_student_summary(student_report, student_name)