import tkinter as tk
import dataquestionnaireunit


def windowcreator():
    window = tk.Tk()    


def activator():
     
    button = tk.Button(text="GlucoseData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Glucosedata)
    button.pack()

    button1 = tk.Button(text="LipidData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Lipiddata)
    button1.pack()

    button2 = tk.Button(text="BloodPressureData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.BloodPressuredata)
    button2.pack()

    button3 = tk.Button(text="UrineAlbuminData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Urinealbumindata)
    button3.pack()

    button4 = tk.Button(text="GeneralUrineandSedimentData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Generalurineandsedimentdata)
    button4.pack()

    button5 = tk.Button(text="UrineCreatinineData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.UrineCreatininedata)
    button5.pack()

    button6 = tk.Button(text="OpthalmologyData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Opthalmologydata)
    button6.pack()

    button7 = tk.Button(text="PhysicalFootData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Physicalfootdata)
    button7.pack()

    button8 = tk.Button(text="FT4andTSHData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.FT4andTSHdata)
    button8.pack()

    button9 = tk.Button(text="ECGData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.ECGdata)
    button9.pack()

    button10 = tk.Button(text="WeightControlData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Weightcontroldata)
    button10.pack()

    button11 = tk.Button(text="MorphologyData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Morphologydata)
    button11.pack()

    button12 = tk.Button(text="ElectrolytesData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Electrolytesdata)
    button12.pack()

    button13 = tk.Button(text="CarotidUltrasoundData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Carotidultrasounddata)
    button13.pack()

    button14 = tk.Button(text="ANPBNPConcentrationData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.ANPBNPconcentrationdata)
    button14.pack()

    button15 = tk.Button(text="GFRrateData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.GFRratedata)
    button15.pack()

    button16 = tk.Button(text="XrayData",width=25,height=1,bg="grey",fg="black",command=dataquestionnaireunit.Xraydata)
    button16.pack()

    return window

def windowdestroyer(value,qns):
    window = value
    window.destroy()
    datacollectionunit.entrywindow(qns)
    
