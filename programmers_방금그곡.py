class Music:
    def __init__(self,string):
        start,end,name,scale = string.split(',')
        start_hour,start_minute = start.split(':')
        end_hour,end_minute = end.split(':')
        self.start = int(start_hour)*60 + int(start_minute)
        self.end = int(end_hour)*60 + int(end_minute)
        self.during = self.end - self.start
        self.name = name
        self.scale = []
        i = 0
        j = 0
        while i < self.during:
            i += 1
            self.scale.append(scale[j%len(scale)])
            j += 1
            if scale[j%len(scale)] == '#':
                self.scale[-1] += '#'
                j += 1

def isSong(mine,scale):
    i = 0
    mine_string = ''.join(mine)
    while i < len(scale):
        if mine[0] != scale[i]:
            i += 1
        else:
            if mine_string == ''.join(scale[i:i+len(mine)]):
                return True
            i += 1
    return False

def solution(m, musicinfos):
    scale_list = []
    for i in m:
        if i == '#':
            scale_list[-1] += i
        else:
            scale_list.append(i)
    m = scale_list[:]
    answer = '(None)'
    answer_time = -1
    start_time = -1
    for i in range(len(musicinfos)):
        musicinfos[i] = Music(musicinfos[i])
    for music in musicinfos:
        if isSong(m,music.scale):
            if answer_time < music.during:
                answer_time = music.during
                answer = music.name
                start_time = music.start
            elif answer_time == music.during:
                if start_time > music.start:
                    start_time = music.start
                    answer_time = music.during
                    answer = music.name
                    start_time = music.start
    return answer