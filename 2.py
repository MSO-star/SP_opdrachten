def fuction():
     a= 0
     b= 0
     eerste_input= input(" Geef een string:")
     tweede_input= input(" Geef een string:")

     for i in range(len(tweede_input)):
         if eerste_input[i] != tweede_input[i]:

          print (" Het eerste verschil zit op index:" , i)
          break



fuction()