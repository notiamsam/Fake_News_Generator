from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Categories
categories = {
    "Politics": {
        "subjects": ["Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Nirmala Sitharaman", "UP Police", "Parliament House"],
        "actions": ["banned", "declared", "arrested for", "promised free", "blamed Pakistan for", "announced free distribution of"],
        "places_or_things": ["Delhi Metro", "Ayodhya Ram Mandir", "Parliament House", "India Gate", "Red Fort"]
    },
    "Bollywood": {
        "subjects": ["Shah Rukh Khan", "Alia Bhatt", "Amitabh Bachchan", "Priyanka Chopra", "Kangana Ranaut", "Kapil Sharma"],
        "actions": ["secretly married", "celebrated", "went viral for", "introduced", "shocked everyone with"],
        "places_or_things": ["Bollywood award show", "Bigg Boss house", "Goa beach shack", "Taj Mahal", "Swiggy delivery"]
    },
    "Sports": {
        "subjects": ["Virat Kohli", "MS Dhoni", "Sachin Tendulkar", "IPL fans", "BCCI"],
        "actions": ["launched", "quit over", "criticized", "filed a case against", "celebrated"],
        "places_or_things": ["IPL final", "Mumbai local train", "Ola auto", "Indian Railways pantry", "Jio 5G tower"]
    },
    "Tech": {
        "subjects": ["ISRO", "Delhi University students", "Baba Ramdev", "Mumbai locals"],
        "actions": ["introduced", "started a campaign for", "tried to sell", "tweeted about", "is planning to move to"],
        "places_or_things": ["Chandrayaan-3 rocket", "WhatsApp University", "Jio 5G tower", "Manali snowstorm", "Swiggy delivery"]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    category = request.form.get("category", "Politics")  # Default category
    data = categories[category]

    subject = random.choice(data["subjects"])
    action = random.choice(data["actions"])
    place_or_thing = random.choice(data["places_or_things"])
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

    return render_template("index.html", headline=headline, categories=categories.keys(), selected=category)

if __name__ == "__main__":
    app.run(debug=True)
