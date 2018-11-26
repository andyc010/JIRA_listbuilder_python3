import xml.etree.ElementTree as ET

""" Only applicable for JIRA XML query files """

""" 
    GOAL:
    Given an XML file from JIRA:
        -Gather information from the XML file

"""


class jiraListBuilder:
    line_text = ""
    output_text = ""

    """ constructor """
    def __init__(self):
        self

    """ given a JIRA XML file's  filename, return the root """
    def getRoot(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        return root

    """ given a root, return a list of JIRA keys (bug numbers) """
    def createList(self, root):
        returnList = []

        for key in root.iter("key"):
            returnList.append(key.text)
        return returnList
