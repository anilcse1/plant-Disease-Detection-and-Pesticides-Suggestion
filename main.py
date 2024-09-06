import os
from flask import Flask,render_template,redirect,request
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import cv2


app = Flask(__name__)

model = pickle.load(open('models/apple_prediction.pkl', 'rb'))
potatomodel = pickle.load(open('models/potato_prediction.pkl', 'rb'))
tomatomodel = pickle.load(open('models/tomato_prediction.pkl','rb'))
grapemodel = pickle.load(open('models/grape_prediction.pkl','rb'))
cornmodel = pickle.load(open('models/corn_prediction.pkl','rb'))
peachmodel = pickle.load(open('models/peach_prediction.pkl','rb'))
pepperbellmodel = pickle.load(open('models/pepperbell_prediction.pkl','rb'))
strawberrymodel = pickle.load(open('models/strawberry_prediction.pkl','rb'))

@app.route("/" , methods=["GET","POST"])
def home():
	return render_template("home.html",title="Plant Disease Detection")

@app.route("/contactus" , methods=["GET","POST"])
def contactus():
	return render_template("contactus.html",title="Plant Disease Detection")

@app.route("/plantDisease", methods=["GET","POST"])
def plantDisease():
	return render_template("PlantDisease.html",title="Plant Disease Detection")

@app.route("/aboutus", methods=["GET","POST"])
def aboutus():
	return render_template("aboutus.html",title="Plant Disease Detection")

@app.route("/plants",methods=["GET","POST"])
def plants():
	return render_template("plants.html",title="Plant Disease Detection")

@app.route("/tomato",methods=["GET","POST"])
def tomato():
	return render_template("tomato.html",title="Plant Disease Detection")

@app.route("/potato",methods=["GET","POST"])
def potato():
	return render_template("potato.html",title="Plant Disease Detection")

@app.route("/grape",methods=["GET","POST"])
def grape():
	return render_template("grape.html",title="Plant Disease Detection")

@app.route("/corn",methods=["GET","POST"])
def corn():
	return render_template("corn.html",title="Plant Disease Detection")

@app.route("/peach",methods=["GET","POST"])
def peach():
	return render_template("peach.html",title="Plant Disease Detection")

@app.route("/pepperbell",methods=["GET","POST"])
def pepperbell():
	return render_template("pepperbell.html",title="Plant Disease Detection")

@app.route("/strawberry",methods=["GET","POST"])
def strawberry():
	return render_template("strawberry.html",title="Plant Disease Detection")

@app.route("/applepredict",methods=["GET","POST"])
def predict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = model.predict(img1)
		apple = { 0 : 'Apple_scab', 1: 'Apple__Blackrot' , 2 : 'Apple__healthy', 3:'Apple___Cedar_apple_rust'}
		if apple[pred[0]] == 'Apple_scab':
			desc = "captan, lime-sulfur  powdered  wettable sulfur"
			prevention = """ Planting disease resistant varieties is the best way to prevent apple scab. Many varieties of apple and crabapple trees are resistant or completely immune to apple scab. """
		if apple[pred[0]] == 'Apple__Blackrot' :
			desc = "captan, lime-sulfur  powdered  wettable sulfur"
			prevention = """ The better solution to avoid the root rot in orchard is by using certified planting material and proper field sanitation. If you are considering planting new trees, choose disease-resistant varieties or cultivars, only plant in well-drained soil, and avoid overwatering. """
		if apple[pred[0]] == 'Apple__healthy':
			desc = "Apple is healthy"
		if apple[pred[0]] == 'Apple___Cedar_apple_rust':
			desc = "captan, lime-sulfur  powdered  wettable sulfur"
			prevention = """ Fungicides with the active ingredient Myclobutanil are most effective in preventing rust. """
		return render_template('PredicitionDisease.html',prediction_text= apple[pred[0]], image= file_path, desc = desc,prevention = prevention)
	

@app.route("/potatopredict",methods=["GET","POST"])
def potatopredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = potatomodel.predict(img1)
		potato = { 0 : 'Potato Early blight' , 1 : 'Potato healthy', 2 : 'Potato Late blight'}
		if potato[pred[0]] == 'Potato___Early_blight':
			desc = "captan, lime-sulfur  powdered  wettable sulfur"
			prevention = """ Water your plants early in the morning and avoid wetting the foliage. 'Earthing up' or mulching the soil with thick layers can reduce tuber infection. If blight strikes, cut away all infected material immediately and burn. Don't wash potatoes that are to be stored. """
		if potato[pred[0]] == 'Potato healthy' :
			desc = "Potato is healthy"
			prevention = ""
		if potato[pred[0]] == 'Potato Late blight':
			desc = "Apple is healthy"
			prevention = """ If there is visible late blight infestation it is recommended to apply fungicides with a spore-killing effect (fluazinam-containing fungicides, Ranman Top) mainly. """
		return render_template('PredicitionDisease.html',prediction_text= potato[pred[0]], image= file_path,desc=desc , prevention = prevention)
	

@app.route("/tomatopredict",methods=["GET","POST"])
def tomatopredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = tomatomodel.predict(img1)
		tomato = { 0 : 'Tomato___Early_blight' , 1 : 'Tomato___Late_blight', 2 : 'Tomato___healthy'}
		if tomato[pred[0]] == 'Tomato___Late_blight':
			desc = "Bordeaux mixture @ 0.8%  Copper Oxychloride @ 0.25%  Carbendazim @ 0.1%"
			prevention = """ Carefully remove and destroy all affected parts as soon as you see them. A degree of protection can be achieved by preventative spraying with a suitable fungicide. Spray before symptoms occur early in the growing season or in warm, moist conditions. """
		if tomato[pred[0]] == 'Tomato___Early_blight' :
			desc = "azoxystrobin, pyraclostrobin, difenoconazole, boscalid, chlorothalonil, fenamidone, maneb, mancozeb, trifloxystrobin, and ziram."
			prevention = """ Cover the soil under the plants with mulch, such as fabric, straw, plastic mulch, or dried leaves. Water at the base of each plant, using drip irrigation, a soaker hose, or careful hand watering.  """
		if tomato[pred[0]] == 'Tomato___healthy':
			desc = "Tomato is healthy"
			prevention = ""
		return render_template('PredicitionDisease.html',prediction_text= tomato[pred[0]], image= file_path,desc = desc,prevention=prevention)


@app.route("/grapepredict",methods=["GET","POST"])
def grapepredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = grapemodel.predict(img1)
		grape = { 0 : 'GrapeLeaf_blight' , 1 :'Grape___healthy' , 2 : 'Grape___Esca', 3 : 'Grape___Black_rot'}
		if grape[pred[0]] == 'GrapeLeaf_blight':
			desc = "Bordeaux mixture @ 0.8%  Copper Oxychloride @ 0.25%  Carbendazim @ 0.1%"
			prevention = """ Grape diseases can be effectively managed through the combined use of culture, sanitation, resistance, and fungicide sprays. """
		if grape[pred[0]] == 'Grape___healthy' :
			desc = "Grape is Healthy"
			prevention = ""
		if grape[pred[0]] == 'Grape___Esca':
			desc="Mancozeb provides protectant control of black rot, downy mildew, and Phomopsis."
			prevention = """Grapevine surgery, where the grapevine trunk is cut open using a chainsaw."""
		if grape[pred[0]] == 'Grape___Black_rot':
			desc = "Captan plus Mycobutanil or Mancozeb + Mycobutanil or Carbaryl or Imidcloprid"
			prevention = """ Early season control (bud break through bloom) is important to keep the disease from getting established on the leaves and the spreading to the fruit. """
		return render_template('PredicitionDisease.html',prediction_text= grape[pred[0]], image= file_path, desc = desc, prevention = prevention)


@app.route("/cornpredict",methods=["GET","POST"])
def cornpredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = cornmodel.predict(img1)
		corn = {0 :'Corn_Northern_Leaf_Blight' , 1 :'Corn__Common_rust', 2 :'Corn__healthy' , 3 :'Corn_Cercospora_leaf_spot'}
		if corn[pred[0]] == 'Corn_Northern_Leaf_Blight':
			desc = " picoxystrobin + cyproconazole, pyraclostrobin + metconazole"
			prevention = """ Selecting resistant hybrids; reducing corn residue by crop rotation, tillage, or stover harvest; and applying foliar fungicides """
		if corn[pred[0]] == 'Corn__Common_rust':
			desc = "Azoxystrobin 18.2% difenoconazole 11.4 % SC"
			prevention = """ Maize rusts are generally controlled by the use of resistant maize hybrids, and by foliar applications of fungicides on sweet corn.  """
		if corn[pred[0]] == 'Corn__healthy':
			desc= "Corn is healthy"
		if corn[pred[0]] == 'Corn_Cercospora_leaf_spot':
			desc = "mancozeb thiophanate-methyl"
			prevention = """ Sanitation: This is one of the most effective practices. Proper Spacing: Ensure plants are spaced adequately for good air circulation."""
		return render_template('PredicitionDisease.html',prediction_text= corn[pred[0]], image= file_path, desc= desc, prevention = prevention)


@app.route("/peachpredict",methods=["GET","POST"])
def peachpredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = peachmodel.predict(img1)
		peach = { 0 : 'Peach__Bacterial_Spot' , 1 : 'Peach_healthy'}
		if peach[pred[0]] == 'Peach__Bacterial_Spot':
			desc = "Sulfur sprays or copper-based fungicides"
			prevention = """ Remove and destroy infected leaves in the early stage of disease epidemics. Use drip irrigation and avoid overhead irrigation if possible. """
		if peach[pred[0]] == 'Peach_healthy' :
			desc = "Peach is Healthy"
			prevention = ""
		return render_template('PredicitionDisease.html',prediction_text= peach[pred[0]], image= file_path, desc = desc,prevention = prevention)
	

@app.route("/pepperbellpredict",methods=["GET","POST"])
def pepperbellpredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = pepperbellmodel.predict(img1)
		pepperbell = { 0 : 'Pepper_bell___Bacterial_spot' , 1 : 'Pepper_bell___healthy'}
		if pepperbell[pred[0]] == 'Pepper_bell___Bacterial_spot':
			desc = "copper and mancozeb-containing fungicides"
			prevention = """ Copper sprays can be used to control bacterial leaf spot, but they are not as effective when used alone on a continuous basis. Thus, combining these sprays with a plant resistance inducer, such as Regalia or Actigard, can provide good protection from the disease. """
		if pepperbell[pred[0]] == 'Pepper_bell___healthy' :
			desc = "Pepper bell is healthy"
			prevention = ""
		return render_template('PredicitionDisease.html',prediction_text= pepperbell[pred[0]], image= file_path,desc = desc , prevention = prevention)

@app.route("/strawberrypredict",methods=["GET","POST"])
def strawbeerypredict():
	if request.method == "POST":
		image = request.files["image"]
		filename = image.filename
		file_path = os.path.join('static/uploads/', filename)
		image.save(file_path)
		print(file_path)
		img = cv2.imread(file_path,0)
		img1 = cv2.resize(img,(256,256))
		img1 = img1.reshape(1,-1)/255
		pred = strawberrymodel.predict(img1)
		strawberry = { 0 : 'Strawberry___Leaf_scorch' , 1 : 'Strawberry___healthy'}
		if strawberry[pred[0]] == 'Strawberry___Leaf_scorch':
			desc = "Cabrio or Pristine (they have a common active ingredient) and Mettle or Rally (both are DMI fungicides)"
			prevention = """ Avoid extreme temperatures and water levels in rootzone Avoid overhead irrigation, since it seems to increase disease development. Avoid damage to the plants by pest insects or plant handling. """
		if strawberry[pred[0]] == 'Strawberry___healthy' :
			desc = "Strawberry is Healthy"
			prevention = ""
		return render_template('PredicitionDisease.html',prediction_text= strawberry[pred[0]], image= file_path,desc = desc , prevention = prevention)


if __name__ == "__main__":
	app.run(debug=True)