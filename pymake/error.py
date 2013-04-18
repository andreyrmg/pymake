class NoTaskSpecifiedError(Exception):

    def __init__(self, tasks):
        super().__init__('no task specified')
        self.tasks = tasks