# 정규식 = re (regular expression)

'''

주민등록번호
이메일 주소
차량번호
ip주소

'''

import re
# abcd, book
# ca?e
# care, cafe, case, cave, cake
# a to z input 

# p = pattern
p = re.compile("ca.e") 
# . (case)  : 하나의 문자를 의미 > care, cafe, case | caffe-x
# ^(^de)    : 문자열의 시작 > desk, destination | fade - x
# $(se$)    : 문자열의 끝 > case, base | face - x

def print_match(m) :

    if m:
        print("m.group() : {}".format(m.group())) # 일치하는 문자열 반환
        print("m.string : {}".format(m.string)) # 입력받은 문자열 반환
        print("m.start() : {}".format(m.start())) # 일치하는 문자열의 시작 index
        print("m.end() : {}".format(m.end())) # 일치하는 문자열의 끝 index
        print("m.span() : {}".format(m.span())) # 일치하는 문자열의 시작 / 끝 index

    else:
        print("매칭실패")
    
    

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
                                # 즉 앞이 일치하고 뒤가 다르더라도 일치판정
# print(m.group()) # 매치되지 않으면 에러가 발생
# m = p.search("good care ") # search : 주어진 문자열 중에 일치하는게 있는지 확인

# print_match(m)

# lst = p.findall("good careless cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

'''
1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열")     : 주어진 문자열이 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열")    : 주어진 문자열 줄에 일치하는게 있는지 확인    
4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 변환
'''