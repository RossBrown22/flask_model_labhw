from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def index():
    return render_template("index.html", title="Orders", orders=orders)

@app.route('/<index>')
def order_details(index):
    order_index = int(index)
    return render_template("order.html", title="Order", order=orders[order_index])