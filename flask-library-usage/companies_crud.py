from flask import Flask, json

companies = [
	{
		"id": 1,
		"name": "Sapient"
	},
	{
		"id": 2,
		"name": "GlobalLogic"
	}
]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
	return json.dumps(companies)

@api.route('/companies', methods=['POST'])
def post_companies():
	return json.dumps({"success": True}), 201

if __name__ == '__main__':
	api.run(host="0.0.0.0", port=int("5000"), debug=True)