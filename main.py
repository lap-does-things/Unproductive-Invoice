from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
global noactions 
noactions = True
DATA = [["*"]]
# TODO : implement editing a specified cell
def refreshtable(DATA):
    return Table(DATA, style=TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( -1 , -1 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( -1, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] ))

def menu(pdf,title,table,titleStyle):
    for k in DATA:
        print()
        print('\t'.join(map(str, k))) # TODO: make this prettier
        print()
    print("0. Build the invoice")
    print("1. Add a new column")
    print("2. Add a new row")
    print("3. Delete a row TODO")
    print("4. Delete a column TODO")
    print("5. Change the invoice title") 
    print("6. Exit")
    choice = input("Enter your choice: ")
    # TODO : add an option to change the style of the table
    if choice == "0":
        table = refreshtable(DATA)
        pdf.build([title, table])
        print("The invoice has been built!!")
    elif choice == "1":
        add_row(pdf,title,table)
    elif choice == "2":
        add_column(pdf,title,table)
    elif choice == "3":
        delete_row(pdf,title,table)
    elif choice == "4":
        delete_column(pdf,title,table)
    elif choice == "6":
        exit()
    elif choice == "5":
        t = input("Enter the title of the invoice: ")
        title = Paragraph(t, titleStyle)
        menu(pdf,title,table,titleStyle)
    else:
        print("Invalid choice")
        menu(pdf,title,table,titleStyle)

def add_row(pdf,title,table):
    global DATA
    global noactions
    if noactions:
        DATA[0][0] = input("Enter the name of the new row: ")
        noactions = False
    else:
        DATA[0].append(input("Enter the name of the new row: "))
    menu(pdf,title,table,titleStyle)

def add_column(pdf,title,table):
    global DATA
    DATA.append(input("Input new row SEPARATED BY COMMAS: ").strip().split(","))
    menu(pdf,title,table,titleStyle)

def delete_row(pdf,title,table):
    global DATA
    #DATA.pop() ## FIXME breaks everything ## FIXEDYOU
    DATA.pop(int(input("Enter the row number to delete (from 1): ")))
    menu(pdf,title,table,titleStyle)

def delete_column(pdf,title,table):
    global DATA
    #DATA.pop() ## FIXME same as above ## FIXEDYOU
    a = int(input("Enter the column number to delete (from 1): "))
    for i in range(len(DATA)):
        DATA[i].pop(a-1)
    menu(pdf,title,table,titleStyle)


def main():
    global DATA
    global titleStyle
    pdf = SimpleDocTemplate("Invoice.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    titleStyle = styles["Heading1"]
    titleStyle.alignment = 1 # 0: left, 1: center, 2: right
    titleStyle.fontSize = 20
    t = input("Enter the title of the invoice: ")
    title = Paragraph(t, titleStyle)
    table = Table

    #INIT PART IS OVER

    table = refreshtable(DATA)
    menu(pdf,title,table,titleStyle)

if __name__ == "__main__":
    main()