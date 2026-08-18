from flask import Flask, render_template

app = Flask(__name__)


NAV_LINKS = [
    {"label": "Home"},
    {"label": "Videos"},
    {"label": "Careers"},
    {
        "label": "About",
        "children": [
            "About", "Education", "Employment", "Talks",
            "Awards", "Media", "Publications", "Wall of Thanks",
        ],
    },
    {"label": "Snatoms"},
    {"label": "VeMail"},
    {"label": "Elements of Truth"},
    {"label": "Contact"},
]

FEATURED_VIDEOS = [
    {
        "tag": "ANNOUNCEMENT",
        "accent": "teal",
        "title": "The Future of Veritasium",
        "date": "Dec 25, 2025",
        "excerpt": "Am I retiring?",
    },
    {
        "tag": "PHYSICS",
        "accent": "orange",
        "title": "There Is Something Faster Than Light",
        "date": "Dec 25, 2025",
        "excerpt": "How an argument between Einstein and Bohr changed quantum mechanics forever.",
    },
    {
        "tag": "HISTORY",
        "accent": "indigo",
        "title": "The Man Who Accidentally Discovered Antimatter",
        "date": "Dec 25, 2025",
        "excerpt": "How Paul Dirac uncovered the anti-universe.",
    },
    {
        "tag": "MATH",
        "accent": "amber",
        "title": "You've (Likely) Been Playing The Game of Life Wrong",
        "date": "Dec 25, 2025",
        "excerpt": "The world is not Normal.",
    },
    {
        "tag": "ENGINEERING",
        "accent": "teal",
        "title": "Why don't jet engines melt?",
        "date": "Dec 25, 2025",
        "excerpt": "How does a jet engine not melt?",
    },
    {
        "tag": "PSYCHOLOGY",
        "accent": "orange",
        "title": "Why People Are So Confident When They're Wrong",
        "date": "Dec 25, 2025",
        "excerpt": "The problem with overconfidence.",
    },
]

SOCIAL_LINKS = ["Instagram", "Facebook", "YouTube", "Twitter / X"]


@app.route("/")
def index():
    return render_template(
        "index.html",
        nav_links=NAV_LINKS,
        featured_videos=FEATURED_VIDEOS,
        social_links=SOCIAL_LINKS,
        year=2026,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
