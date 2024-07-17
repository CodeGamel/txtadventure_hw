attendees = int(input("Enter number of attendees: "))

venue = 'large hall' if attendees > 100 else "conference room"

print (venue)

user_input = input("Do you want Vegetarian food?")

if user_input == ('Yes') :
     print("I recommend Veggie Delight Caterers")
else:
    print("I recommend Gourmet Meals Caterers")