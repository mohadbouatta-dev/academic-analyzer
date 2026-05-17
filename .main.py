import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Sample Data Generation (If no file exists)
def generate_sample_data():
    data = {
        'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'Name': ['Ahmed', 'Sara', 'Mohamed', 'Fatima', 'Amine', 'Lina', 'Youssef', 'Rania', 'Ali', 'Aisha'],
        'Math_Score': [85, 92, 58, 76, 45, 88, 95, 62, 30, 79],
        'Science_Score': [78, 95, 60, 82, 50, 91, 89, 65, 40, 85],
        'English_Score': [90, 88, 70, 80, 55, 85, 92, 60, 50, 88]
    }
    df = pd.DataFrame(data)
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
    
    # Determine Pass/Fail status (Passing average is 60)
    df['Status'] = df['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
    
    # Save processed data to a new CSV
    df.to_csv('academic_report_summary.csv', index=False)
    print("[✓] Analysis complete. Summary saved to 'academic_report_summary.csv'.")
    return df

# 3. Data Visualization
def generate_insights_chart(df):
    plt.figure(figsize=(10, 5))
    
    # Plotting Student Averages
    plt.bar(df['Name'], df['Average'], color='skyblue', edgecolor='black')
    plt.axhline(y=60, color='red', linestyle='--', label='Passing Mark (60)')
    
    plt.title('Student Average Performance Analysis', fontsize=14, fontweight='bold')
    plt.xlabel('Student Name', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the chart as an image
    plt.savefig('performance_chart.png', dpi=300)
    print("[✓] Analytics visualization chart saved as 'performance_chart.png'.")

# Main Execution
if __name__ == "__main__":
    print("--- Starting Academic Data Analyzer ---")
    report_df = analyze_data()
    generate_insights_chart(report_df)
    print("--- Process Finished Successfully ---")
  
