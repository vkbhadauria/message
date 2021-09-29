1. Environment Setup:

    * Install Python 3.7.5 on your system, if not already present. You can install it using the steps mentioned below:-
        * For Linux users:-
            * sudo apt update
            * sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget libsqlite3-dev
            * wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tar.xz
            * tar -xf Python-3.7.5.tar.xz
            * cd Python-3.7.5
            * ./configure --enable-optimizations
            * sudo make altinstall

         * For OSX:-
            * Download and install python 3.7.5 using the link below.
                * https://www.python.org/ftp/python/3.7.5/python-3.7.5-macosx10.9.pkg

    * Create a virtual env with python 3.7.5
    * execute `pip install -r requirements.txt` to setup dependencies
    * Install Sqlite3

2. Run migrations
    * `python manage.py migrate`

2. Make Admin account
    * `python manage.py createsuperuser`
    * mobile: mobile is username
    * email:
    * password:

3. Run test case
    ` python manage.py test`
    
4. Use django restframework UI in browser to call API 

    * [User Signup API](http://localhost:8000/signup)

    * [User login API](http://localhost:8000/login)

    * Message api GET to get all message and POST to send message
    * Note: user must be login before to send message for authentication


    *GET: [Message List](http://localhost:8000/message)
    
    *POST: [send message](http://localhost:8000/message)
    ```
      "message": {
            "text": "",
            "media": null,
            "message_type": 'text'
        },
        "reciever_mobile": ""
```
