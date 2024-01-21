#!/usr/bin/env python
# coding: utf-8

# In[67]:


import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",database='library',passwd="ubuntu@123",use_pure=True)
print(mydb)
from all_book_functions import cls as book_cls
from datetime import date


# In[85]:


class cls:
    def __init__(self,reg_no):
        self.reg_no=reg_no
    
    
#     ------------------
#     def search_book_details(isbn):
#         cursor=mydb.cursor()
#         query="select * from book_details where isbn=%s"

#         cursor.execute(query,(isbn,))
#         a=cursor.fetchall()
#         cursor.close()
#         if len(a):
#             return a[0]
#         else: False
    
    
    
#     ------------------
    
    def search_issue_record(id):
        '''
        searches issue record by id

        parameter:
        id (string): registration of student

        output:
        id| name|phone|hosteler|book1_id|book1_issed|book1_return|book2_id|book2_issued|book2_return 

        eg:

        search_issue_record('23MSD7044')
        output:
        ('23msd7044', 'sourabh', 7428834, 1, 'NULL', None, None, 'NULL', None, None)
        '''
        cursor=mydb.cursor()
        query="select * from issue_record where id=%s"

        cursor.execute(query,(id,))
        a=cursor.fetchall()     
        cursor.close()
        if len(a):
            return a[0]
        
        else: return False



#     def issue_book1(isbn,student_id):
#         search_issue_record
#         student_result=search_issue_record(student_id)
#         if student_result:

#             book_result=search_book_details(isbn)
#             if book_result:



#                 cur_date = date.today()

#                 # print(book_result[5])
#                 cursor=mydb.cursor()
#                 query="update book_details set available=%s where isbn=%s"
#                 update_copies=book_result[5]-1
#                 cursor.execute(query,(update_copies,isbn))

#                 # query="update issue_record set book1_id=%s where id=%s"
#                 query="update issue_record set book1_id=%s, book1_issued=%s where id=%s"
#                 cursor.execute(query,(isbn,cur_date,student_id))
#                 cursor.close()
#                 print('book issued')
#                 mydb.commit()
#             else: 
#                 print('book not found hence not issued')
#                 return 0
#         else:
#             print('student not found hence not issued')
#             return 0


    def issue_book1(isbn,student_id):
        student_result=cls.search_issue_record(student_id)
        if student_result:

            book_result=book_cls.search_book_details(isbn)
            if book_result:
                
                cur_date = date.today()

                # print(book_result[5])
                cursor=mydb.cursor()
                query="update book_details set available=%s where isbn=%s"
                update_copies=book_result[5]-1
                cursor.execute(query,(update_copies,isbn))

                
                query="update issue_record set book1_id=%s, book1_issued=%s where id=%s"
                cursor.execute(query,(isbn,cur_date,student_id))
                # query="update issue_record set book1_id=%s where id=%s"
                # cursor.execute(query,(isbn,student_id))
                cursor.close()
                print('book issued')
                mydb.commit()
                return 1
            else: 
                print('book not found hence not issued')
                return 0
        else:
            print('student not found hence not issued')
            return 0
        
        
    def issue_book2(isbn,student_id):
        student_result=cls.search_issue_record(student_id)
        if student_result:

            book_result=book_cls.search_book_details(isbn)
            if book_result:

                cur_date = date.today()
                # print(book_result[5])
                cursor=mydb.cursor()
                query="update book_details set available=%s where isbn=%s"
                update_copies=book_result[5]-1
                cursor.execute(query,(update_copies,isbn))

                query="update issue_record set book2_id=%s, book2_issued=%s where id=%s"
                cursor.execute(query,(isbn,cur_date,student_id))
                cursor.close()
                print('book issued')
                mydb.commit()
                return 1
            else: 
                print('book not found hence not issued')
                return 0
        else:
            print('student not found hence not issued')
            return 0
        

    def collect_book1(student_id):
    # def collect_book1(isbn,student_id):
        student_result=cls.search_issue_record(student_id)
        isbn=student_result[4]
        if student_result:

            book_result=book_cls.search_book_details(isbn)
            if book_result:

                cur_date=date.today()
                # print(book_result[5])
                cursor=mydb.cursor()
                query="update book_details set available=%s where isbn=%s"
                update_copies=book_result[5]+1
                cursor.execute(query,(update_copies,isbn))

                query="update issue_record set book1_id=%s, book1_issued=%s where id=%s"
                cursor.execute(query,('NULL',None,student_id))
                # query="update issue_record set book1_id=%s where id=%s"
                # cursor.execute(query,('NULL',student_id))
                cursor.close()
                print('book collected')
                mydb.commit()
                return 1
            else: 
                print('book not found hence not collected')
                return 0
        else:
            print('student not found hence not collected')
            return 0        


    def collect_book2(student_id):
        student_result=cls.search_issue_record(student_id)
        isbn=student_result[7]
        if student_result:

            book_result=book_cls.search_book_details(isbn)
            if book_result:

                # print(book_result[5])
                cursor=mydb.cursor()
                query="update book_details set available=%s where isbn=%s"
                update_copies=book_result[5]+1
                cursor.execute(query,(update_copies,isbn))

                query="update issue_record set book2_id=%s, book2_issued=%s where id=%s"
                cursor.execute(query,('NULL',None,student_id))
                cursor.close()
                print('book collected')
                mydb.commit()
                return 1
            else: 
                print('book not found hence not collected')
                return 0
        else:
            print('student not found hence not collected')
            return 0        

        
        
    def add_new_student(student_id,name,phone,hosteler):
        result=cls.search_issue_record(student_id)
        if not result:
            cursor=mydb.cursor()
            query="insert into issue_record(id,name,phone,hosteler) values (%s,%s,%s,%s)"
            cursor.execute(query,(student_id,name,phone,hosteler))
            mydb.commit()
            cursor.close()
            return 1
            print('student added')
        else: 
            print('student already exists')
            return 0
        
        
        
        
    def update_student_record(student_id,name,phone,hosteler):
        cursor=mydb.cursor()
        query="update issue_record set name=%s,phone=%s,hosteler=%s where id=%s"
        cursor.execute(query,(name,phone,hosteler,student_id))
        mydb.commit()
        cursor.close()

        print('student record updated')
        
    def show_all_issue_record():
        # cursor.close()
        cursor=mydb.cursor()
        query="select * from issue_record"
        result=cursor.execute(query)
        result= cursor.fetchall()
        for i in result:
            print(i)
        cursor.close()
        
    def delete_student(student_id):
        
        data=cls.search_issue_record(student_id)
        print(data[4],data[7])
        if data:
            if (data[4]=='NULL' or data[4]==None) and (data[7]=='NULL' or data[7]==None):
                cursor=mydb.cursor()
                query="DELETE FROM issue_record WHERE id=%s"
                cursor.execute(query,(student_id,))
                mydb.commit()
                cursor.close()
                print('student record deleted')
                return 1
            else: 
                print('book are issued, hence cannot delete')
                return 0
        else: 
            print('student record not found')
            return -1
        
        


# In[ ]:




