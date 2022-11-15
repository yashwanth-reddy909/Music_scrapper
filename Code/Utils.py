
                  

def deleteIntroTabs(s):
    """
    @param s: String where we want to delete tabs ("\t") and enters ("\r")
    @return: The same string "s" without those special characters
    """
    s = s.replace("\n","")
    #s = s.replace(" ","")
    s = s.replace("\t","")
    return s

def deleteSpaces(s):
    """
    @param s: String where we want to delete tabs ("\t"), enters ("\r") and spaces (" ")
    @return: The same string "s" without those special characters
    """
    s = s.replace(" ","")
    s = s.replace("\n","")
    s = s.replace("\t","")
    return s