members = [
    {
        '성': '김',
        '이름': '이팝',
        '소속': '나무팀',
        '국적': '대한민국',
        '나이': 40,
    },
    {
        '성': '김',
        '이름': '단풍',
        '소속': '나무팀',
        '국적': '대한민국',
        '나이': 29,
    },
    {
        '성': '이',
        '이름': '버들',
        '소속': '나무팀',
        '국적': '대한민국',
        '나이': 34,
    },
    {
        '성': '박',
        '이름': '바오밥',
        '소속': '나무팀',
        '국적': '대한민국',
        '나이': 27,
    },
    {
        '성': 'May',
        '이름': 'Blossom',
        '소속': '나무팀',
        '국적': '미국',
        '나이': 28,
    },
    {
        '성': '김',
        '이름': '샤프란',
        '소속': '꽃팀',
        '국적': '대한민국',
        '나이': 42,
    },
    {
        '성': '김',
        '이름': '튤립',
        '소속': '꽃팀',
        '국적': '대한민국',
        '나이': 37,
    },
    {
        '성': '박',
        '이름': '수선화',
        '소속': '꽃팀',
        '국적': '대한민국',
        '나이': 33,
    },
    {
        '성': '박',
        '이름': '앵초',
        '소속': '꽃팀',
        '국적': '대한민국',
        '나이': 28,
    },
    {
        '성': 'Sharon',
        '이름': 'Rose',
        '소속': '꽃팀',
        '국적': '미국',
        '나이': 23,
    },
] # 사전 정의 데이터

standard_member = members[4]
member_to_compare = members[8]

if standard_member['나이'] < member_to_compare['나이']:
 print(f"{standard_member['성']}{standard_member['이름']}사원은 {member_to_compare['성']}{member_to_compare['이름']}사원보다 나이가 적습니다.")
elif standard_member['나이'] > member_to_compare['나이']:
 print(f"{standard_member['성']}{standard_member['이름']}사원은 {member_to_compare['성']}{member_to_compare['이름']}사원보다 나이가 많습니다.")
else:
 print(f"{standard_member['성']}{standard_member['이름']}사원은 {member_to_compare['성']}{member_to_compare['이름']}사원과 나이가 같습니다.")



