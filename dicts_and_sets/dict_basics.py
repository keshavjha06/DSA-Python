# a dict is Python's HashMap (it also remembers insertion order)
ages = {}
ages["Keshav"] = 22  # add
ages["Anirudh"] = 21
ages["Manas"] = 11
ages["Ritik"] = 26
for key in ages:
    print(key + " : " + str(ages[key]))
print(ages, len(ages))
del ages["Manas"]
print(ages, len(ages))
print(ages["Keshav"])
ages["Ritik"] = 23  # overwrite
print(ages, len(ages))
print("Anirudh" in ages)
