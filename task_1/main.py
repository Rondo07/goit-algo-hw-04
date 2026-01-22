from pathlib import Path

def total_salary(path):   #Create function 
    salary_file_path = Path(path)
    total = 0
    average = 0
    count = 0
    
    try:
        with open(salary_file_path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    line = line.split(',')
                    salary_part = line[1].strip()
                    salary = int(salary_part)
                except(IndexError, ValueError):
                    continue
                total +=salary
                count +=1
        if count > 0:
            average = int(total / count)
        else:
            average = 0
    except FileNotFoundError:
        print("File not found")    
   
    return total, average

total, average = total_salary("devs.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")