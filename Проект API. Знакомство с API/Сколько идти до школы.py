from sys import argv

from distance import lonlat_distance

argv = argv[1:]

print(lonlat_distance((argv[0].split(',')), (argv[1].split(','))))
