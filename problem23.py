

def hcf(p1,p2):
    hcf = 1
    larger = p1 if p1 > p2 else p2
    for i in range(1,larger):
        if ((p1 % i == 0) and (p2 % i == 0)):
            hcf = i
    return hcf
    
p1 = 10
p2 = 6

print(hcf(p1,p2))
