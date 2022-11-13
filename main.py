from py2neo import Graph, Node, Relationship, NodeMatcher
from bs4 import BeautifulSoup as Soup

graph = Graph("bolt://localhost:7687", auth=('neo4j', 'neo4j'))
graph.delete_all()


def get_graph_from_xml(file_name):
    layers = {}
    with open(file_name, 'r', encoding='utf-8') as xml:
        soup = Soup(xml.read(), 'lxml')
    l_s = soup.find_all('layer')
    for i in l_s:
        # print(i)
        node = Node(i['type'], name=i['name'], id=i['id'])
        graph.create(node)
        layers[int(i['id'])] = {'name': i['name'],  'type': i['type']}

    edges = soup.find_all('edge')
    matcher = NodeMatcher(graph)
    for i in edges:
        from_layer = layers[int(i['from-layer'])]['name']
        from_layer_node = matcher.match(layers[int(i['from-layer'])]['type'], name=from_layer).first()
        to_layer = layers[int(i['to-layer'])]['name']
        to_layer_node = matcher.match(layers[int(i['to-layer'])]['type'], name=to_layer).first()
        relationship = Relationship(from_layer_node, 'SENDING_DATA_TO', to_layer_node)
        graph.create(relationship)


get_graph_from_xml(input("Please enter path to xml model file:"))
