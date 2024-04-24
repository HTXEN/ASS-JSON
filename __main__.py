import  json
from typing import Any
import sys
import inspect

#TODO: do so you can get attribute

class NODE:
    def __init__(self):
        pass

    def create_dict(self,node:"NODE|str",items:list[Any]|dict[Any,Any]):

        for key, item in items.items():
            if node == "master":
                if isinstance(item,dict):
                    self.__setattr__(key,NODE(),private_set=True)
                    self.create_dict(self.__getattribute__(key,private_set=True),item)
                elif isinstance(item,list):
                    self.__setattr__(key,self.create_list_in_json(item),private_set=True)

                else:
                    self.__setattr__(key, item,private_set=True)

            else:
                if isinstance(item, dict):
                    node.__setattr__(key,NODE(),private_set=True)
                    self.create_dict(node.__getattribute__(key,private_set=True),item)
                elif isinstance(item,list):
                    node.__setattr__(key,self.create_list_in_json(item),private_set=True)
                else:
                    node.__setattr__(key,item,private_set=True)
    
    def create_list_in_json(self,item_list:list[Any])->list[Any]:

        for item in item_list:

            if isinstance(item,list):
                self.create_list_in_json(item)
            elif isinstance(item,dict):
                list_index = item_list.index(item)
                item_list[list_index] = NODE()
                self.create_dict(item_list[list_index],item)
        
        return item_list

    def __setattr__(self, key:str, value:Any,private_set:bool=False):

        if private_set:
            super().__setattr__(key,value)

        elif isinstance(value,dict):
            self.create_dict("master",{key:value})
        elif isinstance(value,list):
            self.__setattr__(key,self.create_list_in_json(value),private_set=True)
        else:
            super().__setattr__(key,value)

    def __repr__(self):
        return self.__dict__.__str__()
    
    def __getattribute__(self, name: str,private_set:bool=False) -> Any:
        if private_set:
            return super().__getattribute__(name,private_set=True)

class JSON:

    def __init__(self, json:list[Any]|dict[Any,Any]|None=None):
        
        if json is None:
            pass
        elif isinstance(json,list):
            self.__getattribute__("__setattr__",private_set=True)("list",self.__getattribute__("create_list_in_json")(json),private_set=True)

        else:
            self.create_dict("master",json)

    def create_dict(self,node:NODE|str,items:list[Any]|dict[Any,Any]):

        for key, item in items.items():
            if node == "master":
                if isinstance(item,dict):
                    self.__setattr__(key,NODE(),private_set=True)
                    self.create_dict(self.__getattribute__(key,),item)
                elif isinstance(item,list):
                    self.__setattr__(key,self.create_list_in_json(item),private_set=True)

                else:
                    self.__setattr__(key, item,private_set=True)

            else:
                if isinstance(item, dict):
                    node.__setattr__(key,NODE(),private_set=True)
                    self.create_dict(node.__getattribute__(key,private_set=True),item)
                elif isinstance(item,list):
                    node.__setattr__(key,self.create_list_in_json(item),private_set=True)
                else:
                    node.__setattr__(key,item,private_set=True)

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

    def __setattr__(self, key, value,private_set:bool=False):
        if private_set:
            super().__setattr__(key,value)
        elif isinstance(value,dict):
            self.create_dict("master",{key:value})

        elif isinstance(value,list):
            self.__setattr__(key,self.create_list_in_json(value))
        else:
            super().__setattr__(key,value)


    def __repr__(self):
        return self.__dict__.__str__()

    def __getitem__(self,item:slice):
        return self.list[item]
    
    def __getattribute__(self, name: str,private_set:bool=False) -> Any:
        print(name)
        print(sys._getframe().f_back.f_locals.get(self))
        if private_set:
            return self.__getattribute__(name)




with open("test/json/pokedex.json","r",encoding="UTF-8") as f:
    d = json.load(f)

print(len(d))

import cProfile 

profiler = cProfile.Profile()
profiler.enable()
p = JSON(d)
profiler.disable()
profiler.print_stats("cumtime")

p.name