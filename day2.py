# Day 2 - Red-Nosed Reports

# import the file that we are using which contains all data
with open('list3.txt', 'r') as file:
    # map the data so it is readable
    data = [list(map(int, line.split())) for line in file]
    # now we are going to analyze the data

    # initalize the counter for safe rows
    safe_count = 0

    # create a for loop so that assess all the levels within all the reports of the data

    def is_safe(report):
        increasing = all(report[i] <= report[i + 1] and 1 <= abs(report[i] - report[i+1]) <= 3
                         for i in range(len(report)-1))
        decreasing = all(report[i] >= report[i + 1] and 1 <= abs(report[i] - report[i+1]) <= 3
                         for i in range(len(report)-1))
        return increasing or decreasing

    def is_safe_with_exception(report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                return True
        return False

    for report in data:
        if is_safe(report) or is_safe_with_exception(report):
            safe_count += 1

    print(safe_count)
