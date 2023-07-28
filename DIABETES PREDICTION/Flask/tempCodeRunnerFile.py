

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