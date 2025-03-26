names = ["Josh", "Kirsty", "Euan", "Micheal"]
longestname = len(names[0])
pos = 0
for index in range(1, len(names)):
    if len(names[index]) > longestname:
        longestname = len(names[index])
        pos = index
print(names[pos], "Has the most characters in his name with:", longestname, "characters")