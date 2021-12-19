import _thread

from FaustBot.Communication.Observable import Observable

class PrivmsgObservable(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.user_list = None
    def define_user_list(self, user_list):
        self.user_list = user_list

    def input(self, raw_data, connection):
        data = {'raw': raw_data, 'nick': raw_data.split('!')[0][1:],
                'channel': raw_data.split('PRIVMSG ')[1].split(' :')[0],
                'raw_nick': raw_data.split(' PRIVMSG')[0][1:]}
        # 12 = :<raw_nick> PRIVMSG <channel> :<message>
        data['message'] = raw_data[data['raw_nick'].__len__() + data['channel'].__len__() + 12:]
        data['command'] = 'irgendwas, das mit . oder .. anfängt oder so... oder das sollen module checken?'
        if self.user_list is None:
            return
        if data['nick'] not in self.user_list.userList.keys():
            return
        self.notify_observers(data, connection)

    def notify_observers(self, data, connection):
        for observer in self._observers:
            _thread.start_new_thread(observer.__class__.update_on_priv_msg, (observer, data, connection))
