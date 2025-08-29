with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.strip().upper() + "\n")

print("Processing done")
