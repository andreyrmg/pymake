class NoTaskSpecifiedError(Exception):

    def __init__(self, tasks):
        super().__init__('no task specified')
        self.tasks = tasks


class DefaultTaskAlreadyExists(Exception):

    def __init__(self, first, second):
        super().__init__('default task already exists')
        self.first = first
        self.second = second
