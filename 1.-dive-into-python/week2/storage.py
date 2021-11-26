import argparse
import tempfile
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument("--key", dest="key")
parser.add_argument("--val", dest="val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path):
	with open(storage_path, 'r') as f:
		data = json.loads(f.read())
else:
	data = {}

with open(storage_path, 'w') as f:
	if args.val is None:
		if args.key in data:
			print(", ".join(data[args.key]))
		else:
			print("None")
	else:
		if args.key not in data:
			data[args.key] = []
		data[args.key].append(args.val)
	f.seek(0)
	json.dump(data, f, sort_keys="True", indent=4)
