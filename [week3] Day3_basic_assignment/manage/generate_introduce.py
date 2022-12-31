import sys
import os
# import team_information
import manage.team_information as team_information


def generate_introduce(member):
    if member['국적'] == '대한민국':
        return "안녕하세요, 저는 {} {}의 {}{}입니다.".format(
            team_information.team_prefix[member['소속']],
            member['소속'],
            member['성'],
            member['이름'])
    else:
        return "안녕하세요, 저는 {} {}의 {} {}입니다.".format(
            team_information.team_prefix[member['소속']],
            member['소속'],
            member['이름'],
            member['성'])