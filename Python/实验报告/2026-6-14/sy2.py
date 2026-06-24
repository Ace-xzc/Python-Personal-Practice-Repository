#20255120201100廖懋雄
def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print(isNum("222"))
print(isNum("22.2"))
print(isNum("NCAA"))
print(isNum("CCS666"))