'''
This is the rule module used in part 2 of "The Art of Transpiling" series.

It includes the LengthToLen class. The class will re-write variables 
that match the js "s.length" patern into the pythonic "len(s)". To make this
module visible to JSConvert, add it to the jsconvert.pyrules package and
edit the __init__.py file to include "demorules" in the __all__ list. 

Created on Jul 28, 2022

@author: Demo2
'''

from jsconvert.transpiler import CodeRule

__all__ = ["LengthToLen"]


class LengthToLen(CodeRule):
    
    def __init__(self):
        super().__init__("length-to-len", ["VariableType", "VariableType"])
        
        
    def apply(self, buf, offset):
        c = buf.current(offset)
        
        if c.is_leaf() and c.name == "length" and buf.insert_prefix("len(", {"this":"self"}):
            buf.add(buf.current().name)
            buf.add(")")
            return 2
        
        return 0
