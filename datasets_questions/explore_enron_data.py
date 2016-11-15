#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people in the Enron dataset: {}".format(len(enron_data))

print 'Number of features for each person in the Enron dataset: {0}'.format(len(enron_data["SKILLING JEFFREY K"]))

pois = 0
for i in range(len(enron_data)):
    if enron_data.values()[i]['poi'] == True:
        pois += 1
print 'Number of POI\'s: {0}'.format(pois)

fo = open("../final_project/poi_names.txt", "r")
num_lines = sum(1 for line in fo)
fo.close()
print 'There were {0} POIs on the list of the file poi_names.txt'.format(num_lines - 2)

print 'The total value of the stock belonging to James Prentice: {0}'.format(enron_data['PRENTICE JAMES']['total_stock_value'])

print 'We have {0} email messages from Wesley Colwell to persons of interest.'.format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print 'The value of stock options exercised by Jeffrey K Skilling: {0}'.format(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {}
for name in names:
	names_payments[name] = enron_data[name]['total_payments']
import operator
sorted_names_payments = sorted(names_payments.items(), key=operator.itemgetter(1), reverse=True)
print '{0} took home the money, which was {1}.'.format(sorted_names_payments[0][0], sorted_names_payments[0][1])

salary_count = 0
email_count = 0
for i in range(len(enron_data)):
    if enron_data.values()[i]['salary'] != 'NaN':
        salary_count += 1
    if enron_data.values()[i]['email_address'] != 'NaN':
        email_count += 1
print '{0} folks in the dataset have salary.'.format(salary_count)
print '{0} known email addresses.'.format(email_count)

payment_count = 0
poi_payment_count = 0
for i in range(len(enron_data)):
    if enron_data.values()[i]['total_payments'] == 'NaN':
        payment_count += 1
        if enron_data.values()[i]['poi'] == True:
            poi_payment_count +=1
print '{0} percent of people in the dataset have \'NaN\' for their total payments.'.format(100 * payment_count/len(enron_data))
print '{0} percent of POIs in the dataset have \'NaN\' for their total payments.'.format(100 * poi_payment_count/pois)

print len(enron_data)
print payment_count