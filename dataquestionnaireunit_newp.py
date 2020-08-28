from tkinter import *
import tkinter as tk
import datacollectionunit
import dataquestionnairebutton
import guicontroller
import bayes_

"""st = ['Heartattack','fever','cough']
A = OrderedDict()
A = {st[0]:1.0,st[1]:0.2,st[2]:0.3}
B = OrderedDict()
B = {st[0]:0.2,st[1]:0.4,st[2]:0.6}
Num = []
#print({i:int(A[i])*int(B[i]) for i in A})    
for i,j in enumerate(A):
    Num.append(A[j]*B[j])
    print(Num)"""

bayesian  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qns = [ "Are you physically active person?","How bad is your food habit?","Is your height and weight proportional?",
        "Do you consume food that contains sugar?",
        "How often do you smoke?","How often are you stressed or depressed?",
        "How often do you feel anxiety?","Whats your age?","How often do you consume Alcohol?",
        "How often do you suffer from lack of sleep?","Increased Thirst or urination?",
        "How good is your vision?","Are you in medication?", "Do you feel numb or tingling sensation in legs?"]

class switch(object):
        def selector(self,i):
            methodname = "case"+str(i)
            method = getattr(self,methodname)
            return method()
            
        def case0(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(0)
                myclass2 = switch()
                set1 = "set0"
                window = tk.Tk()
                label = tk.Label(text=qns[0])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()
                label = tk.Label(text=qns[1])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack()
                label = tk.Label(text=qns[2])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack()
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)
                        
                #myclass2.case1()
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case1(),guicontroller.probcalculator(set1)])
                button0.pack()                
                #parameters.update(BMI = )
                #fp = open(r"C:\Users\mbala\Desktop\result.txt".format(mystring),"a+")
                #fp.write(str(int(answ)))
                #fp.write("\n")
                #fp.close()
            
        def case1(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(1)
                myclass2 = switch()
                set1 = "set1"
                window = tk.Tk()
                label = tk.Label(text=qns[1])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()                
                label = tk.Label(text=qns[4])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack()               
                label = tk.Label(text=qns[3])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack() 
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case2(),guicontroller.probcalculator(set1)])
                button0.pack()                
                #parameters.update(gender = )
                
        def case2(self):#
                #window = tk.Tk()
                #print(qns[i])
                value = int(2)
                myclass2 = switch()
                set1 = "set2"
                window = tk.Tk()
                label = tk.Label(text=qns[6])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()               
                label = tk.Label(text=qns[7])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=100, orient="horizontal")
                w1.pack()               
                label = tk.Label(text=qns[5])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack()
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)                
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case3(), guicontroller.probcalculator(set1)])
                button0.pack()
                #parameters.update(physicalactivity = )
                
        def case3(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(3)
                myclass2 = switch()
                set1 = "set3"
                window = tk.Tk()
                label = tk.Label(text=qns[1])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()                
                label = tk.Label(text=qns[8])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack()                
                label = tk.Label(text=qns[5])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack()
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)                 
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case4(),guicontroller.probcalculator(set1)])
                button0.pack()                
                #parameters.update(race = )
                
        def case4(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(4)
                myclass2 = switch()
                set1 = "set4"
                window = tk.Tk()
                label = tk.Label(text=qns[5])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()              
                label = tk.Label(text=qns[8])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack()                
                label = tk.Label(text=qns[9])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack()
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)                
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case5(),guicontroller.probcalculator(set1)])
                button0.pack()
                #parameters.update(age = )
                
        def case5(self):#
                #window = tk.Tk()
                #print(qns[i])
                value = int(5)
                myclass2 = switch()
                set1 = "set5"
                window = tk.Tk()
                label = tk.Label(text=qns[6])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()              
                label = tk.Label(text=qns[8])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack() 
                label = tk.Label(text=qns[5])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack() 
                def getval(w,w1,w2): 
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)                
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case6(),guicontroller.probcalculator(set1)])
                button0.pack()
                #parameters.update(Bloodpressure = )
                
        def case6(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(6)
                myclass2 = switch()
                set1 = "set6"
                window = tk.Tk()
                label = tk.Label(text=qns[6])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()               
                label = tk.Label(text=qns[8])
                label.pack()
                w1 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w1.pack() 
                label = tk.Label(text=qns[4])
                label.pack()
                w2 = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w2.pack()
                def getval(w,w1,w2):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1)  
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[getval(w.get(),w1.get(),w2.get()),window.destroy(),myclass2.case7(),guicontroller.probcalculator(set1)])
                button0.pack()
                #parameters.update(Familyhistory = )

        def case7(self):
                #window = tk.Tk()
                #print(qns[i])
                value = int(7)
                myclass2 = switch()
                set1 = "set7"
                window = tk.Tk()
                label = tk.Label(text=qns[5])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()                               
                label = tk.Label(text=qns[8])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()               
                label = tk.Label(text=qns[5])
                label.pack()
                w = tk.Scale(window, from_=0, to=10, orient="horizontal")
                w.pack()
                def getval(entry):  
                        print(w/10,w1/10,w2/10)
                        answ = [0,0,0]
                        answ[0] = int((w/10)*100)
                        print(answ[0])
                        answ[1] = int((w1/10)*100)
                        print(answ)
                        answ[2] = int((w2/10)*100)
                        guicontroller.dataentry_newp(answ,set1) 
                button0 = tk.Button(text="->",width=5,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),myclass2.case8(),guicontroller.probcalculator(set1)])
                button0.pack()
                #parameters.update(Familyhistory = )

        def case8(self):                
                guicontroller.finalanswer()
                print(bayes_.bayes(ans,bayesian))                


"""class switch(object):
        def selector(self,i):
            methodname = "case"+str(i)
            method = getattr(self,methodname)
            return method()
            
        def case0(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(0)
            guicontroller.dataentry_newp(value)
            #parameters.update(BMI = )
                
        def case1(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(1)
            guicontroller.dataentry_newp(value)
            #parameters.update(gender = )
                
        def case2(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(2)
            guicontroller.dataentry_newp(value)
            
            #parameters.update(physicalactivity = )
                
        def case3(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(3)
            guicontroller.dataentry_newp(value)
            #parameters.update(race = )
                
        def case4(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(4)
            guicontroller.dataentry_newp(value)
            
            #parameters.update(age = )
                
        def case5(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(5)
            guicontroller.dataentry_newp(value)
            #parameters.update(Bloodpressure = )
                
        def case6(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(6)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )

        def case7(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(7)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )
                
        def case8(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(8)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )

        def case9(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(9)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )

        def case10(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(10)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )

        def case11(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(11)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )
          
        def case12(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(12)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )

        def case13(self):
            #print(qns[i])
            value = int(13)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )
                
        def case14(self):
            #window = tk.Tk()
            #print(qns[i])
            value = int(14)
            guicontroller.dataentry_newp(value)
            #parameters.update(Familyhistory = )
            
        def case15(self):
            guicontroller.finalanswer()
            print(bayes_.bayes(ans,bayesian))"""
"""def questionnaire():
            

    for i in range(14):
        myswitch = switch()
        
  
        #ans[i] = input()
    #button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=window.destroy)
    #button0.pack()         
    print(bayes_.bayes(ans,bayesian))
    #guicontroller.dataentry(qns[i])"""            
