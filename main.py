
import os.path
import os


nochars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '/', '<', '>', '?', ' ', ';', ':', '[', ']', '{', '}', '|', '=', '+', '_', '-', '(', ')', '*', '&', '^', '%', '$', '#', '@', '!', '`', '~']
def newpass(): # if there is not password file or you change the password this function will run
  enternewpass = input('Enter Your New 4 Digit Password: ' )
    
  for item in nochars:
    if item in enternewpass:
      print('Error Unkown Character(s) Please Try Again!')

      input('Press any Key to Exit: ')
      break
    if len(enternewpass)  == 4: 
      global file_make
      file_make = open('savedpassword.txt', 'w+')
      file_make
      file_make.write(enternewpass)
      print('Password Successfuly Created!')
      havepassword()
    else:
        print('Error To short or Long try again')

        input('Press any Key to Exit: ')


def havepassword(): #When you have a password this function will run 
  login = input('Enter Your Password to access: ')
  with open('savedpassword.txt') as i:
    content = i.read()
    if login == content:
      with open('hiddentext.txt') as o:
        content2 = o.read()
        os.system('cls||clear')
        print('O-------------------O')
        print('| Password Correct! |')
        print('O-------------------O')
        print(' ')
        print('File Unlocked: ' + content2)
        print(' ')
        input('Press Enter Key to Exit: ')

    elif login == 'changepass':
      oldpass = input('To Change Your Password Please Enter Your Old One: ')
      oldpass
      if oldpass == content:
        os.system('cls||clear')
        print('O-----------------------O')
        print('| Old Password Removed! |')
        print('O-----------------------O')
        print(' ')
        os.remove('savedpassword.txt')
        checkfile()
      else:
        os.system('cls||clear')
        print('Failed To Remove Password [Incorect Password]')

        input('Press Enter Key to Exit: ')
    elif login == 'deletepass':
      delpass = input('Are you sure? [Y/N]: ')
      if delpass == 'Y':
        os.remove('savedpassword.txt')
        os.system('clr||clear')
        print('Password Successfuly Deleted!')
      elif delpass == 'N':
        print('Password not Deleted!')
    else:
        os.system('cls||clear')
        print('Invalid Password--')
        havepassword()


def checkfile(): #Checks for exsiting password file
  if os.path.isfile('savedpassword.txt'):
    print('Existing Password Found')
    havepassword()
  else:
    newpass()


  
    
checkfile()
