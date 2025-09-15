emails = input("Enter emails separated by spaces: ").split()
unique_emails = []
seen = set()

for email in emails:
    email_lower = email.lower()
    if email_lower not in seen:
        seen.add(email_lower)
        unique_emails.append(email)

print("Unique emails (case insensitive):")
for email in unique_emails:
    print(email)