#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb

cgitb.enable()

import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import pymongo
from pymongo import MongoClient

db = MongoClient('mongodb://ls4081:QgBTNNAp@class-mongodb.cims.nyu.edu/ls4081').ls4081


print("Content-Type: text/html;charset=utf-8\r\n\r\n")
print('''
<!DOCTYPE html>
<head>
<title>Cancer Clinical Trial Report</title>
<link href="https://fonts.googleapis.com/css?family=Acme|Cagliostro" rel="stylesheet">
<style>
table{
    border =1;
    font-family: 'Cagliostro', sans-serif;
    width: 80%;
    margin-left:auto;
    margin-right:auto;
    background-color:rgba(255,204,153,0.5)
}
h1{
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Cagliostro', sans-serif;
}
p{
    font-size:12pt;
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Cagliostro', sans-serif;
}

body{
    background-color:rgba(255,204,153,0.2)
}

footer{
    font-family: 'Cagliostro', sans-serif;
}
</style>

</head>
<body>''')


row_template = '''
<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</tr>
'''

print("<p>All Earthquakes Happened in Mexico before 1930</p>")
print("<table border = 1>")
print("<tr>")
print("<th>Year</th>")
print("<th>Location</th>")
print("<th>Earthquake Magnitude</th>")
print("</tr>")

results = db.earthquakes.find({"COUNTRY":"MEXICO","YEAR":{"$lt":1930}}).sort("YEAR", pymongo.ASCENDING)

for item in results:
    year = item.get("YEAR")
    mag = item.get("EQ_MAG")
    location = item.get("LOCATION_NAME")

    if location != "":
        print(row_template.format(year,location,mag))
print("</table>")


print("</body>")

print('''
<footer>
<div><a href="../../index.html"><p>Back to the home page</p></a></div>
</footer>
''')
print("</html>")
