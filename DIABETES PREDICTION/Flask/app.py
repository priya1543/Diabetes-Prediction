from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'C:\Users\nilas\Downloads\DIABETES PREDICTION ADS\DIABETES PREDICTION\Flask\model.pkl','rb'))

@app.route('/')#binds to an url
def diabetes():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    HBP = request.form["HighBP"]
    HCOL = request.form["HighChol"]
    COLC = request.form["CholCheck"]
    BMI = request.form["BMI"]
    SMK = request.form["Smoker"]
    STK = request.form["Stroke"]
    HDA = request.form["HeartDiseaseorAttack"]
    PYA = request.form["PhysActivity"]
    FRT = request.form["Fruits"]
    VEG = request.form["Veggies"]
    HAC = request.form["HvyAlcoholConsump"]
    AHC = request.form["AnyHealthcare"]
    GEH = request.form["GenHlth"]
    MEH = request.form["MentHlth"]
    PYH = request.form["PhysHlth"]
    DW = request.form["DiffWalk"]
    AE = request.form["Age"]

    t=[[int(HBP),int(HCOL),int(COLC),int(BMI),int(SMK),int(STK),int(HDA),int(PYA),int(FRT),int(VEG),int(HAC),int(AHC),int(GEH),int(MEH),int(PYH),int(DW),int(AE)]]
    output= model.predict(t)
    if(output==0):
        output = "Great, Diabetes not present"
    else:
        output = "OOPS you are sufferning from diabetes seek immediate action."
        
        
    return render_template("index.html", y = "Predicted Outcome: " + str(output))


if __name__ == '__main__' :
    app.run(debug= False)
    
