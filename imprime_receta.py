import markdown

with open('recetas.md', 'r') as f:
    markdown_text = f.read()

html = markdown.markdown(markdown_text)

print(html)
