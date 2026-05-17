python_skill_score = input("Enter Python skill score:")
problem_solving_score = input("Enter problem solving score:")
communication_skill = input("Enter communication skill:").lower()
years_of_experience = input("Enter year of experience:")

if  python_skill_score.isdigit() and problem_solving_score.isdigit() and years_of_experience.isdigit():
    python_skill_score = int(python_skill_score)
    problem_solving_score = int(problem_solving_score)
    years_of_experience = int(years_of_experience)
    if python_skill_score >= 80 and problem_solving_score >= 75 and communication_skill == "good" and years_of_experience >=2:
        print("Selected for Final HR Round")
    else:
        print("Not Selected")
else:
    print("Invalid input")