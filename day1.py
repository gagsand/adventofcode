# Advent Calendar - Chief Historian is no where to be found and we need to find him
# As we check each location, we will mark it on our list with a star
# CH must be in one of the first fifty places, so we should get fifty stars on the list before Santa takes off on December 25th
# Collect stars by solving puzzles. 2 puzzles are available for each day
# Day 1 - the historians found a list in the CH office, but there's no names to the list only location ID
# historians split up into two groups and make two lists, and the lists aren't very similar. Let's reconcile the list

# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
# What is the total distance between your lists?

with open('list1.txt', 'r') as file:
    list1 = [int(line.strip()) for line in file]

with open('list2.txt', 'r') as file:
    list2 = [int(line.strip()) for line in file]

# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]

list1.sort()
list2.sort()

list3 = []
for number in range(len(list1)):
    result = list1[number] - list2[number]
    list3.append(abs(result))

total_result = sum(list3)
print("distance between location IDs: ", total_result)

"Part 2"

list4 = []
for number in range(len(list1)):
    if list1[number] not in list4:
        list4.append(list1[number])

list5 = []
for number2 in list4:
    ID_count = list2.count(number2)
    similarity_score = number2 * ID_count
    list5.append(abs(similarity_score))
print("similarity score of location IDs:", sum(list5))
