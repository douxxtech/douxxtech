import feedparser
import re
from pathlib import Path

README_PATH = Path("README.md")

feed = feedparser.parse("https://douxx.blog/articles/?rss")

if not feed.entries:
    raise RuntimeError("RSS feed has no entries")

latest_link = feed.entries[0].link

content = README_PATH.read_text(encoding="utf-8")

new_content = re.sub(
    r'<a href="[^"]*">My Latest Article</a>',
    f'<a href="{latest_link}">My Latest Article</a>',
    content
)

if content != new_content:
    README_PATH.write_text(new_content, encoding="utf-8")
    print("Content updated")

print("Script ran successfully !")
print(f"latest article btw: {latest_link} (go read it)")