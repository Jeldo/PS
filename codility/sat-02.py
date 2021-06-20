import datetime


def solution(S: str):
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    files = S.splitlines()
    admitted = []
    for file in files:
        info = file.split()
        role, permission, day, month, year, size, name = info[0], info[1], info[2], info[3], info[4], info[5], info[6]
        if role == 'admin' and 'x' in permission and int(size) < 14 * (2 ** 20):
            admitted.append(datetime.date(int(year), months[month], int(day)))
    admitted.sort()
    first = admitted[0]
    return f'{first.day} {first.strftime("%b")} {first.year}'


cases = [
    'admin  -wx 29 Sep 1983        833 source.h\n'
    'admin  r-x 23 Jun 2003     854016 blockbuster.mpeg\n'
    'admin  --x 02 Jul 1997        821 delete-this.py\n'
    'admin  -w- 15 Feb 1971      23552 library.dll\n'
    'admin  --x 15 May 1979  645922816 logs.zip\n'
    'jane   --x 04 Dec 2010      93184 old-photos.rar\n'
    'jane   -w- 08 Feb 1982  681574400 important.java\n'
    'admin  rwx 26 Dec 1952   14680064 to-do-list.txt\n'
]

for c in cases:
    res = solution(c)
    print(res)

# input :
'''
admin  -wx 29 Sep 1983        833 source.h
admin  r-x 23 Jun 2003     854016 blockbuster.mpeg
admin  --x 02 Jul 1997        821 delete-this.py
admin  -w- 15 Feb 1971      23552 library.dll
admin  --x 15 May 1979  645922816 logs.zip
jane   --x 04 Dec 2010      93184 old-photos.rar
jane   -w- 08 Feb 1982  681574400 important.java
admin  rwx 26 Dec 1952   14680064 to-do-list.txt
'''

# output :
'29 Sep 1983'

# description
# Role / Executable / Day / Month / Year / Size / Name
# input이 주어졌을때 조건에 맞는 목록들중 제일 앞에 있는 목록의 날짜를 반환
# -조건
# 1. 실행파일이여야 한다. (Executable이 x가 있어야함.)
# 2. admin에 의해 만들어진 파일이어야 한다.
# 3. 파일 사이즈는 14*2^20 보다 작아야 한다.
