import os, fnmatch

# Find and replace in files in a directory
ogText = "<li><a href=\"about.html\">Sobre<\/a><\/li>"

newText = "" 


#The Function
def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

#The Order
findReplace("/home/zany/ZanyMarketing/CLIENTES/Victoh/victoh/", ogText, newText, "*.html")
findReplace("/home/zany/ZanyMarketing/CLIENTES/Victoh/victoh/", ogText, newText, "*.css")
findReplace("/home/zany/ZanyMarketing/CLIENTES/Victoh/victoh/", ogText, newText, "*.scss")
findReplace("/home/zany/ZanyMarketing/CLIENTES/Victoh/victoh/", ogText, newText, "*.js")
