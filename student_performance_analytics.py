"""
Student Performance Analytics System
Python with AI project

Run:
    pip install pandas numpy
    python student_performance_analytics.py

This single-file version includes sample student data, so it can be uploaded
directly to GitHub as one Python file.
"""

import pandas as pd
import numpy as np
from io import StringIO

CSV_DATA = """Student_ID,Name,Department,Python,Mathematics,AI,Data Analysis,Attendance
STU001,Aarav Sharma,ECE,88,76,91,85,94
STU002,Diya Joshi,CSE,92,89,95,90,97
STU003,Kabir Mehta,ECE,67,72,70,65,82
STU004,Ananya Rawat,IT,81,84,79,88,91
STU005,Vivaan Singh,ECE,45,53,49,58,76
STU006,Ishita Pant,CSE,96,93,98,95,99
STU007,Reyansh Bisht,IT,74,69,77,72,87
STU008,Saanvi Kapoor,ECE,59,62,55,64,80
STU009,Advik Verma,CSE,38,61,52,47,68
STU010,Myra Negi,IT,85,91,87,83,95
STU011,Arjun Karki,ECE,71,74,68,76,84
STU012,Aadhya Bhandari,CSE,63,58,66,61,78
STU013,Krish Tiwari,IT,90,86,92,89,93
STU014,Pari Chandra,ECE,54,47,60,52,72
STU015,Atharv Dutt,CSE,77,81,73,79,89
STU016,Navya Saxena,IT,42,39,55,48,70
STU017,Rudra Padiyar,ECE,68,65,71,70,85
STU018,Meera Sethi,CSE,87,82,84,91,96
STU019,Yash Malhotra,IT,50,56,46,59,74
STU020,Tara Mishra,ECE,79,75,82,78,90
"""

SUBJECTS = ["Python", "Mathematics", "AI", "Data Analysis"]


def calculate_grade(average):
    """Assign a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def analyze_students(df):
    """Calculate totals, averages, grades, and pass/fail status."""
    df = df.copy()
    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    df["Average_Marks"] = np.round(df[SUBJECTS].mean(axis=1), 2)
    df["Grade"] = df["Average_Marks"].apply(calculate_grade)
    # Passing rule: at least 40 marks in every subject.
    df["Result"] = np.where((df[SUBJECTS] >= 40).all(axis=1), "Pass", "Fail")
    return df


def show_class_summary(df):
    """Display overall class statistics."""
    print("\nCLASS SUMMARY")
    print("-" * 60)
    print(f"Number of students : {len(df)}")
    print(f"Class average      : {df['Average_Marks'].mean():.2f}")
    print(f"Highest average    : {df['Average_Marks'].max():.2f}")
    print(f"Lowest average     : {df['Average_Marks'].min():.2f}")
    print(f"Students passed    : {(df['Result'] == 'Pass').sum()}")
    print(f"Students failed    : {(df['Result'] == 'Fail').sum()}")
    print(f"Pass percentage    : {df['Result'].eq('Pass').mean() * 100:.2f}%")
    print(f"Mean attendance    : {df['Attendance'].mean():.2f}%")
    top = df.loc[df["Average_Marks"].idxmax()]
    low = df.loc[df["Average_Marks"].idxmin()]
    print(f"Top student        : {top['Name']} ({top['Average_Marks']:.2f})")
    print(f"Lowest student     : {low['Name']} ({low['Average_Marks']:.2f})")


def show_subject_analysis(df):
    """Display subject-wise average, highest, and lowest marks."""
    print("\nSUBJECT-WISE ANALYSIS")
    print("-" * 60)
    for subject in SUBJECTS:
        marks = df[subject].to_numpy()
        print(
            f"{subject:16} Average: {np.mean(marks):6.2f} | "
            f"Highest: {np.max(marks):3.0f} | Lowest: {np.min(marks):3.0f}"
        )
    means = df[SUBJECTS].mean()
    print(f"Best average subject: {means.idxmax()} ({means.max():.2f})")
    print(f"Lowest average subject: {means.idxmin()} ({means.min():.2f})")


def main():
    df = pd.read_csv(StringIO(CSV_DATA))
    df = analyze_students(df)

    print("=" * 65)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)
    columns = [
        "Student_ID", "Name", "Department", *SUBJECTS,
        "Total_Marks", "Average_Marks", "Grade", "Result", "Attendance"
    ]
    print("\nSTUDENT-WISE PERFORMANCE")
    print(df[columns].to_string(index=False, formatters={
        "Average_Marks": "{:.2f}".format
    }))

    show_class_summary(df)
    show_subject_analysis(df)

    print("\nTOP 5 PERFORMERS")
    print("-" * 60)
    for rank, (_, student) in enumerate(
        df.nlargest(5, "Average_Marks").iterrows(), start=1
    ):
        print(
            f"{rank}. {student['Name']} - Average: "
            f"{student['Average_Marks']:.2f}, Grade: {student['Grade']}"
        )

    output_file = "student_analysis_results.csv"
    df.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file}")
    print("\nNote: The included student records are fictional sample data.")


if __name__ == "__main__":
    main()
