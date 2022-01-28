class Logger:
    def __init__(self):
        self.timing = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.timing:
            previous_occurrence = self.timing[message]
            if timestamp >= previous_occurrence + 10:
                self.timing[message] = timestamp
                print("True")
            else:
                print("False")
        else:
            self.timing[message] = timestamp
            print("True")


logger = Logger()
logger.shouldPrintMessage(1, "foo")
logger.shouldPrintMessage(2, "bar")
logger.shouldPrintMessage(3, "foo")
logger.shouldPrintMessage(8, "bar")
logger.shouldPrintMessage(10, "foo")
logger.shouldPrintMessage(11, "foo")

