import sys
import argparse
import os.path

print("Number of arguments:", len(sys.argv), " arguments.")
print("Argument List:", str(sys.argv))

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Parse <filename> - file of emails list.",
                    type=str)
args = parser.parse_args()

if os.path.isfile(args.filename) and os.access(args.filename, os.R_OK):
    print("File: ", args.filename)
    print("File exists and is readable.")
else:
    print("File: ", args.filename)
    print("Either the file is missing or not readable")
    exit(0)

# Try open file
try:
    file = open('input-file', 'open mode')
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as e:
    print("Caught the I/O error.")
    raise ex






