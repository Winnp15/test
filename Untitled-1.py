def calculate_bmi(weight, height):
    try:
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")
        if height*100 < weight:
            raise ValueError("Height need to be more than weight")
        if height*100 - weight > 100:
            raise ValueError("Height and weight are too difference")
        return round(weight / (height ** 2), 2)
    except Exception as e:
        return str(e)


print(calculate_bmi(70, 1.75))  
print(calculate_bmi(-70, 1.75))  
print(calculate_bmi(70, 0.4))  
print(calculate_bmi(2,2))