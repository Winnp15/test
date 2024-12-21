def calculate_bmi(weight, height):
    try:
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        bmi = weight / (height ** 2)
        return {"BMI": round(bmi, 2)}
    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": "Unexpected error occurred."}



try:
    print(calculate_bmi(70, 1.75))  # Valid input
    print(calculate_bmi(-70, 1.75))  # Invalid weight
    print(calculate_bmi(70, 0))  # Invalid height
except Exception as e:
    print("Error: {e}")