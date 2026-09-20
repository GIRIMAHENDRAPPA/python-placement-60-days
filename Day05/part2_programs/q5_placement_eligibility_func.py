def predict_placement(cgpa,attendance):
    if cgpa >= 8 and attendance >= 80:
        return "high chance-90%"
    elif cgpa >= 6.5 and attendance >= 70:
        return "medium chance-60%"
    else:
        return "low chance-30%"
print(predict_placement(8.5, 90))