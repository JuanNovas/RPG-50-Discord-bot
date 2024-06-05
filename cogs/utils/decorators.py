def same_user(original_func):
    def decorator(*args, **kwargs):
        global ctx
        if args[0].user != ctx.author:
            return
        result = original_func(*args, **kwargs)
        return result
    return decorator

def mana_ability(cost):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self.use_mana(cost):
                return False
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def health_ability(cost):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self.use_health(cost):
                return False
            return func(self, *args, **kwargs)
        return wrapper
    return decorator