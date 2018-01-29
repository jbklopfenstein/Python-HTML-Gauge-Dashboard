##########################################################################################################################
#                                                                                                                        #
#                                                    GATEFINDER v.8                                                      #
#                                                                                                                        #
# This script looks for any ISV Technology pages under DataCenter, Network, Collaboration, etc., for "gate" status,      #
# "project" name and "category" names; and updates the appropriate ISV dashboard tabs by editing the appropriate         #
# category's section.md file with HTML div classes (gauge divs) accordingly.                                                          #
#                                                                                                                        #
# Author: Jeff Klopfenstein, jklopfen@cisco.com                                                                          #
#                                                                                                                        #
# Notes:                                                                                                                 #
# 1. Looks for any main directory pages containing "default.md" for gate info,                                           #
#    and parses that file's frontmatter YAML for the "project" key, and "category" key, to add the correspondng status   #
#    HTML gauge for a project to the specified category tab(s) on the ISV dashboard.                                     #
# 2. The "frontend-content" CI pipeline resets all categories' section.md files in /var/www/html/user/pages/, starting   #
#    with a clean dashboard each time the pipeline runs. So there's no need for this code to check a category tab for    #
#    whether a specific technology gauge already exists there.                                                           #
# 3. This code is dependent on first running the gatefind.sh script to create and populate the "projectgates" file.      #
# 4. The "projectgates" file should also be removed before running again, by running the gateclear.sh script.            #
# 5. #3 and #4 have been added to the "frontend-content" pipeline.                                                       #
#                                                                                                                        #
##########################################################################################################################


import os
import fileinput
import sys
import yaml


def extractproject(filename):
    '''
    Opens file containing frontmatter YAML, and looks for 'project' key.
    '''
    with open(filename) as extracted:
        projectstring = ""
        for line in extracted:
            if "project:" in line:
                projectstring += line
    projectdict = yaml.load(projectstring)
    projectname = projectdict.get("project")
    return projectname

def extractcategory(filename):
    '''
    Opens file containing frontmatter YAML, and looks for 'category' key, which is a list of categories.
    '''
    with open(filename) as extracted:
        categorystring = ""
        for line in extracted:
            if "category:" in line:
                categorystring += line
    categorydict = yaml.load(categorystring)
    categorylist = categorydict.get("category")
    return categorylist

def update_line(file_name, old_line, new_line):
    '''
    Overwrites placeholder HTML code with HTML code for new gauges
    '''
    for line in fileinput.input(file_name, inplace=1):
        if old_line in line:
            line = line.replace(old_line,new_line)
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)

def populatecanceldict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate Cancel
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techcanceldict = {}
    for line in searchfile:
        if "default.md:    gate: cancel" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            # techgate = b[2]
            # gatekey = techgate.splitlines()[0]  #removes trailing \n newline in this value
            techcanceldict.update({techheading:techpath})
    return techcanceldict
    searchfile.close()

def populateholddict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate Hold
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techholddict = {}
    for line in searchfile:
        if "default.md:    gate: hold" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techholddict.update({techheading:techpath})
    return techholddict
    searchfile.close()

def populategate5dict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate 5
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techgate5dict = {}
    for line in searchfile:
        if "default.md:    gate: 5" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techgate5dict.update({techheading:techpath})
    return techgate5dict
    searchfile.close()

def populategate4dict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate 4
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techgate4dict = {}
    for line in searchfile:
        if "default.md:    gate: 4" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techgate4dict.update({techheading:techpath})
    return techgate4dict
    searchfile.close()

def populategate3dict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate 3
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techgate3dict = {}
    for line in searchfile:
        if "default.md:    gate: 3" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techgate3dict.update({techheading:techpath})
    return techgate3dict
    searchfile.close()

def populategate2dict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate 2
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techgate2dict = {}
    for line in searchfile:
        if "default.md:    gate: 2" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techgate2dict.update({techheading:techpath})
    return techgate2dict
    searchfile.close()

def populategate1dict():
    '''
    Gets a dict of tech-heading_to_filepath, in gate 1
    '''
    searchfile = open("projectgates", "r") #should use context manager here?
    techgate1dict = {}
    for line in searchfile:
        if "default.md:    gate: 1" in line:
            a = line.split(":")
            techpath = a[0]
            b = line.split("/")
            techheading = b[6]
            techgate1dict.update({techheading:techpath})
    return techgate1dict
    searchfile.close()


def main():
    canceldict = populatecanceldict()
    holddict = populateholddict()
    gate5dict = populategate5dict()
    gate4dict = populategate4dict()
    gate3dict = populategate3dict()
    gate2dict = populategate2dict()
    gate1dict = populategate1dict()

    '''ADD CANCEL GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in canceldict.items():
        print(heading + " = cancel, and is in " + path)
        tech_name = extractproject(path) #function opens each file with 'default.md gate:#', and looks for project key.
        cat_list = extractcategory(path) #function opens same file and looks for category key, which is a list of categories.
        #Iterate over each category in the list, read each category's section.md file and proceed with conditionals below.
        for category in cat_list:
            currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
            #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
            thecat = open(currentcatfile, 'r')
            catname = thecat.read()
            thecat.close()
            #with open(currentcatfile, 'r') as catname: #problems with this file option since opening same file in update_line function below within this same loop
            #If the project key is na, continue to next iteration of for loop
            if tech_name == "na":
                continue
            #Else update each category's section.md file with new status gauge div class for each heading in canceldict
            else:
                print tech_name + " as Cancelled is being added to " + category
                update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Cancel --></h4><br>')
                update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--alt gauge--large" data-percentage="0">')
                update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(currentcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-error icon-xlarge"></div>')
                update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the currentcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(currentcatfile, 'a') as catname:
                    catname.write(addfooter)

    '''ADD HOLD GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in holddict.items():
        if heading not in canceldict:
            print(heading + " = hold, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " as Hold being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Hold --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--alt gauge--large" data-percentage="0">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-raise-hand icon-xlarge"></div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)

    '''ADD GATE5 GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in gate5dict.items():
        if (heading not in canceldict) and (heading not in holddict):
            print(heading + " = gate5, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " at Gate 5 being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate5 --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--success gauge--alt gauge--large" data-percentage="100">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-check icon-xlarge"></div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)

    '''ADD GATE4 GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in gate4dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict):
            print(heading + " = gate4, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " at Gate 4 being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate4 --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--primary gauge--alt gauge--large" data-percentage="80">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">4</div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)

    '''ADD GATE3 GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in gate3dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict):
            print(heading + " = gate3, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " at Gate 3 being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate3 --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--warning-alt gauge--alt gauge--large" data-percentage="60">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">3</div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)

    '''ADD GATE2 GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in gate2dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict) and (heading not in gate3dict):
            print(heading + " = gate2, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " at Gate 2 being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate2 --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--warning gauge--alt gauge--large" data-percentage="40">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">2</div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)

    '''ADD GATE1 GAUGES TO PROPER CATEGORY TABS'''
    for heading,path in gate1dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict) and (heading not in gate3dict) and (heading not in gate2dict):
            print(heading + " = gate1, and is in " + path)
            tech_name = extractproject(path)
            cat_list = extractcategory(path)
            for category in cat_list:
                currentcatfile = "/var/www/html/user/pages/home/_" + category.lower() + "/section.md"
                #currentcatfile = "/home/jeff/workspace/gatefindertestenv/_" + category.lower() + "/section.md"
                thecat = open(currentcatfile, 'r')
                catname = thecat.read()
                thecat.close()
                if tech_name == "na":
                    continue
                else:
                    print tech_name + " at Gate 1 being added to " + category
                    update_line(currentcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                    update_line(currentcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate1 --></h4><br>')
                    update_line(currentcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--danger gauge--alt gauge--large" data-percentage="20">')
                    update_line(currentcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                    update_line(currentcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                    update_line(currentcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace7 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                    update_line(currentcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                    update_line(currentcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                    update_line(currentcatfile, '<!-- catplace11 -->', '            </div>')
                    update_line(currentcatfile, '<!-- catplace12 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                    update_line(currentcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">1</div>')
                    update_line(currentcatfile, '<!-- catplace15 -->', '        </div>')
                    update_line(currentcatfile, '<!-- catplace16 -->', '    </div>')
                    update_line(currentcatfile, '<!-- catplace17 -->', '</div>')
                    update_line(currentcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                    update_line(currentcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                    update_line(currentcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                    update_line(currentcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                    update_line(currentcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                    update_line(currentcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                    forcategory = open("newdivfooter", "r")
                    addfooter = forcategory.read()
                    forcategory.close()
                    with open(currentcatfile, 'a') as catname:
                        catname.write(addfooter)


    '''ADD CANCEL GAUGES TO THE ALL TAB'''
    allcatfile = "/var/www/html/user/pages/home/_all/section.md"
    #allcatfile = "/home/jeff/workspace/gatefindertestenv/_all/section.md"
    for heading,path in canceldict.items():
        print(heading + " = cancel, and is in " + path)
        tech_name = extractproject(path)
        allcat = open(allcatfile, 'r')
        allcatname = allcat.read()
        allcat.close()
        print ("tech name is " + tech_name)
        if tech_name == "na":
            continue
        else:
            print tech_name + " being added as Cancelled to ALL tab"
            update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
            update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Cancel --></h4><br>')
            update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--alt gauge--large" data-percentage="0">')
            update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
            update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
            update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
            update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
            update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
            update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
            update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
            update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
            update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
            update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
            update_line(allcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-error icon-xlarge"></div>')
            update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
            update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
            update_line(allcatfile, '<!-- catplace17 -->', '</div>')
            update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
            update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
            update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
            update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
            update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
            update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

            #Append new div class footer to the allcatfile file
            forcategory = open("newdivfooter", "r")
            addfooter = forcategory.read()
            forcategory.close()
            with open(allcatfile, 'a') as allcatname:
                allcatname.write(addfooter)

    '''ADD HOLD GAUGES TO THE ALL TAB'''
    for heading,path in holddict.items():
        if heading not in canceldict:
            print(heading + " = hold, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Hold to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Hold --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--alt gauge--large" data-percentage="0">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-raise-hand icon-xlarge"></div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

    '''ADD GATE5 GAUGES TO THE ALL TAB'''
    for heading,path in gate5dict.items():
        if (heading not in canceldict) and (heading not in holddict):
            print(heading + " = gate5, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Gate5 to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate5 --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--success gauge--alt gauge--large" data-percentage="100">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            <div class="gauge\__percentage icon-check icon-xlarge"></div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

    '''ADD GATE4 GAUGES TO THE ALL TAB'''
    for heading,path in gate4dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict):
            print(heading + " = gate4, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Gate4 to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate4 --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--primary gauge--alt gauge--large" data-percentage="80">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">4</div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

    '''ADD GATE3 GAUGES TO THE ALL TAB'''
    for heading,path in gate3dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict):
            print(heading + " = gate3, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Gate3 to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate3 --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--warning-alt gauge--alt gauge--large" data-percentage="60">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">3</div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

    '''ADD GATE2 GAUGES TO THE ALL TAB'''
    for heading,path in gate2dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict) and (heading not in gate3dict):
            print(heading + " = gate2, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Gate2 to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate2 --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--warning gauge--alt gauge--large" data-percentage="40">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">2</div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

    '''ADD GATE1 GAUGES TO THE ALL TAB'''
    for heading,path in gate1dict.items():
        if (heading not in canceldict) and (heading not in holddict) and (heading not in gate5dict) and (heading not in gate4dict) and (heading not in gate3dict) and (heading not in gate2dict):
            print(heading + " = gate1, and is in " + path)
            tech_name = extractproject(path)
            allcat = open(allcatfile, 'r')
            allcatname = allcat.read()
            allcat.close()
            if tech_name == "na":
                continue
            else:
                print tech_name + " being added as Gate1 to ALL tab"
                update_line(allcatfile, '<!-- catplace1 -->', '<div style="cursor: pointer; cursor: hand; hover float: left; margin-bottom: .25vw; margin-top: .25vw; margin-left: .5%; margin-right: .5%; width: 19%;" class="gauge-container panel panel--loose panel--bordered text-center panel--hover stagger-in animated animation-delay-500 clickdiv">')
                update_line(allcatfile, '<!-- catplace2 -->', '<a href="{{ base_url }}/content/project:' + tech_name + '"></a><h4 style="margin-bottom:0; margin-top:0; border-bottom: 1px solid #dfdfdf;">' + tech_name + '<!-- Gate1 --></h4><br>')
                update_line(allcatfile, '<!-- catplace3 -->', '    <div class="gauge gauge--danger gauge--alt gauge--large" data-percentage="20">')
                update_line(allcatfile, '<!-- catplace4 -->', '        <div class="gauge\__circle">')
                update_line(allcatfile, '<!-- catplace5 -->', '            <div class="mask full">')
                update_line(allcatfile, '<!-- catplace6 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace7 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace8 -->', '            <div class="mask half">')
                update_line(allcatfile, '<!-- catplace9 -->', '                <div class="fill"></div>')
                update_line(allcatfile, '<!-- catplace10 -->', '                <div class="fill fix"></div>')
                update_line(allcatfile, '<!-- catplace11 -->', '            </div>')
                update_line(allcatfile, '<!-- catplace12 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace13 -->', '        <div class="gauge\__inset">')
                update_line(allcatfile, '<!-- catplace14 -->', '            Gate # <div class="gauge\__percentage">1</div>')
                update_line(allcatfile, '<!-- catplace15 -->', '        </div>')
                update_line(allcatfile, '<!-- catplace16 -->', '    </div>')
                update_line(allcatfile, '<!-- catplace17 -->', '</div>')
                update_line(allcatfile, '</div> <!-- footplace1 -->', '                           <!-- catplace1 -->')
                update_line(allcatfile, '</div> <!-- footplace2 -->', '                       <!-- catplace2 -->')
                update_line(allcatfile, '</div> <!-- footplace3 -->', '                   <!-- catplace3 -->')
                update_line(allcatfile, '</div> <!-- footplace4 -->', '               <!-- catplace4 -->')
                update_line(allcatfile, '</section> <!-- footplace5 -->', '           <!-- catplace5 -->')
                update_line(allcatfile, '</div> <!-- footplace6 -->', '       <!-- catplace6 -->')

                #Append new div class footer to the allcatfile file
                forcategory = open("newdivfooter", "r")
                addfooter = forcategory.read()
                forcategory.close()
                with open(allcatfile, 'a') as allcatname:
                    allcatname.write(addfooter)

if __name__ == '__main__':
    main()
