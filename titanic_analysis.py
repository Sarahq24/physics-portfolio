# Titanic Data Analysis
# Sara - Physics Portfolio

print("=== Titanic Data Analysis ===")
print()

# Basic data
total_passengers = 891
survived = 342
minors = 113

# Calculate statistics
not_survived = total_passengers - survived
survival_rate = (survived / total_passengers) * 100
minor_rate = (minors / total_passengers) * 100

# Display results
print("Total passengers:", total_passengers)
print("Survived:", survived)
print("Did not survive:", not_survived)
print("Passengers under 18:", minors)

print()
print("Survival rate:", round(survival_rate, 2), "%")
print("Passengers under 18:", round(minor_rate, 2), "%")
