import requests

from City import City

newClass = City()
print(newClass.existThisCity("Madrid"))



# city = "Santander"
# KEY_GOOGLE = 'AIza'
# x = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Spain+'+city+'&key='+KEY_GOOGLE)
# 
# print(x.content)





"""
Troubleshooting info:
  Principal: contact.instinct.code@gmail.com
  Resource: imagedeveloper
  Troubleshooting URL: console.cloud.google.com/iam-admin/troubleshooter;
  permissions=resourcemanager.projects.get;
  principal=contact.instinct.code@gmail.com;
  resources=%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2Fimagedeveloper

Missing permissions:
  resourcemanager.projects.get
"""