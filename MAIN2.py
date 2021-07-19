data= open("file1.txt")
file1_data= data.readlines()
data2= open("file2.txt")
file2_data= data2.readlines()
result= [name for name in file1_data if name in file2_data]
result_final= [int(i) for i in result]
print(result_final)
