import os
import platform



if __name__ ==  '__main__':
    system_os = platform.system().lower()

    os.system("rm -rf ./*.html")

    if system_os == "windows":
        os.chdir("src")
        os.system("python ./compile.py")
        os.system("move *.html ../")
        os.system("cp *.xml ../")
        os.chdir("../")
    else:
        os.chdir("src")
        os.system("python compile.py")
        os.system("mv *.html ../")
        os.system("cp *.xml ../")
        os.chdir("../")

    os.system("git add -A")
    os.system("git commit -m \"update\"")
    os.system("git push")