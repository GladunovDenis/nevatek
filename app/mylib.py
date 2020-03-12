from argparse import Namespace 
from typing import Union, Iterable, Callable, Any

class myNamespace(Namespace):
    classname: str = "myNamespace"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    keys = lambda self: self.__dict__.keys()
    values = lambda self: self.__dict__.values()
    items = lambda self: self.__dict__.items()
    __iter__ = lambda self: iter(self.__dict__.items())
    
    def __add__(self, other) -> Namespace:
        if type(other) in [type(Namespace()), type(myNamespace())]:
            return myNamespace(**{**self.__dict__, **other.__dict__})
        elif type(other) in [type({})]:
            return myNamespace(**{**self.__dict__, **other})
        else:
            raise Exception('myNamespace can only add up to Dictionary, Namespace or myNamespace')
            
    def __getitem__(self, item):
        return ord(item)
    
    def __setitem__(self, name, value):
        self.__dict__[name] = value
        
    def __repr__(self):
        repr = [f"{self.classname}("]
        for k,v in self.__dict__.items():
            repr.append(f" {k} = {v}")
        repr.append(")")
        return '\n'.join(repr)
        
        
        
class FunnelMap:
    def __init__(self, keys, values):
        self.items = [*zip(keys, values)]
        
    def __getitem__(self, item):
        for k,v in self.items:
            try:
                k.__iter__
                if item in k:
                    return v
            except:
                if item == k:
                    return v
                
    def __setitem__(self, key, value):
        self.items.append(tuple([key, value]))
                
    def getall(self, item):
        result = []
        for k,v in self.items:
            try:
                k.__iter__
                if item in k:
                    result.append(v)
            except:
                if item == k:
                    result.append(v)
        return result
                    
    def __dict__(self):
        _items = self.items
        try:
            return dict(_items)
        except:
            for i in rng(_items):
                try:
                    hash(_items[i][0])
                except:
                    _items[i] = (tuple(_items[i][0]), _items[i][1])
        return dict(_items)
    
    def __repr__(self):
        string = 'FunnelMap(\n'
        for k,v in self.items:
            string += f' {k} = {v}\n'
        string += ')\n'
        return string
    
    def __iter__(self):
        return iter(self.items)

    
      
def rng(start: Union[int, Iterable] = 0, stop: Union[None, int] = None, step: int = 1) -> Iterable:
    try:
        start.__iter__
        start: int = len(list(start)) - 1
    except:
        pass
    
    if stop == None:
        stop: int = start
        start: int = 0
        
    if step < 1: raise Exception('Step must be greater than 0.')
    mx: int = max(start,stop)
    mn: int = min(start,stop)
    if mx == start:
        step: int = -step
    condition: Callable[[int], bool] = lambda start: (start < start + step <= stop) or (start > start + step >= stop)
    while condition(start):
        yield start
        start: int = start + step
    yield start
    
    
    
def replace(string: str, this: Any, tothis: str = '') -> str:
    '''Replace one or multiple characters in the string.'''
    def fromstr(string, S):
        return string.replace(S, tothis)
            
    def fromarray(string, A):
        for i in rng(A):
            string = string.replace(A[i], tothis)
        return string
    
    def fromdict(string, D):
        for k,v in D.items():
            string = string.replace(k, v)
        return string
            
    method = FunnelMap(keys=[str, (list, tuple, set), dict], values=[fromstr, fromarray, fromdict])
    return method[type(this)](string, this)
    
    
def load_data(fname):
	with open(fname, 'r', encoding='utf-8') as f:
		return f.read()
