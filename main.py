# student club member checher
from pyscript import display, document

def student_club(e):
    document.getElementById("student").innerHTML = ''
    studentnamefirst = document.getElementById("student_name_first").value
    ictclubfirst = ['cean', 'joaquin', 'cholo', 'JM', 'mohammad']
    studentnamelast = document.getElementById("student_name_last").value
    ictclublast = ['alagar', 'tabije', 'comanda', 'piansay', 'calaca']
    member_checker = studentnamefirst in ictclubfirst and studentnamelast in ictclublast
    display_message = (f'Sorry, you are not a member', f'Congratulations, {studentnamefirst} you are now a part of the OBMC ict club')

    display(display_message[member_checker], target="student")