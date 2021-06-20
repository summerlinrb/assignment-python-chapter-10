import requests

# Chapter 10.2 - Pip
# If not installed, install the requests package from
# a terminal using pip or pip3 for Mac.
# pip install requests
# pip3 install requests

# BRANDON SUMMERLIN

response = requests.get("Http://google.com")
print(response)
print(response.url)
# displays the HTML text returned by the web server.
print(response.text)
