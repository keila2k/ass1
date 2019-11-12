# p1.1
original_list = [0, 1, 2, 3]
odds = [x for x in range(10) if x % 2 != 0]
output_list = []
for item in original_list:
    output_list.append(odds[item])
print(output_list)

# p1.2
original_list = [3, 5, 9, 8]


def mod3(n):
    return n % 3 == 0


print(map(mod3, original_list))
