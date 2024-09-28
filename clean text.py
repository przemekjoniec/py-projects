
def cleanText(text):
    clearedText = text.replace("java", "****")
    clearedText = clearedText.replace("php", "***")
    clearedText = clearedText.replace("html", "****")
    clearedText = clearedText.replace("css", "***")
    clearedText = clearedText.replace("javascript", "**********")
    print(clearedText)


text="""
I started programming with php,
as the next step I learned html and css,
but now I'm focusing on javascript and python
"""

cleanText(text)