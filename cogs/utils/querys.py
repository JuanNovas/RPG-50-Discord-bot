from cogs.utils.database import execute_dict


def get_zone(user_id: int) -> int:
    data = execute_dict('''
    SELECT zone_id FROM hero WHERE user_id = (?) AND active = 1
    ''', (user_id,))[0]
    return data["zone_id"]