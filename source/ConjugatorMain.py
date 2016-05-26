'''
Portuguese Conjugator 1.0
By Alvin Williams
'''
#List of Irregular modules to import for special case conjugation.

from caber import *
from crer import *
from dar import *
from estar import *
from fazer import *
from haver import *
from ir import *
from ler import *
from medir import *
from ouvir import *
from perder import *
from poder import *
from pôr import *
from querer import *
from remir import *
from rir import *
from saber import *
from ser import *
from ter import *
from trazer import *
from valer import *
from ver import *
from vir import *


IrrDic = {"ter":ter(),"estar":estar(),"ser":ser(),"ir":ir(),\
              "querer":querer(),"fazer":fazer(), "dar":dar(),"saber":saber(),\
              "caber":caber(),"crer":crer(), "haver":haver(),"ler":ler(),"perder":perder(),\
              "poder":poder(),"trazer":trazer(),"valer":valer(),"ver":ver(),"pôr":pôr(),\
               "medir":medir(),"ouvir":ouvir(),"remir":remir(),\
               "rir":rir(),"vir":()}

class Conjugator():
    print("Welcome to the Portuguese Conjugator ver 1.0\n")
    print("Please make the python shell fullscreen to display\nthis program correctly.")
    def __init__(self, userinput):
        self.userinput = userinput
        self.er = False
        self.ar = False
        self.ir = False
        self.irregular = False
        print("\n\n"+"{:^70}".format(userinput.upper()))
        if userinput in IrrDic:
            f = open(userinput+".py", 'r')
            word_instance = IrrDic.get(userinput)
            word_instance.conjugator(userinput)
            w = input("\nWould you like to conjugate another word? \nPress any key to continue or type quit or n to end the program. ")
            if w.lower() == "quit" or w.lower() == "n":
                print("\nQuitting the program\n")
                print("Thank you for using this conjugator made by Alvin.\n")
            else:
                i = input("\nPlease type in the next word. ")
                a = Conjugator(i)
            
        elif userinput[-2:] == "er":
            self.er = True
            self.conjugator_er(userinput)
        elif userinput[-2:] == "ar":
            self.ar = True
            self.conjugator_ar(userinput)
        elif userinput[-2:] == "ir":
            self.ir = True
            self.conjugator_ir(userinput)
        else:
            raise Exception("Please enter in a verb ending er, ir, or ar.")
        
    def conjugator_er(self, userinput):
        k = userinput[:-2]
        print("------------------------------Indicativo--------------------------------------------------------------")
        print("Form            Presente                         Passado Perfeito              Passado Imperfeito")
        print("------------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "o" + "{:^29}".format(" ") +k + "i" + "{:^25}".format(" ") + k + "ia") 
        print("Tu" +"{:^14}".format(" ") + k + "es" + "{:^28}".format(" ") + k + "este" + "{:^22}".format(" ") + k + "ias")  
        print("Ele/Ela/Você" +"{:^4}".format(" ")+ k + "e" + "{:^29}".format(" ") + k + "eu" + "{:^24}".format(" ") + k + "ia")
        print("Nós" +"{:^13}".format(" ") + k + "emos" + "{:^26}".format(" ") + k + "emos" + "{:^22}".format(" ") + k + "íamos")
        print("Vós" +"{:^13}".format(" ") + k + "eis" + "{:^27}".format(" ") + k + "estes" + "{:^21}".format(" ") + k + "íeis")
        print("Eles/Elas/Vocês"+" " + k + "em" + "{:^28}".format(" ") + k + "eram" + "{:^22}".format(" ") + k + "iam")
        print("-----------------------------------------------------------------------------------------------------")
        print("Form            Pret. Mais-que-Perfeito          Futuro                        Condicional")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "era" +"{:^26}".format(" ") + k + "erei" +"{:^22}".format(" ") + k + "eria") 
        print("Tu" +"{:^14}".format(" ") + k + "eras" +"{:^25}".format(" ") + k + "erás" +"{:^22}".format(" ") + k + "erias")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "era" +"{:^26}".format(" ") + k + "erá" +"{:^23}".format(" ") + k + "eria")
        print("Nós" +"{:^13}".format(" ") + k + "êramos" +"{:^23}".format(" ") + k + "eremos" +"{:^20}".format(" ") + k + "eríamos")
        print("Vós" +"{:^13}".format(" ") + k + "êreis" +"{:^24}".format(" ") + k + "ereis" +"{:^21}".format(" ") + k + "eríeis")
        print("Eles/Elas/Vocês"+" " + k + "eram" +"{:^25}".format(" ") + k + "erão" + "{:^22}".format(" ") + k + "eriam")
        print("                                                                            ")
        print("------------------------------Subjuntivo-------------------------------------------------------------")
        print("Form            Presente                         Preterito Imperfeito          Futuro")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "o" +"{:^28}".format(" ") + k + "esse" +"{:^22}".format(" ") +k + "er") 
        print("Tu" +"{:^14}".format(" ") + k + "es" +"{:^27}".format(" ") + k + "esses" +"{:^21}".format(" ") + k + "eres")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "e" +"{:^28}".format(" ") + k + "esse" +"{:^22}".format(" ") + k + "er")
        print("Nós" +"{:^13}".format(" ") + k + "emos" +"{:^25}".format(" ") + k + "êssemos" +"{:^19}".format(" ") + k + "ermos")
        print("Vós" +"{:^13}".format(" ") + k + "eis" +"{:^26}".format(" ") + k + "êsseis" +"{:^20}".format(" ") + k + "erdes")
        print("Eles/Elas/Vocês"+" " + k + "am" +"{:^27}".format(" ") + k + "essem" +"{:^21}".format(" ") + k + "erem")
        print("                                                                            ")
        print("------------------------------Imperativo-------------------------------------------------------------")
        print("Form            Afirmativo                       Negativo                     Infinitivo Pessoal")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") +"N/A"+"{:^30}".format(" ") + "N/A" +"{:^25}".format(" ") +  " para " + k + "er eu") 
        print("Tu" +"{:^14}".format(" ") + k + "e " + "tu" +"{:^25}".format(" ") + "não " + k + "as tu" +"{:^15}".format(" ") + " para " + k + "eres tu")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "a "  + "ele/ela/você" +"{:^15}".format(" ") + "não " + k + "a ele/ela/você" +"{:^7}".format(" ") + "para " + k + "er ele/ela/você")
        print("Nós" +"{:^13}".format(" ") + k + "amos " + "nós" +"{:^21}".format(" ") + "não " + k + "amos nós" +"{:^12}".format(" ") + " para " +  k + "ermos nós")
        print("Vós" +"{:^13}".format(" ") + k + "ei " + "vós" +"{:^23}".format(" ") + "não " + k + "ais vós" +"{:^13}".format(" ") + " para " +  k + "erdes vós")
        print("Eles/Elas/Vocês"+" " + k + "am " + "eles/elas/vocês" +"{:^11}".format(" ") + "não " + k + "am vocês" +"{:^12}".format(" ") + " para " +  k + "erem vocês")
        
        w = input("\nWould you like to conjugate another word? \nPress any key to continue or type quit to end the program. ")
        if w.lower() == "quit":
            print("\nQuitting the program\n")
            print("Thank you for using this conjugator made by Alvin.\n")
        else:
            i = input("\nPlease type in the next word. ")
            a = Conjugator(i)
            
    def conjugator_ar(self, userinput):
        k = userinput[:-2]
        print("------------------------------Indicativo--------------------------------------------------------------")
        print("Form            Presente                         Passado Perfeito              Passado Imperfeito")
        print("------------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "o" + "{:^28}".format(" ") +k + "ei" + "{:^25}".format(" ") + k + "ava") 
        print("Tu" +"{:^14}".format(" ") + k + "as" + "{:^27}".format(" ") + k + "aste" + "{:^22}".format(" ") + k + "avas")  
        print("Ele/Ela/Você" +"{:^4}".format(" ")+ k + "a" + "{:^28}".format(" ") + k + "ou" + "{:^24}".format(" ") + k + "ava")
        print("Nós" +"{:^13}".format(" ") + k + "amos" + "{:^25}".format(" ") + k + "amos" + "{:^22}".format(" ") + k[:-1] + "ávamos")
        print("Vós" +"{:^13}".format(" ") + k + "ais" + "{:^29}".format(" ") + k + "astes" + "{:^21}".format(" ") + k[:-1] + "áveis")
        print("Eles/Elas/Vocês"+" " + k + "am" + "{:^27}".format(" ") + k + "aram" + "{:^22}".format(" ") + k + "avam")
        print("-----------------------------------------------------------------------------------------------------")
        print("Form            Pret. Mais-que-Perfeito          Futuro                        Condicional")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "ara" +"{:^26}".format(" ") + k + "arei" +"{:^22}".format(" ") + k + "aria") 
        print("Tu" +"{:^14}".format(" ") + k + "aras" +"{:^25}".format(" ") + k + "arás" +"{:^22}".format(" ") + k + "arias")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "ara" +"{:^26}".format(" ") + k + "ará" +"{:^25}".format(" ") + k + "aria")
        print("Nós" +"{:^13}".format(" ") + k + "áramos" +"{:^23}".format(" ") + k + "aremos" +"{:^20}".format(" ") + k + "aríamos")
        print("Vós" +"{:^13}".format(" ") + k + "áreis" +"{:^24}".format(" ") + k + "areis" +"{:^21}".format(" ") + k + "aríeis")
        print("Eles/Elas/Vocês"+" " + k + "aram" +"{:^25}".format(" ") + k + "arão" + "{:^22}".format(" ") + k + "ariam")
        print("                                                                            ")
        print("------------------------------Subjuntivo-------------------------------------------------------------")
        print("Form            Presente                         Preterito Imperfeito          Futuro")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "e" +"{:^28}".format(" ") + k + "asse" +"{:^25}".format(" ") +k + "ar") 
        print("Tu" +"{:^14}".format(" ") + k + "es" +"{:^27}".format(" ") + k + "asses" +"{:^22}".format(" ") + k + "ares")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "e" +"{:^28}".format(" ") + k + "asse" +"{:^24}".format(" ") + k + "ar")
        print("Nós" +"{:^13}".format(" ") + k + "emos" +"{:^25}".format(" ") + k + "ássemos" +"{:^20}".format(" ") + k + "armos")
        print("Vós" +"{:^13}".format(" ") + k + "eis" +"{:^26}".format(" ") + k + "ásseis" +"{:^21}".format(" ") + k + "ardes")
        print("Eles/Elas/Vocês"+" " + k + "em" +"{:^27}".format(" ") + k + "assem" +"{:^22}".format(" ") + k + "arem")
        print("                                                                            ")
        print("------------------------------Imperativo-------------------------------------------------------------")
        print("Form            Afirmativo                       Negativo                     Infinitivo Pessoal")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") +"N/A"+"{:^30}".format(" ") + "N/A" +"{:^25}".format(" ") +  " para " + k + "ar eu") 
        print("Tu" +"{:^14}".format(" ") + k + "a " + "tu" +"{:^25}".format(" ") + "não " + k + "es tu" +"{:^15}".format(" ") + " para " + k + "ares tu")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "e "  + "ele/ela/você" +"{:^15}".format(" ") + "não " + k + "e ele/ela/você" +"{:^7}".format(" ") + "para " + k + "ar ele/ela/você")
        print("Nós" +"{:^13}".format(" ") + k + "emos " + "nós" +"{:^21}".format(" ") + "não " + k + "emos nós" +"{:^12}".format(" ") + " para " +  k + "armos nós")
        print("Vós" +"{:^13}".format(" ") + k + "ai " + "vós" +"{:^23}".format(" ") + "não " + k + "eis vós" +"{:^13}".format(" ") + " para " +  k + "ardes vós")
        print("Eles/Elas/Vocês"+" " + k + "em " + "eles/elas/vocês" +"{:^11}".format(" ") + "não " + k + "em vocês" +"{:^12}".format(" ") + " para " +  k + "arem vocês")        

        w = input("\nWould you like to conjugate another word? \nPress any key to continue or type quit to end the program. ")
        if w.lower() == "quit":
            print("\nQuitting the program\n")
            print("Thank you for using this conjugator made by Alvin.\n")
        else:
            i = input("\nPlease type in the next word. ")
            a = Conjugator(i)
       
    def conjugator_ir(self, userinput):
        k = userinput[:-2]
        print("------------------------------Indicativo--------------------------------------------------------------")
        print("Form            Presente                         Passado Perfeito              Passado Imperfeito")
        print("------------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "o" + "{:^29}".format(" ") +k + "i" + "{:^26}".format(" ") + k + "ia") 
        print("Tu" +"{:^14}".format(" ") + k + "es" + "{:^28}".format(" ") + k + "iste" + "{:^23}".format(" ") + k + "ias")  
        print("Ele/Ela/Você" +"{:^4}".format(" ")+ k + "e" + "{:^29}".format(" ") + k + "iu" + "{:^25}".format(" ") + k + "ia")
        print("Nós" +"{:^13}".format(" ") + k + "imos" + "{:^26}".format(" ") + k + "imos" + "{:^23}".format(" ") + k + "íamos")
        print("Vós" +"{:^13}".format(" ") + k + "is" + "{:^28}".format(" ") + k + "istes" + "{:^22}".format(" ") + k + "íeis")
        print("Eles/Elas/Vocês"+" " + k + "em" + "{:^28}".format(" ") + k + "iram" + "{:^23}".format(" ") + k + "iam")
        print("-----------------------------------------------------------------------------------------------------")
        print("Form            Pret. Mais-que-Perfeito          Futuro                        Condicional")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "ira" +"{:^27}".format(" ") + k + "irei" +"{:^23}".format(" ") + k + "iria") 
        print("Tu" +"{:^14}".format(" ") + k + "iras" +"{:^26}".format(" ") + k + "irás" +"{:^23}".format(" ") + k + "irias")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "ira" +"{:^27}".format(" ") + k + "irá" +"{:^24}".format(" ") + k + "eria")
        print("Nós" +"{:^13}".format(" ") + k + "íramos" +"{:^24}".format(" ") + k + "iremos" +"{:^21}".format(" ") + k + "eríamos")
        print("Vós" +"{:^13}".format(" ") + k + "íreis" +"{:^25}".format(" ") + k + "ireis" +"{:^22}".format(" ") + k + "eríeis")
        print("Eles/Elas/Vocês"+" " + k + "iram" +"{:^26}".format(" ") + k + "irão" + "{:^23}".format(" ") + k + "eriam")
        print("                                                                            ")
        print("------------------------------Subjuntivo-------------------------------------------------------------")
        print("Form            Presente                         Preterito Imperfeito          Futuro")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") + k + "a" +"{:^29}".format(" ") + k + "isse" +"{:^23}".format(" ") +k + "ir") 
        print("Tu" +"{:^14}".format(" ") + k + "as" +"{:^28}".format(" ") + k + "isses" +"{:^22}".format(" ") + k + "ires")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "a" +"{:^29}".format(" ") + k + "isse" +"{:^23}".format(" ") + k + "ir")
        print("Nós" +"{:^13}".format(" ") + k + "amos" +"{:^26}".format(" ") + k + "íssemos" +"{:^20}".format(" ") + k + "irmos")
        print("Vós" +"{:^13}".format(" ") + k + "ais" +"{:^27}".format(" ") + k + "ísseis" +"{:^21}".format(" ") + k + "irdes")
        print("Eles/Elas/Vocês"+" " + k + "am" +"{:^28}".format(" ") + k + "issem" +"{:^22}".format(" ") + k + "irem")
        print("                                                                            ")
        print("------------------------------Imperativo-------------------------------------------------------------")
        print("Form            Afirmativo                       Negativo                     Infinitivo Pessoal")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:^14}".format(" ") +"N/A"+"{:^30}".format(" ") + "N/A" +"{:^25}".format(" ") +  " para " + k + "ir eu") 
        print("Tu" +"{:^14}".format(" ") + k + "e " + "tu" +"{:^26}".format(" ") + "não " + k + "as tu" +"{:^16}".format(" ") + " para " + k + "ires tu")  
        print("Ele/Ela/Você" +"{:^4}".format(" ") + k + "a "  + "ele/ela/você" +"{:^16}".format(" ") + "não " + k + "a ele/ela/você" +"{:^8}".format(" ") + "para " + k + "ir ele/ela/você")
        print("Nós" +"{:^13}".format(" ") + k + "amos " + "nós" +"{:^22}".format(" ") + "não " + k + "amos nós" +"{:^13}".format(" ") + " para " +  k + "irmos nós")
        print("Vós" +"{:^13}".format(" ") + k + "i " + "vós" +"{:^25}".format(" ") + "não " + k + "ais vós" +"{:^14}".format(" ") + " para " +  k + "irdes vós")
        print("Eles/Elas/Vocês"+" " + k + "am " + "eles/elas/vocês" +"{:^12}".format(" ") + "não " + k + "am vocês" +"{:^13}".format(" ") + " para " +  k + "irem vocês")
        
        w = input("\nWould you like to conjugate another word? \nPress any key to continue or type quit to end the program. ")
        if w.lower() == "quit":
            print("\nQuitting the program\n")
            print("Thank you for using this conjugator made by Alvin.\n")
        else:
            i = input("\nPlease type in the next word. ")
            a = Conjugator(i)
fazer = Conjugator("fazer")
