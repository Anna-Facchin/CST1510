"""
RECORD CHECK  -  my version
===========================

Name  : Anna Gracielle Facchin dos Santos
Lane  :  AI
Date  :27/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Enter a name, a hostage, an IP")
first = float(input("Number"))
second = float(input("Number"))


print(f"Label: {label}")
print(f"First: {first}")
print(f"Second: {second}")


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

difference = first - second
percentage = (first / second) * 100
print(f"Difference: {difference}")
print(f"Percentage: {percentage:.1f}%")


# =================================================================== OUTPUT
# 3. Print the report.
#


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Label: {label:>10}")
print(f"First: {first:>10.2f}")
print(f"Second: {second:>10.2f}")
print(f"Difference: {difference:>10.2f}")
print(f"Percentage: {percentage:>+10.2f}%")
print("End of report")


print("=" * 34)