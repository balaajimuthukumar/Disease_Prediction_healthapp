import tkinter as tk

#These are the questions asked for the patient and are common for both - 
#hypertension and diabetes
ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]# this array contains the answers for the question
#factors = [0,0,0,0,0,0,0,0,0,0,0]
conditionalprob = [0,0,0,0,0,0,0,0]#this is the hypothesis probabbility for each parameter
#Past values for bayes theorem and the values are assumed for demo purpose---
chol_past = 0.22
glu_past = 0.22
BP_past = 0.22
creat_alb_past = 0.22
vision_past = 0.22
ft4_tsh_past = 0.22
carotid_past = 0.22
BMI_past = 0.22
#Marginal proabability for bayes conditional and the values inisde the array were manually entered--
Marginal = 0.12
chol_mar = 0.12
glu_mar = 0.12
BP_mar = 0.12
creat_alb_mar = 0.12
vision_mar = 0.12
ft4_tsh_mar = 0.12
carotid_mar = 0.12
BMI_mar = 0.12
#Marginal probability for conditional probability----these values are assumed to be observational data and manually entered--
chol_mar = 0.12
glu_mar = 0.12
BP_mar = 0.12
creat_alb_mar = 0.12
vision_mar = 0.12
ft4_tsh_mar = 0.12
carotid_mar = 0.12
BMI_mar = 0.12
#----------------------Program starts form here---------------------------
x1toy1 = 0.11
x1toy2 = 0.01
x2toy1 = 0.01
x2toy2 = 0.11

cond_prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bayesian  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#probability calculator for patient body parameters(truth table section) like cholesterol-- this is final setup--- 
def conditional_probability(answ1):
    paraval = 0.2 # this is the parameter value(eg: cholesterol)
    for i in range(len(answ1)):
        ((paraval*answ1[i])/ans[i])*paraval




"""def conditional_probability():
    for i in range(14):
        if ans[i-1] == 0:
            cond_prob[3-i] = x1toy1 /(x1toy1+x1toy2)
            
        if ans[i-1] == 1:
            cond_prob[3-i] = x2toy1 /(x1toy1+x1toy2)"""
 
"""def bayes(answ1,bayesian):
    ans = answ1
    ans1 = ans
    bays = bayesian
    if ans1 <= 30:                                        
        bays = ((x1toy1/(x1toy1+x1toy2))*0.22) / (((x2toy1/(x1toy1+x2toy1))*0.10)
        +((x1toy1/(x1toy1+x2toy1))*0.20) + ((x1toy2/(x1toy1+x2toy1))*0.09)
        + ((x1toy1/(x1toy1+x2toy1))*0.22) + ((x1toy2/(x1toy1+x2toy1))*0.08) + ((x1toy1/(x1toy1+x2toy1))*0.11))
           
    if ans > 30:
        bays = (x2toy1/((x2toy1+x2toy2)*0.10)) / ((x2toy1/((x1toy1+x2toy1)*0.10))
        +(x2toy2/((x1toy1+x2toy1)*0.20)) +(x2toy1/((x2toy1+x1toy1)*0.09))
        + (x2toy2/((x1toy1+x2toy2)*0.22)) + (x2toy1/((x1toy1+x2toy1)*0.08)) + (x2toy2/((x2toy1+x2toy2)*0.11)))

    return bays"""

"""def bayes(answ1,bayesian):
    ans = answ1
    bays = bayesian
    paraval = 0.5 # this is the parameter value for rising(eg: cholesterol)
    paraval1 = 0.2 # this is the parameter value for not rising(eg: cholesterol)
    
    for i in range(0,len(ans)):
        print(ans[i])
        bays[i] = ((paraval*answ1[i])/ans[i])*paraval1) / (((paraval*answ1[0])/ans[0])*paraval1)
        +(((paraval*(1-answ1[0]))/(1-ans[0]))*paraval1)  + ((paraval*answ1[1])/ans[1])*paraval1)
        + ((paraval*(1-answ1[1]))/(1-ans[1]))*paraval1) + ((paraval*answ1[2])/ans[2])*paraval1) + ((paraval*(1-answ1[2]))/(1-ans[2]))*paraval))
        print(bays[i])
        
            
    return bays"""



"""def bayes(answ1,bayesian):
    ans = answ1
    bays = bayesian
    for i in range(0,len(ans)):
        if ans[i] <= 30:
            print(ans[i])
            bays[i] = ((x1toy1/(x1toy1+x1toy2))*0.22) / (((x2toy1/(x1toy1+x2toy1))*0.10)
            +((x1toy1/(x1toy1+x2toy1))*0.20) + ((x1toy2/(x1toy1+x2toy1))*0.09)
            + ((x1toy1/(x1toy1+x2toy1))*0.22) + ((x1toy2/(x1toy1+x2toy1))*0.08) + ((x1toy1/(x1toy1+x2toy1))*0.11))
            print(bays[i])
            
           
        if ans[i] > 30:
            print(ans[i])
            bays[i] = (x2toy1/((x2toy1+x2toy2)*0.10)) / ((x2toy1/((x1toy1+x2toy1)*0.10))
            +(x2toy2/((x1toy1+x2toy1)*0.20)) +(x2toy1/((x2toy1+x1toy1)*0.09))
            + (x2toy2/((x1toy1+x2toy2)*0.22)) + (x2toy1/((x1toy1+x2toy1)*0.08)) + (x2toy2/((x2toy1+x2toy2)*0.11)))
            print(bays[i])
    return bays"""     
