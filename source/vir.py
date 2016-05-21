def conjugator(self, userinput):
        k = userinput[:-2]
        print("------------------------------Indicativo--------------------------------------------------------------")
        print("Form            Presente                         Passado Perfeito              Passado Imperfeito")
        print("------------------------------------------------------------------------------------------------------")
        print("Yo" +"{:<14}".format(" ") + k + "enho" + "{:<28}".format(" ") +k + "ive" + "{:<25}".format(" ") + k + "inha") 
        print("Tu" +"{:<14}".format(" ") + k + "ens" + "{:<27}".format(" ") + k + "iveste" + "{:<22}".format(" ") + k + "inhas")  
        print("Ele/Ela/Você" +"{:<4}".format(" ")+ k + "em" + "{:<28}".format(" ") + k + "eve" + "{:<24}".format(" ") + k + "inha")
        print("Nós" +"{:<13}".format(" ") + k + "emos" + "{:<25}".format(" ") + k + "ivemos" + "{:<22}".format(" ") + k + "ínhamos")
        print("Vós" +"{:<13}".format(" ") + k + "endes" + "{:<26}".format(" ") + k + "ivestes" + "{:<21}".format(" ") + k + "ínheis")
        print("Eles/Elas/Vocês"+" " + k + "êm" + "{:<27}".format(" ") + k + "iveram" + "{:<22}".format(" ") + k + "enham")
        print("-----------------------------------------------------------------------------------------------------")
        print("Form            Pret. Mais-que-Perfeito          Futuro                        Condicional")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:<14}".format(" ") + k + "ivera" +"{:<26}".format(" ") + k + "erei" +"{:<22}".format(" ") + k + "eria") 
        print("Tu" +"{:<14}".format(" ") + k + "iveras" +"{:<25}".format(" ") + k + "erás" +"{:<22}".format(" ") + k + "erias")  
        print("Ele/Ela/Você" +"{:<4}".format(" ") + k + "ivera" +"{:<26}".format(" ") + k + "erá" +"{:<23}".format(" ") + k + "eria")
        print("Nós" +"{:<13}".format(" ") + k + "ivéramos" +"{:<23}".format(" ") + k + "eremos" +"{:<20}".format(" ") + k + "eríamos")
        print("Vós" +"{:<13}".format(" ") + k + "ivéreis" +"{:<24}".format(" ") + k + "ereis" +"{:<21}".format(" ") + k + "eríeis")
        print("Eles/Elas/Vocês"+" " + k + "ivéram" +"{:<25}".format(" ") + k + "erão" + "{:<22}".format(" ") + k + "eriam")
        print("                                                                            ")
        print("------------------------------Subjuntivo-------------------------------------------------------------")
        print("Form            Presente                         Preterito Imperfeito          Futuro")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:<14}".format(" ") + k + "enha" +"{:<28}".format(" ") + k + "ivesse" +"{:<22}".format(" ") +k + "iver") 
        print("Tu" +"{:<14}".format(" ") + k + "enhas" +"{:<27}".format(" ") + k + "ivesses" +"{:<21}".format(" ") + k + "iveres")  
        print("Ele/Ela/Você" +"{:<4}".format(" ") + k + "enha" +"{:<28}".format(" ") + k + "ivesse" +"{:<22}".format(" ") + k + "iver")
        print("Nós" +"{:<13}".format(" ") + k + "enhamos" +"{:<25}".format(" ") + k + "ivéssemos" +"{:<19}".format(" ") + k + "ivermos")
        print("Vós" +"{:<13}".format(" ") + k + "enhais" +"{:<26}".format(" ") + k + "ivésseis" +"{:<20}".format(" ") + k + "iverdes")
        print("Eles/Elas/Vocês"+" " + k + "enham" +"{:<27}".format(" ") + k + "ivessem" +"{:<21}".format(" ") + k + "iverem")
        print("                                                                            ")
        print("------------------------------Imperativo-------------------------------------------------------------")
        print("Form            Afirmativo                       Negativo                     Infinitivo Pessoal")
        print("-----------------------------------------------------------------------------------------------------")
        print("Yo" +"{:<14}".format(" ") +"N/A"+"{:<30}".format(" ") + "N/A" +"{:<25}".format(" ") +  " para " + k + "er eu") 
        print("Tu" +"{:<14}".format(" ") + k + "em " + "tu" +"{:<25}".format(" ") + "não " + k + "enhas tu" +"{:<15}".format(" ") + " para " + k + "eres tu")  
        print("Ele/Ela/Você" +"{:<4}".format(" ") + k + "enha "  + "ele/ela/você" +"{:<15}".format(" ") + "não " + k + "enha ele/ela/você" +"{:<7}".format(" ") + "para " + k + "er ele/ela/você")
        print("Nós" +"{:<13}".format(" ") + k + "enhamos " + "nós" +"{:<21}".format(" ") + "não " + k + "enhmos nós" +"{:<12}".format(" ") + " para " +  k + "ermos nós")
        print("Vós" +"{:<13}".format(" ") + k + "ende " + "vós" +"{:<23}".format(" ") + "não " + k + "enhais vós" +"{:<13}".format(" ") + " para " +  k + "erdes vós")
        print("Eles/Elas/Vocês"+" " + k + "enham " + "eles/elas/vocês" +"{:<11}".format(" ") + "não " + k + "enham vocês" +"{:<12}".format(" ") + " para " +  k + "erem vocês")
        
        w = input("\nWould you like to conjugate another word? \nPress any key to continue or type quit to end the program. ")
        if w.lower() == "quit":
            print("\nQuitting the program\n")
            print("Thank you for using this conjugator made by Alvin.\n")
        else:
            i = input("\nPlease type in the next word. ")
            a = Conjugator(i)

