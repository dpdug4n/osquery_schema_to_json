import os,json 
schema = {}
for root, dirs, files in os.walk("windows", topdown=True):
    for name in files:
        table = os.path.join(root, name)
        with open (table, 'r') as f:
            columns = []
            for line in f:
                try:
                    if "table_name" in line:
                        tableName = line.lstrip("table_name(").split(')')[0].replace('"','')
                    if "Column" in line:
                        columnName = line.split("Column(")[1].replace('"','').strip('\,').split()[0][:-1]
                        columns.append(columnName)
                except Exception as e:
                    print(table)
                    print(e)
                    pass
            schema[tableName] = columns
with open('schema.json', 'w') as file:
    json.dump(schema, file)

