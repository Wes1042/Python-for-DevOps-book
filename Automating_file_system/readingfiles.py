# reading json files with python file opener
with open('service-policy.json ' , 'r') as opened_file:
    policy = opened_file.readlines()
print(policy)
print("\n\n\n")


# more readable json opener
import json

with open('service-policy.json' , 'r') as opened_file:
    policy = json.load(opened_file)
print(policy)
print("\n\n\n")


# actual json readable
# makes it readable based positioning
from pprint import pprint
pprint(policy)

print('\n[+] changing a statement \n')

# change a resource on the file structure
# changing a variable by specifying where it is located 
policy['Statement']['Resource'] = 'S3'
pprint(policy)

# to update this file to the actual file you would use json.dump
with open('service-policy.json' , 'w') as opened_file:
    policy = json.dump(policy, opened_file)


############################################################

# Using YAML (YAML Ain't MArkup Language)
# it is a supset of JSON, but has a more compact format using whitespace similar to how pyton uses it
# Ansible is a tool used to automate software configuration, management , and deplyment. 
# Ansible uses files referred to as playbooks to define actions you want to automate

print("\n\nusing and reading YAML\n")
import yaml

with open('verify-apache.yml' , 'r') as opened_file:
    verify_apache = yaml.safe_load(opened_file)

pprint(verify_apache)

# saving python date to a file in YAML format:
with open('verify-apache.yml', 'w') as opened_file:
    yaml.dump(verify_apache,opened_file)



##############################################################

# Using XML (Extensible Markup Language)
# consist of hierchical documents of tagged elemets. 
# Many web systems used XML to transport data. It is used in android apps , adnroid studio

# RSS (Real Simple Syndication) 
# RSS feeds are used to track and notify users of updates to websites and have used to track publication of articles from various sources
# RSS feeds use XML-formated documents. It maps the XML documents 'hierchical structure to a tree like data structure.

# the nodes of the tree are elemts, and parent-child relationship is used to model the hierchy
# The top parent node is referred to as the root element. To parse an RSS ,XML document and get its root:



print('\n\nattempig XML\n')


import xml.etree.ElementTree as ET
tree = ET.parse('http_feeds.feedburner.com_oreilly_radar_atom.xml')

root = tree.getroot()
print(root)