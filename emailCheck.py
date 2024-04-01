from LogIn import LogIn
from email_validator import validate_email, EmailNotValidError
import sys

class EmailCheck(LogIn):
    @staticmethod
    def check(login_instance):
        email = login_instance.email
        if email:
            try:
                v = validate_email(email) 
                email = v["email"] 
                print("Email is valid:", email)
            except EmailNotValidError as e:
                print("Email is not valid:", str(e))
                sys.exit("Invalid email. Closing LogIn.")
                return

if __name__ == "__main__":
    login = LogIn()
    login.main()  # Assuming main method of LogIn class sets the email attribute
    email_checker = EmailCheck()
    email_checker.check(login)

