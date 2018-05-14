import yaml

yaml_file = 'test_yaml_file.yml'
with open(yaml_file, 'r') as f:
	data = yaml.load(f)

print(data)


"""
$ python test_yaml.py
{'hoge': 'str_hoge', 'fuga': 123, 'piyo': ['pika', 'pika']}
"""