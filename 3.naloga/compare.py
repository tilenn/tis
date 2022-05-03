f1 = open("out.txt")
f2 = open("test.txt")

for line1, line2 in zip(f1, f2):
    print(line1, "and", line2)
    if line1 != line2:
        print("Different")
        break
