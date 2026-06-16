# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        res = func()
        text = res['name']
        res['name'] = text[:1] + "*" * (len(text) - 2) + text[-1:]
        res['password'] = '*' * len(res['password'])

        return res

    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }
    
@obfuscator
def get_crede():
    return {
        'name': 'tasSBasov',
        'password': 'rgrt'
    }

print(get_credentials())
print(get_crede())