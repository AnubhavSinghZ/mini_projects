books=[]

while True:
    print("\n1. Add 2. View 3. Issue 4. Retrun 5. Exit")
    choice =input("Choose:")

    if choice=="1":
        title=input("Title:")
        author=input("Author:")
        books.append([title,author,True])
        print("Book Added!")

    elif choice=="2":
        if len(books)==0:
            