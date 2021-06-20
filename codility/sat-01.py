def solution(S, C):
    def create_user_id(first, last, middle=None):
        user_name = ''
        user_name += first[0]
        if middle:
            user_name += middle[0]
        if '-' in last:
            hyphen = last.split('-')
            left, right = hyphen[0], hyphen[1]
            user_name += left + right[:2]
        else:
            user_name += last
        return user_name

    users = S.split(', ')
    registered_id = dict()
    registered_users = []
    for user in users:
        user_id = ''
        names: list[str] = user.split()
        if len(names) == 2:
            user_id = create_user_id(names[0].lower(), names[1].lower())
        elif len(names) == 3:
            user_id = create_user_id(names[0].lower(), names[2].lower(), names[1].lower())

        # register
        if user_id not in registered_id:
            registered_id[user_id] = 1
        else:
            registered_id[user_id] += 1
            user_id += str(registered_id[user_id])
        registered_users.append(f'{user} <{user_id}@{C}.com>')
    return ', '.join(registered_users)


cases = [
    ['John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker', 'example']
]

# 이름은 First-(Middle)-Last Name 순서, Middle은 없을 수도 있음
# Last Name의 하이픈(-)은 없을 수도 있음
# First Name의 첫글자, Last Name을 소문자로해서 이메일의 아이디를 만드는 것
# Last Name에 하이픈이 있다면 하이픈 앞은 모두, 뒤는 두글자만
# Middle Name이 있다면 First Name의 첫글자, Middle Name의 첫글자, Last Name의 소문자로 만들고,

# output
# John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>,
# John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>

for c in cases:
    res = solution(*c)
    print(res)
