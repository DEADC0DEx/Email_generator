from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Data dictionaries for English and Hebrew
data = {
    'en': {
        "names": ["Oren", "Dana", "Yossi", "Tal", "Noa", "Alex", "Jordan", "Taylor", "Sam", "Casey"],
        "social_networks": [
            "Facebook", "Twitter", "Instagram", "LinkedIn", "TikTok", "Snapchat", "Pinterest",
            "Reddit", "Telegram", "Discord", "MySpace", "Friendster", "Habbo Hotel",
            "Club Penguin", "Neopets", "The Matrix", "Subreddit", "Virtual Reality Lounge",
            "Astral Projection Forums", "Telepathic Networks"
        ],
        "games": [
            "FIFA", "Escape Room", "Rock, Paper, Scissors", "Monopoly", "Tetris", "Mario Kart",
            "Fortnite", "Chess", "Checkers", "Chinese Checkers", "Poker", "Catan",
            "Dungeons & Dragons", "Among Us", "Heads or Tails", "Minecraft", "Call of Duty",
            "Paintball", "Bridge", "Quidditch", "Hunger Games Simulator", "Extreme Hide and Seek",
            "Underwater Jenga", "Space Frisbee", "Galactic Treasure Hunt", "Interstellar Tag",
            "Virtual Reality Duck Duck Goose"
        ],
        "linkedin_descriptions": [
            "Expert", "Ninja", "Wizard", "Genius", "Brilliant", "Champion", "Manager",
            "Thought Leader", "Superstar", "Mastermind", "Pioneer", "Senior Technologist",
            "Team Player", "Serial Entrepreneur", "Project Manager", "Visionary", "Evangelist",
            "Disruptor", "Guru", "Rockstar", "Savant", "Maverick", "Game Changer", "Rainmaker",
            "Alchemist", "Trailblazer", "Innovator", "Magician", "Connoisseur", "Maestro"
        ],
        "fake_professions": {
            "levels": [
                "Junior", "Senior", "Lead", "Chief", "Master", "Grandmaster", "Supreme",
                "Ultimate", "Infinite", "Omniscient", "Galactic", "Ethereal", "Transcendent",
                "Interstellar", "Quantum"
            ],
            "actions": [
                "Wrangler", "Herder", "Tamer", "Overthinker", "Whisperer", "Dreamer",
                "Juggler", "Conjurer", "Babbler", "Unfolder", "Collector", "Noodler",
                "Guru", "Manipulator", "Architect", "Sorcerer", "Maestro", "Illusionist",
                "Bender", "Enchanter", "Shapeshifter", "Time Weaver", "Reality Hacker",
                "Dimension Traveler", "Chaos Coordinator"
            ],
            "fields": [
                "Quantum Unicorns", "Interdimensional Pizza Delivery", "Digital Beekeeping",
                "AI-Powered Origami", "Blockchain for Sandwiches", "Robotic Karaoke",
                "Infinite To-Do Lists", "Cybernetic Bubble Wrapping", "Augmented Reality for Cats",
                "Virtual Cabbage Farming", "Autonomous Spoon Design", "Holographic Llama Shows",
                "Time Travel Consultancy", "Parallel Universe Navigation",
                "Emotional Support Chatbots", "Synthetic Coffee Brewing",
                "Alien Communication Protocols", "Esports for Snails",
                "Teleportation Error Debugging", "Dream Sequence Editing",
                "Gravity Defiance Engineering", "Mood Ring Optimization", "Photon Painting",
                "Asteroid Mining Planning", "Teleportation Culinary Arts"
            ]
        },
        "weird_benefits": [
            "Unlimited beanbag chairs", "Weekly underwater basket weaving lessons",
            "Personalized dinosaur name tags", "Free hoverboard parking",
            "A company llama for every employee", "Access to the office's secret slide",
            "Quarterly dragon taming workshops", "Complimentary time travel lessons",
            "A lifetime supply of mismatched socks", "Customizable office air fresheners",
            "Unlimited glitter for all presentations", "Mandatory nap battles in the employee nap pods",
            "Weekly meetings with our in-house fortune teller",
            "Subscription to the company's exclusive 'Socks and Cereal' box",
            "Free teleportation tokens for local travel", "24/7 access to the company bouncy castle",
            "Annual unicorn ride to work day", "In-office cloud watching sessions",
            "Free invisibility cloaks on Fridays", "All-you-can-eat dessert bar with imaginary desserts",
            "Complimentary usage of our zero-gravity room",
            "Personal robot assistant that tells jokes",
            "A library of infinite wisdom (contents may be imaginary)",
            "Access to our secret volcano lair", "Company-sponsored trips to Atlantis"
        ],
        "company_names": {
            "first_word": [
                "Block", "Cyber", "Iron", "Arc", "Vision", "Labs", "Quantum", "Fusion",
                "Platform", "Dynamic", "Star", "Tech", "Pro", "Innovative", "Clarity",
                "Galactic", "Eternal", "Mythic", "Nebula", "Zenith", "Cosmic", "Phoenix",
                "Nimbus", "Echo", "Aurora", "Infinity", "Nova", "Obsidian", "Radiant",
                "Spectral"
            ],
            "second_word": [
                "Dog", "Cat", "Bagel", "Origami", "Dragon", "Sunflower", "Lemon",
                "Lighthouse", "Spaghetti", "Chocolate", "Pearl", "Proton", "Rainbow",
                "Star", "Galaxy", "Whisper", "Echo", "Enigma", "Paradox", "Whimsy",
                "Epiphany", "Serendipity", "Zen", "Eclipse", "Mirage", "Vortex", "Realm",
                "Odyssey", "Spectrum", "Myth"
            ]
        },
        "office_features": [
            "our floating office", "the submarine meeting room", "the treehouse workspace",
            "our cloud-based cafeteria", "the office labyrinth", "the upside-down relaxation room",
            "our secret volcano lair", "the spaceship conference hall",
            "our teleportation-enabled workstations"
        ],
        "mascots": ["unicorn", "dragon", "phoenix", "griffin", "mermaid", "centaur"]
    },
    'he': {
        "names": ["אורן", "דנה", "יוסי", "טל", "נועה", "אלכס", "ירדן", "תמר", "סאם", "קייסי"],
        "social_networks": [
            "פייסבוק", "טוויטר", "אינסטגרם", "לינקדאין", "טיקטוק", "סנאפצ׳ט",
            "פינטרסט", "רדיט", "טלגרם", "דיסקורד", "מייספייס", "פרינדסטר",
            "ניאופטס", "מועדון הפינגווינים", "הרשת הטלפתית", "פורומים אסטרליים",
            "הזירה הרב-ממדית", "רשתות טלפתיות", "מציאות וירטואלית", "אינסטגרם של חדי-קרן"
        ],
        "games": [
            "פיפא", "חדר בריחה", "אבן, נייר ומספריים", "מונופול", "טטריס",
            "מריו קארט", "פורטנייט", "שחמט", "דמקה", "דמקה סינית", "פוקר",
            "קטאן", "מבוכים ודרקונים", "Among Us", "זוג או פרד", "מיינקראפט",
            "Call of Duty", "פיינטבול", "ברידג׳", "קווידיץ'", "סימולטור משחקי הרעב",
            "מחבואים אקסטרים", "ג'נגה תת-מימית", "פריזבי חללי", "ציד אוצרות גלקטי",
            "תפוס ת'דגל בין-כוכבי"
        ],
        "linkedin_descriptions": [
            "תותח", "נינג׳ה", "אשף", "גאון", "מבריק", "אלוף", "מנהל",
            "מוביל דעה", "סופרסטאר", "מומחה-על", "חלוץ", "טכנולוג בכיר",
            "שחקן צוות מוביל", "יזם סדרתי", "מנהל פרויקטים בכיר", "חזון",
            "אוונגליסט", "משבש", "גורו", "רוקסטאר", "סוואנט", "מאבריק",
            "משנה משחק", "אלכימאי", "פורץ דרך", "חדשן", "קוסם", "אנין טעם",
            "מאסטרו"
        ],
        "fake_professions": {
            "levels": [
                "ג׳וניור", "סיניור", "ליד", "צ'יף", "מאסטר", "גרנדמאסטר",
                "סופרים", "אולטימטיבי", "אינסופי", "כל-יודע", "גלקטי",
                "אתרי", "טרנסצנדנטלי", "בין-כוכבי", "קוונטי"
            ],
            "actions": [
                "מאלף", "רועה", "מכוון", "מחשבן יתר על המידה", "לוחש", "חולם",
                "להטוטן", "מכשף", "פטפטן", "מפרש", "אספן", "נודלר", "גורו",
                "מניפולטור", "ארכיטקט", "קוסם", "מאסטרו", "אשליין", "מכופף",
                "מכשף", "משנה צורה", "אורג זמן", "האקר מציאות", "נוסע בין ממדים",
                "מתאם כאוס"
            ],
            "fields": [
                "חדי-קרן קוונטיים", "משלוח פיצה בין-ממדי", "דבוראות דיגיטלית",
                "אוריגמי מבוסס AI", "בלוקצ'יין לסנדוויצ'ים", "קריוקי רובוטי",
                "רשימות מטלות אינסופיות", "עטיפת בועות סייברנטית",
                "מציאות מוגברת לחתולים", "חקלאות כרוב וירטואלית",
                "עיצוב כפיות אוטונומי", "מופעי לאמה הולוגרפיים", "ייעוץ נסיעות בזמן",
                "ניווט יקומים מקבילים", "צ'טבוטים לתמיכה רגשית",
                "בישול קפה סינתטי", "פרוטוקולי תקשורת חייזריים", "ספורט אלקטרוני לחלזונות",
                "ניפוי באגים בטלפורטציה", "עריכת רצפי חלומות", "הנדסת התרסה לכבידה",
                "אופטימיזציית טבעות מצב רוח", "ציור פוטונים", "תכנון כריית אסטרואידים",
                "אמנות קולינרית בטלפורטציה"
            ]
        },
        "weird_benefits": [
            "כיסאות פוף ללא הגבלה", "שיעורי קליעת סלים תת-מימית שבועיים",
            "תגי שם אישיים בצורת דינוזאורים", "חניה חופשית לרחפות", "לאמה חברה לכל עובד",
            "גישה למגלשה הסודית של המשרד", "סדנאות אילוף דרקונים רבעוניות",
            "שיעורי נסיעה בזמן בחינם", "אספקה לכל החיים של גרביים לא תואמים",
            "רענני אוויר מותאמים אישית למשרד", "ניצוצות ללא הגבלה לכל המצגות",
            "קרבות תנומה חובה בקפסולות שינה", "פגישות שבועיות עם מגדת עתידות במשרד",
            "מנוי לקופסת 'גרביים ודגני בוקר' הבלעדית שלנו", "אסימוני טלפורטציה חופשיים לנסיעות מקומיות",
            "גישה 24/7 לטירת הקפיצים של החברה", "יום רכיבה על חד-קרן שנתי לעבודה",
            "מפגשי צפייה בעננים במשרד", "גלימות היעלמות חופשיות בימי שישי",
            "בר קינוחים ללא הגבלה עם קינוחים דמיוניים", "שימוש חופשי בחדר האפס כבידה שלנו",
            "עוזר רובוט אישי שמספר בדיחות", "ספרייה של חוכמה אינסופית (התוכן עשוי להיות דמיוני)",
            "גישה למאורת הר הגעש הסודית שלנו", "טיולים ממומנים לאטלנטיס",
            "השתתפות במסעות ציד אוצרות בין-גלקטיים"
        ],
        "company_names": {
            "first_word": [
                "בלוק", "סייבר", "איירון", "ארק", "ויז׳ן", "לאבס", "קוונטום", "פיוז׳ן",
                "פלטפורמה", "דיינמיק", "סטאר", "טק", "פרו", "אינובייטיב", "קלאריטי",
                "גלקטיק", "אתרנל", "מית׳יק", "נבולה", "זניט", "קוסמיק", "פניקס", "נימבוס",
                "אקו", "אורורה", "אינסופיות", "נובה", "אובסידיאן", "רדייינט", "ספקטראל"
            ],
            "second_word": [
                "כלב", "חתול", "בייגל", "אורגמי", "דרקון", "חמנייה", "לימון", "מגדלור",
                "ספגטי", "שוקולד", "פנינה", "פרוטון", "קשת", "כוכב", "גלקסיה", "לחישה",
                "הד", "אניגמה", "פרדוקס", "קפריז", "תובנה", "סרנדיפיטי", "זן", "ליקוי",
                "מיראז'", "וורטקס", "ממלכה", "אודיסיאה", "ספקטרום", "מיתוס"
            ]
        },
        "office_features": [
            "המשרד הצף שלנו", "חדר הישיבות הצוללת", "מרחב העבודה על העץ",
            "הקפיטריה בענן", "המבוך המשרדי", "חדר ההרפיה ההפוך", "מאורת הר הגעש הסודית שלנו",
            "אולם הכנסים החללי", "תחנות העבודה המאפשרות טלפורטציה"
        ],
        "mascots": ["חד-קרן", "דרקון", "פניקס", "גריפין", "בת-ים", "קנטאור"]
    }
}

# HTML templates
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Humorous Email Generator</title>
</head>
<body>
    <h1>Humorous Email Generator</h1>
    <form method="post">
        <label for="language">Select Language:</label>
        <select name="language">
            <option value="en">English</option>
            <option value="he">עברית</option>
        </select><br><br>
        <label for="name">Enter Your Name:</label>
        <input type="text" name="name" required><br><br>
        <input type="submit" value="Generate Email">
    </form>
</body>
</html>
'''

email_template = '''
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>Generated Email</title>
</head>
<body>
    {{ email_content }}
    <br><br>
    <a href="/">Back</a>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        language = request.form['language']
        user_name = request.form['name']
        email_content = generate_email(language, user_name)
        return render_template_string(email_template, email_content=email_content, lang=language)
    return render_template_string(form_template)

def generate_email(lang, name):
    lang_data = data[lang]
    first_name = name if name else random.choice(lang_data["names"])
    company_name = f"{random.choice(lang_data['company_names']['first_word'])} {random.choice(lang_data['company_names']['second_word'])}"
    job_title = f"{random.choice(lang_data['fake_professions']['levels'])} {random.choice(lang_data['fake_professions']['actions'])} {'of' if lang == 'en' else 'ב-'}{random.choice(lang_data['fake_professions']['fields'])}"
    linkedin_description = random.choice(lang_data["linkedin_descriptions"])
    benefit = random.choice(lang_data["weird_benefits"])
    benefit2 = random.choice([b for b in lang_data["weird_benefits"] if b != benefit])
    benefit3 = random.choice([b for b in lang_data["weird_benefits"] if b not in [benefit, benefit2]])
    favorite_game = random.choice(lang_data["games"])
    social_focus = random.choice(lang_data["social_networks"])
    project_field = random.choice(lang_data['fake_professions']['fields'])
    office_feature = random.choice(lang_data["office_features"])
    mascot = random.choice(lang_data["mascots"])

    if lang == 'en':
        email_content = f"""
    Hi {first_name},

    We couldn't be more thrilled that you've opened this email—it's like the cosmos aligned just for this moment!

    We're embarking on an epic quest at **{company_name}** to find a **{job_title}**. Yes, you read that correctly—it's as extraordinary as it sounds.

    We're assembling a league of {linkedin_description}s who can seamlessly blend cutting-edge development with an unparalleled passion for **{favorite_game}**. Our last project involved **{project_field}**, and let's just say, it was a dimension-defying experience (we may have bent a few laws of physics).

    But let's delve into what truly sets us apart—our perks:

    - **{benefit}**
    - **{benefit2}**
    - **{benefit3}**
    - And, of course, unlimited access to **{office_feature}**

    Our company culture is as vibrant as a supernova. You'll often find us on **{social_focus}**, debating the strategies of **{favorite_game}** or sharing the latest memes from alternate realities. We believe that staying connected across all planes of existence fosters innovation.

    Oh, did we mention our mascot is a {mascot}? It occasionally roams the halls offering wisdom (or just looking for snacks).

    If you're ready to catapult your career into realms unexplored and join a team where the only limit is the multiverse itself, let's get in touch. We promise an adventure that's out of this world (literally).

    Looking forward to bending reality together!

    Best cosmic wishes,

    The {company_name} Team

    P.S. Don't worry about the time difference—we operate across all timelines.
        """
    else:
        email_content = f"""
    היי {first_name},

    אנחנו לא יכולים להיות יותר נרגשים שפתחת את המייל הזה—זה כמו שהקוסמוס התיישר רק עבור הרגע הזה!

    אנחנו יוצאים למסע אפי ב-**{company_name}** ומחפשים **{job_title}**. כן, קראת נכון—זה מרגש כמו שזה נשמע.

    אנחנו מרכיבים קבוצה של {linkedin_description}ים שיכולים לשלב באופן חלקי בין מיומנויות פיתוח מתקדמות ותשוקה בלתי רגילה ל-**{favorite_game}**. הפרויקט האחרון שלנו כלל **{project_field}**, ונאמר שזו הייתה חוויה ששברה ממדים (אולי כופפנו כמה חוקי פיזיקה).

    אבל בוא נדבר על מה שבאמת מייחד אותנו—ההטבות שלנו:

    - **{benefit}**
    - **{benefit2}**
    - **{benefit3}**
    - וכמובן, גישה בלתי מוגבלת ל-**{office_feature}**

    התרבות הארגונית שלנו תוססת כמו סופרנובה. לעיתים קרובות תמצאו אותנו ב-**{social_focus}**, דנים באסטרטגיות של **{favorite_game}** או משתפים ממים מעולמות מקבילים. אנחנו מאמינים שתקשורת בכל הממדים מעודדת חדשנות.

    אה, הזכרנו שהקמע שלנו הוא {mascot}? הוא מדי פעם מסתובב במסדרונות ומציע חוכמה (או סתם מחפש חטיפים).

    אם אתה מוכן להטיס את הקריירה שלך למקומות לא מוכרים ולהצטרף לצוות שבו הגבול היחיד הוא היקום עצמו, בוא נדבר. אנחנו מבטיחים הרפתקה שהיא מעבר לעולם הזה (תרתי משמע).

    מצפים לכופף את המציאות יחד!

    מאחלים ברכות קוסמיות,

    צוות {company_name}

    נ.ב. אל תדאג לגבי הפרשי הזמנים—אנחנו פועלים בכל צירי הזמן.
        """
    return email_content

if __name__ == '__main__':
    app.run(debug=True)
