def solution(record):
    d = dict()
    result = []
    for r in record:
        message = r.split()
        if len(message) == 3:
            uid, nickname = message[1], message[2]
            d[uid] = nickname
    for r in record:
        message = r.split()
        status, uid = message[0], message[1]
        if status == 'Enter':
            result.append('{}님이 들어왔습니다.'.format(d[uid]))
        elif status == 'Leave':
            result.append('{}님이 나갔습니다.'.format(d[uid]))
    return result


cases = [
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ],
]

for c in cases:
    s = solution(c)
    print(s)
