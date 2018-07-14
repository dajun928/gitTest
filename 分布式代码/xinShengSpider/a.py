# -*- encoding:utf-8 -*-
lst = [1,2,3,3,5,7]
s = map(lambda x,y: x-y, lst[1:],lst[:-1])
print s