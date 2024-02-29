# Import libraries
import matplotlib.pyplot as plt

a="Please answer the following questions with Y or y or N or N"
print(a.upper())
print("\n")

#empty list for storing answers
l=[]

#questions
a1=input("In the past two weeks, have you felt down, depressed, or hopeless almost every day?")
l.append(a1)
b1=input("Have you noticed a significant change in your energy levels, feeling more tired or hyperactive than usual?")
l.append(b1)
c1=input("Have you lost interest or pleasure in most activities you used to enjoy?")
l.append(c1)
d1=input("Have you had any thoughts of death or suicide? (Important: If the answer is yes, please seek immediate help from a crisis line or mental health professional.)")
l.append(d1)
e1=input("In the past month, have you experienced difficulty sleeping or sleeping too much most nights?")
l.append(e1)
f1=input("Have you noticed a significant change in your appetite or weight, either eating much more or much less than usual?")
l.append(f1)
g1=input("In the past month, have you had trouble concentrating on things, such as work, school, or household chores?")
l.append(g1)
h1=input("Do you feel restless or fidgety most of the time, even when trying to relax?")
l.append(h1)
i1=input("Have you been experiencing constant worry or anxiety that is difficult to control?")
l.append(i1)
j1=input("Have you had physical problems, such as headaches, stomach aches, or muscle aches, that don't go away or that no physical cause can be found for?")
l.append(j1)
a2=input("Have you been using alcohol or drugs more or less than usual in the past month?")
l.append(a2)
b2=input("Have you felt more withdrawn from friends and family than usual?")
l.append(b2)
c2=input("Have you been arguing with family or friends more often than usual, or do you feel disconnected from them?")
l.append(c2)
d2=input("Do you find it difficult to fulfill your responsibilities at work, school, or home?")
l.append(d2)
e2=input("Have you felt overwhelmed or unable to cope with your problems?")
l.append(e2)
f2=input("Do you feel like you are unable to enjoy life?")
l.append(f2)
g2=input("Do you have feelings of guilt or worthlessness?")
l.append(g2)
h2=input("Do you have trouble making decisions or thinking clearly?")
l.append(h2)
i2=input("Do you feel pessimistic about the future?")
l.append(i2)
j2=input("Do you have difficulty controlling your emotions?")
l.append(j2)
a3=input("Do you have difficulty remembering things?")
l.append(a3)
b3=input("Have you become easily overwhelmed or stressed?")
l.append(b3)
c3=input("Do you find it difficult to relax?")
l.append(c3)
d3=input("Do you have difficulty starting or completing tasks?")
l.append(d3)
e3=input("Do you feel like you are not yourself anymore?")
l.append(e3)

#count of yes and no
cy=l.count("y" or "Y")
cn=l.count("n" or "N")

#conditions
if d1=="y" or "Y":
    print("Better not hurt yourself...!....VISIT A DOC! SOS!")
elif cy<=5:
    print("Nah! Chill bro!")
elif 5<=cy<=10:
    print("Bro you okay?? Talk to someone!")
elif 10<=cy<=20:
    print("Its better to consult a doctor")
elif cy>20:
    print("Bro!! You still there??? Just go a see a Doc...no Excuse!!")
elif c==0:
    print("Thank you for sharing. It appears that you are mentally fine! Remember to cherish each moment, find joy in the little things, and nurture your mental well-being. You deserve to lead a fulfilling and happy life. Stay positive and embrace the beauty that surrounds you. Wishing you continued happiness and contentment on your journey!")


# Create labels for the pie chart slices
labels = ["Answered 'No'", "Answered 'Yes'"]

# Create the pie chart
plt.pie([cn,cy], labels=labels, autopct="%1.1f%%")
plt.title("Your Mental Health Condition")
plt.show()
