from Inheritance_ import *

fraction_dict = {3: "الثمن",  # انصبة كل وارث في هيئة كسور عشرية (المفتاح هنا هو رقم البسط على المقام 24)
                 4: "السدس",
                 6: "الربع",
                 8: "الثلث",
                 12: "النصف",
                 16: "الثلثين",
                 0: "محجوب",
                 -1: "الباقي تعصيبا",
                 -3: "السدس + الباقي",
                 -2: "الباقي للذكر مثل حظ الانثيين",
                 -4: "الباقي للذكر مثل حظ الانثيين", }
fraction_list = []
arbic_hiers = ['ابن', 'ابن الابن', 'اب', 'جد', 'زوج', 'اخ', 'ابن الاخ', 'اخ لاب', "ابن الاخ لاب", 'اخ لام او اخت لام', 'اخت',
               'اخت لاب', 'عم', 'عم لاب', 'ابن العم', 'ابن العم لاب', 'بنت', 'بنت الابن', 'ام', 'جدة', "زوجة"]
english_heirs = ['son',
                 'son\'s son',
                 'father',
                 'grandfather',
                 'husband',
                 'brother',
                 'brother\'s son',
                 'father\'s brother',
                 'father\'s brother\'son',
                 'mother\'s brother & mother\'s sister',
                 'sister',
                 'father\'s sister',
                 'uncle',
                 'father\'s uncle',
                 'uncle\'s son',
                 'father\'s uncle\'s son',
                 'daughter',
                 'son\'s daughter',
                 'mother',
                 'grandmother',
                 'wife']


def sherch(dict, num=-3):  # دالة تقوم بالبحث عن قيمة معينة في القاموس المعطى لها كبارمييتر
    for di in dict:
        if dict[di] == num:
            return True

    return False


def indx(dict, element):  # دالة ترجع ترتيب قيمة ما في قاموس معطى كبارميتر وان لم تجدها ترجع -1
    p = 0
    for d in dict:
        if d == element:
            return p
        else:
            p += 1
    return -1


def sum(dict):  # دالة ترجع مجموع القيم في القاموس
    s = 0
    for d in dict:
        s += dict[d]
    return s


def dev(am={}, dict={}):  # تحديد نصيب الوارثون بالعصبة
    for u in am:
        # هنا نقوم بملئ ليست الانصبة
        fraction_list.append(fraction_dict[am[u]])

    bool = True  # لا يوجد توريث بالعصبة
    for a in am:
        if am[a] < 0:
            bool = False
    if(bool):
        return am
    else:
        b = True  # العصبة ليس بها الذكر مثل حظ الانثيين
        for aa in am:
            if am[aa] < -1:
                b = False
        if(b):
            for aaa in am:
                if am[aaa] == -1:
                    if 24-sum(am)-1 < 0:
                        am[aaa] = 0
                    else:
                        am[aaa] = 24-sum(am)-1
        elif(sherch(am, -3)):  # هناك اب او جد يرث السدس + الباقي

            if(sum(am)+3 >= 24):
                if(heirs_dict["father"] == 1):
                    am["father"] = 4
                else:
                    am["grandfather"] = 4
            else:
                if (heirs_dict["father"] == 1):
                    am["father"] = 24-sum(am)-3
                else:
                    am["grandfather"] = 24-sum(am)-3
        else:  # العصبة بها الذكر مثل حظ الانثيين
            remain = 24-sum(am)-6
            if remain < 0:
                remain = 0

            male = 0
            female = 0
            for i in am:
                if am[i] == -2:
                    male = dict[i]
                if am[i] == -4:
                    female = dict[i]
            arrow = remain/(male*2+female)
            # print(remain,arrow)
            for j in am:
                if am[j] == -2:
                    am[j] = 2*arrow*heirs_dict[j]
                if am[j] == -4:
                    am[j] = arrow*heirs_dict[j]
    return am


def recalc(am):  # دالة الرد (اذا كان مجموع الفرائض اقل من الواحد الصحيح)
    n = 24
    s = sum(am)
    for y in am:
        if y == "wife":  # الزوجة والزوج ممنوعون من الرد
            n = 24-am["wife"]
            s = s-am["wife"]
        if y == "husband":
            n = 24 - am["husband"]
            s = s - am["husband"]
    for u in am:
        if(u != "wife" and u != "husband"):

            am[u] = am[u]*n/s
    return am


totalMoney = 24  # مجموع التركة


def all_amounts(dict):  # انشاء كائي من كلاسات الورثة المتواجدين في اقرباء الميت
    am = {}
    for d in dict:
        if dict[d] > 0:
            if d == english_heirs[0]:
                son = Son(dict)
                am[d] = son.amount()
            elif d == english_heirs[1]:
                son_son = Sons_son(dict)
                am[d] = son_son.amount()
            elif d == english_heirs[2]:
                father = Father(dict)
                am[d] = father.amount()
            elif d == english_heirs[3]:
                grandfather = Grandfather(dict)
                am[d] = grandfather.amount()
            elif d == english_heirs[4]:
                hasband = Husband(dict)
                am[d] = hasband.amount()
            elif d == english_heirs[5]:
                brohter = Brother(dict)
                am[d] = brohter.amount()
            elif d == english_heirs[6]:
                brohter_son = Brother_son(dict)
                am[d] = brohter_son.amount()
            elif d == english_heirs[7]:
                father_brohter = Brother_by_father(dict)
                am[d] = father_brohter.amount()
            elif d == english_heirs[8]:
                father_brohter_son = Brother_by_father_son(dict)
                am[d] = father_brohter_son.amount()
            elif d == english_heirs[9]:
                mohter_son = Mother_sons(dict)
                am[d] = mohter_son.amount()
            elif d == english_heirs[10]:
                sister = Sister(dict)
                am[d] = sister.amount()
            elif d == english_heirs[11]:
                father_sister = Sister_by_father(dict)
                am[d] = father_sister.amount()
            elif d == english_heirs[12]:
                uncle = Uncle(dict)
                am[d] = uncle.amount()
            elif d == english_heirs[13]:
                father_uncle = Uncle_by_father(dict)
                am[d] = father_uncle.amount()
            elif d == english_heirs[14]:
                uncle_son = Uncle_son(dict)
                am[d] = uncle_son.amount()
            elif d == english_heirs[15]:
                father_uncle_son = Uncle_by_father_son(dict)
                am[d] = father_uncle_son.amount()
            elif d == english_heirs[16]:
                daughter = Daughter(dict)
                am[d] = daughter.amount()
            elif d == english_heirs[17]:
                son_daughter = Daughter_of_sons(dict)
                am[d] = son_daughter.amount()
            elif d == english_heirs[18]:
                mother = Mother(dict)
                am[d] = mother.amount()
            elif d == english_heirs[19]:
                grandmother = Grand_mother(dict)
                am[d] = grandmother.amount()
            elif d == english_heirs[20]:
                wife = Wife(dict)
                am[d] = wife.amount()
    return am
# amount=all_amounts(heirs_dict)
# amount=dev(amount,heirs_dict)
#
# if sum(amount)<24:
#     amount=recalc(amount)
# for l in amount:
    # print(l,(amount[l]/sum(amount))*totalMoney)#هذه الجملة تقوم بحل العول تلقائيا ان وجد
