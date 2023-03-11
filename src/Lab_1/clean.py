# f_2022 = open('count_2022.txt','r')
# f_2022_student = open('2022_student.txt','r')
import csv

csvFormat = []

winter_2022 = {}
spring_2022 = {}
autumn_2022 = {}

winter_2021 = {}
spring_2021 = {}
autumn_2021 = {}

country = []

f_student_2022_winter = open('student_2022_winter.txt','r')
with open('count_2022_winter.txt') as f_winter_2022:
    for country_name in f_winter_2022:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2022_winter.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        winter_2022[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)

f_student_2022_spring = open('student_2022_spring.txt','r')
with open('count_2022_spring.txt') as f_spring_2022:
    for country_name in f_spring_2022:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2022_spring.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        spring_2022[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)
        
f_student_2022_autumn = open('student_2022_autumn.txt','r')
with open('count_2022_autumn.txt') as f_autumn_2022:
    for country_name in f_autumn_2022:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2022_autumn.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        autumn_2022[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)

f_student_2021_winter = open('student_2021_winter.txt','r')
with open('count_2021_winter.txt') as f_winter_2021:
    for country_name in f_winter_2021:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2021_winter.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        winter_2021[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)

f_student_2021_spring = open('student_2021_spring.txt','r')
with open('count_2021_spring.txt') as f_spring_2021:
    for country_name in f_spring_2021:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2021_spring.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        spring_2021[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)

f_student_2021_autumn = open('student_2021_autumn.txt','r')
with open('count_2021_autumn.txt') as f_autumn_2021:
    for country_name in f_autumn_2021:
        country_name = country_name.replace('\n','')
        country_name = country_name.replace(',','')
        country_name = country_name.replace(' ','_')
        student_num = f_student_2021_autumn.readline()
        student_num = student_num.replace('\n','')
        student_num = student_num.replace(',','')
        autumn_2021[country_name] = int(student_num)
        country.append(country_name)
        # print(country_name, student_num)




f_student_2022_winter.close()
f_student_2022_spring.close()
f_student_2022_autumn.close()
f_student_2021_winter.close()
f_student_2021_spring.close()
f_student_2021_autumn.close()


country = set(country)

for c in country:
    current = {}
    current['country'] = c

    if (winter_2021.get(c) is None):
        current['winter_2021'] = None
    else:
        current['winter_2021'] = winter_2021[c]
    
    if (spring_2021.get(c) is None):
        current['spring_2021'] = None
    else:
        current['spring_2021'] = spring_2021[c]
    
    if (autumn_2021.get(c) is None):
        current['autumn_2021'] = None
    else:
        current['autumn_2021'] = autumn_2021[c]
    
    if (winter_2022.get(c) is None):
        current['winter_2022'] = None
    else:
        current['winter_2022'] = winter_2022[c]

    if (spring_2022.get(c) is None):
        current['spring_2022'] = None
    else:
        current['spring_2022'] = spring_2022[c]

    if (autumn_2022.get(c) is None):
        current['autumn_2022'] = None
    else:
        current['autumn_2022'] = autumn_2022[c]

    csvFormat.append(current)

csv_columns = ['country','winter_2021','spring_2021','autumn_2021','winter_2022','spring_2022','autumn_2022']

try:
    with open('StudentDemographic_Lab1.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in csvFormat:
            writer.writerow(data)
except IOError:
    print("I/O error")
