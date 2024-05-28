import pymupdf

doc = pymupdf.open("input.pdf")

text = ""

for page in doc:
    text = page.get_text()

with open("output.txt", "w") as file:
    file.write(text)
