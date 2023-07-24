#!/usr/bin/python3
''' A python script that reads standard input line by line and computes  the metrics'''

# to Provide access to some variables used or maintained by the interpreter and functions that interact with the Python runtime environment
import sys

# initializes a dictionary called cache, to keep track of the occurrences of each HTTP status code encountered in the input data
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
# to keep track of the cumulative file size encountered in the input data
total_size = 0
# to keep track of the total number of lines processed in the input data
counter = 0
# the script processes input and computes metrics.
try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass
#  ensures the final metrics are printed
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

