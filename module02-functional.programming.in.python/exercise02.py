names = ["jack", "james", "ben", "Sun", "kate", "jin"]
print(names)
order_by_string_length = lambda name: len(name)
names.sort(key=order_by_string_length, reverse=True)
print(names)
order_by_lower_case = lambda name: name.lower()
names.sort(key=order_by_lower_case, reverse=True)
print(names)
