class DataSource(object):

    def __init__(self, parent, diction):

        self.data = diction.dictionary
        self.parent = parent
        self.keys_list = list(self.data.keys())
        self.keys_list_index = 0
        self.event_listeners = {}

    def broadcastEvent(self, event_name):

        for listener in self.event_listeners[event_name]:
            listener.widget.event_generate(event_name, when='tail')

    def addListener(self, listener):
        listener.widget.bind(listener.event_name, listener.callback)
        listeners = [listener]

        if listener.event_name in self.event_listeners.keys():
            self.event_listeners[listener.event_name] += listeners
        else:
            self.event_listeners[listener.event_name] = listeners
        
    def set_current_record(self, key):
        
        self.keys_list_index = self.keys_list.index(key)
        self.broadcastEvent("<<navigate_record>>");

    def current_record(self):

        return self.data[self.keys_list[self.keys_list_index]]

    def previous_record(self):

        if(self.keys_list_index > 0):
            self.keys_list_index -= 1
            self.broadcastEvent("<<previous_record>>");

    def next_record(self):

        if(self.keys_list_index < len(self.keys_list) - 1):
            self.keys_list_index += 1
            self.broadcastEvent("<<next_record>>");

    def request_update(self):
        self.broadcastEvent("<<update_record>>");

    def request_delete(self):
        
        self.parent.event_generate("<<delete_record>>", when="tail")

    def update_record(self, record):

        self.data[record[0]] = record
        
    def delete_record(self):

        del self.data[self.keys_list[self.keys_list_index]]
        del self.keys_list[self.keys_list_index]

        if(self.keys_list_index + 1 < len(self.keys_list) - 1):
            self.keys_list_index += 1

    def request_add(self):

        self.parent.event_generate("<<add_record>>", when="tail")

            
        
