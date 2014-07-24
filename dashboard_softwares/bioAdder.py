import os.path

def initializeGlobals():
    global ID, tel, email, name, nameSplit, job
    name = input("Name:")
    job = input("Job Title: ")
    ID = input("ID: ")
    tel = input("Phone Extension:")
    nameSplit = name.split(" ")



def main():
    initializeGlobals()
    filename = ID+".txt"
    fullName = os.path.join(os.getcwd()+"\people\\",filename)
    file = open(fullName, "w")
    file.write(" <!-- "+name +" -->\n")

    file.write("    <div id=\""+ID+"\" class=\"row featurette\" style=\"margin-bottom: 100px\">\n<div class=\"col-md-5\">\n")
    file.write("        <img class=\"featurette-image img-responsive img-rounded\" width=\"50%\"  src=\"../Headshots/"+nameSplit[0]+"_"+nameSplit[1]+".jpg\" alt=\"Generic placeholder image\">\n</div>\n<div class=\"col-md-5\">\n")
    file.write("        <h2 class=\"featurette-heading\">"+nameSplit[0]+ "<span class=\"text-muted\"> "+nameSplit[1]+"</span></h2>\n")
    file.write("        <p class=\"lead\"><b style=\"color: Gray\">"+job+"</b> <br>\n")
    file.write("            <span class=\"text-muted\">email: </span><a href=\"mailto:"+ID+"@lee-associates.com?Subject=Hello%20"+nameSplit[0]+"!\" target=\"_top\">"+ID+"@lee-associates.com</a><br>\n")
    file.write("            <span class=\"text-muted\">telephone: </span> 212.776."+tel+"<br><br>\n")
    file.write("            <span class=\"text-muted\">specialties <br></span>\n")

    done = False
    while not done :
        specialty = input("Specialty or press \"Enter\" when done:")
        if (specialty==""):
            done = True
        else:
            file.write("                "+specialty+" <br>\n")
    file.write("            <br><span class=\"text-muted\">geographies<br> </span>"+input("Geographies: ")+"<br><br>\n")
    file.write("            <span class=\"text-muted\">real estate career<br> </span>"+input("Career Start: ")+"<br>\n")
    file.write("        </p>\n")
    file.write("        <div class=\"accordion\" id=\"accordion2\" style=\"font-family: Futura \">\n")


    #Select Transactions
    print("SELECT TRANSACTIONS\n")
    file.write("            <div class=\"accordion-group\" >\n")
    file.write("                <div class=\"accordion-heading\">\n")
    file.write("                    <a class=\"accordion-toggle\" data-toggle=\"collapse\" data-parent=\"#accordion2\" href=\"#"+ID+"TransCollapsable\"> Select Transactions </a>\n")
    file.write("                </div>\n")
    file.write("                <div id=\""+ID+"TransCollapsable\" class=\"accordion-body collapse\">\n")
    file.write("                    <div class=\"accordion-inner\">\n")
    file.write("                        <ul>\n")
    print("    For the next three sections:\n    Enter the data or hit the \"Enter\" key when finished.")
    transDone = False
    while not transDone:
        transaction = input("Select Transaction:")
        if (transaction==""):
            transDone = True
        else:
            file.write("                            <li>"+transaction+"</li>\n")
    file.write("                        </ul>\n")
    file.write("                    </div>\n")
    file.write("                </div>\n")
    file.write("            </div>\n")


    #Affiliations and Awards
    print("AFFILIATIONS AND AWARDS")
    file.write("            <div class=\"accordion-group\" >\n")
    file.write("                <div class=\"accordion-heading\">\n")
    file.write("                    <a class=\"accordion-toggle\" data-toggle=\"collapse\" data-parent=\"#accordion2\" href=\"#"+ID+"AACollapsable\"> Affiliations and Awards </a>\n")
    file.write("                </div>\n")
    file.write("                <div id=\""+ID+"AACollapsable\" class=\"accordion-body collapse\">\n")
    file.write("                    <div class=\"accordion-inner\">\n")
    file.write("                        <ul>\n")

    awardDone = False
    while not awardDone:
        award = input("Affiliation/Award:")
        if (award==""):
            awardDone = True
        else:
            file.write("                            <li>"+award+"</li>\n")
    file.write("                        </ul>\n")
    file.write("                    </div>\n")
    file.write("                </div>\n")
    file.write("            </div>\n")


    #Education and Licenses
    print("EDUCATION AND LICENSES")
    file.write("            <div class=\"accordion-group\" >\n")
    file.write("                <div class=\"accordion-heading\">\n")
    file.write("                    <a class=\"accordion-toggle\" data-toggle=\"collapse\" data-parent=\"#accordion2\" href=\"#"+ID+"EDUCollapsable\"> Education and Licenses </a>\n")
    file.write("                </div>\n")
    file.write("                <div id=\""+ID+"EDUCollapsable\" class=\"accordion-body collapse\">\n")
    file.write("                    <div class=\"accordion-inner\">\n")
    file.write("                        <ul>\n")

    EDUDone = False
    while not EDUDone:
        EDU = input("Education/License:")
        if (EDU==""):
            EDUDone = True
        else:
            file.write("                            <li>"+EDU+"</li>\n")
    file.write("                        </ul>\n")
    file.write("                    </div>\n")
    file.write("                </div>\n")
    file.write("            </div>\n")
    file.write("        </div><!-- accordion close -->\n")
    file.write("    </div>\n")
    file.write("</div>  <!-- End of "+name+" -->\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("<!-- ALLOW SPACE -->\n")
    print("Done!")
main()