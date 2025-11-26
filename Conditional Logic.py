# AND: Both must be True
age = 20
has_id = True
print(age >= 18 and has_id)  # Output: True

# OR: Only one needs to be True
is_raining = False
has_umbrella = True
print(is_raining or has_umbrella)  # Output: True

# NOT: Reverses state
is_logged_in = False
print(not is_logged_in)  # Output: True


marks = 82

if marks >= 90:
    print("Grade A")      # Skipped (82 is not >= 90)
elif marks >= 75:
    print("Grade B")      # MATCH! (82 >= 75). Prints "Grade B" and exits.
elif marks >= 60:
    print("Grade C")      # Skipped (Already found a match above)
else:
    print("Grade D")      # Skipped


x = 15
if x > 20:
    print("High")
elif x > 10:
    print("Medium")
else:
    print("Low")
