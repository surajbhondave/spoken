#!/usr/bin/env python
# coding: utf-8

# In[24]:


def getr():
    rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       }
            }
    return rules
def check_f_l(w):
    f=""
    l=""
    if(len(w)>1):
        if w[-1]==',' or w[-1]=='.':
            l=w[-1]
            w=w[:-1]
        if w[0]==',' or w[0]=='.':
            f=w[0]
            w=w[1:]
    return f,w,l
class Spoken_to_Written:
    def __init__(self):

        self.rules=get_rules()
        self.paragraph=""
        self.ouptut_para=""
    def get_user_input(self):
        self.paragraph=input("\n[IN]:Enter Your paragraph of spoken english:\n\t")
        if not self.paragraph:
            raise ValueError("[Error]: You entered nothing.")
    def show_output(self):
        print("\n[OUT]:The input Spoken English Paragraph: \n\n \" "+ self.paragraph+"\"")
        print("\nConverted Written English Paragraph: \n\n \"" +self.ouptut_para+"\"")
    def Convert(self):
        words_of_para=self.paragraph.split()
        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words_of_para)
        while i<no_of_words: 
            
            front,word,last=check_f_l(words_of_para[i]) 
            if i+1!= no_of_words: 
                front_n,next_word,last_n=check_f_l(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.ouptut_para=self.ouptut_para+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
                    self.ouptut_para=self.ouptut_para+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
                    self.ouptut_para=self.ouptut_para+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                i=i+1
def convert_sp_to_wr():
    obj_spoken=Spoken_To_Written()
    obj_spoken.getr()
    obj_spoken.Convert()
    obj_spoken.show_output()


# In[ ]:




