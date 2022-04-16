from flask import Flask, request
from database.setup import init_db
from encryption.encryption import generate_key, encrypt
from authentication.authentication import verify_credentials
from database.database import add_task, get_tasks, remove_task, mutate_task

app = Flask(__name__)
init_db()
generate_key()

@app.route('/create_task', methods=['POST'])    
def create_task():
    '''
    This function handle create requests
    '''
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    
    user, message = verify_credentials(username=username, password=password)
    
    if not user: response_code = 400
    else:
        content = request.form.get('content', None)
        
        status, message = add_task(content=content, user=user)

        if status: response_code = 201
        else: response_code = 500
    
    message = encrypt(data=message, depth=0) 

    return {'message' : message}, response_code
        
@app.route('/update_task', methods=['POST'])
def update_task():
    '''
    This function handle update requests
    '''
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    
    user, message = verify_credentials(username=username, password=password)
    
    if not user: response_code = 400
    else:
        task = request.form.get('task', None)
        content = request.form.get('content', None)

        status, message = mutate_task(task=task, content=content)

        if status: response_code = 200
        else: response_code = 400
    
    message = encrypt(data=message, depth=0)
    
    return {'message' : message}, response_code


@app.route('/delete_task', methods=['POST'])    
def delete_task():
    '''
    This function handle delete requests
    '''
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    
    user, message = verify_credentials(username=username, password=password)
    
    if not user: response_code = 400
    else:
        task = request.form.get('task', None)
        
        status, message = remove_task(task=task)

        if status: response_code = 200
        else: response_code = 400

    message = encrypt(data=message, depth=0)
    
    return {'message' : message}, response_code


@app.route('/read_task', methods=['POST'])        
def read_task():
    '''
    This function handle read requests
    '''
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    
    user, message = verify_credentials(username=username, password=password)
    
    if not user: response_code = 400
    else:
        status, message = get_tasks(user=user)

        if status: response_code = 200
        else: response_code = 200
    
    if isinstance(message, str): depth = 0
    else: depth = 1
    print("DEPTH", depth)
    message = encrypt(data=message, depth=depth)
    
    return {'message' : message}, response_code
        

if __name__ == '__main__':
    app.run(debug=True)