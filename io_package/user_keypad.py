__author__ = 'redragonx/daemoniclegend'

# future home for keyboard inputs
from plane_controller import plane_ctrl
import re


class User_keypad():
    bullshitVar = None
    pattern = re.compile("[0-9]{4}\#")

    def keypad_input(self, codeIn):
        new_code = codeIn

        if len(new_code) == 5:
            if self.pattern.match(new_code):
                # Can include code later to "read back" the inputted code
                outString = new_code[0:4]
                print(outString)
                plane_ctrl.update_transponder_code(outString)
                return 'Success'
            else:
                # Can include code later to inform user of invalid input
                return 'Fail'
        else:
            # Can include code later to inform user of invalid input
            return 'Fail'

    def __init__(self):
        pass
