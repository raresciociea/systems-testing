from tree import Tree

def test_find_existing_node():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    assert tree.find(3).data == 3
    assert tree.find(4).data == 4
    assert tree.find(0).data == 0
    assert tree.find(8).data == 8
    assert tree.find(2).data == 2

def test_find_non_existing_node():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    assert tree.find(5) is None
    assert tree.find(-1) is None
    assert tree.find(10) is None