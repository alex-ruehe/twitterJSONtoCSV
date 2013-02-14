twitterJSONtoCSV
================

Requires the unicodecsv package (install via pip)

Usage: python extract.py file.js

Notice: Given file needs to end with .js. A suffix longer than two letters will give you mixed up filenames for the output file.


Twitter offers the possibility to download your whole tweet archive. It comes with a nice local website where you can view all your old tweets. The data also comes in two formats. As CSV (.csv) and JSON (.js). Unfortunately at the moment (14/02/2013) the CSV files do not support UTF-8 so any characters like "ä", "ö" etc are replaced with an "?". The JSON files come in the UTF-8 format. This little script extracts the tweet id, timestamp and tweet from the a given .js file and create a .cvs file with the same name containing the data for further use.


This is only a quick and dirty script. There are also some problems with multiple " which are encoded extra I guess. For me it works, feel free to do whatever you want.