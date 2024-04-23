import  json
from typing import Any
class NODE:
    def __init__(self):
        pass

    def __setattr__(self, key:str, value:Any):
        super().__setattr__(key,value)

    def __repr__(self):
        return self.__dict__.__str__()

class JSON:

    def __init__(self, json:list[Any]|dict[Any,Any]|None=None):

        if json is None:
            pass
        elif isinstance(json,list):

            self.list = self.create_list_in_json( json)
        else:
            self.create_dict("master",json)




    def create_dict(self,node:NODE,items:list[Any]|dict[Any,Any]):

        for key, item in items.items():
            if node == "master":
                if isinstance(item,dict):
                    self.__setattr__(key,NODE())
                    self.create_json(self.__getattribute__(key),item)
                elif isinstance(item,list):
                    self.__setattr__(key,self.create_list_in_json(item))

                else:
                    self.__setattr__(key, item)

            else:
                if isinstance(item, dict):
                    node.__setattr__(key,NODE())
                    self.create_json(node.__getattribute__(key),item)
                elif isinstance(item,list):
                    node.__setattr__(key,self.create_list_in_json(item))
                else:
                    node.__setattr__(key,item)

    def create_list_in_json(self,item_list:list[Any])->list[Any]:

        for item in item_list:

            if isinstance(item,list):
                self.create_list_in_json(item)
            elif isinstance(item,dict):
                list_index = item_list.index(item)
                item_list[list_index] = NODE()
                self.create_dict(item_list[list_index],item)

        return  item_list
    
    def load(self):
        pass

    def __setattr__(self, key, value):
        super().__setattr__(key,value)

    def __repr__(self):
        return self.__dict__.__str__()


with open("quote.json","r") as f:
    d = json.load(f)



p = JSON(d)

print(p[1])
