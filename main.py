from flask import Flask, request

app = Flask(__name__)

in_memory_datastore = {
    "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
    "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
    "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
    "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
    "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                 "contribution": "class/object split, subclassing, protected attributes"},
    "Pascal": {"name": "Pascal", "publication_year": 1970,
               "contribution": "modern unary, binary, and assignment operator syntax expectations"},
    "CLU": {"name": "CLU", "publication_year": 1975,
            "contribution": "iterators, abstract data types, generics, checked exceptions"},
}


@app.route("/")
def hello_world():
    return "Home Page."


@app.route('/api/programming_languages', methods=['GET', 'POST'])
def programming_languages():
    if request.method == 'GET':
        return {"programming_languages": list(in_memory_datastore.values())}
    elif request.method == "POST":
        return create_programming_language(request.get_json(force=True))


def create_programming_language(new_lang):
    language_name = new_lang['name']
    in_memory_datastore[language_name] = new_lang
    return new_lang


@app.route('/api/programming_languages/<language>', methods=['GET', 'PUT', 'DELETE'])
def programming_languages_route(language):
    if request.method == 'GET':
        return get_programming_language(language)
    elif request.method == 'PUT':
        return update_programming_language(language, request.get_json(force=True))
    elif request.method == 'DELETE':
        return delete_programming_language(language)


def get_programming_language(language):
    try:
        return in_memory_datastore[language]
    except:
        return {"Error": "This language does not exist in the database"}


def update_programming_language(language, attribute_to_be_updated):
    try:
        in_memory_datastore[language].update(attribute_to_be_updated)
        return in_memory_datastore[language]
    except:
        return {"Error": "This language does not exist in the database"}


def delete_programming_language(language):
    try:
        language_to_del = in_memory_datastore[language]
        del in_memory_datastore[language]
        return language_to_del
    except:
        return {"Error": "This language does not exist in the database"}
