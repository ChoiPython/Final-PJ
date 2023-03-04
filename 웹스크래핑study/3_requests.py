import requests
# res = requests.get("https://naver.com")   
res = requests.get("https://trade.sa.nexon.com/")
res2 = requests.get("https://google.com")
# res = requests.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code) # 200은 정상

res.raise_for_status()
res2.raise_for_status()


# if res.status_code == requests.codes.ok :
#     print("정상")

# else:
#     print("에러발생")
#     exit()

# if문 대신 사용 가능
# res.raise_for_status() # 웹 스크래핑 올바로 가져오지 못하면 에러 발생
# print("웹 스크래핑 진행합니다.")


# print(len(res.text))
print(len(res.text))


# 파일로 만들어보기
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)