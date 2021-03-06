#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):

    if data is None:
        data = input("Veuillez entrer 10 valeurs: ")
    reversed_data = data[::-1]  # Stocker le résultat ici

    return reversed_data


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    newData = [el for el,idx in enumerate(str(data)) if idx != position]
    return Stack(newData)


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    return Queue()


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    return Stack()


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    return Queue()


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.

    fifo, lifo = Queue(), Stack()

    return fifo, lifo


def main() -> None:
    print("On inverse des données...")
    print(f"Résultat: {reverse_data([1,2,3,4,5,5,6,7,2,1])}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(fifo)}")

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
