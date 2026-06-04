"""
File Type	Module / Function
CSV	        csv.reader(), csv.DictReader()
JSON	    json.load(), json.loads()
LOG	        open(), read(), readline()
XML	        ET.parse(), getroot()
"""
# reading a csv file
import csv,json
def readingcsv(filename,num):
    cn=0
    with open(filename,'r') as csvfile:
        reader= csv.DictReader(csvfile)
        for i in reader:
            print(i)
            if (cn<num):
                cn=cn+1
            else:
                break
def writingascsv(nfile,oldfile):
    with open(nfile,'w',newline="") as wcsvfile, open(oldfile,'r') as rcsvfile:
        reader= csv.DictReader(rcsvfile)
        writer=csv.DictWriter(wcsvfile,fieldnames=reader.fieldnames)
        writer.writeheader()
        for i in reader:
            writer.writerow(i)
        print(f"Finished writing data from {oldfile} to {nfile}")
def readingjson(filename):
    with open(filename, 'r') as jsonfile:
        reader= json.load(jsonfile)
        print(reader)
def writingjson(nfile,oldfile):
    with open(nfile,'w',newline="") as wjsonfile,open(oldfile,'r') as rjsonfile:
        reader=json.load(rjsonfile)
        json.dump(reader,wjsonfile)
        print(f"Finished writing data from {oldfile} to {nfile}")
def readinglog(filename):
    with open(filename,'r') as logfile:
            print(logfile.read())
def writinglog(nfile,oldfile):
    with open(nfile,'a',newline="") as wlogfile,open(oldfile,'r') as rlogfile:
        wlogfile.write(rlogfile.read())
        print(f"Finished writing data from {oldfile} to {nfile} in log format")

readingcsv("files/emp.csv",5)
writingascsv("files/emp_out.csv","files/emp.csv")
readingjson("files/emp.json")
writingjson("files/emp_out.json","files/emp.json")
readinglog("files/application.log")
writinglog("files/application_out.log","files/application.log")