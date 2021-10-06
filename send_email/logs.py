import requests


def get_logs(date_start, limit):
    return requests.get(
        "https://api.mailgun.net/v3/YOUR_DOMAIN/events",
        auth=("api", "YOUR_API_KEY"),
        params={"begin": f"{date_start}",
                "ascending": "yes",
                "limit": f"{limit}",
                "event": "rejected OR failed OR delivered"
                })


def delivered(logs):
    total = 0
    successfully = 0
    for log in logs['items']:
        if log['event'] == 'delivered':
            successfully += 1
        total += 1
    return str(round(successfully/total*100))

