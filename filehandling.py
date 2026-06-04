# file=open('day2.py','r')
# print(file.read())
#
# with open('day2.py','r') as f:
# #     print(f.read())
# import csv
#
# with open('students_dataset.csv','r') as f:
#     #file= csv.reader(f)
#     cn=0
#     file=csv.DictReader(f)
#     for r in file:
#         cn+=1
# print(cn)

d1={'name':'sas', 'age':56}
d2={'name':'rohit','age':23,'course':'udemy'}
if set(d1.keys()).symmetric_difference(set(d2.keys())):
    d1.pop(set(d1.keys()).symmetric_difference(set(d2.keys())))
else:
    print("no")
