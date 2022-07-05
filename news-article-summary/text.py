from bs4 import BeautifulSoup
from summarizer import summarizer
import requests

def articleText(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	fullText = ""
	for text in soup.find_all("a"):
		text.decompose()
	for text in soup.find_all("p"):
		fullText += " " + text.get_text()
	fullText = fullText.replace("\n", " ")
	return fullText

def main(url, lines):
	if "https" in url:
		url_text = articleText(url)
		final_summary = summarizer(url_text, lines)
	else:
		final_summary = summarizer(url, lines)
	return " ".join(final_summary)

# url = str(input("Enter an article URL\n"))
# print(summarizeURL(url,3))
