# STAGE 1
class TaskList():
    def __init__(self, tasks):
        self.tasks = tasks

    def today(self):
        print('Today:')
        i = 0
        for item in self.tasks:
            i += 1
            print(f'{i}) {item}')


tasks = ['Do yoga', 'Make breakfast', 'Learn basics of SQL', 'Learn what is ORM']

today = TaskList(tasks)

today.today()