def isNum(entrada):
    for i in entrada:
        try: 
            int(i)
        except ValueError:
            return False    
    return True
