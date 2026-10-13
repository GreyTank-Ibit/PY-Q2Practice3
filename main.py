from pyscript import document,display

def checkNum(e):

    num_bers= ["1", "9", "12", "15", "16"]

    num1=document.getElementById("num1").value
    name="Gian Nevilson Salazar Ibito"

    confirm_num = num1 in num_bers

    message= (f'Me sorry {name}, your number no find.', f'Yahoo! {name}, you number was found!')


    document.getElementById("output1").innerHTML = message[confirm_num]