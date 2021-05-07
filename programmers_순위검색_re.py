import bisect
def makeQuery(string):
    string = string.split()
    string = [string[0],string[2],string[4],string[6],string[7]]
    return string

def binarySearch(arr,N):
    size = len(arr)
    return size - bisect.bisect_left(arr,N,lo=0,hi=size)

def solution(info, query):
    answer = []
    people_list = {}

    for i in range(len(info)):
        people = info[i]
        lang,job,carrer,food,point = people.split()
        if people_list.get(lang+job+carrer+food) == None:
            people_list[lang+job+carrer+food] = [int(point)]
        else:
            people_list[lang+job+carrer+food].append(int(point))
        if people_list.get('-'+job+carrer+food) == None:
            people_list['-'+job+carrer+food] = [int(point)]
        else:
            people_list['-'+job+carrer+food].append(int(point))
        if people_list.get(lang+'-'+carrer+food) == None:
            people_list[lang+'-'+carrer+food] = [int(point)]
        else:
            people_list[lang+'-'+carrer+food].append(int(point))
        if people_list.get(lang+job+'-'+food) == None:
            people_list[lang+job+'-'+food] = [int(point)]
        else:
            people_list[lang+job+'-'+food].append(int(point))
        if people_list.get(lang+job+carrer+'-') == None:
            people_list[lang+job+carrer+'-'] = [int(point)]
        else:
            people_list[lang+job+carrer+'-'].append(int(point))
        if people_list.get('--'+carrer+food) == None:
            people_list['--'+carrer+food] = [int(point)]
        else:
            people_list['--'+carrer+food].append(int(point))
        if people_list.get('-'+job+'-'+food) == None:
            people_list['-'+job+'-'+food] = [int(point)]
        else:
            people_list['-'+job+'-'+food].append(int(point))
        if people_list.get('-'+job+carrer+'-') == None:
            people_list['-'+job+carrer+'-'] = [int(point)]
        else:
            people_list['-'+job+carrer+'-'].append(int(point))
        if people_list.get(lang+'--'+food) == None:
            people_list[lang+'--'+food] = [int(point)]
        else:
            people_list[lang+'--'+food].append(int(point))
        if people_list.get(lang+'-'+carrer+'-') == None:
            people_list[lang+'-'+carrer+'-'] = [int(point)]
        else:
            people_list[lang+'-'+carrer+'-'].append(int(point))
        if people_list.get(lang+job+'--') == None:
            people_list[lang+job+'--'] = [int(point)]
        else:
            people_list[lang+job+'--'].append(int(point))
        if people_list.get('---'+food) == None:
            people_list['---'+food] = [int(point)]
        else:
            people_list['---'+food].append(int(point))
        if people_list.get('--'+carrer+'-') == None:
            people_list['--'+carrer+'-'] = [int(point)]
        else:
            people_list['--'+carrer+'-'].append(int(point))
        if people_list.get('-'+job+'--') == None:
            people_list['-'+job+'--'] = [int(point)]
        else:
            people_list['-'+job+'--'].append(int(point))
        if people_list.get(lang+'---') == None:
            people_list[lang+'---'] = [int(point)]
        else:
            people_list[lang+'---'].append(int(point))
        if people_list.get('----') == None:
            people_list['----'] = [int(point)]
        else:
            people_list['----'].append(int(point))
        
    for i in range(len(query)):
        now_query = query[i]
        lang,job,carrer,food,point = makeQuery(now_query)
        cnt = 0
        if point == '-':
            cnt += len(people_list[lang+job+carrer+food])
        else:
            point = int(point)
            if people_list.get(lang+job+carrer+food) != None:
                cnt += binarySearch(sorted(people_list.get(lang+job+carrer+food)), point)
        answer.append(cnt)

    return answer