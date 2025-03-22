from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Squishmallow cuddle compliments
compliments = [
    "Stink, you’re my Squishmallow snuggle buddy!",
    "Queen Poopy, you’re the fluffiest Squishmallow queen!",
    "Dooper, you’re softer than a Squishmallow cloud!",
    "Fine lil shit, you’re the cutest Squishmallow in my arms!",
    "Stink, you’re a Squishmallow star, cuddly near and far!",
    "Queen Poopy, you’re piled high with Squishmallow love!",
    "Dooper, you’re my Squishmallow dream, plushy supreme!",
    "Fine lil shit, you’re the Squishmallow vibe I can’t resist!",
    "Stink, you’re cuddlier than a Squishmallow rainbow!",
    "RNM + BTP, the ultimate Squishmallow cuddle crew!"
]

# Squishmallow shoutouts
shoutouts = [
    "Stink’s the Squishmallow MVP—most valuable plush!",
    "Queen Poopy rules the Squishmallow pile!",
    "Dooper’s got that Squishmallow swagger!",
    "Fine lil shit owns the Squishmallow cuddle game!",
    "RNM + BTP, the Squishmallow throne is ours!"
]

@app.route('/', methods=['GET', 'POST'])
def squish_corner():
    compliment = random.choice(compliments) if request.method == 'POST' and 'compliment' in request.form else "Grab a Squishmallow cuddle!"
    shoutout = random.choice(shoutouts) if request.method == 'POST' and 'shoutout' in request.form else ""
    promise = "RNM + BTP, cuddliest duo in Squishmallow land!" if request.method == 'POST' and 'promise' in request.form else ""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Squishmallow Cuddle Corner</title>
        <style>
            body {{
                background: linear-gradient(45deg, #ffb6c1, #87cefa, #98fb98, #dda0dd);
                text-align: center;
                font-family: 'Comic Sans MS', cursive;
                color: #ff3366;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #ff6699;
                text-shadow: 2px 2px #fffacd;
                margin-bottom: 20px;
            }}
            .squish-mascot {{
                font-size: 80px;
                color: #ff3366;
                background: #fffacd;
                border-radius: 50%;
                width: 120px;
                height: 120px;
                line-height: 120px;
                margin: 0 auto 20px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                animation: bounce 1.5s infinite;
            }}
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                40% {{ transform: translateY(-20px); }}
                60% {{ transform: translateY(-10px); }}
            }}
            .squish-button {{
                background-color: #ff99cc;
                color: white;
                border: none;
                padding: 15px;
                font-size: 18px;
                font-family: 'Comic Sans MS', cursive;
                border-radius: 50%;
                width: 150px;
                height: 150px;
                display: block;
                margin: 15px auto;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }}
            .squish-button:hover {{
                background-color: #ff66b3;
                transform: scale(1.05);
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }}
            .squish-button:active {{
                transform: scale(0.95);
                box-shadow: 0 3px 10px rgba(0,0,0,0.2);
            }}
            p {{
                background: rgba(255, 255, 255, 0.7);
                padding: 10px;
                border-radius: 15px;
                margin: 10px auto;
                max-width: 300px;
            }}
        </style>
    </head>
    <body>
        <h1>Squishmallow Cuddle Corner</h1>
        <div class="squish-mascot">🧸</div>
        <p>{compliment}</p>
        <form method="post">
            <button type="submit" name="compliment" class="squish-button">Cuddle Compliment</button>
        </form>
        <p>{shoutout}</p>
        <form method="post">
            <button type="submit" name="shoutout" class="squish-button">Squishy Shoutout</button>
        </form>
        <p>{promise}</p>
        <form method="post">
            <button type="submit" name="promise" class="squish-button">Plushy Promise</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)