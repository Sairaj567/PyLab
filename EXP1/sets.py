days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Holiday"}
months = {"jan", "feb", "mar", "jan"}

# printing
print("Days: ",days)
print("Months: ",months)

# adding
months.add("apr")
print("Adding a month: ",months)

# discarding
days.discard("Holiday")
print("Deleting a day: ",days)
