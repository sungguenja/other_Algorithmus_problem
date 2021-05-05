import re
class WebPage:
    def __init__(self,page,name,link_list,index):
        self.page = page
        self.name = name
        self.link_list = link_list
        self.match = 0
        self.basic = 0
        self.external = len(link_list)
        self.index = index

def cleanText(text):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》123456789]', ' ', text)
    return list(text.split())

def findElement(arr):
    start = -1
    end = -1
    name = ''
    link_list = []
    body_list = []
    for i in range(len(arr)):
        if arr[i] == '<body>':
            start = i + 1
        elif arr[i] == '</body>':
            end = i
        elif 'content' in arr[i]:
            name = list(arr[i].split('content='))[1][1:-3]
        elif 'href' in arr[i]:
            link = list(arr[i].split('href='))[1]
            link = list(link.split('>'))[0][1:-1]
            link_list.append(link)
            trigger = True
            now_text = ''
            for j in range(len(arr[i])):
                if arr[i][j] == '<':
                    now_text += ' '
                    trigger = False
                    continue
                elif arr[i][j] == '>':
                    trigger = True
                    continue
                if trigger:
                    now_text += arr[i][j]
            now_text = cleanText(now_text)
            body_list.extend(now_text)
        elif start != -1 and end == -1:
            body_list.extend(cleanText(arr[i]))
    return name,link_list,body_list

def solution(word, pages):
    answer = -1
    answer_point = -1
    web = {}
    for i in range(len(pages)):
        page = pages[i]
        arr = list(page.split('\n'))
        name,link_list,body_list = findElement(arr)
        web[name] = WebPage(body_list,name,link_list,i)
    key_list = list(web.keys())
    for page in key_list:
        body_list = web[page].page
        cnt = 0
        for body in body_list:
            if body.upper() == word.upper():
                cnt += 1
        web[page].basic = cnt
        external_list = web[page].link_list
        for link in external_list:
            print(link)
            if link in key_list:
                web[link].match += web[page].basic/web[page].external
    for page in key_list:
        print(web[page].basic,web[page].external,web[page].match)
        if answer_point < web[page].basic + web[page].match:
            answer_point = web[page].basic + web[page].match
            answer = web[page].index
        elif answer_point == web[page].basic + web[page].match:
            if answer > web[page].index:
                answer = web[page].index

    return answer