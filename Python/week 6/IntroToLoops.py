prompt = input("Do you want to print the list? Y/N ")
geniuses = ["jayden", "Dayyon", "jahlil", "caden", "Timonte", "dj", "malik"]

while (prompt == "Y"):
    for genius in geniuses:
        print(genius)
    prompt = input("Do you want to print the list again? Y/N ")