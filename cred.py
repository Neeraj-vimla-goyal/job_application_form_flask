import os


def get_cred():

    password = "FLASK_APP_PASSWORD"
    sender = "SENDER"
    app_password = os.environ[password]
    sender = os.environ[sender]
    return app_password, sender


if __name__ == "__main__":
     a, b = get_cred()

     print(a)
     print(b)



