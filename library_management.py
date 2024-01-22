#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from all_student_functions import cls as all_stud_func
from all_book_functions import cls as all_book_func
from PIL import ImageTk, Image


root=Tk()
# resize root
root.geometry('1300x600')

# variable for student data
global data, book_data


# -----------------------------------------------------------------------------------------------------------after login

# import image
image=Image.open('library.jpg')

# resize image
resized_image_main=image.resize((1400,900))

# bg image for login page
main_back_img=ImageTk.PhotoImage(resized_image_main)



# define background Label, resize and set background image
# chose label and not frame because it allows background image
back_label=Label(root,width=1400,height=890,image=main_back_img)

# setting location
back_label.grid(row=0,column=0)
back_label.grid_propagate(False)



# # define another frame (shorter)
# main_frame=LabelFrame(back_label,text='main frame',width=1200,height=670)
main_frame=LabelFrame(back_label,width=1200,height=670,bg='#2E314B')

# --------main_frame has width=1200
# --------I devided it into 6 columns of 200 width 

# set location on bakground frame
main_frame.grid(row=0,column=0,padx=85,pady=10)
# set location of main_frame
main_frame.grid_propagate(False)

# side menu frame
side_menu_frame=LabelFrame(main_frame,width=200,height=665,bg='#2E314B')

# set location for side menu
# side_menu span 1 right most column of main_frame
side_menu_frame.grid(row=1,column=5,columnspan=1)
side_menu_frame.grid_propagate(False)
# ========================================================================================================================================







# side_menu_book_frame contains all button for book related opertation like: add, delete, update, show etc
side_menu_book_frame=LabelFrame(side_menu_frame,width=190,height=635)
# setting location
side_menu_book_frame.grid(row=0,column=0,padx=2,pady=2)
side_menu_book_frame.grid_propagate(False)



# interact_window is subframe in main_frame
# books_interact_window_frame=LabelFrame(main_frame,text='book_interact_window_frame',width=1000,height=665,bg='#2E314B')
books_interact_window_frame=LabelFrame(main_frame,width=1000,height=665,bg='#2E314B')


# set location in main frame
# intetact_window span rest 5 columns (left most)
books_interact_window_frame.grid(row=1,column=0,columnspan=5)
books_interact_window_frame.grid_propagate(False)


# this is used to search book record before updating or adding or deleting
# search_book_window_frame=LabelFrame(books_interact_window_frame,text='search book window',width=985,height=50,bg='#A4ABED')
search_book_window_frame=LabelFrame(books_interact_window_frame,width=990,height=50,bg='#AA8479')


# setting location
search_book_window_frame.grid(row=0,column=0,columnspan=2,padx=4,pady=4)
search_book_window_frame.grid_propagate(False)



# window  for issueing or collecting books, also show book details  
# book_details_frame=LabelFrame(books_interact_window_frame,text='book details window',width=990,height=300,bg='#BA968C')
book_details_frame=LabelFrame(books_interact_window_frame,width=987,height=300,bg='#BA968C')

# setting location
# book_details_frame.grid(row=1,column=0,padx=5)
# book_details_frame.grid_propagate(False)
 
# text box on search window to enter ISBN 
book_search_text_box=Entry(search_book_window_frame,text='enter reg. no.',width=20,font=("Helvetica", 15))
# setting location
book_search_text_box.grid(row=0,column=0,padx=6,pady=9)
book_search_text_box.grid_propagate(False)


# frame for updating details of book
update_book_frame=LabelFrame(books_interact_window_frame,text='update book frame',width=985,height=300,bg='#8CBA8C')
update_book_frame.grid_propagate(False)
# # setting location
# update_book_frame.grid(row=1,column=0,columnspan=2,padx=5)
# update_book_frame.grid_propagate(False)

# ISBN label on update_book_frame
update_isbn_label=Label(update_book_frame,text='ISBN:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_isbn_label.grid(row=0,column=0,padx=10,pady=10)
update_isbn_label.grid_propagate(False)
        
# ISBN text box on update_book_frame
update_isbn_val=Label(update_book_frame,text='',width=30,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_isbn_val.grid(row=0,column=1,columnspan=2)
update_isbn_val.grid_propagate(False)

# title label on update_book_frame
update_title_label=Label(update_book_frame,text='Title:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_title_label.grid(row=1,column=0,padx=10,pady=10)
update_title_label.grid_propagate(False)
    
# title text box on update_book_frame
update_title_text_box=Entry(update_book_frame,width=30,font=("Helvetica", 17))
update_title_text_box.grid(row=1,column=1,columnspan=2)
update_title_text_box.grid_propagate(False)

# author label on update_book_frame
update_author_label=Label(update_book_frame,text='Author:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_author_label.grid(row=2,column=0,padx=10,pady=10)
update_author_label.grid_propagate(False)
        
# author text box on update_book_frame
update_author_text_box=Entry(update_book_frame,width=30,font=("Helvetica", 17))
update_author_text_box.grid(row=2,column=1,columnspan=2)
update_author_text_box.grid_propagate(False)

# publication label on update_book_frame
update_publication_label=Label(update_book_frame,text='Publication:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_publication_label.grid(row=3,column=0,padx=10,pady=10)
update_publication_label.grid_propagate(False)
        
# publication text box on update_book_frame
update_publication_text_box=Entry(update_book_frame,width=30,font=("Helvetica", 17))
update_publication_text_box.grid(row=3,column=1,columnspan=2)
update_publication_text_box.grid_propagate(False)

# max books label on update_book_frame
update_max_count_label=Label(update_book_frame,text='Total Copies:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_max_count_label.grid(row=4,column=0,padx=10,pady=10)
update_max_count_label.grid_propagate(False)
        
# available books label on update_book_frame
update_max_count_text_box=Entry(update_book_frame,width=30,font=("Helvetica", 17))
update_max_count_text_box.grid(row=4,column=1,columnspan=2)
update_max_count_text_box.grid_propagate(False)


# max books text box on update_book_frame
update_available_label=Label(update_book_frame,text='Available:',width=20,font=("Helvetica", 18),bg='#8CBA8C',anchor="w",justify="left")
update_available_label.grid(row=5,column=0,padx=10,pady=10)
update_available_label.grid_propagate(False)

# available books text box on update_book_frame
update_available_text_box=Entry(update_book_frame,width=30,font=("Helvetica", 17))
update_available_text_box.grid(row=5,column=1,columnspan=2)
update_available_text_box.grid_propagate(False)

    

# function to call when update_book button is pressed
def update_book_press():
#     hide book_details_frame
    book_details_frame.grid_forget()
    update_book_frame.grid(row=1,column=0,columnspan=2,padx=4,pady=4)
    update_book_frame.grid_propagate(False)
    
#     remove previous content on title, author, publication, max_count, available text box
    update_title_text_box.delete(0,END)
    update_author_text_box.delete(0,END)
    update_publication_text_box.delete(0,END)
    update_max_count_text_box.delete(0,END)
    update_available_text_box.delete(0,END)
    
#     put content of search book in text boxes
    update_isbn_val.config(text=book_data[0])
    update_title_text_box.insert(0,book_data[1])
    update_author_text_box.insert(0,book_data[2])
    update_publication_text_box.insert(0,book_data[3])
    update_max_count_text_box.insert(0,book_data[4])
    update_available_text_box.insert(0,book_data[5])


# button for updating book name, etc. 
update_book_button=Button(side_menu_book_frame,text='Update Record',width=22,height=3,state=DISABLED,command=update_book_press)
update_book_button.grid(row=1,column=0,padx=1)
update_book_button.grid_propagate(False)


# frame for adding new book
add_book_frame=LabelFrame(books_interact_window_frame,text='new book window',width=985,height=300,bg='#BA968C')
add_book_frame.grid_propagate(False)
# add_book_frame.grid(row=1,column=0,columnspan=2,padx=5)
# add_book_frame.grid_propagate(False)




new_book_isbn_label=Label(add_book_frame,text='ISBN:',width=20,font=("Helvetica", 18),bg='#BA968C',anchor="w",justify="left")
new_book_isbn_label.grid(row=0,column=0,padx=10,pady=10)
new_book_isbn_label.grid_propagate(False)
        
new_book_isbn_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
new_book_isbn_text_box.grid(row=0,column=1)
new_book_isbn_text_box.grid_propagate(False)


new_book_title_label=Label(add_book_frame,text='Title:',width=20,font=("Helvetica", 18),bg='#BA968C',anchor="w",justify="left")
new_book_title_label.grid(row=1,column=0,padx=10,pady=10)
new_book_title_label.grid_propagate(False)
        
new_book_title_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
new_book_title_text_box.grid(row=1,column=1)
new_book_title_text_box.grid_propagate(False)


new_book_author_label=Label(add_book_frame,text='Author:',width=20,font=("Helvetica", 18),bg='#BA968C',anchor="w",justify="left")
new_book_author_label.grid(row=2,column=0,padx=10,pady=10)
new_book_author_label.grid_propagate(False)
        
new_book_author_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
new_book_author_text_box.grid(row=2,column=1)
new_book_author_text_box.grid_propagate(False)

new_book_publication_label=Label(add_book_frame,text='Publication:',width=20,font=("Helvetica", 18),bg='#BA968C',anchor="w",justify="left")
new_book_publication_label.grid(row=3,column=0,padx=10,pady=10)
new_book_publication_label.grid_propagate(False)
        
new_book_publication_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
new_book_publication_text_box.grid(row=3,column=1)
new_book_publication_text_box.grid_propagate(False)

new_book_max_count_label=Label(add_book_frame,text='Total Copies:',width=20,font=("Helvetica", 18),bg='#BA968C',anchor="w",justify="left")
new_book_max_count_label.grid(row=4,column=0,padx=10,pady=10)
new_book_max_count_label.grid_propagate(False)
        
new_book_max_count_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
new_book_max_count_text_box.grid(row=4,column=1)
new_book_max_count_text_box.grid_propagate(False)

# new_book_available_label=Label(add_book_frame,text='Available',width=20,font=("Helvetica", 18),bg='#BFFF9D',anchor="w",justify="left")
# new_book_available_label.grid(row=5,column=0,padx=10,pady=10)
# new_book_available_label.grid_propagate(False)
        
# new_book_available_text_box=Entry(add_book_frame,width=30,font=("Helvetica", 17))
# new_book_available_text_box.grid(row=5,column=1)
# new_book_available_text_box.grid_propagate(False)


def remove_book_result():
    book_details_frame.grid_forget()
    for wid in book_details_frame.winfo_children():
        wid.destroy()
        
    update_book_button['state']=DISABLED
    update_book_frame.grid_forget()
    

    book_search_text_box.delete(0,END)
    # book_search_button['state']=NORMAL
    
    

# funtion of book_search_clear_button
def book_search_clear_button_press():
    remove_book_result()
    book_search_button['state']=NORMAL

    


# button for searching book record
def book_search_button_press(temp=0):
    
    if temp:
        book_id=temp
    else:
        book_id=book_search_text_box.get()
        
        if len(book_id)==0:
            book_search_text_box.insert(0,"Please enter book's ISBN no.")
            return
    global book_data
    book_data=all_book_func.search_book_details(book_id)
    
    if book_data:
        
        book_search_button['state']=DISABLED
        
        # book_search_clear_button_press()
        remove_book_result()
        
        book_details_frame.grid(row=1,column=0,columnspan=2,padx=4,pady=4)
        book_details_frame.grid_propagate(False)
        
        update_book_frame.grid_forget()
        update_book_button['state']=NORMAL
        

    
    
    
    
        isbn_label=Label(book_details_frame,text='ISBN:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        isbn_label.grid(row=0,column=0,padx=10,pady=10)
        isbn_label.grid_propagate(False)
        
        isbn_value_label=Label(book_details_frame,text=book_data[0],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        isbn_value_label.grid(row=0,column=1,columnspan=2)
        isbn_value_label.grid_propagate(False)

        title_label=Label(book_details_frame,text='Title:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        title_label.grid(row=1,column=0,padx=10,pady=10)
        title_label.grid_propagate(False)
        
        title_value_label=Label(book_details_frame,text=book_data[1],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        title_value_label.grid(row=1,column=1,columnspan=2)
        title_value_label.grid_propagate(False)

        author_label=Label(book_details_frame,text='Author:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        author_label.grid(row=2,column=0,padx=10,pady=10)
        author_label.grid_propagate(False)
        
        
        author_value_label=Label(book_details_frame,text=book_data[2],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        author_value_label.grid(row=2,column=1,columnspan=2)
        author_value_label.grid_propagate(False)
        
        
        
        publication_label=Label(book_details_frame,text='Publication:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        publication_label.grid(row=3,column=0,padx=10,pady=10)
        publication_label.grid_propagate(False)
        
        
        publication_value_label=Label(book_details_frame,text=book_data[3],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        publication_value_label.grid(row=3,column=1,columnspan=2)
        publication_value_label.grid_propagate(False)
        
        max_count_label=Label(book_details_frame,text='Total Count:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        max_count_label.grid(row=4,column=0,padx=10,pady=10)
        max_count_label.grid_propagate(False)
        
        
        max_count_value_label=Label(book_details_frame,text=book_data[4],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        max_count_value_label.grid(row=4,column=1,columnspan=2)
        max_count_value_label.grid_propagate(False)
        
        available_label=Label(book_details_frame,text='available books:',bg='#BA968C',width=16,font=("Helvetica", 18),anchor="w",justify="left")
        available_label.grid(row=5,column=0,padx=10,pady=10)
        available_label.grid_propagate(False)
        
        
        available_value_label=Label(book_details_frame,text=book_data[5],bg='#BA968C',width=32,font=("Helvetica", 18),anchor="w",justify="left")
        available_value_label.grid(row=5,column=1,columnspan=2)
        available_value_label.grid_propagate(False)
        

            
    else:
        book_search_text_box.delete(0,END)
        book_search_text_box.insert(0,'no record found')
        add_book_button['state']=NORMAL







def submit_book_update_button_press():
    global book_data


    
    # isbn_val=update_isbn_text_box.get()
    title_val=update_title_text_box.get()
    author_val=update_author_text_box.get()
    publ_val=update_publication_text_box.get()
    max_count_val=update_max_count_text_box.get()
    avail_val=update_available_text_box.get()
    
    book_search_button_press(book_data[0])
    all_book_func.update_book_details(book_data[0],title_val,author_val,publ_val,max_count_val,avail_val)
    update_book_frame.grid_forget()
    

    book_search_button_press(book_data[0])
    # book_search_button_press(data[0])
    

submit_book_update_button=Button(update_book_frame,text='Submit',height=2,width=10,command=submit_book_update_button_press)
submit_book_update_button.grid(row=0,column=3,padx=10)
submit_book_update_button.grid_propagate(False)            
            

def delete_book_button_press():
    
    val=all_book_func.delete_book(book_data[0])
    print(val)
    if val==1:
        print('deleted')
        book_search_clear_button_press()
    if val==0:
        print('cannot delete book issue')
        
    

    
    
# button for deleting book
delete_book_button=Button(update_book_frame,text='Delete book',height=2,width=12,command=delete_book_button_press)
delete_book_button.grid(row=1,column=4,padx=10)
delete_book_button.grid_propagate(False)        


def cancel_book_update_button_press(): 
    
    # update_isbn_text_box.delete(0,END)
    update_title_text_box.delete(0,END)
    update_author_text_box.delete(0,END)
    update_publication_text_box.delete(0,END)
    update_max_count_text_box.delete(0,END)
    update_available_text_box.delete(0,END)
    
    book_search_button_press(book_data[0])
    update_book_frame.grid_forget()

cancel_book_update_button=Button(update_book_frame,text='Cancel',height=2,width=10,command=cancel_book_update_button_press)
cancel_book_update_button.grid(row=1,column=3)
cancel_book_update_button.grid_propagate(False)




def add_book_button_press():
    add_book_frame.grid(row=1,column=0,columnspan=2,padx=5)
    add_book_frame.grid_propagate(False)
    # new_book_isbn_text_box.insert(0,book_search_text_box.get)
    book_search_text_box.delete(0,END)

add_book_button=Button(side_menu_book_frame,text='Add book',width=22,height=3,state=DISABLED,command=add_book_button_press)
add_book_button.grid(row=2,column=0,padx=1)
add_book_button.grid_propagate(False)





def submit_add_book_button_press():

    
    isbn_val=new_book_isbn_text_box.get()
    title_val=new_book_title_text_box.get()
    author_val=new_book_author_text_box.get()
    publ_val=new_book_publication_text_box.get()
    max_count_val=new_book_max_count_text_box.get()
    
    
    # if regno_val!=None and name_val!=None and phone_val!=None and hostel_val!=None:
    if len(isbn_val) and len(title_val) and len(author_val) and len(publ_val) and len(max_count_val):
    
        result=all_book_func.add_new_book(isbn_val,title_val, author_val, publ_val, max_count_val)
        if result:
            print('new book added')
            
            new_book_isbn_text_box.delete(0,END)
            new_book_title_text_box.delete(0,END)
            new_book_author_text_box.delete(0,END)
            new_book_publication_text_box.delete(0,END)
            new_book_max_count_text_box.delete(0,END)
            
            add_book_button['state']=DISABLED
            add_book_frame.grid_forget()
            book_search_text_box.delete(0,END)
        else: print('failed to add')
        
    else:
        print('empty columns')

submit_add_book_button=Button(add_book_frame,text='Submit',height=2,width=10,command=submit_add_book_button_press)
submit_add_book_button.grid(row=0,column=3,padx=10)
submit_add_book_button.grid_propagate(False)   


def cancel_add_book_button_press():
    new_book_isbn_text_box.delete(0,END)
    new_book_title_text_box.delete(0,END)
    new_book_author_text_box.delete(0,END)
    new_book_publication_text_box.delete(0,END)
    new_book_max_count_text_box.delete(0,END)
    
    add_book_frame.grid_forget()
    add_book_button['state']=DISABLED

cancel_add_book__button=Button(add_book_frame,text='Cancel',height=2,width=10,command=cancel_add_book_button_press)
cancel_add_book__button.grid(row=1,column=3)
cancel_add_book__button.grid_propagate(False)


    
    
# search button on search window
book_search_button=Button(search_book_window_frame,text='Search',width=15,height=1,command=book_search_button_press)
# setting location
book_search_button.grid(row=0,column=1,padx=3)
book_search_button.grid_propagate(False)





# search button on search window
book_search_clear_button=Button(search_book_window_frame,text='Clear',width=15,height=1,command=book_search_clear_button_press)
# setting location
book_search_clear_button.grid(row=0,column=2,padx=3)
book_search_clear_button.grid_propagate(False)











# ============================================================================================================================


# side_menu_student_frame contains all button for student related opertation like: Issue, collect etc
side_menu_student_frame=LabelFrame(side_menu_frame,width=190,height=635)
# setting location
side_menu_student_frame.grid(row=0,column=0,padx=2,pady=2)
side_menu_student_frame.grid_propagate(False)





# interact_window is subframe in main_frame
# student_interact_window_frame=LabelFrame(main_frame,text='student_interact_window_frame',width=1000,height=665,bg='#2E314B')
student_interact_window_frame=LabelFrame(main_frame,width=1000,height=665,bg='#2E314B')


# set location in main frame
# intetact_window span rest 5 columns (left most)
student_interact_window_frame.grid(row=1,column=0,columnspan=5)
student_interact_window_frame.grid_propagate(False)






# this is used to search a studetn record before issuing, collecting, updating etc
# search_student_window_frame=LabelFrame(student_interact_window_frame,text='search student window',width=985,height=50,bg='#A4ABED')
search_student_window_frame=LabelFrame(student_interact_window_frame,width=990,height=50,bg='#A4ABED')


# setting location
search_student_window_frame.grid(row=0,column=0,columnspan=2,padx=4,pady=4)
search_student_window_frame.grid_propagate(False)



# window  for issueing or collecting books, also show student details  
student_details_frame=LabelFrame(student_interact_window_frame,text='student details window',width=990,height=160,bg='#CED2FF')
# student_details_frame=LabelFrame(student_interact_window_frame,width=987,height=160,bg='#A4ABED')



# setting location
# student_details_frame.grid(row=1,column=0,padx=5)
# student_details_frame.grid_propagate(False)


# frame for book1 
book1_details_frame=Label(student_interact_window_frame,text='book 1',width=70,height=20,bg='#FFFAB5')
# book1_details_frame.grid(row=2,column=0,pady=2)
# book1_details_frame.grid_propagate(False)

# frame for book2
book2_details_frame=Label(student_interact_window_frame,text='book 2',width=69,height=20,bg='#FFFAB5')
# book2_details_frame.grid(row=2,column=1,pady=2)
# book2_details_frame.grid_propagate(False)



book1_selection=StringVar()
book2_selection=StringVar()

def get_book_isbn_with_name():
    data=all_book_func.show_book_details()
    isbn_name_list=['-'*10+'select book'+'-'*10]+[i[0]+':'+i[1] for i in data]
    
    return isbn_name_list



def set_book2_details_frame():
    
    global data
    data=all_stud_func.search_issue_record(data[0])
    
    book2_details_frame.grid(row=2,column=1,pady=2,padx=2)
    book2_details_frame.grid_propagate(False)

    
    if data[6]!='NULL' and data[6]!=None:
        
        for wid in book2_details_frame.winfo_children():
            wid.destroy()    
        global book_data
            
        book_data=all_book_func.search_book_details(data[6])
        
        book2_ISBN_label=Label(book2_details_frame,text='ISBN:',width=10,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_ISBN_label.grid(row=0,column=0,padx=2,pady=2)
        book2_ISBN_label.grid_propagate(False)

        book2_ISBN_value_label=Label(book2_details_frame,text=data[6],width=27,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_ISBN_value_label.grid(row=0,column=1,padx=2,pady=2)
        book2_ISBN_value_label.grid_propagate(False)
            
        book2_name_label=Label(book2_details_frame,text='Title:',width=10,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_name_label.grid(row=1,column=0,padx=2,pady=2)
        book2_name_label.grid_propagate(False)

        book2_name_value_label=Label(book2_details_frame,text=book_data[1],width=27,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_name_value_label.grid(row=1,column=1,padx=2,pady=2)
        book2_name_value_label.grid_propagate(False)
            

        book2_date_label=Label(book2_details_frame,text='Issued on:',width=10,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_date_label.grid(row=2,column=0,padx=2,pady=2)
        book2_date_label.grid_propagate(False)

        book2_date_value_label=Label(book2_details_frame,text=data[7],width=27,font=("Helvetica", 18),anchor="w",justify="left",bg='#FFFAB5')
        book2_date_value_label.grid(row=2,column=1,padx=2,pady=2)
        book2_date_value_label.grid_propagate(False)
            
#            make collect button visible
        collect_book2_button.grid(row=3,column=1,pady=2)
        collect_book2_button.grid_propagate(False)
        
        
    else:
        # book2_empty_label=Label(book2_details_frame,text='No book issued',width=20,font=("Helvetica", 18))
        # book2_empty_label.grid(row=0,column=0,padx=2,pady=2)
        # book2_empty_label.grid_propagate(False)
        
        
        for wid in book2_details_frame.winfo_children():
            wid.destroy()
        book2_empty_label=Label(book2_details_frame,text='No book issued',width=20,font=("Helvetica", 18),bg='#FFFAB5')
        book2_empty_label.grid(row=0,column=0,padx=2,pady=2)
        book2_empty_label.grid_propagate(False)
    
    
    #     drop down menu options
        book_options=get_book_isbn_with_name()
    
    # clicked=StringVar()
        book2_selection.set(book_options[0])
#     drop down menu
        book_option_menu=OptionMenu(book2_details_frame,book2_selection,*book_options)
        book_option_menu.grid(row=1,column=0,padx=2,pady=2)
        book_option_menu.grid_propagate(False)
        book_option_menu.config(width=62)
    
        collect_book2_button.grid_forget()
        
            
        issue_book2_button.grid(row=3,column=1,pady=1)
        issue_book2_button.grid_propagate(False)
            
    

    
def set_book1_details_frame():
    
    print('reached 1')
    
    global data
    data=all_stud_func.search_issue_record(data[0])
    
    book1_details_frame.grid(row=2,column=0,pady=2,padx=2)
    book1_details_frame.grid_propagate(False)

    
    if data[4]!='NULL' and data[4]!=None:
        
        print('reached 2')
        
        for wid in book1_details_frame.winfo_children():
            wid.destroy()    
        global book_data
        book_data=all_book_func.search_book_details(data[4])
        
        # print(data[4])
        
        book1_ISBN_label=Label(book1_details_frame,text='ISBN:',bg='#FFFAB5',width=10,font=("Helvetica", 18),anchor="w",justify="left")
        book1_ISBN_label.grid(row=0,column=0,padx=2,pady=2)
        book1_ISBN_label.grid_propagate(False)

        book1_ISBN_value_label=Label(book1_details_frame,text=data[4],bg='#FFFAB5',width=27,font=("Helvetica", 18),anchor="w",justify="left")
        book1_ISBN_value_label.grid(row=0,column=1,padx=2,pady=2)
        book1_ISBN_value_label.grid_propagate(False)
            
        book1_name_label=Label(book1_details_frame,text='Title:',bg='#FFFAB5',width=10,font=("Helvetica", 18),anchor="w",justify="left")
        book1_name_label.grid(row=1,column=0,padx=2,pady=2)
        book1_name_label.grid_propagate(False)

        book1_name_value_label=Label(book1_details_frame,text=book_data[1],bg='#FFFAB5',width=27,font=("Helvetica", 18),anchor="w",justify="left")
        book1_name_value_label.grid(row=1,column=1,padx=2,pady=2)
        book1_name_value_label.grid_propagate(False)
            

        book1_date_label=Label(book1_details_frame,text='Issued on:',bg='#FFFAB5',width=10,font=("Helvetica", 18),anchor="w",justify="left")
        book1_date_label.grid(row=2,column=0,padx=2,pady=2)
        book1_date_label.grid_propagate(False)

        book1_date_value_label=Label(book1_details_frame,text=data[5],bg='#FFFAB5',width=27,font=("Helvetica", 18),anchor="w",justify="left")
        book1_date_value_label.grid(row=2,column=1,padx=2,pady=2)
        book1_date_value_label.grid_propagate(False)
            
            
#            show collect button
        collect_book1_button.grid(row=3,column=0,pady=1)
        collect_book1_button.grid_propagate(False)
        
        
    else:
        
        for wid in book1_details_frame.winfo_children():
            wid.destroy()
        
        book1_empty_label=Label(book1_details_frame,text='No book issued',bg='#FFFAB5',width=20,font=("Helvetica", 18))
        book1_empty_label.grid(row=0,column=0,padx=2,pady=2)
        book1_empty_label.grid_propagate(False)
        
#     drop down menu options
        book_options=get_book_isbn_with_name()
    
        # clicked=StringVar()
        book1_selection.set(book_options[0])
#     drop down menu
        book_option_menu=OptionMenu(book1_details_frame,book1_selection,*book_options)
        book_option_menu.grid(row=1,column=0,padx=2,pady=2)
        book_option_menu.grid_propagate(False)
        book_option_menu.config(width=63)
    
        collect_book1_button.grid_forget()
            
        issue_book1_button.grid(row=3,column=0,pady=1)
        issue_book1_button.grid_propagate(False)
    



# function for collect_book1_button
def collect_book1_button_press():
    all_stud_func.collect_book1(data[0])
    


    set_book1_details_frame()
    
# function for collect_book2_button
def collect_book2_button_press():
    all_stud_func.collect_book2(data[0])

    set_book2_details_frame()

    
def issue_book1_button_press():
#     get string from book1_selection
    book1_choice_str=book1_selection.get()
    
#     if string matched an isbn then issue
    if book1_choice_str!='-'*10+'select book'+'-'*10:
        
#         seperate book name from isbn
        book_isbn=str(book1_choice_str).split(':')[0]
        # print(book_isbn)
#         issue book
        all_stud_func.issue_book1(book_isbn,data[0])
    
    
    set_book1_details_frame()

issue_book1_button=Button(student_interact_window_frame,text='Issue book',width=67,height=5,bg='#A4F19B',command=issue_book1_button_press)
# issue_book1_button.grid(row=3,column=0,pady=1)
# issue_book1_button.grid_propagate(False)



def issue_book2_button_press():
#     get string from book1_selection
    book2_choice_str=book2_selection.get()
    
#     if string matched an isbn then issue
    if book2_choice_str!='-'*10+'select book'+'-'*10:
        
#         seperate book name from isbn
        book_isbn=str(book2_choice_str).split(':')[0]
        print(book_isbn)
#         issue book
        all_stud_func.issue_book2(book_isbn,data[0])
    
    set_book2_details_frame()
        
        

issue_book2_button=Button(student_interact_window_frame,text='Issue book',width=66,height=5,bg='#A4F19B',command=issue_book2_button_press)
# issue_book2_button.grid(row=3,column=1,pady=1)
# issue_book2_button.grid_propagate(False)

collect_book1_button=Button(student_interact_window_frame,text='collect book',width=67,height=5,bg='#FFBAA7',command=collect_book1_button_press)
# collect_book1_button.grid(row=3,column=0,pady=1)
# collect_book1_button.grid_propagate(False)

collect_book2_button=Button(student_interact_window_frame,text='collect book',width=66,height=5,bg='#FFBAA7',command=collect_book2_button_press)
# collect_book2_button.grid(row=3,column=1,pady=1)
# collect_book2_button.grid_propagate(False)

# text box on search window to entere registration number
student_search_text_box=Entry(search_student_window_frame,text='enter reg. no.',width=20,font=("Helvetica", 15))
# setting location
student_search_text_box.grid(row=0,column=0,padx=6,pady=9)
student_search_text_box.grid_propagate(False)








# frame for updatinf details of student
update_student_frame=LabelFrame(student_interact_window_frame,text='update student frame',width=985,height=160,bg='#BFFF9D')
update_student_frame.grid_propagate(False)
# # setting location
# update_student_frame.grid(row=1,column=0,columnspan=2,padx=5)
# update_student_frame.grid_propagate(False)

update_name_label=Label(update_student_frame,text='Name:',width=20,font=("Helvetica", 18),bg='#BFFF9D',anchor="w",justify="left")
update_name_label.grid(row=0,column=0,padx=10,pady=10)
update_name_label.grid_propagate(False)
        
update_name_text_box=Entry(update_student_frame,width=30,font=("Helvetica", 17))
update_name_text_box.grid(row=0,column=1)
update_name_text_box.grid_propagate(False)


update_Phono_label=Label(update_student_frame,text='Phone no.:',width=20,font=("Helvetica", 18),bg='#BFFF9D',anchor="w",justify="left")
update_Phono_label.grid(row=1,column=0,padx=10,pady=10)
update_Phono_label.grid_propagate(False)
        
update_phono_text_box=Entry(update_student_frame,width=30,font=("Helvetica", 17))
update_phono_text_box.grid(row=1,column=1)
update_phono_text_box.grid_propagate(False)


update_hostel_label=Label(update_student_frame,text='Hosteler:',width=20,font=("Helvetica", 18),bg='#BFFF9D',anchor="w",justify="left")
update_hostel_label.grid(row=2,column=0,padx=10,pady=10)
update_hostel_label.grid_propagate(False)
        
update_hostel_text_box=Entry(update_student_frame,width=30,font=("Helvetica", 17))
update_hostel_text_box.grid(row=2,column=1)
update_hostel_text_box.grid_propagate(False)

    


def update_student_press():
    student_details_frame.grid_forget()
    update_student_frame.grid(row=1,column=0,columnspan=2,padx=4,pady=4)
    update_student_frame.grid_propagate(False)
    
    update_name_text_box.delete(0,END)
    update_phono_text_box.delete(0,END)
    update_hostel_text_box.delete(0,END)
    
    update_name_text_box.insert(0,data[1])
    update_phono_text_box.insert(0,data[2])
    update_hostel_text_box.insert(0,data[3])


# button for updating student name, etc. 
update_student_button=Button(side_menu_student_frame,text='Update Record',width=22,height=3,state=DISABLED,command=update_student_press)
update_student_button.grid(row=1,column=0,padx=1)
update_student_button.grid_propagate(False)


# frame for adding new student
add_student_frame=LabelFrame(student_interact_window_frame,text='new student window',width=985,height=200,bg='#CED2FF')
add_student_frame.grid_propagate(False)
# add_student_frame.grid(row=1,column=0,columnspan=2,padx=5)
# add_student_frame.grid_propagate(False)

# new student reg.no. label
new_student_regno_label=Label(add_student_frame,text='Reg.No.:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
new_student_regno_label.grid(row=0,column=0,padx=10,pady=10)
new_student_regno_label.grid_propagate(False)

# new student reg.no. text box
new_student_regno_text_box=Entry(add_student_frame,width=30,font=("Helvetica", 18))
new_student_regno_text_box.grid(row=0,column=1)
new_student_regno_text_box.grid_propagate()

# new student name label
new_student_name_label=Label(add_student_frame,text='Name:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
new_student_name_label.grid(row=1,column=0,padx=10,pady=10)
new_student_name_label.grid_propagate(False)
        

# new student name text box
new_student_name_text_box=Entry(add_student_frame,width=30,font=("Helvetica", 18))
new_student_name_text_box.grid(row=1,column=1)
new_student_name_text_box.grid_propagate(False)

# new student phone no label
new_student_Phono_label=Label(add_student_frame,text='Phone no.:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
new_student_Phono_label.grid(row=2,column=0,padx=10,pady=10)
new_student_Phono_label.grid_propagate(False)
        
#new student phone text box
new_student_phono_text_box=Entry(add_student_frame,width=30,font=("Helvetica", 18))
new_student_phono_text_box.grid(row=2,column=1)
new_student_phono_text_box.grid_propagate(False)

# new student hostel label
new_student_hostel_label=Label(add_student_frame,text='Hosteler:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
new_student_hostel_label.grid(row=3,column=0,padx=10,pady=10)
new_student_hostel_label.grid_propagate(False)
        
# new student hostel text box
new_student_hostel_text_box=Entry(add_student_frame,width=30,font=("Helvetica", 18))
new_student_hostel_text_box.grid(row=3,column=1)
new_student_hostel_text_box.grid_propagate(False)



def remove_student_result():
    student_details_frame.grid_forget()
    for wid in student_details_frame.winfo_children():
        wid.destroy()
        
    update_student_button['state']=DISABLED
    update_student_frame.grid_forget()
    add_student_button['state']=DISABLED
    
    book1_details_frame.grid_forget()
    book2_details_frame.grid_forget()
    student_search_text_box.delete(0,END)
    # student_search_button['state']=NORMAL
    
    issue_book1_button.grid_forget()
    issue_book2_button.grid_forget()
    collect_book1_button.grid_forget()
    collect_book2_button.grid_forget()
    
    for wid in book1_details_frame.winfo_children():
        wid.destroy()
    for wid in book2_details_frame.winfo_children():
        wid.destroy()

# funtion of student_search_clear_button
def student_search_clear_button_press():
    remove_student_result()
    student_search_button['state']=NORMAL

    
    


# button for searching student record
def student_search_button_press(temp=0):
    
    if temp:
        reg_no=temp
    else:
        reg_no=student_search_text_box.get()
        
        if len(reg_no)==0:
            student_search_text_box.insert(0,'Please enter reg. no.')
            return
    global data
    data=all_stud_func.search_issue_record(reg_no)
    
    if data:
        
        student_search_button['state']=DISABLED
        
        # student_search_clear_button_press()
        remove_student_result()
        
        student_details_frame.grid(row=1,column=0,columnspan=2,padx=4,pady=4)
        student_details_frame.grid_propagate(False)
        
        update_student_frame.grid_forget()
        update_student_button['state']=NORMAL
        

    
    
    
        name_label=Label(student_details_frame,text='Name:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        name_label.grid(row=0,column=0,padx=10,pady=10)
        name_label.grid_propagate(False)
        
        name_value_label=Label(student_details_frame,text=data[1],bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        name_value_label.grid(row=0,column=1)
        name_value_label.grid_propagate(False)

        Phono_label=Label(student_details_frame,text='Phone no.:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        Phono_label.grid(row=1,column=0,padx=10,pady=10)
        Phono_label.grid_propagate(False)
        
        phono_value_label=Label(student_details_frame,text=data[2],bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        phono_value_label.grid(row=1,column=1)
        phono_value_label.grid_propagate(False)

        hostel_label=Label(student_details_frame,text='Hosteler:',bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        hostel_label.grid(row=2,column=0,padx=10,pady=10)
        hostel_label.grid_propagate(False)
        
        
        hostel_value_label=Label(student_details_frame,text=data[3],bg='#CED2FF',width=20,font=("Helvetica", 18),anchor="w",justify="left")
        hostel_value_label.grid(row=2,column=1)
        hostel_value_label.grid_propagate(False)
        

        set_book1_details_frame()            
        set_book2_details_frame()

            
    else:
        student_search_text_box.delete(0,END)
        student_search_text_box.insert(0,'no record found')
        add_student_button['state']=NORMAL







def submit_student_update_button_press():
    global data

    reg_val=data[0]
    name_val=update_name_text_box.get()
    phone_val=update_phono_text_box.get()
    hostel_val=update_hostel_text_box.get()
    
    student_search_button_press(data[0])
    all_stud_func.update_student_record(reg_val,name_val,phone_val,hostel_val)
    update_student_frame.grid_forget()
    

    student_search_button_press(reg_val)
    # student_search_button_press(data[0])
    

submit_student_update_button=Button(update_student_frame,text='Submit',height=2,width=10,command=submit_student_update_button_press)
submit_student_update_button.grid(row=0,column=3,padx=10)
submit_student_update_button.grid_propagate(False)            
            

def delete_student_button_press():
    
    val=all_stud_func.delete_student(data[0])
    print(val)
    if val==1:
        print('deleted')
        student_search_clear_button_press()
    if val==0:
        print('cannot delete book issue')
        
    

    
    
# button for deleting student
delete_student_button=Button(update_student_frame,text='Delete Student',height=2,width=12,command=delete_student_button_press)
delete_student_button.grid(row=1,column=4,padx=10)
delete_student_button.grid_propagate(False)        


def cancel_student_update_button_press():
    update_name_text_box.delete(0,END)
    update_phono_text_box.delete(0,END)
    update_hostel_text_box.delete(0,END)
    
    student_search_button_press(data[0])
    update_student_frame.grid_forget()

cancel_student_update_button=Button(update_student_frame,text='Cancel',height=2,width=10,command=cancel_student_update_button_press)
cancel_student_update_button.grid(row=1,column=3)
cancel_student_update_button.grid_propagate(False)




def add_student_button_press():
    add_student_frame.grid(row=1,column=0,columnspan=2,padx=5)
    add_student_frame.grid_propagate(False)
    # new_student_name_text_box.insert(0,student_search_text_box.get)

add_student_button=Button(side_menu_student_frame,text='Add student',width=22,height=3,state=DISABLED,command=add_student_button_press)
add_student_button.grid(row=2,column=0,padx=1)
add_student_button.grid_propagate(False)





def submit_add_student_button_press():

    regno_val=new_student_regno_text_box.get()
    name_val=new_student_name_text_box.get()
    phone_val=new_student_phono_text_box.get()
    hostel_val=new_student_hostel_text_box.get()
    
    
    # if regno_val!=None and name_val!=None and phone_val!=None and hostel_val!=None:
    if len(regno_val) and len(name_val) and len(phone_val) and len(hostel_val):
    
        result=all_stud_func.add_new_student(regno_val,name_val,phone_val,hostel_val)
        if result:
            print('new student added')
            
            new_student_regno_text_box.delete(0,END)
            new_student_name_text_box.delete(0,END)
            new_student_phono_text_box.delete(0,END)
            new_student_hostel_text_box.delete(0,END)
            add_student_button['state']=DISABLED
            add_student_frame.grid_forget()
            student_search_text_box.delete(0,END)
        else: print('failed to add')
        
    else:
        print('empty columns')

submit_add_student_button=Button(add_student_frame,text='Submit',height=2,width=10,command=submit_add_student_button_press)
submit_add_student_button.grid(row=0,column=3,padx=10)
submit_add_student_button.grid_propagate(False)   


def cancel_add_student_button_press():
    new_student_regno_text_box.delete(0,END)
    new_student_name_text_box.delete(0,END)
    new_student_phono_text_box.delete(0,END)
    new_student_hostel_text_box.delete(0,END)
    
    add_student_frame.grid_forget()
    add_student_button['state']=DISABLED

cancel_add_student__button=Button(add_student_frame,text='Cancel',height=2,width=10,command=cancel_add_student_button_press)
cancel_add_student__button.grid(row=1,column=3)
cancel_add_student__button.grid_propagate(False)


    
    
# search button on search window
student_search_button=Button(search_student_window_frame,text='Search',width=15,height=1,command=student_search_button_press)
# setting location
student_search_button.grid(row=0,column=1,padx=3)
student_search_button.grid_propagate(False)





# search button on search window
student_search_clear_button=Button(search_student_window_frame,text='Clear',width=15,height=1,command=student_search_clear_button_press)
# setting location
student_search_clear_button.grid(row=0,column=2,padx=3)
student_search_clear_button.grid_propagate(False)





# function for student_ops_button
def student_ops_button_press():
#     on click ENABLE book_ops_button
    book_ops_button['state']=NORMAL
#     on click DISABLE book_ops_button
    student_ops_button['state']=DISABLED
    
    
#     on click remove side_menu_book_frame
    side_menu_book_frame.grid_forget()
    
#     on click show side_menu_student_frame
    side_menu_student_frame.grid(row=0,column=0,padx=2,pady=2)
    side_menu_student_frame.grid_propagate(False)
    
    #     hide books_interact_window_frame
    books_interact_window_frame.grid_forget()
    
#     show books_interact_window_frame
    student_interact_window_frame.grid(row=1,column=0,columnspan=5)
    student_interact_window_frame.grid_propagate(False)
    

# function for book_ops_button
def book_ops_button_press():
#     on click DISABLE book_ops_button
    book_ops_button['state']=DISABLED
#     on click ENABLE student_ops_button
    student_ops_button['state']=NORMAL
    
#     on click remove side_menu_student_frame
    side_menu_student_frame.grid_forget()
    
    
#     on click show side_menu_book_frame
    side_menu_book_frame.grid(row=0,column=0,padx=2,pady=2)
    side_menu_book_frame.grid_propagate(False)
    
#     hide student_interact_window_frame
    student_interact_window_frame.grid_forget()
    
#     show books_interact_window_frame
    books_interact_window_frame.grid(row=1,column=0,columnspan=5)
    books_interact_window_frame.grid_propagate(False)

# buttons to toggle student operations of book operations
# student_ops button define
student_ops_button=Button(main_frame,text='Students operations',width=82,command=student_ops_button_press,state=DISABLED)


# setting location for student_ops_button
# student_ops_button span 3 columns of main_frame (left most)
student_ops_button.grid(row=0,column=0,columnspan=3)

# book_ops button define
book_ops_button=Button(main_frame,text='Books operations',width=81,command=book_ops_button_press)


# setting location for book_ops_button
# book_ops_button span 3 columns of main_frame (right most)
book_ops_button.grid(row=0,column=3,columnspan=3)







root.mainloop()



# In[ ]:




