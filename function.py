
def Vinni_Pux(list1):
    list1 = list1.split()
    list_2 = []
    for word in list1:
        summ = 0
        for i in word:
            if i in "ауоыиэяюёе":
                summ += 1
        list_2.append(summ)
    if len(set(list_2)) == 1:
        print("Парам пам-пам")
    else: 
        print("Пам парам")


    # return len(list_2) == list_2.count(list_2[0])
    


    

