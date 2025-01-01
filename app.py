from flask import Flask, render_template, request, redirect
from videoscrape import Videoscraper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        series = request.form.get("series")
        episode = request.form.get("episode")
        season = request.form.get("season")

        scraper = Videoscraper()

        # Parse to get the download link
        downlink = scraper.parse(series=series,episode=episode,season=season)

        return redirect(downlink)
        
    return render_template("app.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
