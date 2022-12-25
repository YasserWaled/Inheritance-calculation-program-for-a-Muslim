from abc import ABC, abstractmethod

heirs_dict = {  # قاموس الورثة
    'son': 0,
    'son\'s son': 0,
    'father': 0,
    'grandfather': 0,
    'husband': 0,
    'brother': 0,
    'brother\'s son': 0,
    'father\'s brother': 0,
    'father\'s brother\'son': 0,
    'mother\'s brother & mother\'s sister': 0,
    'sister': 0,
    'father\'s sister': 0,
    'uncle': 0,
    'father\'s uncle': 0,
    'uncle\'s son': 0,
    'father\'s uncle\'s son': 0,
    'daughter': 0,
    'son\'s daughter': 0,
    'mother': 0,
    'grandmother': 0,
    'wife': 0,
}

################################# abstract class of Heir #################


class Heir(ABC):
    def __init__(self, heirsDict, number=0):
        self.heirsDict = heirsDict
        self.number = number

    @abstractmethod
    def isBlocked(self):
        pass

    @abstractmethod
    def amount(self):
        pass

    def isBlocked(self, blockers):
        for block in self.blockers:
            if self.heirsDict[block] > 0:
                return True
        return False
# son ################################3


class Son(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):

        if (self.heirsDict["daughter"] > 0):
            return -2
        else:
            return -1

######################################### sons of sons ##########################


class Sons_son(Heir):

    blockers = ["son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Sons_son.isBlocked(self, Sons_son.blockers) == False:
            if self.heirsDict["son\'s daughter"] > 0:
                return -2
            else:
                return -1
        else:
            return 0

# Father#########################################3


class Father(Heir):

    def __init__(self, heirsDict, number=1):
        Heir.__init__(self, heirsDict, number)

    def amount(self):

        if self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0:
            return 4
        else:
            return -3


###################################### Grandfather ###############################


class Grandfather(Heir):
    blockers = ["father"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Grandfather.isBlocked(self, Grandfather.blockers) == False:
            if self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0:
                return 4
            else:
                return -3  # الباقي
        else:
            return 0

#################################### Husband ############################################


class Husband(Heir):

    def __init__(self, heirsDict, number=1):
        Heir.__init__(self, heirsDict, number)

    def amount(self):

        if (self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0 or heirs_dict["daughter"] > 0
                or heirs_dict["son\'s daughter"] > 0):
            return 6
        else:
            return 12

# wife ##########################3


class Wife(Heir):
    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if (self.heirsDict["son"] > 0 or self.heirsDict["son\'s son"] > 0 or heirs_dict["daughter"] > 0
                or heirs_dict["son\'s daughter"] > 0):
            return 3
        else:
            return 6

#########################################brother###############################


class Brother(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Brother.isBlocked(self, Brother.blockers) == False:
            if (self.heirsDict["sister"] > 0):
                return -2
            else:
                return -1
        else:
            return 0

###################################brother by father##############################


class Brother_by_father(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Brother_by_father.isBlocked(self, Brother_by_father.blockers) == False:
            if (self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            elif (self.heirsDict["father\'s sister"] > 0):
                return -2
            else:
                return -1
        else:
            return 0
###################################brother son#####################################


class Brother_son(Heir):
    blockers = ["father", "son", "grandfather",
                "son\'s son", "brother", 'father\'s brother']

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Brother_son.isBlocked(self) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0
################################ brother by father sons ######################


class Brother_by_father_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son",
                "brother", 'father\'s brother', "brother\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Brother_by_father_son.isBlocked(self, Brother_by_father_son.blockers) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0
#################################### uncle ################################


class Uncle (Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother",
                'father\'s brother', "brother\'s son", "father\'s brother\'son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Uncle.isBlocked(self, Uncle.blockers) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0

###################################### uncle by father ############################


class Uncle_by_father(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother",
                'father\'s brother', "brother\'s son", "father\'s brother\'son", "uncle"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Uncle_by_father.isBlocked(self, Uncle_by_father.blockers) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0


#################################### uncle son ###############################


class Uncle_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother", 'father\'s brother',
                "brother\'s son", "father\'s brother\'son", "uncle", "father\'s uncle"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Uncle_son.isBlocked(self, Uncle_son.blockers) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0


################################################### uncle by father son#######################################


class Uncle_by_father_son(Heir):
    blockers = ["father", "son", "grandfather", "son\'s son", "brother", 'father\'s brother',
                "brother\'s son", "father\'s brother\'son", "uncle", "father\'s uncle", "uncle\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Uncle_by_father_son.isBlocked(self, Uncle_by_father_son.blockers) == False:
            if (self.heirsDict["father\'s sister"] > 0 or self.heirsDict["sister"] > 0) and (self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            else:
                return -1
        else:
            return 0


# daughter ##################################3


class Daughter(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):

        if (self.heirsDict["son"] == 0 and heirs_dict["daughter"] == 1):
            return 12
        elif(self.heirsDict["son"] == 0 and heirs_dict["daughter"] > 1):
            return 16
        elif(self.heirsDict["son"] >= 1 and heirs_dict["daughter"] >= 1):
            return -4  # return Son.amount()/2
        else:
            return -1

################################################# daughter of sons #############################


class Daughter_of_sons(Heir):

    blockers = ["son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Daughter_of_sons.isBlocked(self, Daughter_of_sons.blockers) == False:
            if (self.heirsDict["daughter"] >= 2 and self.heirsDict["son\'s son"] == 0):
                return 0
            elif (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
                  and self.heirsDict["son\'s daughter"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
                 and self.heirsDict["son\'s daughter"] > 1):
                return 16
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 1 and self.heirsDict["son\'s son"] == 0
                 and (self.heirsDict["son\'s daughter"] == 1 or self.heirsDict["son\'s daughter"] > 1)):
                return 4
            elif(self.heirsDict["son"] == 0 and self.heirsDict["son\'s son"] >= 1
                 and self.heirsDict["son\'s daughter"] >= 1):
                return -4
            else:
                return -1
        else:
            return 0

############################################ mother ############################################


class Mother(Heir):

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if (self.heirsDict["son"] >= 1 or self.heirsDict["daughter"] >= 1 or self.heirsDict["son\'s son"] >= 1
            or self.heirsDict["son\'s daughter"] >= 1) or (self.heirsDict["brother"] + self.heirsDict["sister"] +
                                                           self.heirsDict['father\'s brother'] + self.heirsDict["mother\'s brother & mother\'s sister"] +
                                                           self.heirsDict["father\'s sister"] > 1):

            return 4
        elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0 and self.heirsDict["son\'s son"] == 0
             and self.heirsDict["son\'s daughter"] == 0 and ((self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 0)
                                                             or (self.heirsDict["brother"] == 1 and self.heirsDict["sister"] == 0) or (self.heirsDict["brother"] == 0
                                                                                                                                       and self.heirsDict["sister"] == 1))):
            return 8
        else:
            return -1

# Grand mother########################################33


class Grand_mother(Heir):
    blockers = ["mother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Grand_mother.isBlocked(self, Grand_mother.blockers) == False:
            if(self.heirsDict['grandmother'] == 1):
                return 4
            else:
                return -1
        return 0

######################################sister###########################################


class Sister(Heir):

    blockers = ["father", "son", "grandfather", "son\'s son"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Sister.isBlocked(self, Sister.blockers) == False:

            if (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                    and self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                 and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                 and self.heirsDict["sister"] > 1 and self.heirsDict["brother"] == 0):
                return 16
            elif(self.heirsDict["brother"] >= 1):
                return -4
            else:
                return -1
        else:
            return 0
##################################### sister by father ####################################


class Sister_by_father(Heir):

    blockers = ["father", "son", "grandfather", "son\'s son", "brother"]

    def __init__(self, heirsDict, number=0):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Sister_by_father.isBlocked(self, Sister_by_father.blockers) == False:
            # هنا هحط شرط ان لو كان في اخت شقيقه صارت عصبه مع البنت او بنت الابن
            if (self.heirsDict["sister"] > 0) and (
                    self.heirsDict["son\'s daughter"] > 0 or self.heirsDict["daughter"] > 0):
                return 0
            elif (self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                  and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                  and self.heirsDict["brother"] == 0 and self.heirsDict["sister"] == 0
                  and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["father\'s sister"] == 1):
                return 12
            elif(self.heirsDict["son"] == 0 and self.heirsDict["daughter"] == 0
                 and self.heirsDict["son\'s son"] == 0 and self.heirsDict["son\'s daughter"] == 0
                 and self.heirsDict["sister"] == 0 and self.heirsDict["brother"] == 0
                 and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["father\'s sister"] >= 2):
                return 16
            elif(self.heirsDict["son"] == 0 and self.heirsDict["son\'s son"] == 0
                 and self.heirsDict["father\'s brother"] == 0 and self.heirsDict["sister"] == 1
                 and Sister.amount(self) == 12):
                return 4
            elif self.heirsDict['father\'s brother']:
                return -4
            else:
                return -1
        else:
            return 0


##############################################################################################

# محتاجين نعمل حجب للاخ لاب لو كانت في اخت شقيقه عصبه مع البنات او بنات الابن


class Mother_sons(Heir):
    blockers = ["son", "son\'s son", "daughter",
                "son\'s daughter", "father", "grandfather"]

    def __init__(self, heirsDict, number=heirs_dict["mother\'s brother & mother\'s sister"]):
        Heir.__init__(self, heirsDict, number)

    def amount(self):
        if Mother_sons.isBlocked(self, Mother_sons.blockers) == False:
            if sum(self.heirsDict) == self.heirsDict["mother's brother & mother's sister"]:
                return -1
            elif (self.heirsDict["mother's brother & mother's sister"] > 1):
                return 8
            else:
                return 4
            return 0
