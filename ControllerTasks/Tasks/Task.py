from enum import Enum
import logging

class Task():

    class Status(Enum):
        # task is starting (config for example)
        STARTING = 0
        # task ready for begin
        READY = 1
        # task is running
        RUNNING = 2
        # task is trying stop
        STOPPING = 3
        # task is stopped
        STOPPED = 4
        # task fail
        FAILED = 5
        # task cancelled
        CANCELLED = 6
        # task finished
        FINISHED = 7
        # task aborted
        ABORTED = 8

    def __init__(self, taskName=None):
        if taskName:
            self.taskName = taskName

        self.status = Task.Status.STOPPED

    # Method to prepare the task
    def prepare(self):
        # If task is stopped pass to starting
        if self.status is Task.Status.STOPPED: self.status = Task.Status.STARTING

        # Call to prepare implementation
        self.prepareImpl()

        # If task is starting pass to ready
        if self.status is Task.Status.STARTING: self.status = Task.Status.READY

        if self.taskName: logging.getLogger('application').info("Task %s prepared" % repr(self.taskName))


    # Method to run the task
    def doTask(self):
        # If task is ready then pass to starting
        if self.status is Task.Status.READY: self.status = Task.Status.RUNNING
        # Call to do task implementation and get the result

        if self.taskName: logging.getLogger('application').info("Running task %s" % repr(self.taskName))

        lastResult = self.doTaskImpl()

        if self.status is Task.Status.RUNNING: self.status = Task.Status.FINISHED

        if self.taskName: logging.getLogger('application').info("Task %s done" % repr(self.taskName))

        return lastResult

    # Method to shutdown the task
    def shutdown(self):
        if self.status is Task.Status.RUNNING: self.status = Task.Status.STOPPING

        if self.taskName: logging.getLogger('application').info("Stopping task %s" % repr(self.taskName))

        # Call to shutdown implementation
        self.shutdownImpl()

        if self.status is Task.Status.STOPPED: self.status = Task.Status.ABORTED

        if self.status is Task.Status.STOPPING: self.status = Task.Status.STOPPED

        if self.taskName: logging.getLogger('application').info("Task %s stopped" % repr(self.taskName))

    # Get task name
    def getTaskName(self):
        return self.taskName

    # Set task name
    def setTaskName(self, taskName):
        self.taskName = taskName

    # Get task status
    def getTaskStatus(self):
        return self.status

    # Get last result
    def getLastResult(self):
        return self.lastResult

    # Shutdown user implementation
    def shutdownImpl(self):
        pass

    # DoTask user implementation
    def doTaskImpl(self):
        pass

    # Preprare task implementation
    def prepareImpl(self):
        pass
