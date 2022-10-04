class Password_manager:
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords
    def get_password(self):
        return self.old_passwords[len(self.old_passwords) - 1]
    def set_password(self):
        new_password = input('enter new password ')
        if new_password in self.old_passwords:
            print('enter another password')
        else:
            self.old_passwords.append(new_password)    

    def is_correct(self):
        p = input('try to guess the password ')
        if p == self.get_password():
            return True
        return False    

old_passwords = ['qwerty', '123ghj, dsfgsd', '5678ss', 'cvbnm']
a = Password_manager(old_passwords)
print('current password is', a.get_password())
a.set_password()
print('current password is', a.get_password())
if a.is_correct():
    print('you guessed')
else:
    print('you did not guess')

