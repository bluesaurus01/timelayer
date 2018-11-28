raw_data=open("hi.txt",'r', encoding='utf-8-sig')
read_data=raw_data.read()
print(read_data)

array_data=read_data.split('\n')
name=[]
for i in range(len(array_data)):
	array_data[i]=array_data[i].split(',')
	if (array_data[i][0]):
		name.append(array_data[i][0])
		array_data[i].pop(0) #이름 지움
	else:
		array_data.pop(i)
print(array_data)
print(name)

test_subjects=open("subjects_utf8.txt",'r', encoding='utf-8-sig')
read_s=test_subjects.read()
list_subjects=read_s.split(',')
for a in list_subjects:
    a=a.strip()
print(list_subjects)

final_array=[]

for j in range(len(list_subjects)):
	final_array.append([])
	for i in range(len(array_data)):
		if (list_subjects[j] in array_data[i]):
			final_array[j].append(1)
		else:
			final_array[j].append(0)

#print(final_array)

flag=0;
check_array=[]
for i in range(len(list_subjects)) :
    check_array.append([])
    for j in range(len(list_subjects)) :
        flag=0;
        if(i==j) :
            check_array[i].append(-1)
            continue;
        for k in range(len(final_array[i])) :
            if(final_array[i][k]&final_array[j][k]==1) :
                flag=1;

        if(flag==1) :
            check_array[i].append(0)
        else :
            check_array[i].append(1)

for i in range(len(list_subjects)) :
    print("%s " %(list_subjects[i]))
    for j in range(len(check_array[i])) :
        if(check_array[i][j]==1) :
            print("%s " %(list_subjects[j]))

    print("\n");