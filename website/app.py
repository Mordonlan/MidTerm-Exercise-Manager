from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# I will keep the exercises here in a list
exercises = []

# Home page
@app.route('/')
def home():
    # get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # calculate total calories
    total_calories = 0
    for item in exercises:
        if "calories" in item:
            total_calories = total_calories + item["calories"]

    return render_template("home.html",
                           exercises=exercises,
                           date=current_date,
                           total_calories=total_calories)

# Add exercise page
@app.route('/add', methods=['POST'])
def add_exercise():
    # get form data one by one
    name = request.form.get("name")
    sets = request.form.get("sets")
    duration = request.form.get("duration")
    weight_option = request.form.get("weight_option")
    weight_value = request.form.get("weight_value")

    # make sure numbers are numbers
    try:
        sets = int(sets)
    except:
        sets = 0
    try:
        duration = int(duration)
    except:
        duration = 0
    try:
        weight_value = float(weight_value)
    except:
        weight_value = 0

    # calculate calories burnt (very simple formula)
    if weight_option == "no":
        calories = duration * sets * 3
    else:
        calories = duration * sets * (3 + (weight_value / 10))

    # create the exercise dictionary
    exercise_item = {}
    exercise_item["name"] = name
    exercise_item["sets"] = sets
    exercise_item["duration"] = duration
    exercise_item["weight_option"] = weight_option
    exercise_item["weight_value"] = weight_value
    exercise_item["calories"] = calories

    # add to the exercises list
    exercises.append(exercise_item)

    # go back to home page
    return redirect('/')

# Remove exercise
@app.route('/remove/<int:index>')
def remove_exercise(index):
    if index >= 0 and index < len(exercises):
        exercises.pop(index)
    return redirect('/')

# BMI calculator
@app.route('/bmi', methods=['POST'])
def bmi():
    height = request.form.get("height")
    weight = request.form.get("weight")

    try:
        height = float(height) / 100  # convert to meters
    except:
        height = 0

    try:
        weight = float(weight)
    except:
        weight = 0

    if height > 0:
        bmi_value = weight / (height * height)
    else:
        bmi_value = 0

    # recommend calories to burn
    if bmi_value < 18.5:
        recommendation = "You are underweight, focus on building mass."
    elif bmi_value < 25:
        recommendation = "You have a normal BMI. Keep it up!"
    elif bmi_value < 30:
        recommendation = "Overweight, try to burn around 300 calories/day."
    else:
        recommendation = "Obese, aim to burn around 500 calories/day."

    current_date = datetime.now().strftime("%Y-%m-%d")
    total_calories = 0
    for item in exercises:
        total_calories = total_calories + item["calories"]

    return render_template("home.html",
                           exercises=exercises,
                           date=current_date,
                           total_calories=total_calories,
                           bmi_value=round(bmi_value, 2),
                           recommendation=recommendation)


if __name__ == "__main__":
    app.run(debug=True)

