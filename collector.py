import json
from datetime import datetime
import feedparser

# قائمة حسابات X (تويتر) المستهدفة عبر روابط الـ RSS الموثوقة
# نستخدم خدمات Nitter/RSS البديلة لجلب التغريدات العامة بسلاسة وأمان
TWITTER_FEEDS = [
    {
        "name": "Blue Gaming SA",
        "url": "https://nitter.poast.org/BlueGamingSA/rss",
    },
    {"name": "ReGameIt", "url": "https://nitter.poast.org/ReGameIt_/rss"},
    {"name": "BrhmVG", "url": "https://nitter.poast.org/BrhmVG/rss"},
]


def fetch_tweets():
  all_news = []

  for source in TWITTER_FEEDS:
    print(f"جاري جلب تغريدات: {source['name']}...")
    try:
      feed = feedparser.parse(source["url"])
      # جلب أحدث 2 تغريدة من كل حساب
      for entry in feed.entries[:2]:
        title = entry.title
        link = entry.link
        # تنظيف عنوان التغريدة أو صياغتها بأسلوب إعلاني راقٍ
        clean_title = (
            title[:90] + "..." if len(title) > 90 else title
        )  # اختصار العنوان ليكون جذاباً

        news_item = {
            "category": "Gaming & Community",
            "title": f"جديد {source['name']}: {clean_title}",
            "summary": (
                "متابعة حصرية لأحدث النقاشات، الإعلانات، والمحتوى التقني"
                " المخصص لعالم الألعاب من قلب المنصة."
            ),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": f"X (@{source['name']})",
            "link": link,
        }
        all_news.append(news_item)
    except Exception as e:
      print(f"خطأ أثناء جلب تغريدات {source['name']}: {e}")

  return all_news


def update_news_js():
  # جلب الأخبار الجديدة من الحسابات
  news_data = fetch_tweets()

  # إذا فشل الجلب لأي سبب، نضع أخبار افتراضية تفاعلية
  if not news_data:
    news_data = [{
        "category": "Gaming",
        "title": "تحديثات مجتمع الألعاب والتقنية",
        "summary": (
            "ترقبوا أحدث التغريدات والمحتوى المتجدد من قنوات الألعاب"
            " والمجتمع الرقمي."
        ),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "source": "Adeeb Intelligence Hub",
        "link": "https://twitter.com",
    }]

  js_content = f"const newsData = {json.dumps(news_data, ensure_ascii=False, indent=4)};"

  # كتابة البيانات مباشرة إلى ملف news.js الذي يقرأه الموقع
  with open("news.js", "w", encoding="utf-8") as f:
    f.write(js_content)
  print("تم تحديث ملف news.js بنجاح مع تغريدات X!")


if __name__ == "__main__":
  update_news_js()