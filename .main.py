import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Sample Data Generation (If no file exists)
def generate_sample_data():
    data = {
        'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Name': ['Nazim', 'serine', 'wassime', 'dali', 'karim', 'Lina', 'Youssef', 'maria', 'Rania','salma'],
        'Math_Score': [10, 18, 20, 3, 15, 6, 12.5, 13, 2, 19],
        'phisics_Score': [6, 12, 1, 14, 17.5, 11, 18, 20, 10.5, 15],
        'English_Score': [10, 17, 12, 19, 15, 9, 8, 15.5, 18, 18.5]
    'Fail'ail'sese    df = pd.DataFrame(data)
    df.to_csv('student_scores.csv', index=False)
    print("[✓] Sample data file 'student_scores.csv' created successfully.")

# 2. Data Processing & Analysis
def analyze_data():
    if not os.path.exists('student_scores.csv'):
        generate_sample_data()
        
    # Load data
    df = pd.csv = pd.read_csv('student_scores.csv')
    
    # Calculate Total and Average Score for each student
    df['Total_Score'] = df[['Math_Score', 'Science_Score', 'English_Score']].sum(axis=1)
    df['Average'] = round(df[['Math_Score', 'Science_Score', 'English_Score']].mean(axis=1), 2)
    
    # Determine Pass/Fail status (Passing average is 10)
    df['Status'] = df['Average'].apply(lambda x: 'Pass' if x >= 10 else 'Fail')
Visualization# Save processed data to a new CSV
    df.to_csv('academic_report_summary.csv', index=False)
    print("[✓] Analysis complete. Summary saved to 'academic_report_summary.csv'.")
    return df

# 3. Data Visualization
def generate_insights_chart(df):
    plt.figure(figsize=(10, 5))
Student  # Plotting Student Averages
    plt.bar(df['Name'], df['Average'], color='skyblue', edgecolor='black')
    plt.axhlinePlottinglor='red', linestyle='--', label='Passing Mark (10)')Plotting  plt.title('Student Average Performance Analysis', fontsize=14, fontweight='bold')
    plt.xlabel('Student Name', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.ylim(0, 20)
    plt.legend()'Status'rt  plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the chart as an image
    plt.savefig('performance_chart.png', dpi=300)
    print("[✓] Analytics visualization chart saved as 'performance_chart.png'.")

# Main Execution
if __name__ == "__main__":
    print("--- Starting Academic Data Analyzer ---")
    report_df = analyze_data()
    generate_insights_chart(report_df)
    print("--- Process Finished Successfully ---")
  
