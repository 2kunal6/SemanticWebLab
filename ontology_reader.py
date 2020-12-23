from owlready2 import *
from util import file_util
from util.graph_util import Graph
from service import python_content_creator

import shutil

#onto = get_ontology("https://github.com/2kunal6/SemanticWebLab/blob/master/ml-hierarchy.owl")
onto = get_ontology("https://raw.githubusercontent.com/2kunal6/SemanticWebLab/master/ml-hierarchy.owl")

onto.load()

print(list(onto.classes()))

g = Graph()

for onto_class in list(onto.classes()):
    ontology_class = str(onto_class)
    if (ontology_class == "ml-hierarchy.MachineLearningAlgorithms"):
        for algorithms_ontology_class in list(onto_class.descendants()):
            algorithms_onto_class = str(algorithms_ontology_class)
            algorithms_onto_class = algorithms_onto_class.replace('ml-hierarchy.', '')
            filename = 'ml_algorithms/' + algorithms_onto_class + '.py'

            parent_classes = onto.get_parents_of(algorithms_ontology_class)
            if(not parent_classes):
                continue

            parent_class = str(parent_classes[0])

            print(parent_class.replace('ml-hierarchy.', ''), ' ', algorithms_onto_class)
            g.addEdge(parent_class.replace('ml-hierarchy.', ''), algorithms_onto_class)
        break
print('starting BFS')
file_structures = g.BFS('MachineLearningAlgorithms')
print(file_structures)

shutil.rmtree('MachineLearningAlgorithms', ignore_errors=True)

for file_structure in file_structures:
    file_util.create_folders_and_subfolders(file_structure)
    file_util.create_file(file_structure + '/' + file_structure.split('/')[-1] + '.py')
    #file_util.append_to_file(filename, python_content_creator.create_class(algorithms_onto_class, list(parent_classes)))