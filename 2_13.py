# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
#
# id_ - is just a random unique integer

from random import randint


class Boss:
    def __init__(self, name: str, company: str):
        self.id = randint(1, 101)
        self.name = name
        self.company = company
        self.workers = set()

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.add(worker)
            worker.boss = self
            worker.company = self.company

    def __repr__(self):
        return f'{self.name} | {self.company}'


class Worker:
    def __init__(self, name: str, company: str, boss: Boss):
        self.id = randint(1, 101)
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            self.company = new_boss.company

    def __repr__(self):
        return f'{self.name} | {self.company} | boss: {self.boss.name}'


boss1 = Boss('Elon Musk', 'SpaceX')
boss2 = Boss('Jeff Bezos', 'Blue Origin')
worker1 = Worker('John Doe', 'SpaceX', boss1)
worker2 = Worker('Jane Doe', 'SpaceX', boss1)
boss2.add_worker(worker2)
print(worker2)