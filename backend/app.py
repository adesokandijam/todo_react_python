from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})


import dynamodb_handler as dynamodb



#  Add a book entry
#  Route: http://localhost:5000/book
#  Method : POST
@app.route('/api/todo', methods=['POST'])
def addABook():

    data = request.get_json()
    # id, title, author = 1001, 'Angels and Demons', 'Dan Brown'

    response = dynamodb.addItemToBook(data['id'], data['todo'])    
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/api/todo/<int:id>', methods=['GET'])
def getBook(id):
    response = dynamodb.GetItemFromBook(id)
    #return response
    
    if (response["ResponseMetadata"]['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return response['Item'] 

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }


#  Delete a book entry
#  Route: http://localhost:5000/book/<id>
#  Method : DELETE
@app.route('/api/todo/<int:id>', methods=['DELETE'])
def DeleteABook(id):

    response = dynamodb.DeleteAnItemFromBook(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Deleted successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    } 


#  Update a book entry
#  Route: http://localhost:5000/book/<id>
#  Method : PUT
@app.route('/api/todo/<int:id>', methods=['PUT'])
def UpdateABook(id):

    data = request.get_json()

    response = dynamodb.UpdateItemInBook(id, data)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'                : 'Updated successfully',
            'ModifiedAttributes' : response['Attributes'],
            'response'           : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    }   



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)