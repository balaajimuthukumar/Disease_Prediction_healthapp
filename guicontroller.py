import tkinter as tk
import dataquestionnaireunit
import bayes_
import dataquestionnaireunit_newp
import time

"""def myfunc():
    def myfunc1():
        print("hai
    myfunc1()"""

"""def windowcreator():
    window = tk.Tk()
    return window
  
def windowdestroyer_oldp(value):
    window.destroy()

def windowdestroyer_newp(value):
    if value == object:
        value.destroy()"""

def expertsystemMainpage():
    window = tk.Tk()
    window.minsize(150,100)
    button0 = tk.Button(text="PatinetPortal",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),patientselectioncontroller()])
    button0.pack(pady=20)

def patientselectioncontroller():
    window = tk.Tk()
    def windowdestroyer_oldp():
        window.destroy()
        dataupdate_oldp("0")
    def windowdestroyer_newp():
        window.destroy()
        dataupdate_newp()
        
    oldpatient = tk.Button(text="Old Patient",width=25,height=1,bg="grey",fg="black",command=windowdestroyer_oldp)
    oldpatient.pack()

    newpatient = tk.Button(text="New Patient",width=25,height=1,bg="grey",fg="black", command=windowdestroyer_newp)
    newpatient.pack()

#Test Data entry dialog for the old patient
#all the Tests are listed in this window, user has to select one from the list    
  
def dataupdate_oldp(value):
    if value=="0":
        window = tk.Tk()
        myclass = dataquestionnaireunit.Test()

        """button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=window.destroy)
        button0.pack()"""
        
        button = tk.Button(text="GlucoseData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Glucosedata()])
        button.pack()

        button1 = tk.Button(text="LipidData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Lipiddata()])
        button1.pack()

        button2 = tk.Button(text="BloodPressureData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.BloodPressuredata()])
        button2.pack()

        button3 = tk.Button(text="UrineAlbuminData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Urinealbumindata()])
        button3.pack()

        button4 = tk.Button(text="GeneralUrineandSedimentData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Generalurineandsedimentdata()])
        button4.pack()

        button5 = tk.Button(text="UrineCreatinineData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.UrineCreatininedata()])
        button5.pack()

        button6 = tk.Button(text="OpthalmologyData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Opthalmologydata()])
        button6.pack()

        button7 = tk.Button(text="PhysicalFootData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Physicalfootdata()])
        button7.pack()

        button8 = tk.Button(text="FT4andTSHData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.FT4andTSHdata()])
        button8.pack()

        button9 = tk.Button(text="ECGData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.ECGdata()])
        button9.pack()

        button10 = tk.Button(text="WeightControlData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Weightcontroldata()])
        button10.pack()

        button11 = tk.Button(text="MorphologyData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Morphologydata()])
        button11.pack()

        button12 = tk.Button(text="ElectrolytesData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Electrolytesdata()])
        button12.pack()

        button13 = tk.Button(text="CarotidUltrasoundData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Carotidultrasounddata()])
        button13.pack()

        button14 = tk.Button(text="ANPBNPConcentrationData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.ANPBNPconcentrationdata()])
        button14.pack()

        button15 = tk.Button(text="GFRrateData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.GFRratedata()])
        button15.pack()

        button16 = tk.Button(text="XrayData",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass.Xraydata()])
        button16.pack() 

#Questionnaire session for the old patient
#Each test will have a separate window
def dataentry_oldp(qns):
    def getval():
        value = entry.get()
        print(value)

    label = tk.Label(text=qns)
    label.pack()
    entry = tk.Entry()
    button0 = tk.Button(text="O",width=2,height=1,bg="grey",fg="black",command=getval)
    entry.pack()
    button0.pack()
    
#Questionnaire session for the new patient
#Each question will have a separate window
def dataentry_newp(value,set1):
    print(type(value))
    ans = value
    bayesian  = [0,0,0]
    print(ans)
    mystring = set1
    arrval = bayes_.bayes(ans,bayesian)
    for i in range(0,3):
        arrval[i] = int(arrval[i]*100)
    print(arrval)
    fp = open(r"C:\Users\mbala\Desktop\{0}.txt".format(mystring),"a+")
    for i in range(0,3):
        fp.write("{0}\n".format(arrval[i]))
    fp.close()    

def probcalculator(string):
    strng = string
    #for i in range(7):
    k = open(r"C:\Users\mbala\Desktop\{0}.txt".format(str(strng)),"r")
        #value = slice(0,2)
        #value = fp.read()
        #fp.close()
        #myval = value.split("\n")

    lines = k.readlines()     #i am reading lines here
    print(lines)
    counter = 0          #counter update each time number is entered
    lists = list()
    lists1 = list()
    for line in lines:            #taking each line
        print("indide lines  line:",line)
        val = line.split("\n")
        lists.append(val[0])
        print("inside lines  val:",val)
    print("listvalue",lists)
    conv = 0
    for i in range(len(lists)):
        myval = lists[i]
        if myval.isspace():
            conv += 0
        else:
            conv += int(myval)
        print(conv)
        print("lists1:",int(myval))
    prob = (conv)/3
            
    fp = open(r"C:\Users\mbala\Desktop\result.txt","a+")
    fp.write(str(int(prob)))
    fp.write("\n")
    fp.close()

    #for i in range(7):
    fp = open(r"C:\Users\mbala\Desktop\{0}.txt".format(str(strng)),"r+")
    fp.truncate(0)
    fp.close()        
    
def dataupdate_newp():
    
    myswitch = dataquestionnaireunit_newp.switch()    
    window = tk.Tk()
    def windowcreator():
        time.sleep(1)
        
    button = tk.Button(text="Questionnaire",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myswitch.case0()])
    button.pack()

def finalanswer():
    window = tk.Tk()
    fp = open(r"C:\Users\mbala\Desktop\result.txt","r")
    bayesian = fp.read()
    fp.close()
    fp = open(r"C:\Users\mbala\Desktop\result.txt","r+")
    fp.truncate(0)
    fp.close()
    label = tk.Label(text=bayesian)
    label.pack()
    button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[window.destroy()])
    button0.pack()    
    

