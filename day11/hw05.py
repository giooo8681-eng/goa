#5)მომხმარებელს შეეკითხეთ მისი სახელი,თუ ამ სახელშ იქნება ხმოვნები გამოიტანეთ ეს ხმოვნები,თუ არ იქნება გამოიტანეთ "არ არის ხმოვნები"
name=input("enter your name: ")
vowels="aeiouAEIOU"
age=""
for i in name:
    if i in vowels:
        age+=i
if age=="":
    print("არ არის ხმოვნები")
else:
    print(age)
        