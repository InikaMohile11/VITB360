from main import calculate_score, calculate_grade

# Test 1: Score calculation

subject = {
"cat1": 49,
"cat2": 50,
"term_end": 99,
"internals": 40
}

score = calculate_score(subject)

if score == 60.55:
    print("Score calculation test passed.")
else:
    print("Score calculation test failed.")

# Test 2: Grade calculation

grade = calculate_grade(85)

if grade == "A":
    print("Grade calculation test passed.")
else:
    print("Grade calculation test failed.")

# Test 3: Grade boundary

grade = calculate_grade(90)

if grade == "S":
    print("Grade boundary test passed.")
else:
    print("Grade boundary test failed.")
