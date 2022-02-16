import requests, zipfile, io, re, json

schema_request = requests.get("https://api.github.com/repos/osquery/osquery/zipball/4.6.0", stream=True)

repo_zip = zipfile.ZipFile(io.BytesIO(schema_request.content))

schema = {}
for table_file in repo_zip.namelist():
    if 'specs/' and '.table' in table_file:
        table_name = table_file.split('/')[-1].split('.')[0]
        schema[table_name]=[]
        with repo_zip.open(table_file) as f:
            for line in f.readlines():
                match = re.search(r'(?<=Column\(\")(\w*)', str(line))
                if match: 
                    schema[table_name].append(match.group(0))
with open('schema.json', 'w') as file:
    json.dump(schema, file)

