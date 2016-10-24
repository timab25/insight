from threading import Thread

class InsightServer:

    isRunning = False
    recv_thread = []

    def __init__(self):
        print "init"
        self.isRunning = True
        recv_thread = Thread(target=self.run)
        recv_thread.daemon = True
        recv_thread.start()

    def process_message(self, message):
        print "Processing message"

    def run(self):
        while self.isRunning:
            print "recv messages"

    def shutdown(self):
        self.isRunning = False
