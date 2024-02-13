# file : ds05__orderedList.py
# desc : 선형리스트 응용\2

## 함수 선언부분
def printPoly(p_x):
    term = len(p_x)-1      # 최고차항
    polyStr = "P(x) = "
    
    for i in range(len(px)):   # 계수
        coef = p_x[i]

        if( coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" +str(term) + " "
        term -= 1
    
    return polyStr

def calcPoly(xVal, p_x):
    retValue =0 
    term = len(p_x) -1
     
    for i in range(len(px)):
       coef = p_x[i]
       retValue += coef * xVal ** term
       term -= 1
    
    return retValue

## 전역변수 선언부분
px = [7, -4, 0, 5]

## 메인코드 부분
if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값 -->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)

def  printPoly(t_x, p_x):
    polyStr = "P(x)= "

    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]

        if coef >=0:
            polyStr += "+"
        polyStr += str(coef) + "x^" +str(term) + " "
        
    return polyStr

def calcPoly(xVal, t_x, p_x):
    retValue = 0

    for i in range(len(px)):
        term = t_x[i]
        coef= p_x[i]
        retValue += coef *xValue ** term
    