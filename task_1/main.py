# Read a text file with salaries in the format: "Name,SALARY"
# Calculate total salary and average salary.
# Handle file errors (missing file) and skips corrupted lines.

from pathlib import Path

def total_salary(path):   # Create function
    salary_file_path = Path(path)   # Convert input path (string) to Path object
    total = 0
    average = 0
    count = 0
    
    try:
        with open(salary_file_path, encoding="utf-8") as file:   # Try to open the file
            for line in file:
                line = line.strip()   # Remove leading and trailing whitespace
                if not line:   # Skip empty lines
                    continue
                try:
                    line = line.split(',')   # Split the line by comma
                    salary_part = line[1].strip()   # Remove leading and trailing whitespace
                    salary = float(salary_part)
                except(IndexError, ValueError):   # Manage an exception, skip wrong lines
                    continue
                total +=salary
                count +=1
        if count > 0:   # Avoid division by zero
            average = total / count
        else:
            average = 0
    except FileNotFoundError:   # Manage FileNotFoundError exception, print message
        print("File not found")    
   
    return total, average

total, average = total_salary("devs.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")