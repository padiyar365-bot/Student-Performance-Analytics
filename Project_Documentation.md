# Project Documentation: Student Performance Analytics System

## 1. Project Title
Student Performance Analytics System

**Student Name:** [Enter your name]  
**Course:** Python with AI  
**Technologies:** Python, NumPy, Pandas

## 2. Objective
The objective is to build a Python-based system that reads student marks and attendance from a CSV dataset and turns them into an understandable performance report. It helps identify strong and weak performance, pass/fail status, subject averages, and top performers.

## 3. Technologies Used
- Python: program logic, conditions, loops, and functions.
- Pandas: loading the CSV file, organizing records in a DataFrame, and performing analysis.
- NumPy: numerical calculations and pass/fail array conditions.
- CSV: simple storage format for the sample dataset.

## 4. Dataset Description
The project includes 20 illustrative student records. Columns include Student_ID, Name, Department, marks in Python, Mathematics, AI, and Data Analysis, and Attendance. The included names and marks are fictional sample data.

## 5. Implementation
1. `main.py` reads `students.csv` using `pandas.read_csv()`.
2. The program checks that required columns exist and that the dataset is not empty.
3. Functions in `functions.py` calculate each student's total and average marks.
4. A grading function assigns a grade based on the stated average-mark ranges.
5. NumPy-based conditions determine whether a student has scored at least 40 in every subject.
6. Pandas and NumPy are used to calculate class statistics and subject-wise averages, maximums, and minimums.
7. The top five students are listed in descending order of average marks.
8. The enriched DataFrame is saved to `student_analysis_results.csv`.

## 6. Key Features
- Student-wise totals and averages.
- Grade and pass/fail classification.
- Highest and lowest student averages.
- Class average and pass percentage.
- Subject-wise performance comparison.
- Top five performers.
- CSV export of analyzed results.

## 7. Output / Screenshots
Run `python main.py` and take a screenshot of the terminal showing the student-wise performance table, class summary, subject-wise analysis, and top performers. Add the screenshot to the repository if requested by the trainer.

## 8. Final Outcome
The project demonstrates how Python, Pandas, and NumPy can be used to organize a dataset and calculate useful academic performance indicators. It generates a readable report and an output CSV file.

## 9. Challenges & Learning
This project provides practice with CSV reading, DataFrames, numerical arrays, reusable functions, loops, conditions, sorting, and exporting analysis results. If an error occurs, check that the CSV file is in the same folder as `main.py` and that the required libraries are installed.

## 10. GitHub Repository
Repository URL: [Paste your GitHub repository link here after uploading]

## Grading and Passing Rules
Grades: A+ (90+), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), F (below 50). A student passes only if every subject mark is at least 40. These rules are defined for this project and may be adjusted to match the trainer's instructions.
