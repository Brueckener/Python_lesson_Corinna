# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:58:00 2019

@author: mescherowsky
"""
authors = ["Darwin", "Goethe", "Soundso"]

output_fh = open("list.html", "w")

scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel der Autorenliste</title>
</head>
<body>

<h1>Eine grandiose Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""

for author in authors:
    scaffold_middle = scaffold_middle + "<li>" + author + "</li>\n"
   
output_fh.write(scaffold_middle)
    
scaffold_end = """



</ul>

</body>

</html>""" 


output_fh.write(scaffold_end)
output_fh.close()