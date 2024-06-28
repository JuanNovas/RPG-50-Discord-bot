from discord.ext.commands import command

class LockManager:
    def __init__(self):
        self.locked_users = set()

    def is_locked(self, user_id):
        return user_id in self.locked_users

    def lock(self, user_id):
        self.locked_users.add(user_id)

    async def unlock(self, user_id):
        self.locked_users.remove(user_id)
        
    def command_lock(self, user_id):
        if self.is_locked(user_id):
            return False
        self.lock(user_id)
        return True

lock_manager = LockManager()