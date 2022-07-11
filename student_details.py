'''
Exited to do the first assignment.

This assignment is a simple one to make you ready for the followup assignments.

As a University, students details plays an important role. Instead of one person writing all your details, we intend to take it from you.

The Details are as follows:

Name:
Roll Number:
Branch:
Specialization:
Email ID:
Moodle ID:
GitHub ID:
Replit ID:
Semester:
Year(1-4):

Now your task is to put it in a dictionary like the below example

{
'name': {'first-name':'Rama', 'last-name':'Rao'},
'roll-number':'123456',
'branch':'CSE',
'specialization':'DS',
'email-id':'ramarao@gitam.in',
'moodle-id':'Rama Rao 123456',
'github-id':'ramarao',
'replit-id':'ramarao',
'semester':'2',
'year':'1'
}

In the above example we have a dictionary in a dictionary with `first-name` and `last-name` as the keys, It is must.

Now you are given the function like the below. Fill this function with the necessary code.

This function has to fill in the dictionary with the acquired input and return to the function caller which inturn will print the received dictionary.

This function has to return a dictionary with all your details.
Make sure you fill in the right details.

'''

def my_details():
 x=input('Enter the name of the dict: ')
d={}
n=int(input("Enter the number of inputs in the dict: "))
for j in range(n):
  d[x]={}
  for i in range(0,2):
    key=input("Enter the key name: ")
    value=input("Enter the value: ")
  d[x].update({key:value})
  d.update({'Roll num':'011'})
  d.update({'Branch':'ECE'})
  d.update({'Specialization':'AIML'})
  d.update({'Email-Id':'nsudheer@gitam.in'})
  d.update({'Replit-Id':'SUDHEER-NISTALA'})
  d.update({'GitHub-Id':'Sudheer07-10'})
  d.update({'Moodle-Id':'VU21EECEN0100011'})
  d.update({'Semester':'2'})
  d.update({'Year':'1'})
  return d

# now call your function
dt = my_details()
print(dt)


# Once you complete, no need to submit.
# The changes will be automatically saved.
# Wish you happy coding!!!=
