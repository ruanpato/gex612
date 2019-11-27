import MainMemory
import os # Just to clear console

mainMemory = MainMemory.MainMemory(4, 128, 8)

# Menu
while(True):
    option = int(input("1. Read a memory address.\n2. Write on memory.\n3. Show statistics.\n4. Show all Main Memory.\n5. Show all Cache Memory.\n0. Exit\n"))
    if option ==  1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        mainMemory.printAllCells()
    elif option == 5:
        pass
    elif option == 0:
        exit()
    else:
        os.system('clear' if os.name =='posix' else 'cls')
        print("Inválid Option")