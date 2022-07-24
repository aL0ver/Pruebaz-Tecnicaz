def isNum(entrada):
    count = len(entrada)
    for i in entrada:
        try: 
            int(i)
        except ValueError:
            return False
        else:
            count -= 1
            if count == 0:
                return True
