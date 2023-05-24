class Main:
    def __init__(self):
        pass
                     
    def save(self):
        values=list(self.__dict__.values()) 
        with open(f"{self.__class__.__name__.lower()}.csv","w") as file:
            pass
        
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        # print(data)
        id=str(self.id)
        my_data=[i for i in data if i!="\n"]
        # print(my_data)
        for i in my_data:
            if id in i:      
                print("id must be unique")
                return
        
        string=""
        for i in values:
            string+=str(i) 
            string+="," 
        string=string[:-1]
        with open(f"{self.__class__.__name__.lower()}.csv","a") as file:
            file.writelines(f"\n{string}\n")
            print("Sucessfully saved your data !!! ")
            
        return data
            
            
            
            
        
    def delete(self):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        id=str(self.id)
        num=None
        for i in range(len(data)):
            if id in data[i]:
                num=i
                break
        if num!=None:
            data[num]=""
            
        else:
            print("Enter correct Id")
        
        
        with open(f"{self.__class__.__name__.lower()}.csv","w") as file:
            file.writelines(data)
            print("Sucessfully Deleted !!!!")

        

    
    def update(self,*newdata):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        id=str(newdata[0])
        num=None
        if str(self.id) == id:
            for i in range(len(data)):
                if id in data[i]:
                    print(data[i])
                    num=i
                    break
            if num!=None:
                data[num]=','.join(map(str, newdata))
            else:
                print("Enter correct Id")
            with open(f"{self.__class__.__name__.lower()}.csv","w+") as file:
                file.writelines(data)
                print("Successfully Updated !!!! ")
        else:
            print("Please provide correct id")
            
    def get(self):
        print (self.__dict__)
        
      
    def get_all(self):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        newdata=[i for i in data if i!="\n"]
        for i in newdata:
            print(i)
        

class Book(Main):
    def __init__(self,id,title,author):  
        super().__init__() 
        self.id=id
        self.title=title
        self.author=author
        
class Person(Main):
    def __init__(self,id,name):
        super().__init__()
        self.id=id
        self.name=name
        
p=Person(1,"ram")
p.save()
p.get_all()
# p.delete()
        
# b=Book(2,"GoodBook","Ram1")
# b2=Book(3,"GoodBook2","Ram22")
# # b.save()
# b3=Book(4,"NiceBook","Book1")
# # b.update(2,"Baa",'1234')
# # b3.save()
# # b2.save()
# # b2.update(2,"BadGirl","Ram3")
# # # b.update(2,"asd","asdf")
# # b2.update(3,"Hello","Hello3")
# b.delete()
# print(b2.title)
# # b2.delete()
# b3.get_all()









