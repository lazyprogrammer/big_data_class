#!/usr/bin/env python

# book url: https://www.amazon.com/dp/B01KH9YWSY
import sys
import json

def print_user(j):
  if 'user_id' not in j:
    return
  print "%s\t%s\t%s" % (j['user_id'], j.get('name', ''), j.get('fruit', ''))

current_user_id = None
current_data = {}

for line in sys.stdin:
    line = line.strip()

    user_id, j = line.split("\t", 1)

    if current_user_id != user_id:
      # print data for current user and reset
      print_user(current_data)
      current_data = {}
      current_user_id = user_id

    j = json.loads(j)
    for k, v in j.iteritems():
      current_data[k] = v

# print the last user
print_user(current_data)
