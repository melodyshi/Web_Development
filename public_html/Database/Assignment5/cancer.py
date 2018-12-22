#!/usr/bin/python

import cgi
import sqlite3
import cgitb

cgitb.enable()

print("Content-Type: text/html\r\n\r\n")
print('''
<!DOCTYPE html>
<head>
<title>Cancer Clinical Trial Report</title>
<link rel="stylesheet" href="cancer.css" type="text/css">
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

form = cgi.FieldStorage()
purpose = form.getvalue("purpose")
interventions = ""
if form.getvalue("Behavioral Intervention"):
      interventions += '"Behavioral" '
if form.getvalue("Biological Intervention"):
      interventions += '"Biological" '
if form.getvalue("Device Intervention"):
      interventions += '"Device" '
if form.getvalue("Drug Intervention"):
      interventions += '"Drug" '
if form.getvalue("Genetic Intervention"):
      interventions += '"Genetic" '
if form.getvalue("Procedure Intervention"):
      interventions += '"Procedure" '
if form.getvalue("Radiation Intervention"):
      interventions += '"Radiation" '
where = "({})".format(", ".join(interventions.split()).strip())

if form.getvalue("ordered"):
    order = form.getvalue("ordered")
if form.getvalue("limit"):
    limit = form.getvalue("limit")

query_template = '''
SELECT Conditions, Primary_Purpose, Intervention_Methods
FROM clinical_trial
WHERE Primary_Purpose = "{}"
  AND Intervention_Methods IN {}
ORDER BY {}
LIMIT {};
'''
query = ""
query = query_template.format(purpose,where,order,limit)

conn = sqlite3.connect("cancer.db")
c = conn.cursor()

c.execute(query)
result = c.fetchall()

print("<h1>You have selected:</h1>")
print("<p>The primary purpose of the trial is: {}</p>".format(purpose))
print("<p>The intervention methods are: {}</p>".format(where))
print("<p>The results are ordered by: {}</p>".format(order))
print("<p>Total records displayed: {}</p>".format(limit))

print("<table border = 1>")
print("<tr>")
print("<th>Conditions</th>")
print("<th>Primary Purpose</th>")
print("<th>Intervention Methods</th>")
print("</tr>")

row_template = '''
<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</tr>
'''
for row in result:
    print(row_template.format(row[0],row[1],row[2]))
print("</table>")

print("</body>")

print('''
<footer>
<div><a href="index.html"><p>Back to the form</p></a></div>
</footer>
''')
print("</html>")
