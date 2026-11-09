"""
RECORD CHECK  -  my version
===========================

Name  : Anna Gracielle Facchin dos Santos
Lane  :  AI
Date  : 09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """Turn the messy survey line into a clean dict"""
    
    line = raw_line.strip().strip('"')
    label_part, rest = line.split(",", 1)
    label = label_part.strip().lower()

    fields= {}

    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
    return {
        "label": label,
        "rating": fields["rating"], 
        "age": fields["age"]
        }

def status_of(rating, age):
    """ Return Flagged or OK. """
    if rating <=5 and age <= 20:
            return "FLAGGED"
    else:
        "OK"

flagged_count = 0
record_count = 0


with open(r"C:\Users\graci\Documentos\MDX\CST1510\Week 07 - Strings and Text Manipulation\LAB\messy_records.py") as f:


    for raw_line in f:
        records = parse_line(raw_line)
        status = status_of(records["rating"], records["age"])

        print(records, status)

        record_count += 1
        if status == "FLAGGED":
             flagged_count += 1

print(f"Records: {record_count}, Flagged: {flagged_count}")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
# PS C:\Users\graci\Documentos\MDX\CST1510> & 'C:\Users\graci\AppData\Local\Python\pythoncore-3.14-64\python.exe' '"c:/Users/graci/Documentos/MDX/CST1510/Week 07 - Strings and Text Manipulation/LAB/template.py"'
# Traceback (most recent call last):
# File "c:\Users\graci\Documentos\MDX\CST1510\Week 07 - Strings and Text Manipulation\LAB\template.py", line 80, in <module>
#   records = parse_line(raw_line)
# File "c:\Users\graci\Documentos\MDX\CST1510\Week 07 - Strings and Text Manipulation\LAB\template.py", line 36, in parse_line
#   fields[key.strip().lower()] = float(value.strip())
#                                 ~~~~~^^^^^^^^^^^^^^^
# ValueError: could not convert string to float: '23  "'
# PS C:\Users\graci\Documentos\MDX\CST1510>"""

#    [ ] Check every function does one job, with a docstring
