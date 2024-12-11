list1 = [];
list2 = [];
#store those distances in another list
distances = [];

#sort the lists from smallest to biggest

with open('Python/advent of code/advc1.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

# print("list 1:", list1)
# print()
# print("list 2:", list2)

#sort them
list1.sort()
list2.sort()

#compare list ids to get the distance
for num1, num2 in zip(list1, list2):
        distance = abs(num1 - num2)
        distances.append(distance)
        
#sum them up
total_distance = sum(distances)

print("distances:", distances )
print()
print("total distance:", total_distance)


