"""Browser History
Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

"URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
"Back" - moves to the previous page in history, or stays on the current page if there isn't one.
"Forward" - moves to the next page in history, or stays on the current page if there isn't one."""

def get_browser_history(commands):

    history_page = []
    temp_page= []
    index = 0

    for command in commands:

        if command != "Back" and command != "Forward":

            history_page.append(command)
            index = len(history_page) - 1
            temp_page = []

        elif command == "Back" and index != 0:
            
            temp_page.append(history_page[index])
            history_page = history_page[:index]
            index = len(history_page) - 1

        elif command == "Forward" and len(temp_page) > 1:

            history_page.append(temp_page[len(temp_page) - 1])
            temp_page = temp_page[: len(temp_page) - 1]
            index = len(history_page) - 1
         
        
        

    return [history_page + temp_page,index]


print(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]))

print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))

print(get_browser_history(["example.com", "example.com/about", "Back", "Back"]))

#chat's

def get_browser_history(commands):
    history = []
    current = -1

    for command in commands:
        if command == "Back":
            if current > 0:
                current -= 1

        elif command == "Forward":
            if current < len(history) - 1:
                current += 1

        else:
            history = history[:current + 1]
            history.append(command)
            current += 1

    return [history, current]
  

