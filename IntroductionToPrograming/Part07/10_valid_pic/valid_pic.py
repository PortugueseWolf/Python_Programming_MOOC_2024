# ddmmyyXyyyz || dd mm yy X yyyy
# X = +(1800) or -(1900) or A(2000)
# yyy = personnel identifier
# z = control (ddmmyyyyy) %% 31 = 0123456789ABCDEFHJKLMNPRSTUVWXY (12 == C)

from datetime import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    day = int(pic[:2])
    month = int(pic[2:4])
    if pic[6] == "+":
        year = "18" + pic[4:6]
    if pic[6] == "-":
        year = "19" + pic[4:6]
    if pic[6] == "A":
        year = "20" + pic[4:6]

    year = int(year)
    # print(day)
    # print(month)
    # print(year)

    try:
        birth_date = datetime(year,month,day)
    except:
        return False
    
    control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    expected_control = control[int(pic[:6] + pic[7:10]) % 31]
    
    if expected_control != pic[10]:
        return False
    
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))