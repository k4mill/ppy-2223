class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return " -> ".join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return
        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return
        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                self.size -= 1
                return
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
        else:
            current = self.head
            prev = None
            while current and (func is None or func(e, current.data)):
                prev = current
                current = current.nextE
            if prev is None:
                new_element.nextE = self.head
                self.head = new_element
            else:
                prev.nextE = new_element
                new_element.nextE = current
            if current is None:
                self.tail = new_element
        self.size += 1