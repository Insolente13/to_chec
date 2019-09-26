class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    '''1.1.Добавьте в класс LinkedList метод удаления одного
    узла по его значению delete(val, all=False)
    где флажок all = False по умолчанию -- удаляем только первый
    нашедшийся элемент.
    1.2.Дополните этот метод удалением всех узлов
    по конкретному значению (флажок all = True).'''

    def delete(self, val, all=False):
        node = self.head
        node_len = 0
        break_point = 0

        while node is not None:
            node_len += 1
            # Первое и единственное
            if node.value == val and node.next is None and node_len == 1:
                self.head = None
                self.tail = None
                break_point += 1
            # Первое не единственное
            elif node.value == val and node.next is not None and node_len == 1:
                self.head = node.next
                break_point += 1
            elif node.value == val and node.next is not None and node_len != 1:
                break_point += 1
            # Последующее
            elif node.value != val and node.next is not None:
                # Если несколько подрят
                if node.next.value == val and node.next.next is not None:
                    while node.next.value == val \
                            and node.next.next is not None:
                        if all is False and break_point != 0:
                            break
                        else:
                            node.next = node.next.next
                            break_point += 1
                    if node.next.value == val and node.next.next is None \
                            and break_point != 0 and all is True:
                        node.next = None
                        self.tail = node
                        break_point += 1
                    break_point += 1
                elif node.next.value == val and node.next.next is None:
                    node.next = None
                    self.tail = node
                    break_point += 1

            node = node.next

            if all is False and break_point != 0:
                break

    '''1.3.Добавьте в класс LinkedList метод очистки
    всего содержимого(создание пустого списка) -- clean()'''

    def clean(self):
        self.head = None
        self.tail = None

    '''1.4.Добавьте в класс LinkedList метод поиска всех
    узлов по конкретному значению(возвращается стандартный
    питоновский список найденных узлов).'''

    def find_all(self, val):
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    '''1.5. Добавьте в класс LinkedList метод
    вычисления текущей длины списка -- len()'''

    def len(self):
        node = self.head
        count_node = 0
        while node is not None:
            count_node += 1
            node = node.next
        return count_node

    '''1.6. Добавьте в класс LinkedList метод вставки узла
    newNode после заданного узла afterNode (из списка)
    insert(afterNode, newNode). Если afterNode = None и
    список пустой, добавьте новый элемент первым в списке.'''

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None and self.head is not None:
            head_node = self.head
            self.head = newNode
            newNode.next = head_node
        elif afterNode is not None and self.head is not None:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    if node is not None and node.next is None:
                        node.next = newNode
                        self.tail = newNode
                        break
                    elif node is not None and node.next is not None:
                        newNode.next = node.next
                        node.next = newNode
                        break
                node = node.next
        else:
            return None

'''* 1.8. Напишите функцию, которая получает на вход два связанных списка,
состоящие из целых значений, и если их длины равны,
возвращает список, каждый элемент которого равен
сумме соответствующих элементов входных списков.'''


def linked_list_sum(list_1, list_2):
    if list_1.len() == list_2.len():
        node_1 = list_1.head
        node_2 = list_2.head
        sum_list = []
        while node_1 is not None:
            sum_list.append(node_1.value + node_2.value)
            node_1 = node_1.next
            node_2 = node_2.next
        return sum_list
    else:
        print('NO')
