
Marks = [20, 30, 35, 55, 70, 80, 90]

def calculate_mean(marks):
    return sum(marks) / len(marks)
def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        median = sorted_marks[mid]
    
    return median
mean = calculate_mean(Marks)
median = calculate_median(Marks)

print(f"Mean: {mean}")
print(f"Median: {median}")