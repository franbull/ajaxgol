#!/usr/bin/env python
import cgi
import gol

form = cgi.FieldStorage()
response = ''
if 'data' in form:
    response = gol.gol(form['data'].value)

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
#print "<TITLE>CGI script output</TITLE>"
print response 
