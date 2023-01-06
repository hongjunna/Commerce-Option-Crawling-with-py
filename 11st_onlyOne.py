import requests
from bs4 import BeautifulSoup

link = input("11번가 링크를 입력하세요 : ")[:42]

def Press_Enter_to_Continue1():
    import os
    print("\n이 링크는 상품 정보를 불러올 수 없어 크롤링 작업에 실패했습니다."+"\n링크를 확인 후 재시도 해주세요.\n입력 된 값 : "+link+"\n\n")
    os.system("pause")

if len(link)==42:
    raw = requests.get(link)
    html = BeautifulSoup(raw.text, "html.parser")

    items = []
    price = []

    container = html.select("li.option_item.c_product_option_item")
    for con in container:
        i = con.select_one("strong").text.strip()
        items.append(i)
        p = con.select_one("span.num.value")
        if p == None:
            p='품절'
        else:
            p=con.select_one("span.num.value").text.strip()
        price.append(p)


    trytime = 0
    commalist = ''
    writelist = ''
    f = open("11번가("+link[-10:]+") 상품 옵션 크롤링.txt",'w', encoding="UTF-8")
    
    while trytime < len(items):
        if price[trytime] == "품절":
            data = "\t[옵션"+str(trytime+1)+"] "+items[trytime]+" (품절)\n"
        else:
            data = "\t[옵션"+str(trytime+1)+"] "+items[trytime]+" ("+price[trytime]+"원)\n"
        print(data)
        commalist = commalist+items[trytime]+","
        writelist = writelist+data
        trytime = trytime+1
    f.write("<11번가 상품 크롤링 결과>\n상품 코드 : "+link[-10:]+"\n상품 문자열 : \n"+commalist[:-1]+"\n\n상품 리스트 :\n"+writelist)
    f.close()
else:
    Press_Enter_to_Continue1()