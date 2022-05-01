def openFile():
    file1 = input("Enter File name: ")
    with open(file1,"r") as a:
        data_a = a.read()
    with open(file1,"w") as a:
        a.write(data_a)