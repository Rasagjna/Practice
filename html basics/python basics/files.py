import csv
data=open('example.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
print("datalines[0]",data_lines[0])#column names
print(len(data_lines))# no of rows
for line in data_lines[:5]:
    print(line)
print("datalines[10][3]",data_lines[2][7])
all_emails=[]
for line in data_lines[1:15]:
    all_emails.append(line[7]) # only one particular row
print(all_emails)
full_names=[]
for line in data_lines[1:]:
    full_names.append(line[1]+''+line[2]) # concatinating 2 rows
file_to_out=open('to_save_file.csv',mode='w',newline='')
csv_writer=csv.writer(file_to_out,delimiter=',')

csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_out.close()
f=open('to_save_file.csv',mode='a',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()