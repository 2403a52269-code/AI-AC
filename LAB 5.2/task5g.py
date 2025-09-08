def greet_user(name, gender):
    
    titles = {
        "male": "Mr.",
        "female": "Ms.",
        "non-binary": "Mx."  
    }
    
    
    title = titles.get(gender.lower(), "Hello,")
    
    
    if title in ["Mr.", "Ms.", "Mx."]:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."


print(greet_user("Alex", "non-binary"))
print(greet_user("Jane", "female"))
print(greet_user("John", "male"))
print(greet_user("Casey", "prefer not to say"))