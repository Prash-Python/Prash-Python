# For loop demonstration.
countries_list = ['USA', 'Canada', 'Germany', 'France', 'Australia']
for country in countries_list:
    print(country)

for i in range(0, len(countries_list)):
    print(f"{i+1}: {countries_list[i]}")

# While loop demonstration.
count = 0
while count < len(countries_list):
    print(f"{count+1}: {countries_list[count]}")
    count += 1
else:
    print("All countries have been printed.")