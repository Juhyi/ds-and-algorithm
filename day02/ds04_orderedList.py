# file : ds04_o4_orderedList.py
# desc : 

kakaotalk = [] 
def add_data(friend):
    kakaotalk.append(None) # 배열에 빈자리를 생성
    size =len(kakaotalk)    #배열의 전체 크기
    kakaotalk[size -1] = friend

def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입 범위 초과')
        return # 함수를 빠져나감
    
    # 정상적인 처리 시작
    kakaotalk.append(None) # 빈칸 추가
    size = len(kakaotalk) # 배열의 현재 크기
    # 데이터 삽입 위치까지 데이터를 하나씩 뒤로 보냄
    for i in range(size-1, pos, -1): #역순으로 맨뒤에서 부터
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None
    
    kakaotalk[pos] = friend

def delete_data(pos): # 데이터 삭제시는 위치값만
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삭제 범위 초과')
        return
    
    size =len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제

    for i in range( pos +1, size): 
        kakaotalk[i-1] = kakaotalk[i] # 뒤에 값을 앞으로
        kakaotalk[i] = None
    
    del(kakaotalk[size-1]) #배열의 제일 마지막 값 삭제

# 전역변수 선언
kakaotalk = []   # 빈 배열 생성
select = -1  # 1/ 추가 2/ 삽입 3/ 삭제 4/종료

if __name__ == '__main__':
    while (select != 4):
        select  = int(input(' 선택( 1: 추가, 2:삽입, 3:삭제, 4:종료) > '))

        if select == 1:
            data = input('추가 데이터 ------>')
            add_data(data)
            print(kakaotalk)
        elif select == 2:
            pos = int(input('삽입위치 -->'))
            data = input('추가 데이터 ------>')
            insert_data(pos, data)
            print(kakaotalk)
    
        elif select == 3:
            pos = int(input('삭제위치 -->'))
            delete_data(pos)
            print(kakaotalk)
        elif select == 4:
            exit(0) # 프로그램 완전 종료 함수
        
        else:
            print('1~4 중 하나를 선택하세요.')
            continue