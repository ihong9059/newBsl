def FileSave(filename,content):
    with open(filename, "a") as myfile:
        myfile.write(content)

FileSave("test.txt","test1 \n")

FileSave("test.txt","test2 \n")
