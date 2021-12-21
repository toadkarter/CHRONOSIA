        display(screen62)
        display(screen63)

        """
        PUZZLES FOR THE FIRST PATH
        """

        bool1,bool2,bool3,bool5 = False,False,False,False
        # Setting looping for the entire path
        looping_path1=True

        # Clear inventory if user has gone down other paths
        inventory.inventory.clear()

        # Add standard items to inventory
        inventory.inventory.append(knife)
        inventory.inventory.append(holotool)

        while looping_path1:

            totalBreak=False
            # User goes to main room
            looping_path1main=True

            # Closes the door from second floor
            path1office_door.item_used_alone=False

            while looping_path1main:
                # If main door has been used, break out of loop and go to second floor
                if path1main_door.item_used_alone:
                    looping_path1main=False
                else:
                    
                    if path1main_computer.item_used_alone:
                        ClearScreen()
                        header2()
                        print()
                        q1=input("Please type your answer to question 1: ")
                        if q1=="2102":
                            print()
                            q2=input("Please type your answer to question 2: ")
                            if "turner" in q2.lower():
                                print()
                                q3=input("Please type your answer to question 3: ")
                                if "chronosia" in q3.lower():
                                    looping_path1=False
                                    looping_path1main=False
                                    looping_path1office=False
                                    totalBreak=True
                                    break
                                else:
                                    ClearScreen()
                                    header2()
                                    print()
                                    print("Sorry that is not correct...")
                                    print("Please press enter to return")
                                    path1main_computer.item_used_alone=False
                            else:
                                ClearScreen()
                                header2()
                                print()
                                print("Sorry that is not correct...")
                                print("Please press enter to return")
                                path1main_computer.item_used_alone=False
                        else:
                            ClearScreen()
                            header2()
                            print()
                            print("Sorry that is not correct...")
                            input("Please press enter to return")
                            path1main_computer.item_used_alone=False

                    if totalBreak:
                        break

                    if path1main_statue.item_used_alone and path1main_keycard1 in inventory.inventory and path1main_keycard2 in inventory.inventory:
                        removeFromScene(path1main6, path1main)
                        addToScene(path1main12, path1main)
                        addToScene(path1main_computer, path1main_items)
                        removeFromScene(path1main_statue,path1main_items)

                    if path1main_keycard1 in inventory.inventory:
                        removeFromScene(path1main7, path1main)
                        removeFromScene(path1main8, path1main)

                    if path1main_boots.item_used_alone:
                        removeFromScene(path1main10, path1main)
                        removeFromScene(path1office10, path1office)
                        addToScene(path1office11, path1office)
                        removeFromScene(path1office_panel, path1office_items)
                        addToScene(path1office_panel2, path1office_items)


                    if path1main_display.item_used_with_otherItem:
                        addToScene(path1main_keycard2, path1main_items)
                        addToScene(path1main_keycard2, inventory.inventory)
                        removeFromScene(path1main4, path1main)
                        removeFromScene(path1main11, path1main)

                    if path1main_baton.item_used_with_otherItem:
                        addToScene(path1main_tip, inventory.inventory)
                        addToScene(path1main_tip, path1office_items)
                        removeFromScene(path1main_baton, path1main_items)
                        removeFromScene(path1main9, path1main)

                    if path1main_dispenser.item_used_alone:
                        if path1main_token not in inventory.inventory:
                            inventory.inventory.append(path1main_token)
                            if path1main_token not in path1main_items:
                                path1main_items.append(path1main_token)
                        if path1main5 in path1main:
                            path1main.remove(path1main5)
                            if path1main_dispenser in path1main_items:
                                path1main_items.remove(path1main_dispenser)

                    initialHeader()
                    displayPuzzleText(path1main)
                    print()
                    display_commands()
                    command=input().lower()
                    if "examine" in command:
                        examine_command(command,path1main_items)
                    elif "pick" in command:
                        pick_command(command,path1main_items)
                    elif command=="inventory":
                        inventory_command()
                    elif "use" in command:
                        use_command(command,path1main_items)

            if totalBreak:
                break

            # User goes to second floor
            looping_path1office=True

            # Closes the door from the main floor
            path1main_door.item_used_alone=False

            # If second floor door has been used, break out of loop and go back to main floor
            while looping_path1office:
                if path1office_door.item_used_alone:
                    looping_path1office=False
                else:
                    if path1office_keycard1.item_used_alone:
                        if path1main1 in path1main and path1main2 in path1main:
                            path1main.remove(path1main1)
                            path1main.remove(path1main2)
                            path1main.append(path1main7)
                        if path1office_keycard1.item_used_alone:
                            if path1main8 not in path1main:
                                path1main.append(path1main8)
                                if path1main_keycard1 not in path1main_items:
                                    path1main_items.append(path1main_keycard1)
                                if path1office_keycard1 not in path1office_items:
                                    path1main_items.append(path1office_keycard1)
                                if path1office12 not in path1office:
                                    path1office.append(path1office12)
                                if path1office9 in path1office:
                                    path1office.remove(path1office9)

                    if path1main_keycard1 in inventory.inventory:
                        if path1main8 in path1main:
                            path1main.remove(path1main8)
                    
                    if path1office_panel2.item_used_with_otherItem:
                        if path1main4 in path1main:
                            path1main.remove(path1main4)
                        if path1main11 not in path1main:
                            path1main.append(path1main11)
                        if path1main_display not in path1main_items:
                            path1main_items.append(path1main_display)

                    if path1office_boxes.item_used_alone and bool1==False:
                        if path1office6 not in path1office and path1office8 not in path1office:
                            path1office.append(path1office6)
                            path1office.append(path1office7)
                            path1office.remove(path1office5)
                            path1office_items.remove(path1office_boxes)
                            path1office_items.append(path1office_crackdummy)
                            bool1=True

                    if path1office_crackdummy.item_used_with_otherItem and bool2==False:
                        if path1office8 not in path1office:
                            path1office.append(path1office8)
                            path1office.remove(path1office6)
                            path1office.remove(path1office7)
                            path1office_items.remove(path1office_crackdummy)
                            path1office_items.append(path1office_desk)
                            bool2=True

                    if path1office_desk.item_used_alone and bool3==False:
                        if path1office9 not in path1office:
                            path1office.append(path1office9)
                            path1office.remove(path1office8)
                            path1office_items.remove(path1office_desk)
                            path1office_items.append(path1office_keycard1)
                            path1office_items.append(path1office_hololog1)
                            bool3=True

                    initialHeader()
                    displayPuzzleText(path1office)
                    print()
                    display_commands()
                    command=input().lower()
                    if "examine" in command:
                        examine_command(command,path1office_items)
                    elif "pick" in command:
                        pick_command(command,path1office_items)
                    elif command=="inventory":
                        inventory_command()
                    elif "use" in command:
                        use_command(command,path1office_items)

        print("This is the end of the level! Ya did it!")

        display(screen64)
        display(screen65)
        display(screen66)