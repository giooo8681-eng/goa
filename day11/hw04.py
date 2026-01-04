#4)მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group"
score=input("enter your score: ")
if int(score)==100:
    print("A GROUP")
if 80<int(score)<99:
    print("B GROUP")
elif 40<int(score)<70:
    print("C GROUP")
else:
    print("D GROUP")
    
