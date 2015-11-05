__author__ = 'redragonx/daemoniclegend'

# future home for keyboard inputs


class User_keypad():

    bullshitVar = None

    def keypad_input(self, codeIn):
        new_code = codeIn

        if len(new_code) == 5:
            # code to be inserted here to determine correctness of user input
            return 'Success'
        else:
            return 'Fail'



    def __init__(self):
        pass
