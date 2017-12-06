class Listener:

    def __init__(self, widget, event_name, callback):

        self.widget = widget
        self.event_name = event_name
        self.callback = callback
