import re
class Methods:
    def Check_seating(seat):
        pat = r"[A-E][0-9]$"
        if re.match(pat,seat):
            pass
        else:
            if '10' in seat :
                pass
            else:
                return True
