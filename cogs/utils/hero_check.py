from cogs.utils.database import execute_dict
from cogs.utils.create import create_hero

async def hero_created(inte):
    data = execute_dict('''
    SELECT id FROM hero WHERE user_id=(?) AND active = 1
    ''', (inte.user.id,))
    if data == []:
        await create_hero(inte)
        return False
    else:
        return True