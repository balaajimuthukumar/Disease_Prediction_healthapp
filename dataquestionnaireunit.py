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

class Test(object):
    def selector(self,i):
        methodname = str(i)
        method = getattr(self,methodname)
        return method()


    def Glucosedata(self):
        window = tk.Tk()
        qns = ["glucose level before food and on empty stomach?",
               "what is your Postcrandial glucose level?",
               "Since how long when you were diagnosed diabetic?",
               "What is your highest level ever recorded?",
               "What is your Hba1c value?"]

        class switch():
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
        
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            #dataquestionnairebutton.windowdestroyer(qns[i])
            guicontroller.dataentry_oldp(qns[i])
           
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()

        
    """        def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )"""


    def Lipiddata(self):
        window = tk.Tk()
        qns = ["wht is your LDL-C level?",
               "What is your Triglyceride count?",
               "Your Highest ever recorded?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )

            def case2(self,i):
                print(qns[i])
                #parameters.update(gender = )        

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()                         
               
    """        def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )"""

       


    def BloodPressuredata(self):
        window = tk.Tk()
        qns = ["What is your systolic Blood pressure level?",
               "What was your highest systolic ever recorded?",
               "What is your diastolic Blood pressure level?",
               "What was your highest diastolic ever recorded?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )


        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selec
            tor(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
    """    def case4(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(race = )"""


    def Urinealbumindata(self):
        window = tk.Tk()
        qns = ["What is your Normoalbumin urea level?",
               "What is your Microalbumin urea level?",
               "What is your Microalbumin urea level?",
               "What was your Highest Microalbumin urea level?",
               "What was your Highest Macroalbumin urea level?",
               "What was your Highest Normooalbumin urea level?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])        
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
    """     def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )"""


    def Generalurineandsedimentdata(self):
        window = tk.Tk()
        qns = ["No physical activity?","bad food habits?","Normal BMI?",
                 "Controlled sugar intake?","Family history?","smoke?","stress or depression?",
               "anxiety?","age?","Alcohol?","gender?","Race or Ethnicity","BP?","bad sleep routine?",
                 "visual impairment?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()

       
    def UrineCreatininedata(self):
        window = tk.Tk()
        qns = ["What is your GFR level?",
               "what was your highest value ever recorded?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])        
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    """     def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )"""
                



    def Opthalmologydata(self):
        window = tk.Tk()
        qns = ["Is your vision blurred?",
               "Can you see colour contrast?",
               "Do you see black patches in your vision?",
               "Do you have high blood pressure?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
                    
        
    def Physicalfootdata(self):
        window = tk.Tk()
        qns = ["what is your FT4 concentration?",
               "What is your TSH concentration?",
               "What was your Highest FT4?",
               "What was your Highest TSH?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
               
            guicontroller.dataentry_oldp(qns[i])        
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
    """     def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )"""
             



    def FT4andTSHdata(self):
        window = tk.Tk()
        qns = ["what is your FT4 concentration?",
               "What is your TSH concentration?",
               "What was your Highest FT4?",
               "What was your Highest TSH?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])        
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    """     def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )"""



    def ECGdata(self):
        window = tk.Tk()
        qns = ["What is your Sokolev Index?",
               "what is your cornell product?",
               "When was your sokolev index above threshold?",
               "when was your cornell product above threshold?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            guicontroller.dataentry_oldp(qns[i])    
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
    """     def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )"""
                



    def Weightcontroldata(self):
        window = tk.Tk()
        qns = ["what is your Gender?",
               "How old are you?",
               "What is your Height?"
               "What is your Weight?"
               "Were you fat before, If so what was your highest? "]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    """     def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )"""



    def Morphologydata(self):
        window = tk.Tk()
        qns = ["No physical activity?","bad food habits?","Normal BMI?",
                 "Controlled sugar intake?","Family history?","smoke?","stress or depression?",
               "anxiety?","age?","Alcohol?","gender?","Race or Ethnicity","BP?","bad sleep routine?",
                 "visual impairment?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def Electrolytesdata(self):
        window = tk.Tk()
        qns = ["What is your sodium level?",
               "What is your potassium level?",
               "What was your Highest sodium level?",
                "What was your highest potassium level?"
                "What is your calcium level?",
                "What was your highest calcium level?"
                "What is your phosphate level?",
                "What was your highest phosphate level?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case7(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])        
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def Carotidultrasounddata(self):
        window = tk.Tk()
        qns = ["what is your Intimia Media Thickness?",
               "What was your Highest Thickness?","Normal BMI?",
                 "Controlled sugar intake?","Family history?","smoke?","stress or depression?",
               "anxiety?","age?","Alcohol?","gender?","Race or Ethnicity","BP?","bad sleep routine?",
                 "visual impairment?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def ANPBNPconcentrationdata(self):
        window = tk.Tk()
        qns = ["what is your ANP concentration?",
               "What was your Highest ANP concentration?",
               "what is your BNP concentration?",
               "What was your Highest BNP concentration?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            

            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def GFRratedata(self):
        window = tk.Tk()
        qns = ["what is your GFR rate?",
               "What was your Highest GFR rate?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
                        
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def Xraydata(self):
        window = tk.Tk()
        qns = ["what is your GFR rate?",
               "What was your Highest GFR rate?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])
        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            
            guicontroller.dataentry_oldp(qns[i])
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=lambda:[window.destroy(),guicontroller.dataupdate_oldp("0")])
        button0.pack()
        
    def Liverenzymesdata(self):

        qns = ["what is your GFR rate?",
               "What was your Highest GFR rate?"]

        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])

        for i in range(len(qns)):
            myswitch = switch()
            myswitch.selector(i)
            



if __name__ == "__main__":
    print("start making changes")
    Glucosedata()




"""    def questionnaire(self):
        window = tk.Tk()
        
        qns = ["No physical activity?","bad food habits?","Normal BMI?",
             "Controlled sugar intake?","Family history?","smoke?","stress or depression?",
           "anxiety?","age?","Alcohol?","gender?","Race or Ethnicity","BP?","bad sleep routine?",
             "visual impairment?"]
        bayesian  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        class switch(object):
            def selector(self,i):
                methodname = "case"+str(i)
                method = getattr(self,methodname)
                return method(i)
            
            def case0(self,i):
                print(qns[i])
                #parameters.update(BMI = )
                
            def case1(self,i):
                print(qns[i])
                #parameters.update(gender = )
                
            def case2(self,i):
                print(qns[i])
                #parameters.update(physicalactivity = )
                
            def case3(self,i):
                print(qns[i])
                #parameters.update(race = )
                
            def case4(self,i):
                print(qns[i])
                #parameters.update(age = )
                
            def case5(self,i):
                print(qns[i])
                #parameters.update(Bloodpressure = )
                
            def case6(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case7(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case8(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case9(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case10(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case11(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
          
            def case12(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )

            def case13(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def case14(self,i):
                print(qns[i])
                #parameters.update(Familyhistory = )
                
            def dataprint(value):
                window.destroy()
                
            def wincreate():
                window = tk.Tk()
        for i in range(14):
            myswitch = switch()
            myswitch.selector(i)
            guicontroller.dataentry_oldp_newp(qns[i])
            myswitch.wincreate()
            #ans[i] = input()
        button0 = tk.Button(text="Submit",width=25,height=1,bg="grey",fg="black",command=window.destroy)
        button0.pack()         
        print(bayes_.bayes(ans,bayesian))
        #guicontroller.dataentry_oldp(qns[i])

"""
