try:
    cgpa=float(input("Enter CGPA:"))
    if cgpa>10:
        raise ValueError("CGPA cannot be>10")
    print(f"Your CGPA:{cgpa}")
except ValueError as e:
    print(f"Error:{e}")
except Exception as e:
    print(f"Something went wrong:{e}")