import csv
fields=['Name','Department','Semester']
rows=[['Amala','MCA','S1'],['Alfiya','MCA','S1']]
with open('abc.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
    f.close()
