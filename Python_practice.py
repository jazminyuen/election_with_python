counties = []
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
                
# #What is the score?
# score = int(input("What is your test score? "))

# #Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F')

# #Membership Operators
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else: 
#     print("El Paso is not the list of counties.")

# #While Loop
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {}
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

voting_data = []
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for i in voting_data[i]:
    for county, registered_voters in counties_dict:
        print(f"{county} county has {registered_voters:,} registered voters")



