from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
import jwt
import openai
import pandas as pd
from openai.embeddings_utils import get_embedding,cosine_similarity
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity
import time
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///flipkart.db"  # Change this to your database URI
CORS(app, origins="http://localhost:8080", supports_credentials=True)
app.config["SECRET_KEY"] = "your_secret_key_here"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    keywords = db.Column(db.JSON())  # Assuming cart is a JSON field


@app.route("/signup", methods=["POST"])  # signup API call using method POST
def signup():
    hello = [
        {
            "id": 1,
            "category": "saree",
            "url": "https://rukminim2.flixcart.com/image/612/612/xif0q/sari/4/j/s/free-ls-pinkberry-light-benaifer-fashion-unstitched-original-imagc97syewyypqw.jpeg?q=70",
            "brand": "Divastri",
            "name": "Woven Kanjivaram Pure Silk, Art Silk Saree",
            "price": "₹599",
            "gender": "female",
            "Occasion": "Casual, Party & Festive, Wedding, Wedding & Festive",
            "Display Type": "NULL",
            "Strap Color": "NULL",
            "Type": "Kanjivaram",
            "Color": "NULL",
            "Outer material": "NULL",
            "Type for Flats": "NULL",
            "Base Material": "NULL",
            "Gemstone": "NULL",
            "Diameter": "NULL",
            "Bangle Size": "NULL",
            "Collection": "NULL",
            "Design": "NULL",
            "Pattern": "Woven",
            "Fabric": "Pure Silk, Art Silk",
        },
        {
            "id": 2,
            "category": "saree",
            "url": "https://rukminim2.flixcart.com/image/612/612/xif0q/sari/f/w/t/free-dt-paithani-art-silk-designer-bollywood-fashion-style-original-imagq779ed3grrhg.jpeg?q=70",
            "brand": "Divastri",
            "name": "Woven Kanjivaram Pure Silk Saree",
            "price": "₹649",
            "gender": "female",
            "Occasion": "Wedding & Festive, Party & Festive, Wedding, Casual",
            "Display Type": "NULL",
            "Strap Color": "NULL",
            "Type": "Kanjivaram",
            "Color": "NULL",
            "Outer material": "NULL",
            "Type for Flats": "NULL",
            "Base Material": "NULL",
            "Gemstone": "NULL",
            "Diameter": "NULL",
            "Bangle Size": "NULL",
            "Collection": "NULL",
            "Design": "NULL",
            "Pattern": "Woven",
            "Fabric": "Pure Silk",
        },
        {
            "id": 3,
            "category": "saree",
            "url": "https://rukminim2.flixcart.com/image/612/612/l1pc3gw0/sari/k/g/q/free-bsp1625-banaras-silk-palace-unstitched-original-imagd7kkk39qhsrw.jpeg?q=70",
            "brand": "Shradhha Fashion",
            "name": "Embroidered Banarasi Satin Saree",
            "price": "₹565",
            "gender": "female",
            "Occasion": "Party & Festive, Wedding",
            "Display Type": "NULL",
            "Strap Color": "NULL",
            "Type": "Banarasi",
            "Color": "NULL",
            "Outer material": "NULL",
            "Type for Flats": "NULL",
            "Base Material": "NULL",
            "Gemstone": "NULL",
            "Diameter": "NULL",
            "Bangle Size": "NULL",
            "Collection": "NULL",
            "Design": "NULL",
            "Pattern": "Embroidered",
            "Fabric": "Satin",
        },
    ]
    final_dict = {}
    for i in range(len(hello)):
        final_dict[i] = hello[i]
    print(type(final_dict))
    data = (
        request.get_json()
    )  # Data object consists of username, password, role, name, email
    username = data["username"]
    password = data["password"]
    age = data["age"]
    fullname = data["fullName"]
    email = data["email"]
    gender = data["gender"]
    if User.query.filter_by(username=username).first():
        return jsonify({"flash_message": "Username already exists"}), 200

    user = User(
        name=fullname,
        username=username,
        password=password,
        age=age,
        gender=gender,
        email=email,
        keywords=json.dumps(final_dict),
    )
    db.session.add(user)
    db.session.commit()

    return (
        jsonify({"message": "User registered successfully"}),
        201,
    )  # user created and response sent to frontend


@app.route(
    "/logger", methods=["POST"]
)  # login api for logging and based on role user admin mangager
def logger():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    print(
        username, password
    )  # if a manager who is not approved by admin tries to login sends flash message
    user = User.query.filter_by(username=username, password=password).first()
    # user = User.query.filter_by(username=username, password=password,role=role,status='approved').first()
    print(user)
    if user:
        print("hello world")
        expiration = datetime.utcnow() + timedelta(minutes=30)
        expiration_timestamp = int(expiration.timestamp())

        # Generate JWT token
        token_payload = {"user": username, "exp": expiration_timestamp}
        token = jwt.encode(token_payload, app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"message": "login succesfully", "token": token}), 200
    else:
        return (
            jsonify(
                {
                    "message": "Credentials Mismatch",
                }
            ),
            202,
        )


@app.route("/getUserDetails/<string:name>", methods=["GET"])
def getUserDetails(name):
    # data = request.get_json()
    # username=data['username']
    userDetails = User.query.filter_by(username=name).first()
    hello = userDetails.keywords
    hello = json.loads(hello)
    anisha = []
    for values in hello.values():
        anisha.append(values)
    f_details = {
        "fullName": userDetails.name,
        "gender": userDetails.gender,
        "age": userDetails.age,
        "keywords": anisha,
    }
    return jsonify({"details": f_details})


@app.route("/getKeywords/<string:name>", methods=["GET"])
def getKeywords(name):
    # data = request.get_json()
    # username=data['username']
    userDetails = User.query.filter_by(username=name).first()
    hello = userDetails.keywords
    hello = json.loads(hello)
    anisha = []
    for values in hello.values():
        anisha.append(values)
    # print(anisha)
    # print(type(anisha))

    return jsonify({"keywords": anisha})


@app.route("/query", methods=["POST"])
def query():
    api_key ="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"
    openai.api_key = api_key
    data = request.get_json()
    customer_input=data['query']
    print(customer_input)
    customer_order_df=pd.read_csv('./customer_dataset.csv')
    product_data_df=pd.read_csv('./embeddings.csv')
    print(customer_order_df)
    print(product_data_df)
    
    customer_input1="convert the products list into json file"
    response = openai.Embedding.create(
        input=customer_input,
        model="text-embedding-ada-002"
    )
    embeddings_customer_question = response['data'][0]['embedding']
    response = openai.Embedding.create(
    input=customer_input1,
    model="text-embedding-ada-002"
    )
    embeddings_customer_question = response['data'][0]['embedding']



    customer_order_df['search_purchase_history'] = customer_order_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    customer_order_df = customer_order_df.sort_values('search_purchase_history', ascending=False)
    top_3_purchases_df = customer_order_df.head(3)

    product_data_df['search_products'] = product_data_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    product_data_df = product_data_df.sort_values('search_products', ascending=False)
    top_3_products_df = product_data_df.head(40)


    message_objects = []
    message_objects.append({"role":"system", "content":"You're a chatbot helping customers with otfit related questions and helping them with product recommendations full otfit items such as Saree,bangles,jhumka,bangles etc "})
    message_objects1 = []
    message_objects1.append({"role":"system", "content":"You're a chatbot who converts the given list into JSON format"})


    message_objects.append({"role":"user", "content": customer_input})
    message_objects1.append({"role":"user", "content": customer_input1})

    
    prev_purchases = ". ".join([f"{row['combined']}" for index, row in top_3_purchases_df.iterrows()])

    message_objects.append({"role":"user", "content": f"Here're my latest product orders: {prev_purchases}"})
    message_objects.append({"role":"user", "content": f"Please give recomend me one product from each category, the categories are given to you"})
    message_objects.append({"role":"user", "content": f"Please give me a detailed explanation of your recommendations"})
    message_objects.append({"role":"user", "content": "Please be friendly and talk to me like a person, don't just give me a list of recommendations"})



    products_list = []
    for row in top_3_products_df.iterrows():
        brand_dict = {'role': "assistant", "content":  f"{row['id']}, {row['category']},{row['brand']}, {row['name']}, {row['price']},{row['gender']},{row['Occasion']},{row['Display Type']}, {row['Strap Color']}, {row['Type']},{row['Color']}, {row['Outer material']}, {row['Type for Flats']},{row['Base Material']},{row['Gemstone']},{row['Diameter']}, {row['Bangle Size']}, {row['Collection']},{row['Design']},{row['Pattern']},{row['Fabric']},{row['url']}"}
        products_list.append(brand_dict)

    message_objects.append({"role": "assistant", "content": f"I found these  products I would recommend"})
    message_objects1.extend(products_list)
    message_objects1.extend


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_objects
    )
    query_text=completion.choices[0].message['content']


    completion1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_objects1
    )
    query_products=completion1.choices[0].message['content']['products']
   

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(debug=True, port=2000)
