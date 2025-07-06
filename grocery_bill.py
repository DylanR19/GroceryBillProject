# Program: Grocery Bill Calculator
# 1. Prompt user for coupon amount (decimal, example: 0.10 for 10%)
# 2. If coupon > 1 <= 0, default to 10% discount
# 3. Prompt for grocery bill amounts for 4 weeks
# 4. Calculate monthly total and weekly average (before coupon)
# 5. Apply coupon discount to total and weekly average
# 6. Display results with and without coupon applied

# Program starts here

# Ask for the coupon amount
coupon = float(input("Enter the coupon amount as a decimal  (Example: 0.10 for 10%): "))

# Validate coupon amount
if coupon > 1 or coupon <= 0:
    print("Invalid coupon entered. Defaulting to 10% discount.")
    coupon = 0.10
    
# Get grocery bills for each week
bills = []
for week in range(1, 5):
    bill = float(input(f"Enter grocery bill for week {week}: "))
    bills.append(bill)

# Calculate totals
total_monthly = sum(bills)
weekly_avg = total_monthly / 4

# Apply coupon discount
discounted_total = total_monthly * (1 - coupon)
discounted_weekly_avg = discounted_total / 4

# Display results
print(f"\nMonthly Total (No Coupon): ${total_monthly:.2f}")
print(f"Weekly Average (No Coupon): ${weekly_avg:.2f}")
print(f"Monthly Total (With Coupon): ${discounted_total:.2f}")
print(f"Weekly Average (With Coupon): ${discounted_weekly_avg:.2f}")