
import os.path
import os


nochars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '/', '<', '>', '?', ' ', ';', ':', '[', ']', '{', '}', '|', '=', '+', '_', '-', '(', ')', '*', '&', '^', '%', '$', '#', '@', '!', '`', '~']
def newpass():
  enternewpass = input('Enter Your New 4 Digit Password: ' )
    
  for item in nochars:
    if item in enternewpass:
      print('Error Unkown Character(s) Please Try Again!')
      break
    if len(enternewpass)  == 4: 
      global file_make
      file_make = open('savedpassword.txt', 'w+')
      file_make
      file_make.write(enternewpass)
    else:
        print('Error To short or Long try again')


def havepassword():
  login = input('Enter Your Password to access: ')
  with open('savedpassword.txt') as i:
    content = i.read()
    if login == content:
      with open('hiddentext.txt') as o:
        content2 = o.read()
        print(content2)

    else:
        print('Invalid Password--')
        os.system('cls||clear')
        checkfile()


def checkfile():
  if os.path.isfile('savedpassword.txt'):
    print('Existing Password Found')
    havepassword()
  else:
    newpass()


  
    
checkfile()
