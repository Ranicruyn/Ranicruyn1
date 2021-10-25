#!/usr/bin/env python
# coding: utf-8

# In[6]:


def pyramid (n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i +j <= n:
                print(' ',end=' ')
            else:
                print('#', end=' ')
        print()
pyramid(8)



# In[ ]:
