import json, sys, unicodecsv

filename = sys.argv[1]

input = open(filename)
input.readline()
data = json.load(input)
input.close()

out = open(filename[:-2]+"csv","wb")

output = unicodecsv.writer(out, encoding='utf-8')

output.writerow(["id"]+["timestamp"]+["tweet"])  # header row

for row in data:
	if row["text"].startswith('"') and row["text"].endswith('"'):
		row["text"] = row["text"][1:-1]
	output.writerow([row["id"],row["created_at"],row["text"]])