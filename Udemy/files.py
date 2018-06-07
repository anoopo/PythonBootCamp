my_file = open('D:\\Anoop\\personal\\learning\\python\\OtherFiles\\myfile.txt')
#my_file.seek(0)
#print (my_file.readlines())
#my_file.seek(0)
print (my_file.read())
my_file.close()

with open('D:\\Anoop\\personal\\learning\\python\\OtherFiles\\myfile.txt') as my_file2:
    print (my_file2.readlines())

with open("D:\\Anoop\\personal\\learning\\python\\OtherFiles\\myfile3.txt", mode='w') as myfile_write:
    myfile_write.write("\nThis is the fourth line of the file")

with open('D:\\Anoop\\personal\\learning\\python\\OtherFiles\\myfile3.txt') as my_file3:
    print (my_file3.read())
