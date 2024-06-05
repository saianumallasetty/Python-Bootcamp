#!/usr/bin/env python
# coding: utf-8

# In[2]:


2+1


# In[3]:


2-1


# In[4]:


2*2


# In[5]:


4/2


# # Modulo or "Mod" Operator

# In[6]:


7/4


# In[7]:


7 % 4


# In[8]:


50 % 5


# In[9]:


23 % 2


# In[10]:


20 % 2


# In[11]:


2 ** 3


# In[14]:


2 + 10 * 10  + 3


# In[15]:


(2+10) * (10+3)


# # Variables

# In[16]:


a = 5


# In[17]:


a


# In[18]:


a = 10


# In[19]:


a


# In[30]:


a+a


# In[32]:


a = a+a


# In[33]:


a


# In[34]:


type(a)


# In[35]:


a = 30.1


# In[36]:


type(a)


# In[37]:


income = 100
tax = 0.1
my_taxes = income * tax
my_taxes


# # String

# In[38]:


'hello'


# In[39]:


"Hello"


# In[41]:


print("hello")


# In[44]:


print('hello \nworld')


# In[45]:


print('hello \tworld') #tab


# In[46]:


len('hello')


# In[48]:


len('I am')


# String Indexing and Slicing

# In[49]:


mystring = 'hello world'


# In[50]:


mystring


# In[52]:


mystring[0]


# In[53]:


mystring[-2]


# In[54]:


mystring = 'abcdefghijk'


# In[56]:


mystring


# In[58]:


mystring[2:] #slice


# In[59]:


mystring[:3]


# In[60]:


mystring[3:7]


# In[64]:


mystring[::] #begin to end


# In[65]:


mystring[::2]


# In[66]:


mystring[2:7:2]


# In[68]:


mystring[::-1]


# # Immutability

# In[70]:


name = 'sai'


# In[71]:


# name[0] = 'p'


# In[74]:


last_letters = name[1:]


# In[75]:


last_letters


# In[77]:


's' + last_letters #concatinate


# In[78]:


x = 'hello world'


# In[84]:


x = x + ' how are you doin'


# In[85]:


x


# In[86]:


2 + 3


# In[87]:


'2' + '3'


# In[88]:


x = 'hello world'


# In[89]:


x.upper()


# In[91]:


x.lower()


# In[92]:


x.split()


# In[94]:


x.split('o')


# # formatting with the .format() method

# In[97]:


print('this is a string {}'.format('inserted'))


# In[104]:


print('the {2} {1} {0}'. format('car', 'bike', 'jeep'))


# In[108]:


print('the {c} {b} {a}' .format(a='car', b='bike', c='jeep'))


# # float fromating follow '{value:width.precison f}'

# In[119]:


result = 100/777


# In[120]:


result


# In[130]:


print('the result was {r:1.5f}' .format(r= result))


# In[ ]:





# In[ ]:





# In[131]:


name = 'sai'


# In[7]:


print(f'helo, his name is {name}')


# In[6]:


name = 'sai'
age = 4


# In[140]:


print(f'{name} is {age} years old.') #new mothed


# In[142]:


print("I'm going to inject %s here." %'something' ) #old method


# # Lists

# In[8]:


my_lists = [1,2,3]


# In[9]:


my_list = ['string', 100, 23, 2]


# In[10]:


len(my_list)


# In[11]:


mylist = ['one', 'two', 'three']


# In[13]:


mylist[0] #indexing


# In[14]:


mylist[1:] #slicing


# In[15]:


another_list = ['four', 'five']


# In[16]:


another_list


# In[18]:


new_list = mylist + another_list #concatination
new_list


# In[19]:


new_list[0] = 'ONE All caps'


# In[20]:


new_list


# In[21]:


new_list.append('six')


# In[22]:


new_list


# In[23]:


new_list.pop() 


# In[24]:


new_list


# In[25]:


popped_item = new_list.pop()


# In[26]:


popped_item


# In[27]:


new_list


# In[28]:


new_list.pop(0)


# In[29]:


new_list


# In[31]:


new_list = ['a', 'e', 'i', 'o', 'u']
num_list = [4,1,8,3]


# In[32]:


new_list.sort()


# In[33]:


new_list


# In[34]:


my_sorted_list = new_list.sort()


# In[36]:


type(my_sorted_list)


# In[38]:


new_list.sort()
my_soreted_list = new_list


# In[39]:


my_soreted_list


# In[40]:


num_list


# In[41]:


num_list.sort()


# In[42]:


num_list


# In[43]:


num_list.reverse()
num_list


# # dictionaries

# In[44]:


my_dictionaries = {'key1':'value1', 'key2':'value2'}


# In[45]:


my_dictionaries


# In[46]:


my_dictionaries['key1']


# In[47]:


prices_lookup = {'apple':2.88, 'oranges':1.99,'milk':5.80}


# In[48]:


prices_lookup['apple']


# In[49]:


d = {'k1':123, 'k2':[0,1,2], 'k3':{'insidekey':100}}


# In[50]:


d['k2']


# In[52]:


d['k3']['insidekey']


# In[53]:


d['k2'][2]


# In[54]:


d = {'key1': ['a','b','c']}


# In[55]:


d


# In[56]:


mylist= d['key1']


# In[57]:


mylist


# In[58]:


letter = mylist[2]


# In[59]:


letter


# In[61]:


letter.upper()


# In[64]:


d['key1'][2].upper()


# In[66]:


d = {'k1':100, 'k2':200}


# In[67]:


d


# In[68]:


d['k3'] = 300


# In[69]:


d


# In[70]:


d['k1'] ='newvalue'


# In[71]:


d


# In[73]:


d = {'k1': 100, 'k2': 200, 'k3': 300}


# In[74]:


d.keys()


# In[76]:


d.values()


# In[78]:


d.items()


# # Tuples

# In[80]:


t = (1,2,3)


# In[81]:


my_list = [1,2,3]


# In[82]:


type(t)


# In[83]:


type(my_list)


# In[84]:


len(t)


# In[85]:


t


# In[86]:


t = ('one', 2)


# In[87]:


t[0]


# In[88]:


t[-1]


# In[89]:


t = ('a','a','b')


# In[90]:


t.count('a')


# In[91]:


t.index('a')


# In[92]:


t.index('b')


# In[93]:


mylist[0] = 'new'


# In[94]:


mylist


# In[97]:


set('mississippi') #set


# In[98]:


1 > 2 #boolean


# In[99]:


1 == 1


# # I/O .txt

# In[100]:


get_ipython().run_cell_magic('wrirtefile', 'myfile.txt', 'Hello this is text file\nHow are you doing\nI am good\n')


# In[ ]:





# In[ ]:


with open ('myfile.txt, mode', mode = 'r') as f:
    print(f.read())


# In[104]:


with open ('myfile.txt, mode', mode = 'a') as f:
    f.write('same as well')


# In[ ]:


with open ('myfile.txt, mode', mode = 'r') as f:
    print(f.read())


# In[105]:


with open ('abcdef.txt, mode', mode = 'w') as f:
    f.write('I created this file!')


# In[106]:


with open ('abcdef.txt, mode', mode = 'r') as f:
    print(f.read())
    


# In[ ]:




