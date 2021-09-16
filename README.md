# HKTVMall stock alert bot
This program would send stock availability alert via email, with time interval specified by the user. User can add product's link in a file ```links.txt```, then the program will keep track of them. This program is dockerized and can run anywhere.

## Steps to run the program
1. Install *Python 3* with *pip*
2. Run ```pip install -r requirements.txt``` to install the rquired python libraries.
3. Get Less Secure App Password at https://myaccount.google.com/u/1/security
4. Create a specify envrionment variables in a ```.env``` file, add your own values (after equal sign)
```
# User agent text, you can copy from http://www.useragentstring.com/
USER_AGENT=user_agent_text_string

# Google Less Secure App Password
GMAIL_APP_KEY=my_app_password

# Enter a valid gmail as sender
SENDER_GMAIL=mygmail@gmail.com

# Enter a valid email for receiving alert
RECEIVER_EMAIL=mymail@email.com

# Time interval for checking (in minutes)
CHECK_INTERVAL=15
```
5. Prepare a file named ```links.txt``` and put the product's URL in there, separated links by newline
6. Run ```python -u hktv.py```

##### Tips:
1. The product's links should start with ```https```
2. You can add comments in ```links.txt``` if you wants