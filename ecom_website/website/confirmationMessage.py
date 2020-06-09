import requests


def sendMessage(contactNumber=None, msg=None):
    """
    To send a text message
    :param contactNumber: Phone number of receiver
    :param msg: message to be sent (None for failed transaction )
    :return: None
    """

    if contactNumber is None:
        return

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "5opOL4g8RtrVU6lHMS0nWqdQfBa7jhbAJKNCZ31czFewPXvTyxHDBQVsmeRYSlT4wW8Ov9br3UpCkgIN"
        , "sender_id": "FSTSMS", "message": msg, "language": "english",
                   "route": "p", "numbers": str(contactNumber)}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
