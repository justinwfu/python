# linked_list_test.py
# Test linked_list.py

import linked_list

# test cases
# 1. append
# 2. prepend
# 3. append, append
# 4. append, prepend
# 5. prepend, append
# 6. append, prepend, append
# 7. prepend, append, prepend


def test_append():
    ll = linked_list.LinkedList()
    ll.append(1)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def test_prepend():
    ll = linked_list.LinkedList()
    ll.prepend(1)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def test_append_and_prepend():
    ll = linked_list.LinkedList()
    ll.append(2)
    ll.prepend(1)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def test_prepend_and_append():
    ll = linked_list.LinkedList()
    ll.prepend(1)
    ll.append(2)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def test_append_and_prepend_and_append():
    ll = linked_list.LinkedList()
    ll.append(2)
    ll.prepend(1)
    ll.append(3)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def test_prepend_and_append_and_prepend():
    ll = linked_list.LinkedList()
    ll.prepend(2)
    ll.append(3)
    ll.prepend(1)
    while ll.current is not None:
        print(ll.current.value)
        ll.current = ll.current.next


def main():
    # all tests should print increasing integers
    print('-------******* append *******-------')
    test_append()

    print('-------******* prepend *******-------')
    test_prepend()

    print('-------******* append, prepend *******-------')
    test_append_and_prepend()

    print('-------******* prepend, append *******-------')
    test_prepend_and_append()

    print('-------******* append, prepend, append *******-------')
    test_append_and_prepend_and_append()

    print('-------******* prepend, append, prepend *******-------')
    test_prepend_and_append_and_prepend()


if __name__ == '__main__':
    main()
