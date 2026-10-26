# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, percent):    # this parameter should be self
        self.percent = percent       
    
    def status(self):
        p = self.percent
        if p > 100:
            return'over limit'
        elif p >=90:
            return 'warning'
        else:
            return 'ok'

    def __str__(self):
        return f'Record value={self.percent}'




r = Record(95)
print(r.status())
