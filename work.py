workdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]

today = input("What day is it today?").strip().lower()

if today not in workdays and today not in weekend:
  print("Unvalid day!")
elif today in workdays:
  print("You have to work!")
else:
  print("You can sleep in!")
