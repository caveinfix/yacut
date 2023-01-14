from flask import flash, redirect, render_template

from yacut.utils import get_unique_short_id

from . import app, db
from .forms import YacutForm
from .models import URLMap


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash(f"Имя {custom_id} уже занято!")
            return render_template("index.html", form=form)
        new_url = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(new_url)
        db.session.commit()
        return render_template("index.html", form=form, short=custom_id)
    return render_template("index.html", form=form)


@app.route("/<string:custom_id>")
def redirect_view(custom_id):
    url_map = URLMap.query.filter_by(short=custom_id).first_or_404()
    return redirect(url_map.original)
