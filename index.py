from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuários (simulação de um banco de dados)
users = [
    {'id': 1, 'nome': 'João', 'email': 'joao@example.com'},
    {'id': 2, 'nome': 'Maria', 'email': 'maria@example.com'},
    {'id': 3, 'nome': 'José', 'email': 'jose@example.com'}
]

# Rota para obter todos os usuários
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Rota para obter um usuário específico
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Rota para criar um novo usuário
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = {'id': len(users) + 1, 'nome': request.json['nome'], 'email': request.json['email']}
    users.append(new_user)
    return jsonify(new_user), 201

# Rota para atualizar um usuário existente
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['nome'] = request.json.get('nome', user['nome'])
        user['email'] = request.json.get('email', user['email'])
        return jsonify(user)
    return jsonify({'message': 'Usuário não encontrado.'}), 404 

# Rota para excluir um usuário
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users.remove(user)
        return jsonify({'message': 'Usuário removido'})
    return jsonify({'message': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run() 
