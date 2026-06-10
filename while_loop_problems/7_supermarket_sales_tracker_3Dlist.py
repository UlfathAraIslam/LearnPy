# step-1: Create branch names list
branches = ["Shibuya", "Shinjuku"]

# step-2: Create category names list
categories = ["Food", "Drinks", "Snacks"]

# step-3: Create 3D sales list =sales[branch][category][week]

sales = [

    [   # Branch 0 -> Shibuya

        [120000, 135000, 118000, 142000],  # Food sales for 4 weeks
        [85000, 90000, 88000, 95000],      # Drinks sales for 4 weeks
        [45000, 50000, 47000, 53000]       # Snacks sales for 4 weeks
    ],

    [   # Branch 1 -> Shinjuku

        [155000, 160000, 148000, 170000],  # Food sales for 4 weeks
        [92000, 98000, 94000, 102000],     # Drinks sales for 4 weeks
        [60000, 65000, 58000, 70000]       # Snacks sales for 4 weeks
    ]
]

# Step 4: Create variables for highest sale tracking

highest_sale = 0
highest_branch = ""
highest_category = ""
highest_week = 0

# Step 5: Print report heading

print("========================================")
print("SUPERMARKET SALES REPORT")
print("========================================")

# Step 6: Create branch index

b = 0

# Step 7: Loop through branches

while b < len(branches):

    # Step 8: Print current branch name

    print(f"Branch: {branches[b]}")

    # Step 9: Store total sales of one branch

    branch_total = 0

    # Step 10: Create category index

    c = 0

    # Step 11: Loop through categories

    while c < len(sales[b]):

        # Step 12: Print category name

        print(f"{categories[c]} | ", end="")

        # Step 13: Create week index

        w = 0

        # Step 14: Loop through weekly sales

        while w < len(sales[b][c]):

            # Step 15: Get current weekly sale

            current_sale = sales[b][c][w]

            # Step 16: Print week number and sale

            print(
                f"Week {w + 1}: {current_sale}",
                end=" "
            )

            # Step 17: Add sale to branch total

            branch_total += current_sale

            # Step 18: Check highest sale

            if current_sale > highest_sale:

                # Step 19: Update highest sale details

                highest_sale = current_sale
                highest_branch = branches[b]
                highest_category = categories[c]
                highest_week = w + 1

            # Step 20: Move to next week

            w += 1

        # Step 21: Move to next line after weeks

        print()

        # Step 22: Move to next category

        c += 1

    # Step 23: Print branch total

    print(f"Branch Total: {branch_total}")
    print()

    # Step 24: Move to next branch

    b += 1

# Step 25: Print highest sale information

print("Highest single-week sale:", highest_sale)

print(
    f"Branch: {highest_branch} | "
    f"Category: {highest_category} | "
    f"Week {highest_week}"
)