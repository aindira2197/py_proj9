balance = 500

while True:
    print("1. Balans")
    print("2. Pul yechish")
    print("3. Pul qo'shish")
    print("4. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        print("Balans:", balance)

    elif choice == "2":
        amount = int(input("Miqdor: "))

        if amount <= balance:
            balance -= amount
            print("Pul yechildi")
        else:
            print("Yetarli mablag' yo'q")

    elif choice == "3":
        amount = int(input("Qo'shiladigan pul: "))
        balance += amount
        print("Balans yangilandi")

    elif choice == "4":
        print("Dastur tugadi")
        break

    else:
        print("Noto'g'ri tanlov")
