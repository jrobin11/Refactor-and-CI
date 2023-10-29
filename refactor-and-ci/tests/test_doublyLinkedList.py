from refactor_and_ci.assignment_lists_solutions import Node, DoublyLinkedList


def test_node():
    node1 = Node(1)
    node2 = Node(2, next_node=node1)
    node1.set_previous(node2)
    
    assert node1.get_element() == 1
    assert node2.get_next() == node1
    assert node1.get_previous() == node2
    
    node1.set_element(3)
    assert node1.get_element() == 3

    assert repr(node2) == "(2, (3, None))"


def test_doubly_linked_list_initialization():
    dll = DoublyLinkedList()
    assert dll.size() == 0
    assert dll.is_empty()
    assert dll.get_first().get_element() == "Header"
    assert dll.get_last().get_element() == "Trailer"


def test_adding_and_removing():
    dll = DoublyLinkedList()
    
    node1 = Node(1)
    dll.add_first(node1)
    assert dll.size() == 1
    assert dll.get_first() == node1
    assert dll.get_last() == node1
    
    node2 = Node(2)
    dll.add_after(node2, node1)
    assert dll.size() == 2
    assert dll.get_last() == node2

    node3 = Node(3)
    dll.add_before(node3, node2)
    assert dll.size() == 3
    assert dll.get_previous(node2) == node3
    
    dll.remove(node3)
    assert dll.size() == 2
    assert dll.get_previous(node2) == node1


def test_iteration():
    dll = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    dll.add_first(node1)
    dll.add_last(node2)
    dll.add_last(node3)

    elements = [1, 2, 3]
    for node, expected_element in zip(dll, elements):
        assert node.get_element() == expected_element

    # Ensure we have tested the StopIteration condition
    iterator = iter(dll)
    for _ in range(3):
        next(iterator)
    try:
        next(iterator)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass


def test_mapping():
    dll = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    dll.add_first(node1)
    dll.add_last(node2)
    dll.add_last(node3)

    dll.map(lambda x: x * 2)
    assert dll.get_first().get_element() == 2
    assert dll.get_first().get_next().get_element() == 4
    assert dll.get_last().get_element() == 6


# Run the tests
test_node()
test_doubly_linked_list_initialization()
test_adding_and_removing()
test_iteration()
test_mapping()

print("All tests passed!")
