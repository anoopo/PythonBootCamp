british_number = "020 7123 4567"
british_number = (british_number.replace(" ", ""))[1:]
normalized = "+" + "44" + british_number
first_enum = list(normalized[:1:-1])
final = ".".join(first_enum)
print (final)
