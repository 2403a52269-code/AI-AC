def score_applicant(education, experience, gender, age):
   
    edu_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score = edu_scores.get(education.lower(), 0)

    score += min(experience, 20) * 2  

    gender_scores = {
        'male': 0,
        'female': 0,
        'other': 0
    }
    score += gender_scores.get(gender.lower(), 0)

    
    if 22 <= age <= 60:
        score += 10 
    else:
        score += 0

    return score

applicant1 = score_applicant('master', 5, 'female', 30)
applicant2 = score_applicant('bachelor', 10, 'male', 45)
print("Applicant 1 Score:", applicant1)
print("Applicant 2 Score:", applicant2)
