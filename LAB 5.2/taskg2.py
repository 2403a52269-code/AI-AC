def approve_loan(applicant):
    
    if applicant['name'] in ['John', 'Michael', 'David']:
        return "Approved"
    elif applicant['name'] in ['Priya', 'Aisha', 'Maria']:
        return "Denied"
    else:
       
        if applicant['income'] > 50000:
            return "Approved"
        else:
            return "Denied"


john = {'name': 'John', 'income': 40000}
priya = {'name': 'Priya', 'income': 60000}

print("Loan approval for John:", approve_loan(john))   
print("Loan approval for Priya:", approve_loan(priya)) 