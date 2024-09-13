import math

import pandas as pd

names = list()
prices = list()

done = False
while not done:
    name = input('Please enter a name, or "stop" to continue: ')
    if "stop" in name:
        done = True
        continue

    names.append(name)

if not len(names):
    print("Sorry, no names were given.")
    exit(0)

print("\nIndexed list of names:")
for i in range(len(names)):
    print(
        i + 1,
        " " * (math.floor(math.log(len(names), 10)) - math.floor(math.log(i + 1, 10))),
        names[i],
    )

print("")

done = False
while not done:
    data = input(
        'Please enter a price, followed by the indices of people who will split it evenly (separate values with spaces, or say "stop" to continue): '
    )
    if "stop" in data:
        done = True
        continue

    data = data.split()
    if len(data) < 2:
        print("Please try again.")
        continue

    item = (float(data[0]), list())
    for i in data[1:]:
        if int(i) > len(names) or int(i) < 1:
            print("Error: invalid index")
            break
        item[1].append(int(i) - 1)
    if len(item[1]) < len(data) - 1:
        continue
    prices.append(item)

largest = max([i[0] for i in prices])
space_num = math.floor(math.log(largest, 10))

table = [
    [
        (item[0] / len(item[1]) * item[1].count(i) if i in item[1] else "")
        for i in range(len(names))
    ]
    for item in prices
]
row_indices = [item[0] for item in prices]
subtotal = sum(row_indices)

table.append(["" for i in names])
row_indices.append("")

table.append(
    [
        sum([(row[i] if row[i] != "" else 0) for row in table[:-1]])
        for i in range(len(names))
    ]
)
row_indices.append(subtotal)

total = float(input("How much is the total (after tax, tip, etc)? "))

table.append([i * total / subtotal for i in table[-1]])
row_indices.append(total)

for j in range(len(row_indices)):
    if row_indices[j] == "":
        continue
    row_indices[j] = round(row_indices[j], 2)
    for i in range(len(names)):
        if table[j][i] != "":
            table[j][i] = round(table[j][i], 2)

print("")
print(pd.DataFrame(table, columns=names, index=row_indices))
