def compare_age(standard_member, member_to_compare):
    if standard_member['나이'] < member_to_compare['나이']:
        return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원보다 나이가 적습니다."
    elif standard_member['나이'] > member_to_compare['나이']:
        return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원보다 나이가 많습니다."
    else:
        return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원과 나이가 같습니다."
