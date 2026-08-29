#Working with CSV Files
import csv
import io

# Simulated CSV content
csv_data = """name,phone,skill,city,steps
James Omondi,0712345678,welding,Nairobi,9200
Sandra Weru,0723456789,tiling,Mombasa,8800
Patrick Njiru,0734567890,phone repair,Nairobi,11000
Grace Achieng,0745678901,copywriting,Kisumu,10200
Brian Kamau,0756789012,upholstery,Nairobi,7900"""

f = io.StringIO(csv_data)
reader = csv.reader(f)
reader_2= csv.DictReader(f)
for row in reader:
    print(row)
for ro in reader_2:
    print(ro)
