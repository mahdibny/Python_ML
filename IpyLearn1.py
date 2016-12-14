# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:35:54 2016

@author: Mahdi
"""


from numpy.random import randn
data={i:randn() for i in range(7)}
print data

"""
#ipython also has tab completion
#typing a question mark asfter will give you details of the variable

In[69] data?
Type:        dict
String form: {0: -0.13745712247532044, 1: -0.505574799240464, 2: 0.814433286521197, 3: -0.17184486809268157, 4: -0.41666057302770404, 5: 0.01814192776776625, 6: 0.2846730061119816}
Length:      7
Docstring:  
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
    


_i(#on line) is the input at that line
_(#on line)  is the output at that line


%log allows the ipython session to be saved
%bookmark (short_name) (path_to_directory)

"""

