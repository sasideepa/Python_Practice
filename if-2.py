indian=["Butter nanna","daal","samosa"]
chinese=["Noodle","Snake fry","fried rice"]
italian=["Pizza","Pasta","Risotto"]

dish=input("Enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("italian")
else:
    print("Based on little knowledge I have I don't know which cuisine is",dish)
