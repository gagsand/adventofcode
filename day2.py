# Day 2 - Red-Nosed Reports

# import the file that we are using which contains all data
with open('list3.txt', 'r') as file:
    # map the data so it is readable
    data = [list(map(int, line.split())) for line in file]
    # now we are going to analyze the data

    # initalize the counter for safe rows
    safe_count = 0

    # create a for loop so that assess all the levels within all the reports of the data
    for report in data:

        # the next three lines are to define variables that are acceptable. these variables determine whether the report is safe or unsafe
        decreasing = all(report[i] > report[i + 1]
                         for i in range(len(report)-1))
        increasing = all(report[i] < report[i + 1]
                         for i in range(len(report)-1))
        valid_difference = all(
            1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

        valid_change = decreasing or increasing

        # if valid_change:
        #     safe_count += 1

        # if valid_difference:
        #     safe_count += 1

        if valid_change and valid_difference:
            safe_count += 1

    print(safe_count)
