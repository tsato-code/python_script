import argparse
import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-df', '--date_from', required=True, type=str, help='YYYY-MM-DD')
    parser.add_argument('-dt', '--date_to', required=True, type=str, help='YYYY-MM-DD')
    args = parser.parse_args()
    args.date_from = datetime.datetime.strptime(args.date_from, '%Y-%m-%d').date()
    args.date_to = datetime.datetime.strptime(args.date_to, '%Y-%m-%d').date()
    return args

args = get_args()

print(type(args.date_from))
print(args.date_from)

print(type(args.date_to))
print(args.date_to)
