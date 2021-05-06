def makeQuery(string):
    string = string.split()
    string = [string[0],string[2],string[4],string[6],string[7]]
    return string

def binarySearch(arr,N):
    start = 0
    end = len(arr)
    mid = (start + end) // 2
    while start < end:
        if arr[mid] == N:
            print(N,'hi')
            return end - mid
        if arr[mid] < N:
            start = mid + 1
            mid = (start + end) // 2
        elif arr[mid] > N:
            end = mid - 1
            mid = (start + end) // 2
    print(arr,N,start,mid,end)
    return end - mid

def solution(info, query):
    answer = []
    people_list = {
        'cpp':{
            'backend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            },
            'frontend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            }
        },
        'java':{
            'backend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            },
            'frontend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            }
        },
        'python':{
            'backend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            },
            'frontend':{
                'junior':{
                    'chicken':[],
                    'pizza':[]
                },
                'senior':{
                    'chicken':[],
                    'pizza':[]
                }
            }
        }
    }

    for i in range(len(info)):
        people = info[i]
        lang,job,carrer,food,point = people.split()
        people_list[lang][job][carrer][food].append(int(point))
        people_list[lang][job][carrer][food].sort()
    
    for i in range(len(query)):
        now_query = query[i]
        lang,job,carrer,food,point = makeQuery(now_query)
        cnt = 0
        if lang == '-':
            lang_list = ['cpp','java','python']
        else:
            lang_list = [lang]
        
        if job == '-':
            job_list = ['frontend','backend']
        else:
            job_list = [job]
        
        if carrer == '-':
            carrer_list = ['junior','senior']
        else:
            carrer_list = [carrer]
        
        if food == '-':
            food_list = ['chicken','pizza']
        else:
            food_list = [food]
        
        for la in lang_list:
            for jo in job_list:
                for ca in carrer_list:
                    for fo in food_list:
                        if point == '-':
                            cnt += len(people_list[la][jo][ca][fo])
                            continue
                        point = int(point)
                        cnt += binarySearch(people_list[la][jo][ca][fo],point)
        print(cnt)
        answer.append(cnt)

    return answer