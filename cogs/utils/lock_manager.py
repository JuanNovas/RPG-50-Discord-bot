from discord.ext.commands import command

class LockManager:
    def __init__(self):
        self.locked_users = set()

    def is_locked(self, user_id):
        return user_id in self.locked_users

    def lock(self, user_id):
        self.locked_users.add(user_id)

    def unlock(self, user_id):
        self.locked_users.remove(user_id)

lock_manager = LockManager()