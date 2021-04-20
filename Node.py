class Node:
    value = 0
    node_list = []

    def Node(self, node_list, value):
        self.value = value
        self.node_list = node_list

    def setValue(self, value):
        self.value = value

    def setNodelist(self, node_list):
        self.node_list = node_list