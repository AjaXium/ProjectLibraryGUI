import os
import tkinter as tk
import customtkinter as customtk
from PIL import Image
from CTkTable import CTkTable
from custom_hovertip import CustomTooltipLabel

signedInId = None
errorText = None
addUserCanvas = None
addNewBookCanvas = None
showUsersFrame = None
showUsersFrame2 = None
showUsersFrame3 = None
booksTableScrollableFrame = None
showBookBorrowHistoryScrollabeFrame = None
miniSideBarLabel = None
isbnOfBookToBorrowEntry = None
suspendUserBotFrame = None
suspendUserBotFrame2 = None
isbnEntry = None
unitsToAddEntry = None
sideBarLabel = None
backButton = None
suspendIdEntry = None; unsuspendUserBotFrame = None; unsuspendIdEntry = None
welcomeToDashboardMessageLabel = None
helloAdminMessageLabel = None
borrowBookBotFrame = None
helloStudentMessageLabel = None
addBookToExistingTitleBotFrame = None
booksTableScrollableFrame2 = None
isbnOfBookToReturnEntry = None
showStudentsPastDaysScrollableFrame = None
usersButtonList = []
booksButtonList = []
addUserFieldsList = []
addUserErrorTextsList = []
usersList = []
booksList = []
borrowedBooksList = []
studentsPastDaysList = []
addNewBookFieldsList = []
suspendedUsersList = []
bookBorrowHistoryList = []
studentMenuButtons = []
othersMenuButtonsList = []


#App Frame
app = customtk.CTk(fg_color="white")
app.resizable(False, False)
app.geometry("800x600+350+150")
app.title("Library Application")

#Adding images
loginImage = customtk.CTkImage(Image.open("images/loginImage.png"), size=(800, 600))
exitIcon = customtk.CTkImage(Image.open("images/exitIcon.png"), size=(20, 20))
sideImage = customtk.CTkImage(Image.open("images/sideImage.png"), size=(234, 600))
miniSideImage = customtk.CTkImage(Image.open("images/miniSideImage.png"), size=(75, 600))
logOutImage = customtk.CTkImage(Image.open("images/logOutIcon.png"), size=(20, 20))
addUserIcon = customtk.CTkImage(Image.open("images/addUserIcon.png"), size=(73, 73))
addUserIcon2 = customtk.CTkImage(Image.open("images/addUserIcon.png"), size=(20, 20))
addBookIcon = customtk.CTkImage(Image.open("images/addBookIcon.png"), size=(100, 73))
showAllBooksIcon = customtk.CTkImage(Image.open("images/showAllBooksIcon.png"), size=(90, 40))
bookBorrowHistoryIcon = customtk.CTkImage(Image.open("images/bookBorrowHistoryIcon.png"), size=(90, 100))
suspendUserIcon = customtk.CTkImage(Image.open("images/suspendUserIcon.png"), size=(62, 73))
showAllUsersIcon = customtk.CTkImage(Image.open("images/showAllUsersIcon.png"), size=(90, 50))
unsuspendUserIcon = customtk.CTkImage(Image.open("images/unsuspendUserIcon.png"), size=(77, 73))
userIcon = customtk.CTkImage(Image.open("images/userIcon.png"), size=(30, 30))
booksIcon = customtk.CTkImage(Image.open("images/bookIcon.png"), size=(30, 30))
othersIcon = customtk.CTkImage(Image.open("images/othersIcon.png"), size=(30, 30))
libraryLogoImage = customtk.CTkImage(Image.open("images/libraryLogo.png"), size=(120, 120))
borrowBookIcon = customtk.CTkImage(Image.open("images/borrowBookIcon.png"), size=(100, 120))
returnBookIcon = customtk.CTkImage(Image.open("images/returnBookIcon.png"), size=(80, 60))
bookReturnPast7DaysIcon = customtk.CTkImage(Image.open("images/bookReturnPast7DaysIcon.png"), size=(85, 60))
backArrowIcon = customtk.CTkImage(Image.open("images/backArrowIcon.png"), size=(40, 40))
addBookToExistingTitleIcon = customtk.CTkImage(Image.open("images/addBookToExistingTitleIcon.png"), size=(80, 80))


#Useful Functions

#Function that checks if an id exists at all
def doesIdExist(id):
    with open('creds.txt', 'r') as credsFile:
        for line in credsFile:
            wordList = line.split(' -- ')   
            if wordList[0] == ("ID:" + id):
                return True
    return False

#Function to check if the pass matches the id
def doesPassMatchId(id, password):
    with open('creds.txt', 'r') as credsFile:
        for line in credsFile:
            wordList = line.split(' -- ')
            for i in range(len(wordList)):
                if ("ID:" + id) == wordList[i]:
                    if ("pass:" + password) == wordList[i+1] or ("pass:" + password + "\n") == wordList[i+1]:
                        return True
    return False
 
#Function to process a click on the log out button
def onLogOutButtonClick():
    showUsersMenuButtons(False)
    showBooksMenuButtons(False)
    showStudentMenuButtons(False)
    showOthersMenuButtons(False)
    if suspendUserBotFrame2 != None:
        suspendUserBotFrame2.place_forget()
    if sideBarLabel != None:
     sideBarLabel.place_forget()
    if helloAdminMessageLabel != None:
        helloAdminMessageLabel.place_forget()
    if welcomeToDashboardMessageLabel != None:
        welcomeToDashboardMessageLabel.place_forget()
    if addUserCanvas != None:
        addUserCanvas.place_forget()
    if showUsersFrame != None:
        showUsersFrame.place_forget()
    if showUsersFrame2 != None:
        showUsersFrame2.place_forget()
    if suspendUserBotFrame != None:
        suspendUserBotFrame.place_forget()
    if showUsersFrame3 != None:
        showUsersFrame3.place_forget()
    if unsuspendUserBotFrame != None:
        unsuspendUserBotFrame.place_forget()
    if addNewBookCanvas != None:
        addNewBookCanvas.place_forget()
    if miniSideBarLabel != None:
        miniSideBarLabel.place_forget()
    if booksTableScrollableFrame != None:
        booksTableScrollableFrame.place_forget()
    if showBookBorrowHistoryScrollabeFrame != None:
        showBookBorrowHistoryScrollabeFrame.place_forget()
    if logOutButton != None:
        logOutButton.place_forget()
    if helloStudentMessageLabel != None:
        helloStudentMessageLabel.place_forget()
    if booksTableScrollableFrame2 != None:
        booksTableScrollableFrame2.place_forget()
    if borrowBookBotFrame != None:
        borrowBookBotFrame.place_forget()
    if backButton != None:
        backButton.place_forget()
    if addBookToExistingTitleBotFrame != None:
        addBookToExistingTitleBotFrame.place_forget()
    if showStudentsPastDaysScrollableFrame != None:
        showStudentsPastDaysScrollableFrame.place_forget()
    loginFrame.place(relx = 0.5, rely = 0.5, anchor = "center")
    loginBglabel.place(relx = 0, rely = 0)
    exitButton.place(x= 700, y= 550, anchor="center")

#Function to show (True) or hide (False) Users Menu buttons
def showUsersMenuButtons(bool):
    if bool:
        usersButtonList[0].place(relx = 0.5, rely = 0.4, anchor = "center")
        usersButtonList[1].place(relx = 0.8, rely = 0.4, anchor = "center")
        usersButtonList[2].place(relx = 0.5, rely = 0.75, anchor = "center")
        usersButtonList[3].place(relx = 0.8, rely = 0.75, anchor = "center")
    else:
        for button in usersButtonList:
            button.place_forget()

#Function to show (True) or hide (False) Student Menu buttons
def showStudentMenuButtons(bool):
    if bool:
        studentMenuButtons[0].place(relx = 0.2, rely = 0.35, anchor = "center")
        studentMenuButtons[1].place(relx = 0.5, rely = 0.35, anchor = "center")
    else:
        for button in studentMenuButtons:
            button.place_forget()

#Function to show (True) or hide (False) Book Menu buttons
def showBooksMenuButtons(bool):
    if bool:
        booksButtonList[0].place(relx = 0.5, rely = 0.4, anchor = "center")
        booksButtonList[1].place(relx = 0.8, rely = 0.4, anchor = "center")
        booksButtonList[2].place(relx = 0.5, rely = 0.75, anchor = "center")
        booksButtonList[3].place(relx=0.647, rely=0.575, anchor="center")

    else:
        for button in booksButtonList:
            button.place_forget()

#Function that creates are you sure you wanna exit pop up
def showAreYouSurePopup():
    def exitApp():
        window.destroy()
        app.destroy()
    def dontExitApp():
        window.destroy()
    window = customtk.CTk()
    window.title("Exit PopUp")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="Are you sure you want to Exit the App?", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    yesButton = customtk.CTkButton(window, text="Yes", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitApp)
    yesButton.place(relx = 0.7, rely = 0.6, anchor="center")
    noButton = customtk.CTkButton(window, text="No", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=dontExitApp)
    noButton.place(relx = 0.3, rely = 0.6, anchor="center")

#Function to process Users button click
def onUsersButtonClick():
    showOthersMenuButtons(False)
    showBooksMenuButtons(False)
    showUsersMenuButtons(True)
    if addUserCanvas != None:
        addUserCanvas.place_forget()
    if showUsersFrame != None:
        showUsersFrame.place_forget()
    if showUsersFrame2 != None:
        showUsersFrame2.place_forget()
    if suspendUserBotFrame != None:
        suspendUserBotFrame.place_forget()
    if showUsersFrame3 != None:
        showUsersFrame3.place_forget()
    if suspendUserBotFrame2 != None:
        suspendUserBotFrame2.place_forget()
    if unsuspendUserBotFrame != None:
        unsuspendUserBotFrame.place_forget()
    if addNewBookCanvas != None:
        addNewBookCanvas.place_forget()
    if miniSideBarLabel != None:
        miniSideBarLabel.place_forget()
    if booksTableScrollableFrame != None:
        booksTableScrollableFrame.place_forget()
    if showBookBorrowHistoryScrollabeFrame != None:
        showBookBorrowHistoryScrollabeFrame.place_forget()
    if addBookToExistingTitleBotFrame != None:
        addBookToExistingTitleBotFrame.place_forget()
    if showStudentsPastDaysScrollableFrame != None:
        showStudentsPastDaysScrollableFrame.place_forget()
    sideBarLabel.place(relx=0, rely=0.5, anchor="w")


#Function to pop up confirmation message upon user add success
def userAddConfirmationPopUp():
    def exitUserAddPopUpConfirmation():
        window.destroy()
    window = customtk.CTk()
    window.title("User Addition Confirmation")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="User Added Successfully!", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitUserAddPopUpConfirmation)
    okButton.place(relx = 0.5, rely = 0.6, anchor="center")
    window.focus_force() 

#Function to check if any of the Add User fields is empty and displaying error message
def checkIfUserFieldEmpty():
    if len(addUserFieldsList[0].get()) == 0:
        missingIdText=customtk.CTkLabel(addUserCanvas, text="     Id field cannot be empty     ", text_color="#4461C7")
        missingIdText.place(relx=0.25, rely=0.28, anchor="center")
        addUserCanvas.after(3000, missingIdText.destroy)
    if len(addUserFieldsList[1].get()) == 0: 
        missingPassText=customtk.CTkLabel(addUserCanvas, text="Password field cannot be empty", text_color="#4461C7")
        missingPassText.place(relx=0.75, rely=0.28, anchor="center")   
        addUserCanvas.after(3000, missingPassText.destroy)
    if len(addUserFieldsList[2].get()) == 0: 
        missingFirstNameText=customtk.CTkLabel(addUserCanvas, text="First Name field cannot be empty", text_color="#4461C7")
        missingFirstNameText.place(relx=0.25, rely=0.48, anchor="center")   
        addUserCanvas.after(3000, missingFirstNameText.destroy)
    if len(addUserFieldsList[3].get()) == 0: 
        missingLastNameText=customtk.CTkLabel(addUserCanvas, text="Last Name field cannot be empty", text_color="#4461C7")
        missingLastNameText.place(relx=0.75, rely=0.48, anchor="center")
        addUserCanvas.after(3000, missingLastNameText.destroy)      
    if len(addUserFieldsList[4].get()) == 0: 
        missingEmailText=customtk.CTkLabel(addUserCanvas, text="Email field cannot be empty", text_color="#4461C7")
        missingEmailText.place(relx=0.25, rely=0.68, anchor="center")   
        addUserCanvas.after(3000, missingEmailText.destroy)

#Function to check if User Add fields are empty
def addUserFieldsEmpty():
    if (len(addUserFieldsList[0].get()) == 0) or len(addUserFieldsList[1].get()) == 0 or (len(addUserFieldsList[2].get()) == 0) or (len(addUserFieldsList[3].get()) == 0) or (len(addUserFieldsList[4].get()) == 0):
        return True
    return False 

#Function to check if Add New Book fields are empty
def addNewBookFieldsEmpty():
    if (len(addNewBookFieldsList[0].get()) == 0) or len(addNewBookFieldsList[1].get()) == 0 or (len(addNewBookFieldsList[2].get()) == 0) or (len(addNewBookFieldsList[3].get()) == 0) or (len(addNewBookFieldsList[4].get()) == 0) or (len(addNewBookFieldsList[5].get()) == 0) or (len(addNewBookFieldsList[6].get()) == 0):
        return True
    return False   

#Function to pop up confirmation message upon user add success
def addNewBookConfirmationPopUp():
    def exitAddNewBookPopUpConfirmation():
        window.destroy()
    window = customtk.CTk()
    window.title("Book Addition Confirmation")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="Book Added Successfully!", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitAddNewBookPopUpConfirmation)
    okButton.place(relx = 0.5, rely = 0.6, anchor="center")
    window.focus_force()

#Function to process click on Add User button
def onAddUserButtonClick():
    global addUserCanvas; global addUserFieldsList
    showUsersMenuButtons(False)
    addUserCanvas = customtk.CTkCanvas(app, width=557, height=450, bg="white", highlightthickness=0)
    addUserCanvas.place(relx=0.64, rely=0.55, anchor="center")
    idEntry = customtk.CTkEntry(addUserCanvas, width=220, height=40, placeholder_text="Student Id", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    idEntry.place(relx=0.25, rely=0.2, anchor="center")
    idEntry.focus()
    passEntry = customtk.CTkEntry(addUserCanvas, width=220, height=40, show="*", placeholder_text="Student Password", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    passEntry.place(relx=0.75, rely=0.2, anchor="center")
    passEntry.focus()
    firstNameEntry = customtk.CTkEntry(addUserCanvas, width=220, height=40, placeholder_text="Student's First Name", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    firstNameEntry.place(relx=0.25, rely=0.4, anchor="center")
    lastNameEntry = customtk.CTkEntry(addUserCanvas, width=220, height=40, placeholder_text="Student's Last Name", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    lastNameEntry.place(relx=0.75, rely=0.4, anchor="center")
    emailEntry = customtk.CTkEntry(addUserCanvas, width=220, height=40, placeholder_text="Email", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    emailEntry.place(relx=0.25, rely=0.6, anchor="center")
    emailEntry.focus()
    addUserButton2 = customtk.CTkButton(addUserCanvas, width=220, height=40, text="Add Student", text_color="white", image=addUserIcon2, corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=addUser)
    addUserButton2.place(relx=0.75, rely=0.6, anchor="center")
    CustomTooltipLabel(anchor_widget=addUserButton2, text="Add Student")
    addUserFieldsList=[idEntry, passEntry, firstNameEntry, lastNameEntry, emailEntry]
    
#Function that adds a user to the database
def addUserToDb():
    id = addUserFieldsList[0].get()       
    password = addUserFieldsList[1].get()
    fname = addUserFieldsList[2].get()
    lname = addUserFieldsList[3].get()
    email = addUserFieldsList[4].get()
    with open('creds.txt', 'a') as credsFile:
        credsFile.write("\n\n#Student:\nID:")
        credsFile.write(id)
        credsFile.write(" -- pass:")
        credsFile.write(password)
        credsFile.write(" -- First Name:")
        credsFile.write(fname)
        credsFile.write(" -- Last Name:")
        credsFile.write(lname)
        credsFile.write(" -- Email:")
        credsFile.write(email)
        credsFile.write(" -- Suspended:NO")
        credsFile.write(" -- Book1ISBN:NONE -- Book1Days:0 -- Book2ISBN:NONE -- Book2Days:0")
        credsFile.write(" -- Book3ISBN:NONE -- Book3Days:0")

#Function that clears add user fields
def clearAddUserFields():
    for entry in addUserFieldsList:
        entry.delete(0, 'end')

#Function that adds an user based on button click
def addUser():
    if doesIdExist(addUserFieldsList[0].get()):
        idAlreadyExistsErrorText=customtk.CTkLabel(addUserCanvas, text="    This Student ID already exists    ", text_color="#4461C7")
        idAlreadyExistsErrorText.place(relx=0.25, rely=0.28, anchor="center")
        addUserCanvas.after(3000, idAlreadyExistsErrorText.destroy)
    else:
        checkIfUserFieldEmpty()
        if not addUserFieldsEmpty():
            addUserToDb()
            clearAddUserFields()
            userAddConfirmationPopUp()

#Function to fetch all users for table
def fetchUsersFromDb():
    global usersList
    with open('creds.txt', 'r') as credsFile:
        usersList = []
        usersList.append(['Student ID', 'Password', 'First Name', 'Last Name', 'Email'])
        for line in credsFile:
            if len(line) > 30:
                wordList = line.split(' -- ')
                wordList2 = wordList[0].split(':')
                id = wordList2[1]
                wordList = line.split(' -- ')
                wordList2 = wordList[1].split(':')
                password = wordList2[1]
                wordList = line.split(' -- ')
                wordList2 = wordList[2].split(':')
                firstName = wordList2[1]
                wordList = line.split(' -- ')
                wordList2 = wordList[3].split(':')
                lastName = wordList2[1]
                wordList = line.split(' -- ')
                wordList2 = wordList[4].split(':')
                email = wordList2[1]
                userList = [id, password, firstName, lastName, email]
                usersList.append(userList)                                                

#Function to fetch all suspended users for table
def fetchUnsuspendedUsersFromDb():
    global usersList
    with open('creds.txt', 'r') as credsFile:
        usersList = []
        usersList.append(['Student ID', 'Password', 'First Name', 'Last Name', 'Email'])
        for line in credsFile:
            if len(line) > 30:
                wordList = line.split(' -- ')
                wordList3 = wordList[5].split(':')
                if wordList3[1] == "NO":
                    wordList2 = wordList[0].split(':')
                    id = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[1].split(':')
                    password = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[2].split(':')
                    firstName = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[3].split(':')
                    lastName = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[4].split(':')
                    email = wordList2[1]
                    userList = [id, password, firstName, lastName, email]
                    usersList.append(userList)

#Function to fetch all non-suspended users for table
def fetchSuspendedUsersFromDb():
    global usersList
    with open('creds.txt', 'r') as credsFile:
        usersList = []
        usersList.append(['Student ID', 'Password', 'First Name', 'Last Name', 'Email'])
        for line in credsFile:
            if len(line) > 30:
                wordList = line.split(' -- ')
                wordList3 = wordList[5].split(':')
                if wordList3[1] == "YES":
                    wordList2 = wordList[0].split(':')
                    id = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[1].split(':')
                    password = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[2].split(':')
                    firstName = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[3].split(':')
                    lastName = wordList2[1]
                    wordList = line.split(' -- ')
                    wordList2 = wordList[4].split(':')
                    email = wordList2[1]
                    userList = [id, password, firstName, lastName, email]
                    usersList.append(userList)

#Function to fetch all books from database
def fetchBooksFromDb():
    global booksList
    with open('books.txt', 'r') as booksFile:
        booksList = []
        booksList.append(['Book Id', 'ISBN', 'Title', 'Autor', 'Editor', 'Year', 'Units'])    
        for line in booksFile:
            wordList = line.split('  --  ')
            wordList3 = wordList[0].split(' -- ')
            wordList2 = wordList3[0].split(':')
            bookId = wordList2[1]
            wordList2 = wordList3[1].split(':')
            title = wordList2[1]
            wordList2 = wordList3[2].split(':')
            author = wordList2[1]
            wordList2 = wordList3[3].split(':')
            editor = wordList2[1]
            wordList2 = wordList3[4].split(':') 
            year = wordList2[1]
            wordList2 = wordList3[5].split(':')
            units = wordList2[1]
            wordList2 = wordList3[6].split(':')
            isbn = wordList2[1]
            bookList = [bookId, isbn, title, author, editor, year, units]     
            booksList.append(bookList)      

#Function that procsseses click on show all users button
def onShowAllUsersButtonCLick():
    global showUsersFrame
    fetchUsersFromDb()
    showUsersMenuButtons(False)
    showUsersFrame = customtk.CTkScrollableFrame(app, width=520, height=380, bg_color="transparent", fg_color="white")
    showUsersFrame.place(relx=0.645, rely=0.55, anchor="center")
    showUsersTable = CTkTable(showUsersFrame, corner_radius=8, values=usersList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showUsersTable.columnconfigure(4, pad=70)
    showUsersTable.columnconfigure(0, pad=14.2)
    showUsersTable.columnconfigure(1, pad=20)
    showUsersTable.pack(expand=True, fill="both", padx=0, pady=20)

#Function that procees a click on confirm suspend user button click
def onConfirmUnsuspendUserButtonClick():
    if doesIdExist(unsuspendIdEntry.get()):     
        userUnsuspendPopUp(isUserSuspended(unsuspendIdEntry.get()))
        unsuspendIdEntry.delete(0, 'end')
    else:
        unsuspendIdEntry.delete(0, 'end')
        def exitPopUpMessage():
            window.destroy()
        window = customtk.CTk()
        window.title("User Suspension")
        window.resizable(False, False)
        window.geometry("400x100+550+350")
        bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
        bgLabel.place(x = 0, y = 0)
        text = customtk.CTkLabel(window, text="Error, this Student's Account doesn't Exist", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
        text.place(relx = 0.5, rely = 0.2, anchor="center")
        okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
        okButton.place(relx = 0.5, rely = 0.6, anchor="center")
        window.focus_force()

#Function that procees a click on confirm suspend user button click
def onConfirmSuspendUserButtonClick():
    if doesIdExist(suspendIdEntry.get()):
        userSuspendPopUp(isUserSuspended(suspendIdEntry.get()))
        suspendIdEntry.delete(0, 'end')
    else:
        suspendIdEntry.delete(0, 'end')
        def exitPopUpMessage():
            window.destroy()
        window = customtk.CTk()
        window.title("User Suspension")
        window.resizable(False, False)
        window.geometry("400x100+550+350")
        bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
        bgLabel.place(x = 0, y = 0)
        text = customtk.CTkLabel(window, text="Error, this Student's Account doesn't Exist", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
        text.place(relx = 0.5, rely = 0.2, anchor="center")
        okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
        okButton.place(relx = 0.5, rely = 0.6, anchor="center")
        window.focus_force()

#Function that suspends a user
def suspendUser(id):
    with open('creds.txt', 'r') as credsFile:
        content = credsFile.readlines()
        for i in range(len(content)):
            if id in content[i]:
                wordList = content[i].split(' -- ')
                if wordList[0] == ("ID:" + id):
                    if "Suspended:NO" in content[i]:
                        content[i] = content[i].replace('Suspended:NO', 'Suspended:YES')
    with open('creds.txt', 'w') as credsFile:
        credsFile.writelines(content)

#Function that unsuspends a user:
def unsuspendUser(id):
    with open('creds.txt', 'r') as credsFile:
        content = credsFile.readlines()
        for i in range(len(content)):
            if id in content[i]:
                wordList = content[i].split(' -- ')
                if wordList[0] == ("ID:" + id):
                    if "Suspended:YES" in content[i]:
                        content[i] = content[i].replace('Suspended:YES', 'Suspended:NO')
    with open('creds.txt', 'w') as credsFile:
        credsFile.writelines(content)    

#Function that pop up message for user suspend confirmation
def userSuspendPopUp(bool):
    if bool:
        def exitPopUpMessage():
            window.destroy()
        window = customtk.CTk()
        window.title("User Suspension")
        window.resizable(False, False)
        window.geometry("400x100+550+350")
        bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
        bgLabel.place(x = 0, y = 0)
        text = customtk.CTkLabel(window, text="Error, this Student is already Suspended", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
        text.place(relx = 0.5, rely = 0.2, anchor="center")
        okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
        okButton.place(relx = 0.5, rely = 0.6, anchor="center")
        window.focus_force()
    else:
        if suspendIdEntry.get() == "0":
            def exitPopUpMessage():
                window2.destroy()
            window2 = customtk.CTk()
            window2.title("User Suspension")
            window2.resizable(False, False)
            window2.geometry("400x100+550+350")
            bgLabel2 = customtk.CTkLabel(window2, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
            bgLabel2.place(x = 0, y = 0)
            text2 = customtk.CTkLabel(window2, text="Error, you can't Suspend an Admin's Account", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
            text2.place(relx = 0.5, rely = 0.2, anchor="center")
            okButton2 = customtk.CTkButton(window2, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
            okButton2.place(relx = 0.5, rely = 0.6, anchor="center")
            window2.focus_force()
        else:
            suspendUser(suspendIdEntry.get())
            def exitPopUpMessage():
                window3.destroy()
            window3 = customtk.CTk()
            window3.title("User Suspension")
            window3.resizable(False, False)
            window3.geometry("400x100+550+350")
            bgLabel3 = customtk.CTkLabel(window3, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
            bgLabel3.place(x = 0, y = 0)
            text3 = customtk.CTkLabel(window3, text="Student's Account Successfully Suspended", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
            text3.place(relx = 0.5, rely = 0.2, anchor="center")
            okButton3 = customtk.CTkButton(window3, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
            okButton3.place(relx = 0.5, rely = 0.6, anchor="center")
            window3.focus_force()

#Function that pop up message for user suspend confirmation
def userUnsuspendPopUp(bool):
    if bool:
        unsuspendUser(unsuspendIdEntry.get())
        def exitPopUpMessage():
            window.destroy()
        window = customtk.CTk()
        window.title("User Suspension")
        window.resizable(False, False)
        window.geometry("400x100+550+350")
        bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
        bgLabel.place(x = 0, y = 0)
        text = customtk.CTkLabel(window, text="Student's Account Successfully Unsuspended", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
        text.place(relx = 0.5, rely = 0.2, anchor="center")
        okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
        okButton.place(relx = 0.5, rely = 0.6, anchor="center")
        window.focus_force()
    else:
        if unsuspendIdEntry.get() == "0":
            def exitPopUpMessage():
                window2.destroy()
            window2 = customtk.CTk()
            window2.title("User Suspension")
            window2.resizable(False, False)
            window2.geometry("400x100+550+350")
            bgLabel2 = customtk.CTkLabel(window2, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
            bgLabel2.place(x = 0, y = 0)
            text2 = customtk.CTkLabel(window2, text="Error, you can't Unsuspend an Admin's Account", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
            text2.place(relx = 0.5, rely = 0.2, anchor="center")
            okButton2 = customtk.CTkButton(window2, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
            okButton2.place(relx = 0.5, rely = 0.6, anchor="center")
            window2.focus_force()
        else:
            unsuspendUser(unsuspendIdEntry.get())
            def exitPopUpMessage():
                window3.destroy()
            window3 = customtk.CTk()
            window3.title("User Suspension")
            window3.resizable(False, False)
            window3.geometry("450x80+550+350")
            bgLabel3 = customtk.CTkLabel(window3, width= 450, height=200,text= "This Student's Account is Already Unsuspended", fg_color="#4461C7", bg_color="#4461C7")
            bgLabel3.place(x = 0, y = 0)
            text3 = customtk.CTkLabel(window3, text="Error, this Student's Account is Already Unsuspended", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
            text3.place(relx = 0.5, rely = 0.2, anchor="center")
            okButton3 = customtk.CTkButton(window3, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitPopUpMessage)
            okButton3.place(relx = 0.5, rely = 0.6, anchor="center")
            window3.focus_force()

#Function to process click on Suspend User button
def onSuspendUserButtonClick():
    global showUsersFrame2, suspendUserBotFrame, suspendIdEntry
    showUsersMenuButtons(False)
    fetchUnsuspendedUsersFromDb()
    showUsersFrame2 = customtk.CTkScrollableFrame(app, width=520, height=380, bg_color="transparent", fg_color="white")
    showUsersFrame2.place(relx=0.645, rely=0.5, anchor="center")
    showUsersTable2 = CTkTable(showUsersFrame2, corner_radius=8, values=usersList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showUsersTable2.columnconfigure(4, pad=70)
    showUsersTable2.columnconfigure(0, pad=14.2)
    showUsersTable2.columnconfigure(1, pad=20)
    showUsersTable2.pack(expand=True, fill="both", padx=0, pady=20)
    suspendUserBotFrame = customtk.CTkFrame(app, fg_color="transparent", bg_color="white", width=520, height=100)
    suspendUserBotFrame.place(relx=0.645, rely=0.92, anchor="center")
    suspendIdEntry = customtk.CTkEntry(suspendUserBotFrame, width=220, height=40, placeholder_text="Student Id to Suspend", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    suspendIdEntry.place(relx=0.23, rely=0.25, anchor="center")
    confirmSuspendUserButton = customtk.CTkButton(suspendUserBotFrame, text="Suspend Student", width=220, height=40, corner_radius=20, fg_color="#5E7BE3",font=('Hind', 17), text_color="white", hover_color="#4461C7", bg_color="white", command=onConfirmSuspendUserButtonClick)
    confirmSuspendUserButton.place(relx = 0.75, rely = 0.25, anchor = "center")
    usersFilterNoteLabel = customtk.CTkLabel(suspendUserBotFrame, text="Note: Suspended Students are not shown in the table above.", bg_color="transparent", fg_color="white", font=('Hind', 13), text_color="#4461C7")
    usersFilterNoteLabel.place(relx=0.35, rely=0.6, anchor="center")

#Function to process click on Unuspend User button
def onUnsuspendUserButtonClick():
    global showUsersFrame3, unsuspendUserBotFrame, unsuspendIdEntry
    showUsersMenuButtons(False)
    fetchSuspendedUsersFromDb()
    showUsersFrame3 = customtk.CTkScrollableFrame(app, width=520, height=380, bg_color="transparent", fg_color="white")
    showUsersFrame3.place(relx=0.645, rely=0.5, anchor="center")
    showUsersTable3 = CTkTable(showUsersFrame3, corner_radius=8, values=usersList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showUsersTable3.columnconfigure(4, pad=70)
    showUsersTable3.columnconfigure(0, pad=14.2)
    showUsersTable3.columnconfigure(1, pad=20)
    showUsersTable3.pack(expand=True, fill="both", padx=0, pady=20)
    unsuspendUserBotFrame = customtk.CTkFrame(app, fg_color="transparent", bg_color="white", width=520, height=100)
    unsuspendUserBotFrame.place(relx=0.645, rely=0.92, anchor="center")
    unsuspendIdEntry = customtk.CTkEntry(unsuspendUserBotFrame, width=220, height=40, placeholder_text="Student Id to Unsuspend", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    unsuspendIdEntry.place(relx=0.23, rely=0.25, anchor="center")
    confirmUnsuspendUserButton = customtk.CTkButton(unsuspendUserBotFrame, text="Unsuspend Student", width=220, height=40, corner_radius=20, fg_color="#5E7BE3",font=('Hind', 17), text_color="white", hover_color="#4461C7", bg_color="white", command=onConfirmUnsuspendUserButtonClick)
    confirmUnsuspendUserButton.place(relx = 0.75, rely = 0.25, anchor = "center")
    usersFilterNoteLabel2 = customtk.CTkLabel(unsuspendUserBotFrame, text="Note: Only Suspended Students are shown in the table above.", bg_color="transparent", fg_color="white", font=('Hind', 13), text_color="#4461C7")
    usersFilterNoteLabel2.place(relx=0.35, rely=0.6, anchor="center")

#Function to check if book ID already exists
def bookIdAlreadyExists(id):
    with open('books.txt', 'r') as booksFile:
        content = booksFile.readlines()
        for line in content:
            wordList = line.split(' -- ')
            if wordList[0] == ("ID:" + id):
                return True
    return False

#Function that adds a new book to the database
def addNewBookToDb():
        with open('books.txt', 'a') as booksFile:
            booksFile.write("ID:")
            booksFile.write(addNewBookFieldsList[0].get())
            booksFile.write(" -- Title:")
            booksFile.write(addNewBookFieldsList[2].get())
            booksFile.write(" -- Author:")
            booksFile.write(addNewBookFieldsList[3].get())
            booksFile.write(" -- Editor:")
            booksFile.write(addNewBookFieldsList[4].get())
            booksFile.write(" -- YearOfRelease:")
            booksFile.write(addNewBookFieldsList[5].get())
            booksFile.write(" -- NumberOfUnits:")
            booksFile.write(addNewBookFieldsList[6].get())
            booksFile.write(" -- ISBN:")
            booksFile.write(addNewBookFieldsList[1].get())
            booksFile.write("\n")

#Function that clears add new book fields
def clearAddNewBookFields():
    for entry in addNewBookFieldsList:
        entry.delete(0, 'end')

#Function that adds a new book
def addNewBook():
    if bookIdAlreadyExists(addNewBookFieldsList[0].get()):
        bookIdAlreadyExistsErrorText=customtk.CTkLabel(addNewBookCanvas, text="    This Book ID already exists    ", text_color="#4461C7")
        bookIdAlreadyExistsErrorText.place(relx=0.25, rely=0.28, anchor="center")
        addNewBookCanvas.after(3000, bookIdAlreadyExistsErrorText.destroy)
    if not addNewBookFieldsList[1].get() == "":
        if bookInLibrary(int(addNewBookFieldsList[1].get())):
            bookAlreadyExistsErrorText=customtk.CTkLabel(addNewBookCanvas, text="    This Book already exists in the Library    ", text_color="#4461C7")
            bookAlreadyExistsErrorText.place(relx=0.75, rely=0.28, anchor="center")
            addNewBookCanvas.after(3000, bookAlreadyExistsErrorText.destroy)
        else:
            checkIfAddNewBookFieldsEmpty()
            if not addNewBookFieldsEmpty():
                addNewBookToDb()
                clearAddNewBookFields()
                addNewBookConfirmationPopUp()


#Function that processes click on add new book button
def onAddNewBookButtonClick():
    showBooksMenuButtons(False)
    global addNewBookCanvas; global addNewBookFieldsList
    addNewBookCanvas = customtk.CTkCanvas(app, width=557, height=450, bg="white", highlightthickness=0)
    addNewBookCanvas.place(relx=0.64, rely=0.55, anchor="center")
    bookIdEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's ID", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    bookIdEntry.place(relx=0.25, rely=0.2, anchor="center")
    bookIdEntry.focus()
    isbnEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's ISBN", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    isbnEntry.place(relx=0.75, rely=0.2, anchor="center")
    isbnEntry.focus()
    titleEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's Title", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    titleEntry.place(relx=0.25, rely=0.4, anchor="center")
    authorEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's Author", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    authorEntry.place(relx=0.75, rely=0.4, anchor="center")
    editorEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's Editor", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    editorEntry.place(relx=0.25, rely=0.6, anchor="center")
    editorEntry.focus()
    yearOfReleaseEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's Year of Release", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    yearOfReleaseEntry.place(relx=0.75, rely=0.6, anchor="center")
    yearOfReleaseEntry.focus()
    unitsEntry = customtk.CTkEntry(addNewBookCanvas, width=220, height=40, placeholder_text="Book's Available Units", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    unitsEntry.place(relx=0.25, rely=0.8, anchor="center")
    unitsEntry.focus()
    addNewBookButton2 = customtk.CTkButton(addNewBookCanvas, width=220, height=40, text="Add Book", text_color="white", corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=addNewBook)
    addNewBookButton2.place(relx=0.75, rely=0.8, anchor="center")
    CustomTooltipLabel(anchor_widget=addNewBookButton2, text="Add New Book")
    addNewBookFieldsList=[bookIdEntry, isbnEntry, titleEntry, authorEntry, editorEntry, yearOfReleaseEntry, unitsEntry]

#Function the processes click on show all books button
def onShowAllBooksButtonClick():
    global miniSideBarLabel, booksTableScrollableFrame
    fetchBooksFromDb()
    sideBarLabel.place_forget()
    showBooksMenuButtons(False)
    miniSideBarLabel = customtk.CTkLabel(app, width=75, height=600, image=miniSideImage, text="")
    miniSideBarLabel.place(relx=0, rely=0.5, anchor="w")
    miniUsersButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=userIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onUsersButtonClick)
    miniUsersButton.place(relx=0.5, rely=0.3, anchor="center")
    miniBooksButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=booksIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onBooksButtonClick)
    miniBooksButton.place(relx=0.5, rely=0.45, anchor="center")
    miniOtherButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=othersIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onOthersButtonClick)
    miniOtherButton.place(relx=0.5, rely=0.6, anchor="center")
    miniLogOutButton = customtk.CTkButton(miniSideBarLabel, width=150, height=40, text="", image=logOutImage, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="#4461C7", command=onLogOutButtonClick)
    miniLogOutButton.place(relx = 0.5, rely = 0.85, anchor="center")
    booksTableScrollableFrame = customtk.CTkScrollableFrame(app, width=650, height=400, bg_color="transparent", fg_color="white")
    booksTableScrollableFrame.place(relx=0.55, rely=0.55, anchor="center")
    showBooksTable = CTkTable(booksTableScrollableFrame, corner_radius=8, values=booksList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showBooksTable.columnconfigure(1, pad=60)
    showBooksTable.columnconfigure(2, pad=30)
    showBooksTable.pack(expand=True, fill="both", padx=0, pady=20)

#Function to fetch book borrow history
def fetchBookBorrowHistory():
    global bookBorrowHistoryList
    bookBorrowHistoryList = []
    bookBorrowHistoryList.append(['Student ID', 'Book ISBN'])
    if os.path.getsize('borrows.txt') != 0:
        with open('borrows.txt', 'r') as borrowsFile:
            for line in borrowsFile:
                wordList = line.split(' ')
                wordList2 = wordList[2].split(':')
                studentId = wordList2[1]
                wordList2 = wordList[6].split(':')
                isbn = wordList2[1]
                bookBorrowList = [studentId, isbn]
                bookBorrowHistoryList.append(bookBorrowList)

#Function the process click on show book borrow history
def onShowBookBorrowHistoryButtonClick():
    global showBookBorrowHistoryScrollabeFrame
    fetchBookBorrowHistory()
    showBooksMenuButtons(False)
    showBookBorrowHistoryScrollabeFrame = customtk.CTkScrollableFrame(app, width=520, height=380, bg_color="transparent", fg_color="white")
    showBookBorrowHistoryScrollabeFrame.place(relx=0.645, rely=0.55, anchor="center")
    showBookBorrowHistoryTable = CTkTable(showBookBorrowHistoryScrollabeFrame, corner_radius=8, values=bookBorrowHistoryList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showBookBorrowHistoryTable.pack(expand=True, fill="both", padx=0, pady=20)

#Function that process click on second add book to existing title button
def onAddBookToExistingTitleButton2Click():
    if len(isbnEntry.get()) == 0:
        missingIsbnText=customtk.CTkLabel(addBookToExistingTitleBotFrame, text="     Book ISBN field cannot be empty     ", bg_color="transparent", fg_color="transparent", text_color="#4461C7")
        missingIsbnText.place(relx=0.18, rely=0.7, anchor="center")
        app.after(3000, missingIsbnText.place_forget)
    else:
        if not bookInLibrary(int(isbnEntry.get())):
            bookDoesntExistText=customtk.CTkLabel(addBookToExistingTitleBotFrame, text="     Book Doesn't Exist in Library     ", bg_color="transparent", fg_color="transparent", text_color="#4461C7")
            bookDoesntExistText.place(relx=0.18, rely=0.7, anchor="center")
            app.after(3000, bookDoesntExistText.place_forget)
        else:
            if len(unitsToAddEntry.get()) == 0:
                missingUnitsToAddText=customtk.CTkLabel(addBookToExistingTitleBotFrame, text="     Units to Add field cannot be empty     ", bg_color="transparent", fg_color="transparent", text_color="#4461C7")
                missingUnitsToAddText.place(relx=0.5, rely=0.7, anchor="center")
                app.after(3000, missingUnitsToAddText.place_forget)
            else:
                incrementBookUnits(int(isbnEntry.get()), int(unitsToAddEntry.get()))
                unitsAdditionConfirmationPopUp()
                unitsToAddEntry.delete(0, 'end')
                isbnEntry.delete(0, 'end')

#Function to pop up confirmation message upon user add success
def unitsAdditionConfirmationPopUp():
    def exitUnitsAdditionPopUpConfirmation():
        window.destroy()
    window = customtk.CTk()
    window.title("Units Addition Confirmation")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="Book Units Added Successfully!", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitUnitsAdditionPopUpConfirmation)
    okButton.place(relx = 0.5, rely = 0.6, anchor="center")
    window.focus_force() 

#Function that processes click on add book to existing title button
def onAddBookToExistingTitleButtonClick():
    global miniSideBarLabel, booksTableScrollableFrame, addBookToExistingTitleBotFrame
    global isbnEntry, unitsToAddEntry
    showBooksMenuButtons(False)
    sideBarLabel.place_forget()
    fetchBooksFromDb()
    miniSideBarLabel = customtk.CTkLabel(app, width=75, height=600, image=miniSideImage, text="")
    miniSideBarLabel.place(relx=0, rely=0.5, anchor="w")
    miniUsersButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=userIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onUsersButtonClick)
    miniUsersButton.place(relx=0.5, rely=0.3, anchor="center")
    miniBooksButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=booksIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onBooksButtonClick)
    miniBooksButton.place(relx=0.5, rely=0.45, anchor="center")
    miniOtherButton = customtk.CTkButton(miniSideBarLabel, width=100, height=60, image=othersIcon, text="", fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onOthersButtonClick)
    miniOtherButton.place(relx=0.5, rely=0.6, anchor="center")
    miniLogOutButton = customtk.CTkButton(miniSideBarLabel, width=150, height=40, text="", image=logOutImage, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="#4461C7", command=onLogOutButtonClick)
    miniLogOutButton.place(relx = 0.5, rely = 0.85, anchor="center")
    booksTableScrollableFrame = customtk.CTkScrollableFrame(app, width=650, height=350, bg_color="transparent", fg_color="white")
    booksTableScrollableFrame.place(relx=0.55, rely=0.5, anchor="center")
    showBooksTable = CTkTable(booksTableScrollableFrame, corner_radius=8, values=booksList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showBooksTable.columnconfigure(1, pad=60)
    showBooksTable.columnconfigure(2, pad=30)
    showBooksTable.pack(expand=True, fill="both", padx=0, pady=20)
    addBookToExistingTitleBotFrame = customtk.CTkFrame(app, width=700, height=100, fg_color="white", bg_color="transparent")
    addBookToExistingTitleBotFrame.place(relx=0.55, rely=0.89, anchor="center")
    isbnEntry = customtk.CTkEntry(addBookToExistingTitleBotFrame, width=220, height=40, placeholder_text="ISBN", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    isbnEntry.place(relx=0.18, rely=0.33, anchor="center")
    unitsToAddEntry = customtk.CTkEntry(addBookToExistingTitleBotFrame, width=220, height=40, placeholder_text="Nb of Units to Add", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    unitsToAddEntry.place(relx=0.5, rely=0.33, anchor="center")
    addBookToExistingTitle2 = customtk.CTkButton(addBookToExistingTitleBotFrame, width=220, height=40, text="Add Units", image=addUserIcon2, corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=onAddBookToExistingTitleButton2Click)
    addBookToExistingTitle2.place(relx=0.82, rely=0.35, anchor="center")

#Function the processes click on Books Button
def onBooksButtonClick():
    global booksButtonList
    if suspendUserBotFrame2 != None:
        suspendUserBotFrame2.place_forget()
    if addUserCanvas != None:
        addUserCanvas.place_forget()
    if showUsersFrame != None:
        showUsersFrame.place_forget()
    if showUsersFrame2 != None:
        showUsersFrame2.place_forget()
    if suspendUserBotFrame != None:
        suspendUserBotFrame.place_forget()
    if showUsersFrame3 != None:
        showUsersFrame3.place_forget()
    if unsuspendUserBotFrame != None:
        unsuspendUserBotFrame.place_forget()
    if addNewBookCanvas != None:
        addNewBookCanvas.place_forget()
    if miniSideBarLabel != None:
        miniSideBarLabel.place_forget()
    if booksTableScrollableFrame != None:
        booksTableScrollableFrame.place_forget()
    if showBookBorrowHistoryScrollabeFrame != None:
        showBookBorrowHistoryScrollabeFrame.place_forget()
    if addBookToExistingTitleBotFrame != None:
        addBookToExistingTitleBotFrame.place_forget()
    if showStudentsPastDaysScrollableFrame != None:
        showStudentsPastDaysScrollableFrame.place_forget()
    sideBarLabel.place(relx=0, rely=0.5, anchor="w")
    showUsersMenuButtons(False)
    addNewBookButton = customtk.CTkButton(app, image=addBookIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onAddNewBookButtonClick)
    addNewBookButton.place(relx = 0.5, rely = 0.4, anchor = "center")
    CustomTooltipLabel(anchor_widget=addNewBookButton, text="Add New Book")
    showALLBooksButton = customtk.CTkButton(app, image=showAllBooksIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onShowAllBooksButtonClick)
    showALLBooksButton.place(relx = 0.8, rely = 0.4, anchor = "center")
    CustomTooltipLabel(anchor_widget=showALLBooksButton, text="Show All Books")
    showBookBorrowHistoryButton = customtk.CTkButton(app, image=bookBorrowHistoryIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onShowBookBorrowHistoryButtonClick)
    showBookBorrowHistoryButton.place(relx = 0.5, rely = 0.75, anchor = "center")
    CustomTooltipLabel(anchor_widget=showBookBorrowHistoryButton, text="Show Current Book Borrows")
    addBookToExistingTitleButton = customtk.CTkButton(app, image=addBookToExistingTitleIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onAddBookToExistingTitleButtonClick)
    addBookToExistingTitleButton.place(relx = 0.8, rely = 0.75, anchor = "center")
    CustomTooltipLabel(anchor_widget=addBookToExistingTitleButton, text="Add Book to Existing Title")
    booksButtonList = [addNewBookButton, showALLBooksButton, showBookBorrowHistoryButton, addBookToExistingTitleButton]

#Function to check if book exists in Library
def bookInLibrary(isbn):
    with open('books.txt', 'r') as booksFile:
       content = booksFile.readlines()
       for line in content:
           wordList = line.split(' -- ')
           wordList2 = wordList[6].split(':')
           if int(wordList2[1]) == isbn:
               return True
    return False

#Function that checks if any of the add new books field is empty and displays error messages
def checkIfAddNewBookFieldsEmpty():

    if len(addNewBookFieldsList[0].get()) == 0:
        missingBookIdText=customtk.CTkLabel(addNewBookCanvas, text="     Book Id field cannot be empty     ", text_color="#4461C7")
        missingBookIdText.place(relx=0.25, rely=0.28, anchor="center")
        addNewBookCanvas.after(3000, missingBookIdText.destroy)
    if len(addNewBookFieldsList[1].get()) == 0: 
        missingIsbnText=customtk.CTkLabel(addNewBookCanvas, text="ISBN field cannot be empty", text_color="#4461C7")
        missingIsbnText.place(relx=0.75, rely=0.28, anchor="center")   
        addNewBookCanvas.after(3000, missingIsbnText.destroy)
    if len(addNewBookFieldsList[2].get()) == 0: 
        missingTitleText=customtk.CTkLabel(addNewBookCanvas, text="Title field cannot be empty", text_color="#4461C7")
        missingTitleText.place(relx=0.25, rely=0.48, anchor="center")   
        addNewBookCanvas.after(3000, missingTitleText.destroy)
    if len(addNewBookFieldsList[3].get()) == 0: 
        missingAuthorText=customtk.CTkLabel(addNewBookCanvas, text="Author field cannot be empty", text_color="#4461C7")
        missingAuthorText.place(relx=0.75, rely=0.48, anchor="center")
        addNewBookCanvas.after(3000, missingAuthorText.destroy)      
    if len(addNewBookFieldsList[4].get()) == 0: 
        missingEditorText=customtk.CTkLabel(addNewBookCanvas, text="Editor field cannot be empty", text_color="#4461C7")
        missingEditorText.place(relx=0.25, rely=0.68, anchor="center")   
        addNewBookCanvas.after(3000, missingEditorText.destroy)
    if len(addNewBookFieldsList[5].get()) == 0: 
        missingYearOfReleaseText=customtk.CTkLabel(addNewBookCanvas, text="Year of Release field cannot be empty", text_color="#4461C7")
        missingYearOfReleaseText.place(relx=0.75, rely=0.68, anchor="center")   
        addNewBookCanvas.after(3000, missingYearOfReleaseText.destroy)
    if len(addNewBookFieldsList[6].get()) == 0: 
        missingUnitsText=customtk.CTkLabel(addNewBookCanvas, text="Available Units field cannot be empty", text_color="#4461C7")
        missingUnitsText.place(relx=0.25, rely=0.88, anchor="center")   
        addNewBookCanvas.after(3000, missingUnitsText.destroy)

#Function to check if user has already requested to borrow a book
def hasAlreadyRequestedBorrow(id, isbn):
    with open('borrows.txt', 'r') as borrowsFile:
        for line in borrowsFile:
            if str(id) in line:
                wordList = line.split(' ')
                wordList2 = wordList[2].split(':')
                wordList3 = wordList[6].split(':')
                if int(wordList2[1]) == int(id):
                    if int(wordList3[1]) == int(isbn):
                        return True
    return False

#Function to check if any book units are left
def anyUnitsLeft(isbn):
    with open('books.txt', 'r') as booksFile:
        content = booksFile.readlines()
        for line in content:
            wordList = line.split(' -- ')
            wordList2 = wordList[6].split(':')
            if int(wordList2[1]) == isbn:
                wordList3 = wordList[5].split(':')
                if int(wordList3[1]) > 0:
                    return True
    return False

#Function that increments book units based on passed value
def incrementBookUnits(isbn, units):
    updated_lines = []
    with open('books.txt', 'r') as booksFile:
        content = booksFile.readlines()
        for i in range(len(content)):
            wordList = content[i].split(' -- ')
            wordList2 = wordList[5].split(':')
            if ("ISBN:" + str(isbn)) in content[i]:
                wordList3 = wordList[6].split(':')
                if int(wordList3[1]) == isbn:
                    newUnits = str(int(wordList2[1]) + units)
                    content[i] = content[i].replace(('NumberOfUnits:'+wordList2[1]), ('NumberOfUnits:'+newUnits))                
    with open('books.txt', 'w') as booksFile2:
        booksFile2.writelines(content)

#Function that decrements  book units
def decrementBookUnits(isbn):
    updated_lines = []
    with open('books.txt', 'r') as booksFile:
        content = booksFile.readlines()
        for i in range(len(content)):
            wordList = content[i].split(' -- ')
            wordList2 = wordList[5].split(':')
            if ("ISBN:" + str(isbn)) in content[i]:
                wordList3 = wordList[6].split(':')
                if int(wordList3[1]) == isbn:
                    newUnits = str(int(wordList2[1]) - 1)
                    content[i] = content[i].replace(('NumberOfUnits:'+wordList2[1]), ('NumberOfUnits:'+newUnits))                
    with open('books.txt', 'w') as booksFile2:
        booksFile2.writelines(content)
                    

#Function to send a borrow request
def sendBorrowRequest(bookIsbn):
    global signedInId
    with open('borrows.txt', 'a') as borrowsFile:
        borrowsFile.write("-Student of ID:")
        borrowsFile.write(signedInId)
        borrowsFile.write(" has requested book ISBN:")
        borrowsFile.write(str(bookIsbn))
        borrowsFile.write("\n")

#Function that pops up a window up successful book borrow
def successfulBookBorrowConfirmationPopUp():
    def exitSuccessfulBookBorrowPopUpConfirmation():
        window.destroy()
    window = customtk.CTk()
    window.title("Book Borrow Confirmation")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="Book Borrowed! Please return it within 7 days", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitSuccessfulBookBorrowPopUpConfirmation)
    okButton.place(relx = 0.5, rely = 0.6, anchor="center")
    window.focus_force() 

#Function that dsiplays error message while borrowing a book
def borrowBookErrorMsg(errorMsg):
    errorText = customtk.CTkLabel(borrowBookBotFrame, text=errorMsg, font=('Hind', 13), text_color="#4461C7")
    errorText.place(relx = 0.4, rely = 0.7, anchor = "center")
    app.after(3000, errorText.place_forget)

#Function to check which book borrow slot is free:
def whichBookBorrowSlotIsFree():
    with open('creds.txt', 'r') as credsFile:
        content = credsFile.readlines()
        for i in range(len(content)):
            if len(content[i]) > 30:
                wordList = content[i].split(' -- ')
                wordList2 = wordList[0].split(':')
                if signedInId == wordList2[1]:
                   if wordList[6] == "Book1ISBN:NONE":
                        return 6
                   elif wordList[8] == "Book2ISBN:NONE":
                        return 8
                   elif wordList[10] == "Book3ISBN:NONE":
                        return 10
    return 0

#Function to add borrowed book to user's borrowed books:
def addBorrowedBookToBorrowedBooks(isbn):
    with open('creds.txt', 'r') as credsFile:
        content = credsFile.readlines()
        for i in range(len(content)):
            if len(content[i]) > 30:
                wordList = content[i].split(' -- ')
                wordList2 = wordList[0].split(':')
                if signedInId == wordList2[1]:
                    freeSlot = whichBookBorrowSlotIsFree()
                    wordList2 = wordList[freeSlot].split(':')
                    wordList2[1] = wordList2[1].replace('NONE', str(isbn))
                    wordList[freeSlot] = ':'.join(wordList2)
                    content[i] = ' -- '.join(wordList)
    with open('creds.txt', 'w') as credsFile2:
        credsFile2.writelines(content)

#Function to borrow a book
def borrowBook():
    global signedInId
    isbn = int(isbnOfBookToBorrowEntry.get())
    if hasAlreadyRequestedBorrow(signedInId, isbn):
        borrowBookErrorMsg("This book is already in your posession")
    else:
        if bookInLibrary(isbn):
            if anyUnitsLeft(isbn):
                if whichBookBorrowSlotIsFree() == 0:
                    borrowBookErrorMsg("You already have 3 books in your posession. Return some to get more books")
                else:
                    sendBorrowRequest(isbn)
                    decrementBookUnits(isbn)
                    addBorrowedBookToBorrowedBooks(isbn)
                    successfulBookBorrowConfirmationPopUp()
            else:
                borrowBookErrorMsg("The book you requested is no longer available in our Library. Check back after Re-stock")
        else:
            borrowBookErrorMsg("We are sorry, we don't have that book in the Library")

#Function to treat back button click
def onBackButtonClick():
    backButton.place_forget()
    booksTableScrollableFrame2.place_forget()
    borrowBookBotFrame.place_forget()
    showStudentMenuButtons(True)

#Function that processes click on borrow book button
def onBorrowBookButtonClick():
    global booksTableScrollableFrame2, borrowBookBotFrame, isbnOfBookToBorrowEntry
    global backButton
    showStudentMenuButtons(False)
    fetchBooksFromDb()
    backButton = customtk.CTkButton(app, width=40, height=10, text="", corner_radius=100, image=backArrowIcon, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="transparent", command=onBackButtonClick)
    backButton.place(relx=0, rely=0.5, anchor="w")
    booksTableScrollableFrame2 = customtk.CTkScrollableFrame(app, width=650, height=400, bg_color="transparent", fg_color="white")
    booksTableScrollableFrame2.place(relx=0.53, rely=0.5, anchor="center")
    showBooksTable = CTkTable(booksTableScrollableFrame2, corner_radius=8, values=booksList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showBooksTable.columnconfigure(1, pad=60)
    showBooksTable.columnconfigure(2, pad=30)
    showBooksTable.pack(expand=True, fill="both", padx=0, pady=20)
    borrowBookBotFrame = customtk.CTkFrame(app, fg_color="transparent", bg_color="white", width=680, height=100)
    borrowBookBotFrame.place(relx=0.645, rely=0.92, anchor="center")
    isbnOfBookToBorrowEntry = customtk.CTkEntry(borrowBookBotFrame, width=220, height=40, placeholder_text="ISBN of Book To Borrow", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    isbnOfBookToBorrowEntry.place(relx=0.2, rely=0.35, anchor="center")
    borrowBookButton2 = customtk.CTkButton(borrowBookBotFrame, width=220, height=40, text="Borrow Book", text_color="white", corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=borrowBook)
    borrowBookButton2.place(relx=0.6, rely=0.35, anchor="center")

#Function to fetch borrowed books by student id
def fetchBorrowedBooksFromDb(signedInId):
    global borrowedBooksList
    with open('creds.txt', 'r') as credsFile:
        borrowedBooksList = []
        borrowedBooksList.append(['Book 1 ISBN', 'Days Passed', 'Book 2 ISBN', 'Days Passed', 'Book 3 ISBN', 'Days Passed'])
        content = credsFile.readlines()
        for i in range(len(content)):
            if len(content[i]) > 30:
                wordList = content[i].split(' -- ')
                wordList2 = wordList[0].split(':')
                if signedInId == wordList2[1]:
                    wordList2 = wordList[6].split(':')
                    book1 = wordList2[1]
                    wordList2 = wordList[7].split(':')
                    days1 = wordList2[1]
                    wordList2 = wordList[8].split(':')
                    book2 = wordList2[1]
                    wordList2 = wordList[9].split(':')
                    days2 = wordList2[1]
                    wordList2 = wordList[10].split(':')
                    book3 = wordList2[1]
                    wordList2 = wordList[11].split(':')
                    days3 = wordList2[1]
                    borrowedBookList = [book1, days1, book2, days2, book3, days3]
                    borrowedBooksList.append(borrowedBookList)
                                                                              
#Function to process click on the second return book button
def onBookReturnButton2Click():
    isbn = isbnOfBookToReturnEntry.get()
    if len(isbn) == 0:
        borrowBookErrorMsg("Books ISBN field cannot be empty")
    else:
        if not hasAlreadyRequestedBorrow(signedInId, isbn):
           borrowBookErrorMsg("You don't have that book in your posession.") 
        else:
            returnBook(isbn)
            returnBookPopUpConfirmation()

#Function that pops up confirmation pop up upon returning a book
def returnBookPopUpConfirmation():
    def exitReturnBookPopUpConfirmation():
        window.destroy()
    window = customtk.CTk()
    window.title("Book Borrow Confirmation")
    window.resizable(False, False)
    window.geometry("400x100+550+350")
    bgLabel = customtk.CTkLabel(window, width= 400, height=200,text= "", fg_color="#4461C7", bg_color="#4461C7")
    bgLabel.place(x = 0, y = 0)
    text = customtk.CTkLabel(window, text="Book Returned. Thank you for using our Service!", font=('Pilcrow Rounded', 20), fg_color="#4461C7", bg_color="#4461C7")
    text.place(relx = 0.5, rely = 0.2, anchor="center")
    okButton = customtk.CTkButton(window, text="OK", bg_color="#4461C7", fg_color="#4461C7", hover_color="#5E7BE3", corner_radius=20, command=exitReturnBookPopUpConfirmation)
    okButton.place(relx = 0.5, rely = 0.6, anchor="center")
    window.focus_force()

#Function that returns a book
def returnBook(isbn):
    with open('borrows.txt', 'r') as borrowsFile:
        content = borrowsFile.readlines()
        for i in range(len(content)):
            wordList = content[i].split(' ')
            wordList2 = wordList[2].split(':')
            wordList3 = wordList[6].split(':')
            if (wordList2[1] == str(signedInId)):
                if (wordList3[1] == (str(isbn)+"\n")):
                    del content[i]
                    break
    with open('borrows.txt', 'w') as borrowsFile:
        borrowsFile.writelines(content)
    with open('creds.txt', 'r') as credsFile:
        content = credsFile.readlines()
        for i in range(len(content)):
            if len(content[i]) > 30:
                wordList = content[i].split(' -- ')
                if signedInId == wordList2[1]:
                    if wordList[6] == ("Book1ISBN:" + str(isbn)):
                        wordList[6] = wordList[6].replace(("Book1ISBN:" + str(isbn)), 'Book1ISBN:NONE')
                        wordList2 = wordList[7].split(':')
                        wordList[7] = wordList[7].replace(("Book1Days:" + wordList2[1]), 'Book1Days:0')
                        break
                    elif wordList[8] == ("Book2ISBN:" + str(isbn)):
                        wordList[8] = wordList[8].replace(("Book2ISBN:" + str(isbn)), 'Book2ISBN:NONE')
                        wordList2 = wordList[9].split(':')
                        wordList[9] = wordList[9].replace(("Book2Days:" + wordList2[1]), 'Book2Days:0')
                        break
                    elif wordList[10] == ("Book3ISBN:" + str(isbn)):
                        wordList[10] = wordList[10].replace(("Book3ISBN:" + str(isbn)), 'Book3ISBN:NONE')
                        wordList2 = wordList[11].split(':')
                        wordList[11] = wordList[11].replace(("Book3Days:" + wordList2[1]), 'Book3Days:0')
                        break
    content[i] = ' -- '.join(wordList)
    with open('creds.txt', 'w') as credsFile:
        credsFile.writelines(content)


#Function that returns a book:
def onReturnBookButtonClick():
    global booksTableScrollableFrame2, borrowBookBotFrame, isbnOfBookToReturnEntry
    global backButton
    showStudentMenuButtons(False)
    fetchBorrowedBooksFromDb(signedInId)
    backButton = customtk.CTkButton(app, width=40, height=10, text="", corner_radius=100, image=backArrowIcon, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="transparent", command=onBackButtonClick)
    backButton.place(relx=0, rely=0.5, anchor="w")
    booksTableScrollableFrame2 = customtk.CTkScrollableFrame(app, width=650, height=400, bg_color="transparent", fg_color="white")
    booksTableScrollableFrame2.place(relx=0.53, rely=0.5, anchor="center")
    showBooksTable = CTkTable(booksTableScrollableFrame2, corner_radius=8, values=borrowedBooksList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white",)
    showBooksTable.pack(expand=True, fill="both", padx=0, pady=20)
    borrowBookBotFrame = customtk.CTkFrame(app, fg_color="transparent", bg_color="white", width=680, height=100)
    borrowBookBotFrame.place(relx=0.645, rely=0.92, anchor="center")
    isbnOfBookToReturnEntry = customtk.CTkEntry(borrowBookBotFrame, width=220, height=40, placeholder_text="ISBN of Book To Return", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    isbnOfBookToReturnEntry.place(relx=0.2, rely=0.35, anchor="center")
    bookReturnButton2 = customtk.CTkButton(borrowBookBotFrame, width=220, height=40, text="Return Book", text_color="white", corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=onBookReturnButton2Click)
    bookReturnButton2.place(relx=0.6, rely=0.35, anchor="center")

#Function to show or hide others menu buttons
def showOthersMenuButtons(bool):
    if bool:
        othersMenuButtonsList[0].place(relx = 0.5, rely = 0.4, anchor = "center")
    else:
        for button in othersMenuButtonsList:
            button.place_forget()

#Function to fetch users who borrowed books past 7 days
def fetchUsersPast7Days():
    global studentsPastDaysList
    with open('creds.txt', 'r') as credsFile:
        studentsPastDaysList = []
        studentsPastDaysList.append(["Student ID", "First Name", "Last Name"])
        content = credsFile.readlines()
        for i in range(len(content)):
            if len(content[i]) > 30:
                wordList = content[i].split(' -- ')
                wordList2 = wordList[7].split(':')
                wordList3 = wordList[9].split(':')
                wordList4 = wordList[11].split(':')
                if (int(wordList2[1]) >= 7) or (int(wordList3[1]) >= 7) or (int(wordList4[1]) >= 7):
                    wordList5 = wordList[0].split(':')
                    userId = wordList5[1]
                    wordList5 = wordList[2].split(':')
                    fName = wordList5[1]
                    wordList5 = wordList[3].split(':')
                    lName = wordList5[1]
                    userPastDaysList = [userId, fName, lName]
                    studentsPastDaysList.append(userPastDaysList)


#Function that processes click on show students past 7 days borrow  button
def onShow7DaysLateStudentButtonClick():
    global suspendUserBotFrame2, suspendIdEntry
    global showStudentsPastDaysScrollableFrame
    showStudentsPastDaysScrollableFrame = customtk.CTkScrollableFrame(app, width=520, height=380, bg_color="transparent", fg_color="white")
    showStudentsPastDaysScrollableFrame.place(relx=0.645, rely=0.55, anchor="center")
    showUsersPastDaysTable = CTkTable(showStudentsPastDaysScrollableFrame, corner_radius=8, values=studentsPastDaysList, colors=["#4461C7", "#5E7BE3"], header_color="#0730C0", hover_color="#0730C0", text_color="white")
    showUsersPastDaysTable.pack(expand=True, fill="both", padx=0, pady=20)
    suspendUserBotFrame2 = customtk.CTkFrame(app, fg_color="white", bg_color="white", width=520, height=100)
    suspendUserBotFrame2.place(relx=0.645, rely=0.92, anchor="center")
    suspendIdEntry = customtk.CTkEntry(suspendUserBotFrame2, width=220, height=40, placeholder_text="Student Id to Suspend", corner_radius=200, fg_color="transparent", text_color="black", border_color="#4461C7", font=('Hind', 15))
    suspendIdEntry.place(relx=0.23, rely=0.25, anchor="center")
    confirmSuspendUserButton = customtk.CTkButton(suspendUserBotFrame2, text="Suspend Student", width=220, height=40, corner_radius=20, fg_color="#5E7BE3",font=('Hind', 17), text_color="white", hover_color="#4461C7", bg_color="white", command=onConfirmSuspendUserButtonClick)
    confirmSuspendUserButton.place(relx = 0.75, rely = 0.25, anchor = "center")
    usersFilterNoteLabel = customtk.CTkLabel(suspendUserBotFrame2, text="Note: The students shown in the table are Students who have borrowed at-least\n1 book for 7 days or more. Suspended students would still appear in this table for record.", bg_color="transparent", fg_color="white", font=('Hind', 13), text_color="#4461C7")
    usersFilterNoteLabel.place(relx=0.46, rely=0.64, anchor="center")

#Function that treats click on others button
def onOthersButtonClick():
    global othersMenuButtonsList
    showUsersMenuButtons(False)
    showBooksMenuButtons(False)
    if suspendUserBotFrame2 != None:
        suspendUserBotFrame2.place_forget()
    if addUserCanvas != None:
        addUserCanvas.place_forget()
    if showUsersFrame != None:
        showUsersFrame.place_forget()
    if showUsersFrame2 != None:
        showUsersFrame2.place_forget()
    if suspendUserBotFrame != None:
        suspendUserBotFrame.place_forget()
    if showUsersFrame3 != None:
        showUsersFrame3.place_forget()
    if unsuspendUserBotFrame != None:
        unsuspendUserBotFrame.place_forget()
    if addNewBookCanvas != None:
        addNewBookCanvas.place_forget()
    if miniSideBarLabel != None:
        miniSideBarLabel.place_forget()
    if booksTableScrollableFrame != None:
        booksTableScrollableFrame.place_forget()
    if showBookBorrowHistoryScrollabeFrame != None:
        showBookBorrowHistoryScrollabeFrame.place_forget()
    if addBookToExistingTitleBotFrame != None:
        addBookToExistingTitleBotFrame.place_forget()
    if suspendUserBotFrame2 != None:
        suspendUserBotFrame2.place_forget()
    if showStudentsPastDaysScrollableFrame != None:
        showStudentsPastDaysScrollableFrame.place_forget()
    fetchUsersPast7Days()
    sideBarLabel.place(relx=0, rely=0.5, anchor="w")
    show7DaysLateStudentButton = customtk.CTkButton(app, image=bookReturnPast7DaysIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onShow7DaysLateStudentButtonClick)
    show7DaysLateStudentButton.place(relx = 0.5, rely = 0.4, anchor = "center")
    CustomTooltipLabel(anchor_widget=show7DaysLateStudentButton, text="Show Students who are 7 days late in returning a book")
    othersMenuButtonsList = [show7DaysLateStudentButton]

    

#Function that treats successful Student Login
def onSuccessfulStudentLogin():
    global logOutButton; global helloStudentMessageLabel
    global welcomeToDashboardMessageLabel, studentMenuButtons
    loginFrame.place_forget()
    exitButton.place_forget()
    loginBglabel.place_forget()
    logOutButton = customtk.CTkButton(app, width=150, height=40, corner_radius=20, compound="left", text="Log Out", font=('Hind', 20), image=logOutImage, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="transparent", command=onLogOutButtonClick)
    logOutButton.place(relx = 0.03, rely = 0.896, anchor="w")
    helloStudentMessageLabel = customtk.CTkLabel(app, text="Hello Student!", font=('Pilcrow Rounded', 40), text_color="#4461C7", fg_color="white")
    helloStudentMessageLabel.place(relx = 0.5, rely = 0.03, anchor = "n")
    welcomeToDashboardMessageLabel = customtk.CTkLabel(app, text="Welcome to your Dashboard!", font=('Hind', 20), text_color="#4461C7", fg_color="white")
    welcomeToDashboardMessageLabel.place(relx = 0.498, rely = 0.1, anchor = "n")
    borrowBookButton = customtk.CTkButton(app, image=borrowBookIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onBorrowBookButtonClick)
    borrowBookButton.place(relx = 0.2, rely = 0.35, anchor = "center")
    CustomTooltipLabel(anchor_widget=borrowBookButton, text="Borrow Book")
    returnBookButton = customtk.CTkButton(app, image=returnBookIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", bg_color="white", command=onReturnBookButtonClick)
    returnBookButton.place(relx = 0.5, rely = 0.35, anchor = "center")
    CustomTooltipLabel(anchor_widget=returnBookButton, text="Return Book")
    studentMenuButtons = [borrowBookButton, returnBookButton]

#Function that treats successful Admin Login
def onSuccessfullAdminLogin():
    global sideBarLabel; global logOutButton; global helloAdminMessageLabel
    global welcomeToDashboardMessageLabel; global usersButtonList
    loginFrame.place_forget()
    exitButton.place_forget()
    loginBglabel.place_forget()
    sideBarLabel = customtk.CTkLabel(app, image=sideImage, width = 234, height= 600, text="")
    sideBarLabel.place(relx = 0, rely= 0.5, anchor = "w")
    logoLabel = customtk.CTkLabel(sideBarLabel, text="", image=libraryLogoImage, fg_color="#4461C7", bg_color="#4461C7")
    logoLabel.place(relx = 0.5, rely = 0.14, anchor = "center")
    logOutButton = customtk.CTkButton(sideBarLabel, width=150, height=40, compound="left", text="Log Out", font=('Hind', 20), image=logOutImage, fg_color="#5E7BE3", hover_color="#0730C0", bg_color="#4461C7", command=onLogOutButtonClick)
    logOutButton.place(relx = 0.5, rely = 0.85, anchor="n")
    CustomTooltipLabel(anchor_widget=logOutButton, text="Log Out")
    helloAdminMessageLabel = customtk.CTkLabel(app, text="Hello Administrator!", font=('Pilcrow Rounded', 40), text_color="#4461C7", fg_color="white")
    helloAdminMessageLabel.place(relx = 0.53, rely = 0.03, anchor = "n")
    welcomeToDashboardMessageLabel = customtk.CTkLabel(app, text="Welcome to your Dashboard!", font=('Hind', 20), text_color="#4461C7", fg_color="white")
    welcomeToDashboardMessageLabel.place(relx = 0.495, rely = 0.1, anchor = "n")
    addUserButton = customtk.CTkButton(app, image=addUserIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", command=onAddUserButtonClick, bg_color="white")
    addUserButton.place(relx = 0.5, rely = 0.4, anchor = "center")
    CustomTooltipLabel(anchor_widget=addUserButton, text="Add Student Account")
    suspendUserButton = customtk.CTkButton(app, image=suspendUserIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", command=onSuspendUserButtonClick, bg_color="white")
    suspendUserButton.place(relx = 0.8, rely = 0.4, anchor = "center")
    CustomTooltipLabel(anchor_widget=suspendUserButton, text="Suspend Student Account")
    unsuspendUserButton = customtk.CTkButton(app, image=unsuspendUserIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", command=onUnsuspendUserButtonClick, bg_color="white")
    unsuspendUserButton.place(relx = 0.5, rely = 0.75, anchor = "center")
    CustomTooltipLabel(anchor_widget=unsuspendUserButton, text="Unsuspend Student Account")
    showUsersButton = customtk.CTkButton(app, image=showAllUsersIcon, width=150, height=150, text="", corner_radius=20, fg_color="#5E7BE3", hover_color="#4461C7", command=onShowAllUsersButtonCLick, bg_color="white")
    showUsersButton.place(relx = 0.8, rely = 0.75, anchor = "center")
    CustomTooltipLabel(anchor_widget=showUsersButton, text="Show All Student Accounts")
    usersButton = customtk.CTkButton(sideBarLabel, image=userIcon, compound="left", width= 150, height= 10, text="Students", font=("Hind", 25), corner_radius= 20, fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onUsersButtonClick)
    usersButton.place(relx= 0.5, rely= 0.3, anchor="center")
    CustomTooltipLabel(anchor_widget=usersButton, text="Students Menu")
    booksButton = customtk.CTkButton(sideBarLabel, image=booksIcon, compound="left", width= 150, height= 10, text="Books", font=("Hind", 25), corner_radius= 20, fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onBooksButtonClick)
    booksButton.place(relx= 0.5, rely= 0.45, anchor="center")
    CustomTooltipLabel(anchor_widget=booksButton, text="Books Menu")
    othersButton = customtk.CTkButton(sideBarLabel, image=othersIcon, compound="left", width= 150, height= 10, text="Other", font=("Hind", 25), corner_radius= 20, fg_color="#4461C7", bg_color="#4461C7", hover_color="#5E7BE3", command=onOthersButtonClick)
    othersButton.place(relx= 0.5, rely= 0.6, anchor="center")
    CustomTooltipLabel(anchor_widget=othersButton, text="Other Menu")
    usersButtonList = [addUserButton, suspendUserButton, unsuspendUserButton, showUsersButton]

#Function that checks if the user is suspended
def isUserSuspended(id):
    with open('creds.txt', 'r') as credsFile:
            content = credsFile.readlines()
            for i in range(len(content)):
                if id in content[i]:
                    if "Suspended:YES" in content[i]:
                        return True
                    else:
                        return False

#Function that checks if the user is suspended
def isUserSuspended(id):
    with open('creds.txt', 'r') as credsFile:
            content = credsFile.readlines()
            for i in range(len(content)):
                if id in content[i]:
                    if "Suspended:YES" in content[i]:
                        return True
                    else:
                        return False

#Function that updates the wrong / missing id text
def updateErrorText(id, password):
    global errorText
    if doesIdExist(id):
        if errorText is not None:
            errorText.destroy()
        if len(password) == 0:
            errorText = customtk.CTkLabel(master=loginFrame, text="Sorry, Password field cannot be empty", font=('Hind', 12), text_color="white")
            errorText.place(relx = 0.5, rely = 0.8, anchor = "center")
        else:            
            if doesPassMatchId(id, password):
                if not isUserSuspended(id):
                    if id == "0":
                        onSuccessfullAdminLogin()
                    else:
                        onSuccessfulStudentLogin()
                else:
                    errorText = customtk.CTkLabel(master=loginFrame, text="Sorry, your Account was Suspended by an Admin", font=('Hind', 12), text_color="white")
                    errorText.place(relx = 0.5, rely = 0.8, anchor = "center") 
                idEntry.delete(0, 'end')
                passEntry.delete(0, 'end')
            else: 
                errorText = customtk.CTkLabel(master=loginFrame, text="Sorry, the Password you've entered\ndoesn't match the Id", font=('Hind', 12), text_color="white")
                errorText.place(relx = 0.5, rely = 0.8, anchor = "center")                     
    else:
        if errorText is not None:
            errorText.destroy()
        if len(id) == 0:
            errorText = customtk.CTkLabel(master=loginFrame, text="Sorry, Studnet Id case cannot be empty", font=('Hind', 12), text_color="white")
            errorText.place(relx = 0.5, rely = 0.8, anchor = "center")
        else:         
            errorText = customtk.CTkLabel(master=loginFrame, text="Sorry, this Student ID is not registerd in our Library", font=('Hind', 12), text_color="white")
            errorText.place(relx = 0.5, rely = 0.8, anchor = "center")

#Function that exists the app
def onExitButtonClick():
    showAreYouSurePopup()

#Button Clicks Events
def onLoginButtonClick():
    global signedInId
    id = idEntry.get()
    signedInId = idEntry.get()
    password = passEntry.get()
    doesIdExist(id)
    updateErrorText(id, password)

#Visual Content
loginBglabel = customtk.CTkLabel(app, width=800, height=600, image=loginImage, text="")
loginBglabel.place(relx = 0, rely = 0)

loginFrame = customtk.CTkFrame(master = loginBglabel, fg_color = "#5E7BE3", width = 320, height = 360, corner_radius = 25, bg_color="#4461C7")
loginFrame.place(relx = 0.5, rely = 0.5, anchor = "center")

loginTextLabel = customtk.CTkLabel(master=loginFrame, text="Login Page", font=('Pilcrow Rounded', 40))
loginTextLabel.place(relx=0.5, rely=0.1, anchor="n")

idEntry = customtk.CTkEntry(master=loginFrame, width=220, height=40, placeholder_text="Student Id", corner_radius=200, fg_color="#4461C7", border_color="#4461C7", font=('Hind', 15))
idEntry.place(relx = 0.5, rely = 0.4, anchor="center")

passEntry = customtk.CTkEntry(master=loginFrame, width=220, height=40, placeholder_text="Password", corner_radius=200, fg_color="#4461C7", show="*", border_color="#4461C7", font=('Hind', 15))
passEntry.place(relx = 0.5, rely = 0.55, anchor="center")

loginButton = customtk.CTkButton(master=loginFrame, width=220, height=40, text="LOGIN", corner_radius=200, fg_color="#4461C7", hover_color="#0730C0", font=('Hind', 20), command=onLoginButtonClick)
loginButton.place(relx = 0.5, rely = 0.7, anchor = "center")
CustomTooltipLabel(anchor_widget=loginButton, text="Login")

exitButton = customtk.CTkButton(master = app, width=150, height=40, image=exitIcon, compound="left", text="Exit App", font=('Hind', 20), fg_color="#5E7BE3", hover_color="#0730C0", bg_color="#4461C7", command=onExitButtonClick)
exitButton.place(x= 700, y= 550, anchor="center")
CustomTooltipLabel(anchor_widget=exitButton, text="Exit")
onSuccessfullAdminLogin()
#Logic

#Check if the file that stores IDs and password exists
#If not then create it and add the admin credentials
#Also create an empty books.txt file if it doesn't exist
#Also create an empty borrows.txt file if doesn't exist
if os.path.exists('creds.txt'):
    pass
else:
    with open('creds.txt', 'w') as credsFile:
        credsFile.write('#Admin\nID:0 -- pass:admin')
if os.path.exists('books.txt'):
    pass
else:
    with open('books.txt', 'w') as booksFile:
        pass
if os.path.exists('borrows.txt'):
    pass
else:
    with open('borrows.txt', 'w') as borrowsFile:
        pass    


#Running App
app.mainloop()