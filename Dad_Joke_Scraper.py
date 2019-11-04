""" Little scraper program to pull the Dad-Joke of the day from the fatherhood.gov website
By: Lance Harlan"""

#Modules
import requests
import bs4
import tkinter

#Getting the webpage and saving it to variable response.
url = "https://www.fatherhood.gov/dad-jokes/jokes"
headers = {'User-Agent': 'Mozillla/5. (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers = headers)
response.raise_for_status()

#Parsing the html into text and storing in memory
page = bs4.BeautifulSoup(response.text, features="html.parser")

#Finding the element "joke" in the text and selecting it
joke = page.find('div', {"class": "field-content"})
joke = str(joke)
joke = joke.strip("'<div class=")
joke = joke.strip('"field-content">')
joke = joke.strip('</div')

#Printing the joke out in a popup
root = tkinter.Tk()
root.title("Dad_Joke")

joke_label = tkinter.Label(root, text=joke)
but = tkinter.Button(root, text="Close", command=root.destroy)

joke_label.pack()
but.pack()

root.mainloop()
















