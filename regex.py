import re

# 1️⃣ Match a simple pattern
text = "Hello World, welcome to regex in Python!"
pattern = r"Hello"
match = re.match(pattern, text)
print("1. Match:", match.group() if match else "No match")

# 2️⃣ Search for a word
pattern = r"regex"
search = re.search(pattern, text)
print("2. Search:", search.group() if search else "Not found")

# 3️⃣ Find all digits
text_with_numbers = "My phone is 9876543210 and pin is 411001"
digits = re.findall(r"\d+", text_with_numbers)
print("3. All Digits:", digits)

# 4️⃣ Replace with regex
new_text = re.sub(r"World", "Universe", text)
print("4. Replace:", new_text)

# 5️⃣ Validate Email
emails = ["test@example.com", "invalid-email", "user@domain.co.in"]
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$"
for email in emails:
    if re.match(email_pattern, email):
        print(f"5. Valid Email: {email}")
    else:
        print(f"5. Invalid Email: {email}")

# 6️⃣ Split using regex
sentence = "Python,Java;C++|Go"
split_result = re.split(r"[,;|]", sentence)
print("6. Split:", split_result)

# 7️⃣ Extract hashtags
tweet = "Learning #Python is fun! #Regex #GitHub"
hashtags = re.findall(r"#\w+", tweet)
print("7. Hashtags:", hashtags)

