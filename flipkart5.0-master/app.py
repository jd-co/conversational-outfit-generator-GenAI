from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
import jwt 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flipkart.db'  # Change this to your database URI
CORS(app, origins='*')
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    keywords = db.Column(db.JSON())     # Assuming cart is a JSON field


# hello=[{'id': 1,
#  'category': 'saree',
#  'url': 'https://rukminim2.flixcart.com/image/612/612/xif0q/sari/4/j/s/free-ls-pinkberry-light-benaifer-fashion-unstitched-original-imagc97syewyypqw.jpeg?q=70',
#  'brand': 'Divastri',
#  'name': 'Woven Kanjivaram Pure Silk, Art Silk Saree',
#  'price': '₹599',
#  'gender': 'female',
#  'Occasion': 'Casual, Party & Festive, Wedding, Wedding & Festive',
#  'Display Type': 'NULL',
#  'Strap Color': 'NULL',
#  'Type': 'Kanjivaram',
#  'Color': 'NULL',
#  'Outer material': 'NULL',
#  'Type for Flats': 'NULL',
#  'Base Material': 'NULL',
#  'Gemstone': 'NULL',
#  'Diameter': 'NULL',
#  'Bangle Size': 'NULL',
#  'Collection': 'NULL',
#  'Design': 'NULL',
#  'Pattern': 'Woven',
#  'Fabric': 'Pure Silk, Art Silk'
#  },
# {'id': 2,
#  'category': 'saree',
#  'url': 'https://rukminim2.flixcart.com/image/612/612/xif0q/sari/f/w/t/free-dt-paithani-art-silk-designer-bollywood-fashion-style-original-imagq779ed3grrhg.jpeg?q=70',
#  'brand': 'Divastri',
#  'name': 'Woven Kanjivaram Pure Silk Saree',
#  'price': '₹649',
#  'gender': 'female',
#  'Occasion': 'Wedding & Festive, Party & Festive, Wedding, Casual',
#  'Display Type': 'NULL',
#  'Strap Color': 'NULL',
#  'Type': 'Kanjivaram',
#  'Color': 'NULL',
#  'Outer material': 'NULL',
#  'Type for Flats': 'NULL',
#  'Base Material': 'NULL',
#  'Gemstone': 'NULL',
#  'Diameter': 'NULL',
#  'Bangle Size': 'NULL',
#  'Collection': 'NULL',
#  'Design': 'NULL',
#  'Pattern': 'Woven',
#  'Fabric': 'Pure Silk'},
# {'id': 3,
#  'category': 'saree',
#  'url': 'https://rukminim2.flixcart.com/image/612/612/l1pc3gw0/sari/k/g/q/free-bsp1625-banaras-silk-palace-unstitched-original-imagd7kkk39qhsrw.jpeg?q=70',
#  'brand': 'Shradhha Fashion',
#  'name': 'Embroidered Banarasi Satin Saree',
#  'price': '₹565',
#  'gender': 'female',
#  'Occasion': 'Party & Festive, Wedding',
#  'Display Type': 'NULL',
#  'Strap Color': 'NULL',
#  'Type': 'Banarasi',
#  'Color': 'NULL',
#  'Outer material': 'NULL',
#  'Type for Flats': 'NULL',
#  'Base Material': 'NULL',
#  'Gemstone': 'NULL',
#  'Diameter': 'NULL',
#  'Bangle Size': 'NULL',
#  'Collection': 'NULL',
#  'Design': 'NULL',
#  'Pattern': 'Embroidered',
#  'Fabric': 'Satin'}]

@app.route('/signup', methods=['POST'])  # signup API call using method POST
def signup():
    hello=[{'id': 1,
 'category': 'saree',
 'url': 'https://rukminim2.flixcart.com/image/612/612/xif0q/sari/4/j/s/free-ls-pinkberry-light-benaifer-fashion-unstitched-original-imagc97syewyypqw.jpeg?q=70',
 'brand': 'Divastri',
 'name': 'Woven Kanjivaram Pure Silk, Art Silk Saree',
 'price': '₹599',
 'gender': 'female',
 'Occasion': 'Casual, Party & Festive, Wedding, Wedding & Festive',
 'Display Type': 'NULL',
 'Strap Color': 'NULL',
 'Type': 'Kanjivaram',
 'Color': 'NULL',
 'Outer material': 'NULL',
 'Type for Flats': 'NULL',
 'Base Material': 'NULL',
 'Gemstone': 'NULL',
 'Diameter': 'NULL',
 'Bangle Size': 'NULL',
 'Collection': 'NULL',
 'Design': 'NULL',
 'Pattern': 'Woven',
 'Fabric': 'Pure Silk, Art Silk'
 },
{'id': 2,
 'category': 'saree',
 'url': 'https://rukminim2.flixcart.com/image/612/612/xif0q/sari/f/w/t/free-dt-paithani-art-silk-designer-bollywood-fashion-style-original-imagq779ed3grrhg.jpeg?q=70',
 'brand': 'Divastri',
 'name': 'Woven Kanjivaram Pure Silk Saree',
 'price': '₹649',
 'gender': 'female',
 'Occasion': 'Wedding & Festive, Party & Festive, Wedding, Casual',
 'Display Type': 'NULL',
 'Strap Color': 'NULL',
 'Type': 'Kanjivaram',
 'Color': 'NULL',
 'Outer material': 'NULL',
 'Type for Flats': 'NULL',
 'Base Material': 'NULL',
 'Gemstone': 'NULL',
 'Diameter': 'NULL',
 'Bangle Size': 'NULL',
 'Collection': 'NULL',
 'Design': 'NULL',
 'Pattern': 'Woven',
 'Fabric': 'Pure Silk'},
{'id': 3,
 'category': 'saree',
 'url': 'https://rukminim2.flixcart.com/image/612/612/l1pc3gw0/sari/k/g/q/free-bsp1625-banaras-silk-palace-unstitched-original-imagd7kkk39qhsrw.jpeg?q=70',
 'brand': 'Shradhha Fashion',
 'name': 'Embroidered Banarasi Satin Saree',
 'price': '₹565',
 'gender': 'female',
 'Occasion': 'Party & Festive, Wedding',
 'Display Type': 'NULL',
 'Strap Color': 'NULL',
 'Type': 'Banarasi',
 'Color': 'NULL',
 'Outer material': 'NULL',
 'Type for Flats': 'NULL',
 'Base Material': 'NULL',
 'Gemstone': 'NULL',
 'Diameter': 'NULL',
 'Bangle Size': 'NULL',
 'Collection': 'NULL',
 'Design': 'NULL',
 'Pattern': 'Embroidered',
 'Fabric': 'Satin'}]
    final_dict = {}
    for i in range(len(hello)):
        final_dict[i] = hello[i]
    print(type(final_dict))
    data = request.get_json()  # Data object consists of username, password, role, name, email
    username = data['username']
    password = data['password']
    age = data['age']
    fullname = data['fullName']
    email = data['email']
    gender = data['gender']
    if User.query.filter_by(username=username).first():
        return jsonify({'flash_message': 'Username already exists'}), 200  
    
    user = User(name=fullname, username=username, password=password, age=age, gender=gender, email=email, keywords=json.dumps(final_dict))   
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201  # user created and response sent to frontend


@app.route('/logger', methods=['POST']) #login api for logging and based on role user admin mangager
def logger():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(username,password) #if a manager who is not approved by admin tries to login sends flash message
    user = User.query.filter_by(username=username, password=password).first()
    # user = User.query.filter_by(username=username, password=password,role=role,status='approved').first()
    print(user)
    if user:
        expiration = datetime.utcnow() + timedelta(minutes=30)
        expiration_timestamp = int(expiration.timestamp())

        # Generate JWT token
        token_payload = {
            'user': username,
            'exp': expiration_timestamp
        }
        token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'message':"login succesfully" ,"token":token}),201
    else:
        return jsonify({'message':"Credentials Mismatch" ,}),202
            
@app.route("/getUserDetails/<string:name>",methods=["GET"]) 
def getUserDetails(name):
    # data = request.get_json()
    # username=data['username']
    userDetails  = User.query.filter_by(username=name).first()
    hello=userDetails.keywords
    hello = json.loads(hello)
    anisha=[]
    for values in hello.values():
        anisha.append(values)
    f_details = {"fullName":userDetails.name,"gender":userDetails.gender,"age":userDetails.age ,"keywords":anisha}
    return jsonify({'details':f_details}) 



@app.route("/getKeywords/<string:name>",methods=["GET"]) 
def getKeywords(name):
    # data = request.get_json()
    # username=data['username']
    userDetails  = User.query.filter_by(username=name).first()
    hello=userDetails.keywords
    hello = json.loads(hello)
    anisha=[]
    for values in hello.values():
        anisha.append(values)
    # print(anisha)
    # print(type(anisha))
        
    return jsonify({'keywords':anisha}) 
 
 

            
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        app.run(debug=True,port=2000)
