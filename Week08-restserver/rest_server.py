from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path= '', static_folder='staticpages')

books=[
    {"id":1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id":2, "Title": "Some Cook Book", "Author": "Mister Angry Man", "Price": 5000},
    {"id":3, "Title": "Python Made Easy", "Author": "Some Liar", "Price": 1500}
]
nextId=4

@app.route('/')
def index():
    return "hello"

@app.route('/books')
def getAll():
    #return "served by Get All()"
    return jsonify(books)

@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) ==0:
        return jsonify(()), 204
    return jsonify(foundBooks[0])
    #return  "served by find by id with it "+ str(id)

@app.route('/books', methods=['POST'])
def create():
   #return  "served by Create" curl -X "POST" -H "content-type:application/json" -d "{\"Title\":\"test\",\"Author\":\"Some Guy\", \"Price\":123}" http://127.0.0.1:5000/books
   global nextId
   if not request.json:
        abort(400)

   book = {
       "id": nextId,
       "Title": request.json ["Title"],
       "Author": request.json ["Author"],
       "Price": request.json ["Price"]
   }
   books.append(book)
   nextId += 1
   return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
#curl -X PUT -d "{\"Title\":\"new Title\",\"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
def update(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) ==0:
        return jsonify({}), 404
    currentBooks = foundBooks[0]
    if 'Title' in request.json:
        currentBooks['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBooks['Author'] = request.json['Author'] 
    if 'Price' in request.json:
        currentBooks[ 'Price'] = request.json['Price']
    
    return jsonify(currentBooks)
    #return  "served by update with it "+ str(id)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) ==0:
        return jsonify({}), 404
    books.remove(foundBooks[0])
    return jsonify({"done":True})
    #return  "served by delete with it "+ str(id)

if __name__ == '__main__':
    app.run(debug= True)
    


