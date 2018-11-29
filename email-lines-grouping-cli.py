#!/bin/python
import re
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Parse <filename> - file of emails list.",
                    type=str)
args = parser.parse_args()

if os.path.isfile(args.filename) and os.access(args.filename, os.R_OK):
    pass
else:
    print("File: ", args.filename)
    print("Either the file is missing or not readable")
    exit(0)

# Try open file
try:
    f = open("emails.txt", "r")
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as ex:
    print("Caught the I/O error.")
    raise ex

emails = f.readlines()
dec_email = ''
i = 1
for email in emails:
        email = email.replace('\n', '')
        m = re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', email)
       #print("MATC.group(0) = ", m.group(0));
        if m :
            dec_email = dec_email + email + '; '
            if ( i % 10 == 0) :
                dec_email = re.sub(r'(.*)(; )($)', r'\1\3', dec_email)
                #dec_email = dec_email[:-2] # remove 2 chars '; ' at the end of line.
                #print("emails = ", dec_email)
                prefix = ""
                if ((i//10) % 2 == 0) :
                    prefix = "Cc:"
                else :
                    prefix = "To:"
                print(prefix, dec_email)
                dec_email = ''
            if ( i % 20 == 0) :
                print("")
            i = i + 1
#print ("dec_email = %s") % dec_email
if dec_email :
    dec_email = dec_email[:-2] # remove 2 chars '; ' at the end of line.
    #print("emails = ", dec_email)
    if ((i // 10) % 2 == 0):
        prefix = "Cc:"
    else:
        prefix = "To:"
    print(prefix, dec_email)

class EmailGroupLines:
    pass
