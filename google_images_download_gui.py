from google_images_download import google_images_download
import tkinter
from tkinter import *
from tkinter import messagebox
import os
#------------CENSORSHIPS----------# 1st Feature
#Appending the list of words into array
def append_txt_to_array(txt_file):
    word_list = []
    f = open(txt_file,"r")
    for x in f:
        word_list.append(x.rstrip("\n").lower())
        word_list = list(set(word_list))
    f.close()
    return word_list

#------HISTORY KEYWORD-----# 2nd Feature
def store_keyword_to_history(keyword_array):
    f = open("history_keyword.txt","w+")
    for keyword in keyword_array:
        f.write("%s\n"%keyword)
    print("storing to history done")
    f.close()
    
#--------------GUI------------------# 3rd Feature
def mainMenu():
    #take all the variables
    global searchHistory
    global mainMenuCounter
    global Records
    global formatList
    global userRightList
    global languageList
    global sizeList
    global inputOption

    #main menu GUI size and parameter
    mainMenu = Tk()
    mainMenu.title("Google Images Download")
    mainMenu.geometry('550x320')
    mainMenu.resizable(width=False, height=False)
    mainMenu.tk.call('tk', 'scaling', 1.4)

    
    #++++row 0+++++ Keyword
    l_Keyword = Label(mainMenu, text="Keyword: ").grid(row=0, sticky=W,pady=5)  #keyword label (text)
    e_Keyword = Entry(mainMenu,width=20)                                                                         #entry for keyword (entry box)
    e_Keyword.grid(row=0, column=1,pady=5,sticky='ew')                                                 #shape and position of the entry box

    defaultSearchHistoryValue = StringVar(mainMenu)                                                        #Variable to store the default value for searchHistory drop down button
    file_is_empty = check_empty_file("history_keyword.txt")                                            #Check whether text file is empty
    if file_is_empty==False:                                                                                                           # If it is not empty set execute, if it is empty do not show the drop down button
        defaultSearchHistoryValue.set(searchHistory[0])                                                         
        l_Keyword = Label(mainMenu,text="Search History: ").grid(row=0,column=2,pady=5)
        om_SearchHistory = OptionMenu(mainMenu,defaultSearchHistoryValue,*searchHistory)        #drop down button for searched word
        om_SearchHistory.grid(row=0,column=3)                                                                                                #drop down button position
    
    #+++++row 1++++ Input Keyword choice
    l_InputOption = Label(mainMenu,text="Search by: ").grid(row=1, column=0,pady=5,sticky=W)    
    inputOption = ["Entry","History"]                                                                                                                   #list of possible input option
    defaultInputOption = StringVar(mainMenu)                                                                        
    defaultInputOption.set(inputOption[0])                                                                                                       #default input option -> Entry
    om_InputOption = OptionMenu(mainMenu, defaultInputOption,*inputOption)                              #drop down button
    om_InputOption.grid(row=1,column=1,sticky='ew')

    #+++++row1++++ checkbox Numbering
    varNumberingOption = IntVar()                                                                                                                     #checkbox value (0 or 1)
    varNumberingOption.set(0)                                                                                                                            #set the checkbox to empty
    checkBoxNumberingOption = Checkbutton(mainMenu,  text="No Numbering",variable= varNumberingOption,).grid(row=1,column=2) #initialize checkbox
    
    #+++++row 2+++++ Limit choice 
    l_Limit = Label(mainMenu,text="Limit: ").grid(row=2,column=0,pady=5,sticky=W)
    e_Limit = Entry(mainMenu, width=20)
    e_Limit.grid(row=2,column=1,pady=5,sticky='ew')
     #the checkbox
    varLimitOption = IntVar()
    varLimitOption.set(0)
    checkBoxInputOption = Checkbutton(mainMenu,  text="On Parameter",variable= varLimitOption,).grid(row=2,column=2)
    

   #++++++row 3++++++ File extension choice
    l_FormatOption = Label(mainMenu, text="Format Option: ").grid(row=3, column=0, pady=5, sticky=W)
    defaultFormatOption = StringVar(mainMenu)
    defaultFormatOption.set(formatList[0])
    om_FormatOption = OptionMenu(mainMenu, defaultFormatOption,*formatList)
    om_FormatOption.grid(row=3,column=1,pady=5,sticky='ew')
    #checkbox
    varFormatOption = IntVar()
    varFormatOption.set(0)
    checkBoxFormatOption = Checkbutton(mainMenu,  text="On Parameter",variable= varFormatOption,).grid(row=3,column=2)

    #++++++row 4++++++ user right choice 
    l_UserRightOption = Label(mainMenu, text="User Right: ").grid(row=4, column=0, pady=5, sticky=W)
    defaultUserRightOption = StringVar(mainMenu)
    defaultUserRightOption.set(userRightList[0])                                                                                                #user right choice drop down button value
    om_UserRightOption = OptionMenu(mainMenu, defaultUserRightOption,*userRightList)
    om_UserRightOption.configure(width=20)
    om_UserRightOption.grid(row=4,column=1,pady=5,sticky=W)
    #checkbox
    varUserRightOption = IntVar()
    varUserRightOption.set(0)
    checkBoxUserRightOption = Checkbutton(mainMenu,  text="On Parameter",variable= varUserRightOption,).grid(row=4,column=2)

    #++++++row 5++++++ language
    l_LanguageOption = Label(mainMenu, text="Language: ").grid(row=5, column=0, pady=5, sticky=W)
    defaultLanguageOption = StringVar(mainMenu)
    defaultLanguageOption.set(languageList[0])
    om_LanguageOption = OptionMenu(mainMenu, defaultLanguageOption,*languageList)
    om_LanguageOption.configure(width=20)
    om_LanguageOption.grid(row=5,column=1,pady=5,sticky=W)
    #checkbox
    varLanguageOption = IntVar()
    varLanguageOption.set(0)
    checkBoxLanguageOption = Checkbutton(mainMenu,  text="On Parameter",variable= varLanguageOption,).grid(row=5,column=2)

    #++++++row 5++++++ size
    l_SizeOption = Label(mainMenu, text="Size: ").grid(row=6, column=0, pady=5, sticky=W)
    defaultSizeOption = StringVar(mainMenu)
    defaultSizeOption.set(sizeList[0])
    om_SizeOption = OptionMenu(mainMenu, defaultSizeOption,*sizeList)
    om_SizeOption.configure(width=20)
    om_SizeOption.grid(row=6,column=1,pady=5,sticky=W)
    #checkbox
    varSizeOption = IntVar()
    varSizeOption.set(0)
    checkBoxSizeOption = Checkbutton(mainMenu,  text="On Parameter",variable= varSizeOption,).grid(row=6,column=2)

    def execute():
        global Records
        global censored_word
        global searchHistory
        global inputOption
        try:
            #Keywords parameter storing (store into dictionary)
            var_inputOption = defaultInputOption.get() #get the input option 
            keywords = ""                                                       #variable to store the keywords so it can be stored into searched history txt file
            if var_inputOption == inputOption[0]:           #if the input option is -> Entry
                entry = e_Keyword.get().lower()             
                validated = entry_validation(entry, censored_word)
                keywords = entry
                if validated == True:                                       #if the keyword is not in the list of censored word
                    if keywords=="":
                            messagebox.showinfo("WARNING!","Keyword must not be empty\nPlease enter something")
                            return
                    else:    
                        store_parameter_value_to_dictionary("keywords",entry,Records)
                else:                                                                   #if the keyword is in the list of censored word
                    messagebox.showinfo("WARNING!","You have entered keywords which are OBSCENE\nWe cannot process your request")
                    return
            else:                                                                       #if the input option is -> Search by History
                var_searchHistory = defaultSearchHistoryValue.get()
                if var_searchHistory=="":
                        messagebox.showinfo("WARNING!","History is empty\nPlease use the entry")
                        return
                store_parameter_value_to_dictionary("keywords",var_searchHistory,Records)
                
            #Numbering parameter storing (store into dictionary)
            if check_box_state(varNumberingOption)==True:
                Records["no_numbering"]=True
                
             #Limit parameter storing (store into dictionary)
            limitEntry = e_Limit.get()
            check_store(varLimitOption,"limit",limitEntry,Records)
            
            #Format parameter storing (store into dictionary)
            var_formatOption = defaultFormatOption.get()
            check_store(varFormatOption,"format",var_formatOption,Records)
            
            #User Right parameter storing (store into dictionary)
            var_userRightOption = defaultUserRightOption.get()
            check_store(varUserRightOption,"usage_rights",var_userRightOption,Records)
            
            #Language parameter storing (store into dictionary)
            var_languageOption = defaultLanguageOption.get()
            check_store(varLanguageOption,"language",var_languageOption,Records)
            
            #Size parameter storing (store into dictionary)
            var_sizeOption = defaultSizeOption.get()
            check_store(varSizeOption,"size",var_sizeOption,Records)
            
            #--->download the image---->
            download_images(Records)                                                                #takes in Records(dictionary) as argument for download
            messagebox.showinfo("NOTIFICATION","Download success")

            #if input option is -> Entry, then store the keyword into searchHistory array and txt file
            if var_inputOption == inputOption[0]:
                searchHistory.insert(0,keywords)
                store_keyword_to_history(searchHistory)
                searchHistory = append_txt_to_searchHistory()
                om_SearchHistory = OptionMenu(mainMenu,defaultSearchHistoryValue,*searchHistory)
                om_SearchHistory.grid(row=0,column=3)

            #if previously the search history file is empty (searchHistory box did not show)
            #initialize (show) the search history drop down button
            if file_is_empty==True:
                defaultSearchHistoryValue.set(searchHistory[0])
                l_Keyword = Label(mainMenu,text="Search History: ").grid(row=0,column=2,pady=5)

            #re-initializing the searchHistory drop down button
            #updating items in the searchHistory drop down button to include the keyword that has just been entered
            defaultSearchHistoryValue.set(searchHistory[0])
            om_SearchHistory = OptionMenu(mainMenu,defaultSearchHistoryValue,*searchHistory)
            om_SearchHistory.grid(row=0,column=3)
        except ValueError: #for wrong value error handling
            messagebox.showinfo("WARNING!","There is some value entered not intended for it's field\nPlease check your input again")

    #++++last row+++++ Enter button
    enterEntry = Button(mainMenu, text= "Enter", command=execute,bg="yellow")
    enterEntry.grid(row=7,column=1,columnspan=2,sticky='nesw')

#HELP functions

#return the state of the checkbox True (Checked) or False (unChecked)
def check_box_state(checkBoxVariable):
    if checkBoxVariable.get()==1:
        return True
    return False

#function to store the parameters into the record dictionary for images downloading
def store_parameter_value_to_dictionary (parameter,value,dictionary):
    dictionary[parameter] = value

#check for checkbox state
#if checked then store the parameter into the dictionary
def check_store(checkBoxVariable,parameter,value,dictionary):
    if check_box_state(checkBoxVariable)==True:
        store_parameter_value_to_dictionary(parameter,value,dictionary)

#function to download images
def download_images(dictionary):
    global Records
    response = google_images_download.googleimagesdownload()
    arguments = Records
    paths = response.download(arguments)

#check whether the given file is empty or not
def check_empty_file(txt_file):
    if  os.stat(txt_file).st_size==0:
        return True
    return False

#check keywords in word list
def entry_validation(keywords,word_list):
    for word in word_list:
        if word == keywords.lower():
            return False
    return True

#taking the word from each line of the text file and store it into variable called "searchHistory"
def append_txt_to_searchHistory():
    word_list = []
    f = open('history_keyword.txt',"r")
    counter=1
    for x in f:
        if counter <=10:
            word_list.append(x.rstrip("\n").lower())
            word_list = list(set(word_list))
            counter+=1
    f.close()
    return word_list

#----------------MAIN-----------------#
Records = {}
inputOption=[]

#Parameters value 
formatList = ["jpg", "gif", "png", "bmp", "svg", "webp", "ico", "raw"]
userRightList =["labeled-for-reuse-with-modifications","labeled-for-reuse","labeled-for-noncommercial-reuse-with-modification","labeled-for-nocommercial-reuse"]
languageList = ["Arabic", "Chinese (Simplified)", "Chinese (Traditional)", "Czech", "Danish", "Dutch", "English", "Estonian. Finnish", "French", "German", "Greek", "Hebrew", "Hungarian", "Icelandic", "Italian", "Japanese", "Korean", "Latvianm", "Lithuanian", "Norwegian", "Portuguese", "Polish", "Romanian", "Russian", "Spanish", "Swedish", "Turkish"]
sizeList =["large", "medium", "icon", ">400*300", ">640*480", ">800*600", ">1024*768", ">2MP", ">4MP", ">6MP", ">8MP", ">10MP", ">12MP", ">15MP", ">20MP", ">40MP", ">70MP"]

#Retrieve all previously searched word from search history txt and store it to searchHistory as an array
#Store list of censored word to censored_word array
searchHistory = append_txt_to_searchHistory()
censored_word = append_txt_to_array("censored_list_of_words.txt")

#initialize the main gui
mainMenu()

