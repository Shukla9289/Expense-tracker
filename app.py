from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.expensetracker
expenses = db.expenses

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    data = []
    for expense in expenses.find():
        data.append({
            "_id": str(expense["_id"]),
            "name": expense["name"],
            "amount": expense["amount"],
            "category": expense["category"]
        })
    return jsonify(data)

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense_id = expenses.insert_one({
        "name": data['name'],
        "amount": data['amount'],
        "category": data['category']
    }).inserted_id
    return jsonify({"_id": str(expense_id)})

@app.route('/api/expenses/<id>', methods=['DELETE'])
def delete_expense(id):
    expenses.delete_one({"_id": ObjectId(id)})
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)