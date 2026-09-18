import feedparser
import json
from datetime import datetime

# قائمة مصادر الأخبار (RSS Links) التي اخترتها
# يمكنك إضافة أو تعديل أي مصدر تريده هنا مستقبلاً
SOURCES = [
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/news/rss.xml",
        "category": "Artificial Intelligence"
    },
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/feed/",
        "category": "Technology & Design"
    }
]

def fetch_news():
    all_articles = []
    
    for source in SOURCES:
        print(f"جاري سحب الأخبار من: {source['name']}...")
        feed = feedparser.parse(source['url'])
        
        # جلب أحدث 3 أخبار من كل مصدر كمرحلة أولى
        for entry in feed.entries[:3]:
            article = {
                "title": entry.get('title', 'بدون عنوان'),
                "summary": entry.get('summary', 'لا يوجد ملخص متاح').replace('<p>', '').replace('</p>', ''),
                "link": entry.get('link', '#'),
                "published": entry.get('published', datetime.now().strftime('%Y-%m-%d %H:%M')),
                "source": source['name'],
                "category": source['category']
            }
            all_articles.append(article)
            
    # حفظ الأخبار في ملف JSON لتستعرضها صفحة الموقع
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(all_articles, f, ensure_ascii=False, indent=4)
        
    print("تم تحديث وجلب الأخبار وحفظها بنجاح في ملف data.json!")

if __name__ == "__main__":
    fetch_news()
    # حفظ الأخبار كملف جافاسكريبت مباشر
# حفظ الأخبار كملف جافاسكريبت مباشر
    with open('news.js', 'w', encoding='utf-8') as f:
        f.write("const newsData = ")
        json.dump(all_articles, f, ensure_ascii=False, indent=4)
        f.write(";")
        
    print("تم تحديث وجلب الأخبار وحفظها بنجاح في ملف news.js!")