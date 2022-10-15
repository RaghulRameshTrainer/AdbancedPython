from flask import Flask,jsonify,request,Response
app=Flask(__name__)

emp=[
    {
        'name':'Raghul Ramesh',
        'exp':[
            {
                'tech':'Python',
                'years':16
            }
        ]
    },
    {
        'name':'Malini',
        'exp':[
            {
                'tech':'Java',
                'years':12
            }
        ]
    }
]
@app.route('/')
def home_page():
    return "Hello!"

@app.route('/emp/<string:name>')
def get_emp(name):
    for employee in emp:
        if(employee['name']==name):
            return jsonify(employee['name'], 201)
    return jsonify({'message':'employee not found'}, 404)

@app.route('/emp',methods=['POST'])
def add_emp():
    req_data=request.get_json()
    new_emp={
        'name':req_data['name'],
        'exp':req_data['experience']
    }
    emp.append(new_emp)
    return jsonify(new_emp)

@app.route('/emp/<string:name>/info',methods=['GET'])
def get_emp_details(name):
    for employee in emp:
        if(employee['name']==name):
            req_data=request.get_json()
            return jsonify(employee)
    return jsonify({"message":"NOT FOUND"},404)

if __name__ == "__main__":
    app.run()


#return Response("{'a':'b'}", status=201, mimetype='application/json')
