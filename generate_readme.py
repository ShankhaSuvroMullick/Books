from pathlib import Path
from datetime import datetime
import urllib.parse

ROOT = Path.cwd()
README = ROOT / "README.md"

pdfs = sorted(ROOT.rglob("*.pdf"))

categories = {}

for pdf in pdfs:
    category = pdf.parent.name
    categories.setdefault(category, []).append(pdf)


content = []

content.append("# 📚 Personal Book Library\n")
content.append(
    f"Automatically generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
)

content.append(f"**Total Categories:** {len(categories)}\n")
content.append(f"**Total Books:** {len(pdfs)}\n")

content.append("---\n")

content.append("## 📑 Table of Contents\n")

for category in sorted(categories):
    anchor = (
        category.lower()
        .replace(" ", "-")
        .replace("+", "")
        .replace("&", "")
    )
    content.append(f"- [{category}](#{anchor})")

content.append("\n---\n")


for category in sorted(categories):

    content.append(f"## {category}\n")

    books = sorted(categories[category])

    for book in books:

        relative = book.relative_to(ROOT)

        # GitHub compatible path
        github_path = "/".join(
            urllib.parse.quote(part)
            for part in relative.parts
        )

        title = book.stem

        content.append(
            f"- 📖 [{title}](./{github_path})"
        )

    content.append("")


README.write_text(
    "\n".join(content),
    encoding="utf-8"
)

print("README.md generated successfully")
print(f"Books: {len(pdfs)}")