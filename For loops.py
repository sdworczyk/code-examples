
row = 5
# outer loop defining how many rows I need in the loop
for x in range(1, row + 1):
    # inner loop determines that in each loop there will be one additional print in the column
    for y in range(1, x + 1):
        print("*", end="")
    print()