import requests
from send_email import send_email

# Type in a topic you are interested in.
topic = "tesla"

# Type in your API key.
api_key = "YOUR_API_KEY"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-05&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}" \
      "language=en"

# Make a request:
req = requests.get(url)

# Create a dictionary out of the JSON data:
content = req.json()
# print(content["articles"])

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)


