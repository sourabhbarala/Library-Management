#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",database='library',passwd="ubuntu@123",use_pure=True)
print(mydb)

from datetime import date


# In[2]:


class cls:
    def show_book_details():
        # cursor.close()
        cursor=mydb.cursor()
        query="select * from book_details "
        result=cursor.execute(query)
        result= cursor.fetchall()
        
        result_list=[]
        for i in result:
            print(i)
            result_list.append(i)
        cursor.close()
        
        return result_list

    def search_book_details(isbn):
        cursor=mydb.cursor()
        query="select * from book_details where isbn=%s"

        cursor.execute(query,(isbn,))
        a=cursor.fetchall()
        cursor.close()
        if len(a):
            return a[0]
        else: False



    def add_new_book(isbn,title,author,publication,max_count):
        result=cls.search_book_details(isbn)
        if not result:
            cursor=mydb.cursor()
            query="insert into book_details values (%s,%s,%s,%s,%s,%s)"
            cursor.execute(query,(isbn,title,author,publication,max_count,max_count))
            mydb.commit()
            # cursor.commit()
            cursor.close()

            print('book added')
            return 1
        else: 
            print('book already exists')
            return 0


    def update_book_details(isbn,title,author,publication,max_count,available):
        cursor=mydb.cursor()
        query="update book_details set title=%s, author=%s, publication=%s, max_count=%s, available= %s where isbn=%s"
        cursor.execute(query,(title,author,publication,max_count,available,isbn))
        mydb.commit()
        cursor.close()

        print('book details updated')
        
        
    def delete_book(isbn):
        
        data=cls.search_book_details(isbn)
        if data:
            
            cursor=mydb.cursor()
            query="DELETE FROM book_details WHERE isbn=%s"
            cursor.execute(query,(isbn,))
            mydb.commit()
            cursor.close()
            print('book deleted')
            return 1
       
        else: 
            print('book not found')
            return -1


# In[ ]:





# In[ ]:




