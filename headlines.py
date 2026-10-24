import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}

# 1. Fetch the page
response = requests.get(URL, headers=headers, timeout=10)

# 2. Check the status code before parsing anything
if response.status_code != 200:
    print("Could not fetch the page. Status code:", response.status_code)
    raise SystemExit

# 3. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 4. Find every headline tag we found by inspecting
items = soup.find_all("h2", attrs={"data-testid": "card-headline"})

# 5. Clean the text, skip empty and duplicate entries, stop at 5
headlines = []
for item in items:
    text = item.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)
    if len(headlines) == 5:
        break

# 6. Print the result (and handle fewer than 5 without crashing)
if not headlines:
    print("No headlines found. The page may load them with JavaScript.")
else:
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
    if len(headlines) < 5:
        print(f"(Only {len(headlines)} headlines were found.)")