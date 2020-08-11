
class RegisterController:

    def validate(self,name,email,password):

        if len(name) == 0:
            return 'The name cannot be empty'
        elif len(email) == 0:
            return 'Email cannot be empty'
        elif len(password) == 0:
            return 'Passowrd cannot be empty'

        return 1



