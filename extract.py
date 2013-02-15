import json, sys, unicodecsv

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

filename = sys.argv[1]
print filename

input = open(filename)
input.readline()
data = json.load(input)
input.close()

out = open(filename[:-2]+"csv","wb")

output = unicodecsv.writer(out, encoding='utf-8')

output.writerow(["id"]+["timestamp"]+["tweet"])  # header row

for row in data:
	output.writerow([row["id"],row["created_at"],row["text"]])
out.close()

source = open(filename[:-2]+"csv","r")
tmp = open(filename[:-2]+"tmp","wb")

tmp.write("id,timestamp,tweet")

for line in source:
	pos = find_nth(line, ",",2)
	tweet = line[pos+1:-2]
	tweet = tweet.replace('""','"')
	if tweet.startswith('"') and tweet.endswith('"'):
		tweet = tweet[1:-1]
	line = line[:pos+1] + tweet + "\r\n"
	tmp.write(line)
	print line

	
tmp.close()
source.close()