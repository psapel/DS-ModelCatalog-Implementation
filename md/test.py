def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Perform search in Elasticsearch
    result = es.search(index='models', body={'query': {'match': {'alpha': query}}})
    hits = result['hits']['hits']

    # Return the search results
    return jsonify({'results': hits}), 200


def find_matching_model(models, alpha, beta, gamma):
    print("Finding matching model...")
    print(f"Form Alpha: {alpha}, Beta: {beta}, Gamma: {gamma}")

    # Prepare the query to search for matching models in Elasticsearch
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"GrahamNotation.alpha": alpha}},
                    {"match": {"GrahamNotation.beta": beta}},
                    {"match": {"GrahamNotation.gamma": gamma}}
                ]
            }
        }
    }

    # Perform the search in Elasticsearch
    result = es.search(index='models', body=query)
    hits = result['hits']['hits']
    if hits:
        model = hits[0]['_source']
        print(f"Matching model: {model}")
        return model
    return None