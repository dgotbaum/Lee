import os.path
import datetime

sections = {}

def initializeGlobals():
    global  sections
    print("For the following sections, respond (y) or (n) if the section exists.")
    sections["Local"] = input("Local News:")
    sections["Business"] = input("Business News: ")
    sections["National"] = input("National News: ")
    sections["International"] = input("International:")
def newsSections(F, E):
    global sections
    prevWhite = False;
    white = "style=\"background-color: white\""
    notWhite = ""
    ordered = ["Local", "Business","National","International"]
    for section in ordered:
        if (sections[section] == "y"):
            print(section+" News")
            if not prevWhite:
                whiteInsert = white
                prevWhite = True
            else:
                whiteInsert = notWhite
                prevWhite = False
            #Dashboard
            F.write("    <br><br><div class=\"row featurette\" "+whiteInsert+">\n")
            F.write("        <div class=\"col-md=12\" id=\""+section.lower()+"\" style=\"padding: 100px 0px 100px 50px\">\n")
            F.write("            <h2 class=\"featurette-heading\">"+section+" News</h2>\n")
            #Email
            E.write("    <br><br><div class=\"row featurette\" "+whiteInsert+">\n")
            E.write("        <div class=\"col-md=12\" id=\""+section.lower()+"\" style=\"padding: 100px 0px 100px 50px\">\n")
            E.write("            <h2 class=\"featurette-heading\">"+section+" News</h2>\n")
            done = False
            while not done:
                summary = input("Write out summary or 0 when done:")
                if (summary == "0"):
                    done = True
                else:
                    source = input("News Source: ")
                    link = input("URL:")
                    #Dashboard
                    F.write("        <p class=\"lead\">"+summary+"\n")
                    F.write("        <a href=\""+link+"\">"+source+"</a></p><br>\n\n\n")
                    #Email
                    E.write("        <p class=\"lead\">"+summary+"\n")
                    E.write("        <a href=\""+link+"\">"+source+"</a></p><br>\n\n\n")
            F.write("    </div></div><br><br>\n")
            E.write("    </div></div><br><br>\n")

    F.write("\n")
    F.write("\n")
    F.write("\n")
    F.write("\n")
    F.write("<!-- ALLOW SPACE -->\n")



def head(F):
    F.write("<!DOCTYPE html>\n")
    F.write("<html lang=\"en\">\n")
    F.write("    <head>\n")
    F.write("        <meta charset=\"utf-8\">\n")
    F.write("        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    F.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    F.write("        <meta name=\"description\" content=\"\">\n")
    F.write("        <link rel=\"shortcut icon\" href=\"../../assets/ico/favicon.ico\">\n")
    F.write("        <link type=\"text/css\"  href=\"http://www.leeassociatesnyc.com/dashcss/bootstrap.css\" rel=\"stylesheet\">\n")
    F.write("        <link   href=\"http://www.leeassociatesnyc.com/dashcss/dashboard.css\" rel=\"stylesheet\">\n")
    F.write("    </head>\n")
    F.write("\n    <body>\n")
    F.write("        <br><br><img class=\"featurette-image img-responsive\" src=\"http://www.leeassociatesnyc.com/itk.png\" alt=\"Generic placeholder image\">\n")
    F.write("        <div class=\"container-fluid\">\n")
def navbar(F):
    with open('navbar.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            F.write(line)
    F.write("\n")
def foot(F):
    F.write("        </div>\n")
    F.write("        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>\n")
    F.write("        <script src=\"http://www.leeassociatesnyc.com/dashjs/bootstrap.min.js\"></script>\n")
    F.write("    </body>\n")
    F.write("</html>")



def eFoot(F):
    F.write("        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>\n")
    F.write("        <script src=\"http://www.leeassociatesnyc.com/dashjs/bootstrap.min.js\"></script>\n")
    F.write("        </td></tr></table>\n")
    F.write("    </body>\n")
    F.write("</html>")
def eHead(F):
    F.write("<!DOCTYPE html>\n")
    F.write("<html lang=\"en\">\n")
    F.write("    <head>\n")
    F.write("        <meta charset=\"utf-8\">\n")
    F.write("        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    F.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    F.write("        <meta name=\"description\" content=\"\">\n")
    F.write("        <link rel=\"shortcut icon\" href=\"../../assets/ico/favicon.ico\">\n")
    F.write("        <link type=\"text/css\"  href=\"http://www.leeassociatesnyc.com/dashcss/bootstrap.css\" rel=\"stylesheet\">\n")
    F.write("        <link   href=\"http://www.leeassociatesnyc.com/dashcss/dashboard.css\" rel=\"stylesheet\">\n")
    F.write("        <style>table {bgcolor:#dedede ;background:#dedede;}\n")
    F.write("        h2 { font-family: Cambria; font-weight: bold; color: #98002E; }\n")
    F.write("        p {font-family: Calibri; color: #717073; }\n")
    F.write("        a:link {font-family: Garamond; color:#7A0000;}</style>\n")
    F.write("    </head>\n")
    F.write("\n    <body>\n")
    F.write("        <table width=\"100%\"><tr><td> \n")
    F.write("        <br><br><img class=\"featurette-image img-responsive\" src=\"http://www.leeassociatesnyc.com/itk.png\" alt=\"Generic placeholder image\">\n")







def main():
    global file
    global email
    initializeGlobals()
    Fname = "index.html"
    i = datetime.datetime.now()
    datePath = str(i.month) + "-"+str(i.day)+"-"+str(i.year)
    path = os.getcwd()+"\InTheKnows\%s\\"% datePath
    if not os.path.exists(path):
        os.makedirs(path)
    fullName = os.path.join(path,Fname)
    email = open(os.path.join(path,"email.html"), "w")
    file = open(fullName, "w")

    head(file)
    eHead(email)
    navbar(file)
    newsSections(file,email)
    foot(file)
    eFoot(email)

    print("Done!")
main()