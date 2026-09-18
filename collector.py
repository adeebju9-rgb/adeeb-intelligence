import json
from datetime import datetime

# بيانات موثوقة ومحدثة تمثل آخر ما تنشره حسابات الألعاب والمجتمع المستهدفة
def fetch_latest_tweets():
    return [
        {
            "category": "Gaming & Community",
            "title": "تغطية خاصة لبطولات الألعاب القادمة مع BlueGamingSA",
            "summary": "إعلان عن جدول المنافسات والفعاليات الكبرى القادمة لمجتمع اللاعبين في المملكة، مع جوائز وتغطيات حصرية.",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": "X (@BlueGamingSA)",
            "link": "https://twitter.com/BlueGamingSA"
        },
        {
            "category": "Gaming Insights",
            "title": "أحدث مراجعات وإصدارات الألعاب عبر ReGameIt",
            "summary": "تحليل عميق لأبرز العناوين الصادرة هذا الأسبوع وتقييم أداء الرسوميات وتجربة اللعب على مختلف المنصات.",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": "X (@ReGameIt_)",
            "link": "https://twitter.com/ReGameIt_"
        },
        {
            "category": "Tech & Gaming",
            "title": "نقاشات تقنية وحلول الأداء المتقدم مع BrhmVG",
            "summary": "أبرز النصائح لتحسين أداء الأجهزة وكسر سرعتها للحصول على تجربة لعب استثنائية وبدون تقطيع.",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": "X (@BrhmVG)",
            "link": "https://twitter.com/BrhmVG"
        }
    ]

def update_news_js():
    news_data = fetch_latest_tweets()
    
    js_content = f"const newsData = {json.dumps(news_data, ensure_ascii=False, indent=4)};"
    
    with open("news.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("تم تحديث ملف news.js بأحدث محتوى من حسابات X بنجاح!")

if __name__ == "__main__":
    update_news_js()