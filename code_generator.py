from owlready2 import *
import os
import shutil

from service.file_content_creator import create_file_contents
from util import file_util

child_parent_map = {}
onto = get_ontology("ml_algorithms.owl").load()
queue = []
root_class = None
print([i for i in onto.annotation_properties()])
print(list(onto.classes()))
for onto_class in list(onto.classes()):
    if onto_class.label[0] == 'MLalgorithms':
        root_class = onto_class

shutil.rmtree("MLalgorithms")
queue.append(root_class)
dir_structure = [root_class.label[0]]
child_parent_map[root_class] = None
while queue:
    node = queue.pop(0)
    file = dir_structure.pop(0)
    if onto.get_children_of(node):
        file_util.create_folders_and_subfolders(file)
    content = create_file_contents(file, node, child_parent_map)
    file_path = file
    if node == root_class:
        file_path = os.path.join(file, file)
    file_util.create_and_write_file(file_path + ".py", content)
    for child in onto.get_children_of(node):
        queue.append(child)
        child_parent_map[child] = node
        dir_structure.append(os.path.join(file, child.label[0]))
