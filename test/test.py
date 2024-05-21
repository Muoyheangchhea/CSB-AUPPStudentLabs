import csv
import pandas as pd
from urllib.request import urlopen
from datetime import datetime
import os

class SchoolAssessmentAnalyzer:
    def init(self):
        self.data = pd.DataFrame()

    def process_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"The file {file_path} does not exist.")
            return False
        
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path)
        else:
            print("Unsupported file format.")
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

    def generate_summary(self, report):
        if not report:
            print("No report to generate summary from.")
            return

        summary = f"""
School Assessment Summary Report:

1. Overall Performance of Students:
   - Average score: {report['overall_performance']['average_score']}
   - Top-performing class: {report['overall_performance']['top_class']}

2. Subject-wise Analysis:
   - INF 652: {report['subject_analysis']['INF 652']}
   - CSC 241: {report['subject_analysis']['CSC 241']}
   - ITM 101: {report['subject_analysis']['ITM 101']}
   - ITM 371: {report['subject_analysis']['ITM 371']}
   - COSC 201: {report['subject_analysis']['COSC 201']}

3. Notable Observations:
   - {report['notable_observations']}

4. Web Data Insights:
   - {report['web_data_insights']}

5. Recommendations:
   - {report['recommendations']}

Report generated on: {datetime.now().date()}
"""
        print(summary)

    def _calculate_overall_performance(self):
        self.data['Average'] = self.data[['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']].mean(axis=1)
        top_class = self.data.groupby('Semester')['Average'].mean().idxmax()
        avg_score = self.data['Average'].mean()
        return {'average_score': round(avg_score, 2), 'top_class': top_class}

    def _subject_wise_analysis(self):
        analysis = {}
        for subject in ['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']:
            avg_improvement = self.data.groupby('Semester')[subject].mean().pct_change().iloc[-1] * 100
            analysis[subject] = f"Improved by {avg_improvement:.2f}%" if not pd.isna(avg_improvement) else "No change"
        return analysis

    def _notable_observations(self):
        notable_students = self.data.loc[self.data['Average'] > 90, 'Name'].tolist()
        return f"Students with average > 90: {', '.join(notable_students)}"

    def _web_data_insights(self):
        return self.web_data

    def _generate_recommendations(self):
        underperforming_students = self.data.loc[self.data['Average'] < 85, 'Name'].tolist()
        return f"Consider additional support for students: {', '.join(underperforming_students)}"

# Example usage
if __name__ == "__main__":
    analyzer = SchoolAssessmentAnalyzer()
    file_path = 'all_semester.csv'
    
    if analyzer.process_file(file_path):
        analyzer.fetch_web_data('http://example.com/school-assessment')
        report = analyzer.analyze_content()
        analyzer.generate_summary(report)