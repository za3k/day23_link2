#!/bin/python3
import flask, flask_login
from flask import url_for, request, render_template, redirect
from flask_login import current_user
import collections, json, queue, random
from datetime import datetime
from base import app,load_info,ajax,DBDict,DBList,random_id,hash_id,full_url_for

# -- Info for every Hack-A-Day project --
load_info({
    "project_name": "Hack-A-Link 2",
    "source_url": "https://github.com/za3k/day23_link2",
    "subdir": "/hackaday/link2",
    "description": "is a public list of links anyone can contribute to",
    "login": False,
    "fullscreen": False,
})

# -- Routes specific to this Hack-A-Day project --

links = DBList("link")
link_info = DBDict("link_info")
@app.route("/")
def index():
    return render_template('index.html', links=reversed(links), link_info=link_info)

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    else:
        link = request.form.get("link")
        if link.startswith("http") and link not in links: # 'in' is slow. Hack!
            links.append(link)
            link_info[link] = {
                "created": datetime.now(),
            }
        info = link_info[link]
        info["updated"] = datetime.now()
        link_info[link] = info
        return redirect(url_for("index"))
