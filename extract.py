import json, sys, unicodecsv, os

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

filename = sys.argv[1]

input = open(filename)
input.readline()
data = json.load(input)
input.close()

out = open(filename[:-2]+"tmp","wb")

output = unicodecsv.writer(out, encoding='utf-8')

output.writerow(["id"]+["timestamp"]+["tweet"])  # header row

for row in data:
	output.writerow([row["id"],row["created_at"],row["text"]])
out.close()

source = open(filename[:-2]+"tmp","r")
csv = open(filename[:-2]+"csv","wb")

for line in source:
	pos = find_nth(line, ",",2)
	print pos
	tweet = line[pos+1:-2]
	tweet = tweet.replace('""','"')
	if "\n" in tweet:
		print tweet
	if tweet.startswith('"') and tweet.endswith('"'):
		tweet = tweet[1:-1]
	line = line[:pos+1] + tweet + "\r\n"
	csv.write(line)
	

	
csv.close()

source.close()
os.unlink(filename[:-2]+"tmp")