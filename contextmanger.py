class Filemanager:
    def __init__(self,file,mode):
        self.file=file
        self.mode=mode
    def __enter__(self):
        self.object=open(self.file,self.mode)
        return self.object
    def __exit__(self, exc_type, exc, tb):
        print(f'An exception accure {exc_type},{exc},{tb}')
        self.object.close()
        return False
with Filemanager("test.txt","w") as file:
    file.write("try class for write\n")
    file.write("close file automatic\n")
print(file.closed)


    
        
        