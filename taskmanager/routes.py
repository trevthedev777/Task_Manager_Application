from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # order_by method shows all records on the database stored in the Category table  ## noqa
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories=categories displayes all the information to our users
    # the first categories is the var name we can use within the HTML template
    # the second categories which is a list is the variable defined within our function  # noqa
    return render_template("categories.html", categories=categories)


# include methods as we are submitting a form to the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# the path will select the selected category to update
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
# we need to wire the category_id to identify which one we want to change
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)