# Student Performance Analytics System

**Python with AI Course Project**  
**Technologies:** Python, Pandas, NumPy

## Overview
Student Performance Analytics System reads student records from a CSV file and analyzes subject marks and attendance. It reports totals, averages, grades, pass/fail counts, class statistics, subject-wise performance, and the top-performing students.

## Features
- Loads student data into a Pandas DataFrame.
- Uses NumPy for numerical calculations.
- Calculates total and average marks for every student.
- Assigns grades using clear grading rules.
- Identifies pass/fail students.
- Reports class average, highest/lowest average, pass percentage, and average attendance.
- Compares subjects and lists the top five performers.
- Exports the full analysis to `student_analysis_results.csv`.

## Project files
- `main.py` — main program and final report.
- `functions.py` — reusable calculations and analysis functions.
- `students.csv` — sample dataset containing 20 student records.
- `Project_Documentation.md` — project report.
- `requirements.txt` — required Python libraries.

## Requirements
- Python 3.9 or newer recommended.
- Pandas
- NumPy

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python main.py
   ```
5. The program prints the analysis and creates `student_analysis_results.csv`.

## Grading and passing rules
Grades are based on the student's average across the four subjects:
- A+: 90 and above
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: below 50

A student passes only if they score at least 40 in **each** subject. These are project-defined rules and can be changed if the trainer specifies different criteria.

## Dataset
The included CSV has 20 illustrative sample records. Names and scores are fictional and intended for demonstrating data analysis.

## Output
After a successful run, the program creates `student_analysis_results.csv`, which contains the original fields plus total marks, average marks, grade, and result.

## Author
Student Name: [Enter your name]  
Course: Python with AI
