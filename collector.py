import feedparser
import json
from datetime import datetime

# قائمة الحسابات أو المصادر الإخبارية (يمكنك إضافة مصادرك هنا)
feeds = [
    {"name": "Gaming News 1", "url": "https://ign.com/rss.xml"},
    {"name": "Gaming News 2", "url": "https://gamespot.com/feeds/news/"}
]

all_news = []

for feed_info in feeds:
    parsed_feed = feedparser.parse(feed_info["url"])
    # اخذ آخر 5 أخبار فقط من كل مصدر
    entries = parsed_feed.entries[:5]
    
    for entry in entries:
        news_item = {
            "source": feed_info["name"],
            "title": entry.get("title", "بدون عنوان"),
            "link": entry.get("link", "#"),
            "published": entry.get("published", str(datetime.now())),
            "summary": entry.get("summary", "لا توجد تفاصيل متاحة.")
        }
        all_news.append(news_item)

# حفظ النتائج في ملف news.js بالصيغة التي تقرؤها واجهة المنصة
js_content = f"const dualNewsData = {json.dumps(all_news, ensure_ascii=False, indent=2)};"

with open("news.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully collected latest 5 news items per source!")
