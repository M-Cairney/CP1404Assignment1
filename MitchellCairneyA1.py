"""
CP1404 Assignment 1 - 2016
Shopping List 1.0
Mitchell Cairney - 128437334
Due date: 9/9/2016

Pseudocode:

Function main()

    COMPLETED_ITEMS = []
    REQUIRED_ITEMS = []
    MENU = the menu

    display welcome message

    for lines in fileName
        if line[-1] == 'r'
            add the line to REQUIRED_ITEMS
        if line[-1] == 'c'
            add the line to COMPLETED_ITEMS
    close file

    display number of lines in the file

    display MENU
    get userMenuInput

    while userMenuInput.lower != 'q'

        if userMenuInput.lower = 'r'

            for item in Required_Items
                display item with a number, a priority and their price
                add the price to a total
            display total expected price

            display MENU
            get userMenuInput

        elif userMenuInput.lower = 'm'
            count = 0

            for item in Required_Items
                display item with a number, a priority and their price
                add the price to a total
                add count by 1
            display total expected price
            display asking the user for a number to mark

            try get itemToMark
            except value error
                display invalid input enter a number
                get itemToMark
            except itemToMark >= count or -0
                display invalid item number
                get itemToMark

            get itemToMark
            append COMPLETED_ITEMS with Required_Items[itemToMark]
            remove Reuired_Items[itemToMark]

            display MENU
            get userMenuInput

        elif userMenuInput.lower = 'c'

            if COMPLETED_ITEMS is empty
                display no completed items
            else
                for item in COMPLETED_ITEMS
                    display item with a number, a priority and there price
                    add the price to a total
                display total expected price
            display MENU
            get userMenuInput

        elif userMenuInput.lower = 'a'

            get newItemName
            while newItemName is empty
                display input can not be blank
                get newItemName

            try get newPrice
            except value error
                display invalid input; enter a valid number
                get newPrice
            except newPrice is less then 0
                display price needs to be 0 or more
                get newPrice

            try get newPriority
            except value error
                display invalid input; enter a valid number
                get newPriority
            except newPriority is less then 0 and greater the 3
                display priority must be 1, 2 or 3
                get newPriority

            display the item name price and priority and added to shopping list
            append Required_Items with the new item

    count = 0
    for item in REQUIRED_LIST
        write item to items.csv
        count +1
    for item in COMPLETED_LIST
        write item to items.csv
        count +1
    display number of items saved
    display goodbye message

main()
"""

