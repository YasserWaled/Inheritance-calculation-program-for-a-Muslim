from tkinter import messagebox
from tkinter import *
from Inheritance_ import *
from Calculation import *

input_list = []  # الورثاء الذين قام المستخدم بادخالهم
st = ''  # الوريث الذي اختاره المستخدم من القائمة


def add(val):
    global st
    st = val


x = 700
y = 140
i = 0


def show():
    global comboBox_list
    global x
    global y
    global i
    global st
    # global input_list
    if st != '':
        input_list.append(st)

        wa = Label(fr2, font=('VEXA', 10),
                   text=input_list[i], fg='#fed049', bg='#3d5656')
        wa.place(x=x, y=y)
        if input_list[i] == 'اب':
            comboBox_list.delete('اب')
            st = ""
        elif input_list[i] == 'جد':
            comboBox_list.delete('جد')
            st = ""
        elif input_list[i] == 'ام':
            comboBox_list.delete('ام')
            st = ''
        elif input_list[i] == 'جدة':
            comboBox_list.delete('جدة')
            st = ''
        elif input_list[i] == 'زوج':
            comboBox_list.delete('زوج')
            st = ''
        if input_list[i] == 'زوج':
            comboBox_list.delete('زوجة')
            st = ''
        elif input_list[i] == 'زوجة':
            comboBox_list.delete('زوج')
            st = ''
        i += 1
        x = x - 350
        if x <= 0:
            x = 700
            y = y + 30


mainwind = Tk()  # النافذة الرئيسية

mainwind.geometry('800x653+350+30')
mainwind.config(background='#3d5656')
# mainwind.iconbitmap("D:\\4rth year data\\Python\\project\\مشروع المواريث\\IMG20221120083447.jpg")
mainwind.title('مشروع المواريث')
mainwind.resizable(False, False)

# Frame 1 to title
fr1 = Frame(mainwind, width=800, height=120, bg='#3d5656')
fr1.place(x=0, y=0)
title = Label(fr1, font=('Aviny', 30),
              text='لِقَوْمٍ يُوقِنُونََ', fg='#fed049', bg='#3d5656')
title.place(x=325, y=40)
title = Label(fr1, font=('Aviny', 20),
              text='وَمَنْ أَحْسَنُ مِنَ اللَّه حُكْمًاَ', fg='#fed049', bg='#3d5656')
title.place(x=300, y=0)
# Frame 4 as dash
fr4 = Frame(width=200, height=2, bg='#CFFDE1')
fr4.place(x=300, y=120)

# frame 2 to process
fr2 = Frame(width=800, height='430', bg='#3d5656')
fr2.place(x=0, y=122)
entiry = Entry(fr2, font=('VEXA', 15), fg='#000000',
               bg='#CFFDE1', relief='groove', width="10")
entiry.place(x=510, y=10)
title_entiry = Label(fr2, font=('VEXA', 15),
                     text="أدخل التركة", fg='#fed049', bg='#3d5656')
title_entiry.place(x=610, y=10)
#####-------------------------------------------------------------------------------
entiry2 = Entry(fr2, font=('VEXA', 15), fg='#000000',
                bg='#CFFDE1', relief='groove', width="10")
entiry2.place(x=110, y=10)
title_entiry2 = Label(fr2, font=('VEXA', 15),
                      text="أدخل الوصية إن وجدت", fg='#fed049', bg='#3d5656')
title_entiry2.place(x=210, y=10)
#####------------------------------------------------------------------------------
menu_bt = Menubutton(fr2, font=('VEXA', 15), text='تحديد الورثة',
                     fg='#3d5656', bg='#CFFDE1', relief='groove')
menu_bt.place(x=345, y=50)
comboBox_list = Menu(menu_bt, tearoff=0)
menu_bt['menu'] = comboBox_list

comboBox_list.add_radiobutton(label='ابن', font=(
    'VEXA', 10), command=lambda: add('ابن'))
comboBox_list.add_radiobutton(label='ابن الابن', font=(
    'VEXA', 10), command=lambda: add('ابن الابن'))
comboBox_list.add_radiobutton(label='اب', font=(
    'VEXA', 10), command=lambda: add('اب'))
comboBox_list.add_radiobutton(label='جد', font=(
    'VEXA', 10), command=lambda: add('جد'))
comboBox_list.add_radiobutton(label='زوج', font=(
    'VEXA', 10), command=lambda: add('زوج'))
comboBox_list.add_radiobutton(label='اخ', font=(
    'VEXA', 10), command=lambda: add('اخ'))
comboBox_list.add_radiobutton(label='ابن الاخ', font=(
    'VEXA', 10), command=lambda: add('ابن الاخ'))
comboBox_list.add_radiobutton(label='اخ لاب', font=(
    'VEXA', 10), command=lambda: add('اخ لاب'))
comboBox_list.add_radiobutton(label='ابن الاخ لاب', font=(
    'VEXA', 10), command=lambda: add('ابن الاخ لاب'))
comboBox_list.add_radiobutton(label='اخ لام او اخت لام', font=(
    'VEXA', 10), command=lambda: add('اخ لام او اخت لام'))
comboBox_list.add_radiobutton(label='اخت', font=(
    'VEXA', 10), command=lambda: add('اخت'))
comboBox_list.add_radiobutton(label='اخت لاب', font=(
    'VEXA', 10), command=lambda: add('اخت لاب'))
comboBox_list.add_radiobutton(label='عم', font=(
    'VEXA', 10), command=lambda: add('عم'))
comboBox_list.add_radiobutton(label='عم لاب', font=(
    'VEXA', 10), command=lambda: add('عم لاب'))
comboBox_list.add_radiobutton(label='ابن العم', font=(
    'VEXA', 10), command=lambda: add('ابن العم'))
comboBox_list.add_radiobutton(label='ابن العم لاب', font=(
    'VEXA', 10), command=lambda: add('ابن العم لاب'))
comboBox_list.add_radiobutton(label='بنت', font=(
    'VEXA', 10), command=lambda: add('بنت'))
comboBox_list.add_radiobutton(label='بنت الابن', font=(
    'VEXA', 10), command=lambda: add('بنت الابن'))
comboBox_list.add_radiobutton(label='ام', font=(
    'VEXA', 10), command=lambda: add('ام'))
comboBox_list.add_radiobutton(label='جدة', font=(
    'VEXA', 10), command=lambda: add('جدة'))
comboBox_list.add_radiobutton(label='زوجة', font=(
    'VEXA', 10), command=lambda: add('زوجة'))

add_bt = Button(fr2, font=('VEXA', 13), text='اضافه', fg='#3d5656',
                bg='#fed049', width=7, command=lambda: show())
add_bt.place(x=365, y=90)

# Frame 3 to button
fr3 = Frame(width=800, height='85', bg='#3d5656')
fr3.place(x=0, y=547)

totalMoney = 0


def ca(list):
    x = 550
    y = 110
    s = str(entiry.get())
    slist = s.split(sep=".")

    for sl in slist:
        if (sl.isdigit() and len(slist) <= 2) and s != "" and float(entiry.get()) > 0:
            totalMoney = float(entiry.get())
        else:
            messagebox.showerror("حدث خطأ في ادخال التركة",
                                 "الرجاء ادخال التركة في هيئة رقم صحيح او عشري")
            return None
       #---------------------------------------------------------------------------------------------
        #الوصية تكون  فيما دون الثلث

    third = totalMoney / 3
    will = 0
    if float(entiry2.get()) < third:
        totalMoney = totalMoney - float(entiry2.get())
        will = float(entiry2.get())
    else:
        totalMoney = totalMoney - third
        will = third

    lb = Label(fr2, font=('VEXA', 10), text=will, fg='#212121', bg='#3d5656')
    lb.place(x=210, y=5)

        #-------------------------------------------------------------------------------------------


    for l in list:
        heirs_dict[english_heirs[arbic_hiers.index(l)]] += 1

    amount = all_amounts(heirs_dict)

    amount = dev(amount, heirs_dict)

    if sum(amount) < 24:
        amount = recalc(amount)
    for o in range(0, len(list)):
        if o % 2 == 0:
            x = 550
            y = y + 30
        else:
            x = 200
        if heirs_dict[english_heirs[arbic_hiers.index(list[o])]] > 1 and (fraction_list[int(indx(amount, english_heirs[
            arbic_hiers.index(list[o])]))] != "الباقي تعصيبا") and (fraction_list[int(indx(amount, english_heirs[
            arbic_hiers.index(list[o])]))] != "الباقي للذكر مثل حظ الانثيين") and (
                fraction_list[int(indx(amount, english_heirs[
                    arbic_hiers.index(list[o])]))] != "السدس + الباقي") and (
                fraction_list[int(indx(amount, english_heirs[
                    arbic_hiers.index(list[o])]))] != "محجوب"):
            lb = Label(fr2, font=('VEXA', 10), text="مشترك في " + fraction_list[int(indx(amount,
                                                                                         english_heirs[
                                                                                             arbic_hiers.index(
                                                                                                 list[o])]))],
                       fg='#212121', bg='#3d5656')
            lb.place(x=x, y=y)
            lb2 = Label(fr2, font=('VEXA', 12, "bold"), text=(round((amount[english_heirs[arbic_hiers.index(
                list[o])]] / heirs_dict[english_heirs[arbic_hiers.index(list[o])]] / sum(amount)) * totalMoney, 2)),
                        fg='white', bg='#3d5656')
            lb2.place(x=x - 70, y=y)
        else:
            lb = Label(fr2, font=('VEXA', 10), text=fraction_list[int(indx(
                amount, english_heirs[arbic_hiers.index(list[o])]))], fg='#212121', bg='#3d5656')
            lb.place(x=x, y=y)
            lb2 = Label(fr2, font=('VEXA', 12, "bold"), text=(round((amount[english_heirs[arbic_hiers.index(
                list[o])]] / heirs_dict[english_heirs[arbic_hiers.index(list[o])]] / sum(amount)) * totalMoney, 2)),
                        fg='white', bg='#3d5656')
            lb2.place(x=x - 70, y=y)


process_bt = Button(fr3, font=('VEXA', 15), text='تقسيم الميراث',
                    fg='#3d5656', bg='#fed049', width=20, command=lambda: ca(input_list))
process_bt.place(x=300, y=30)
mainwind.mainloop()
