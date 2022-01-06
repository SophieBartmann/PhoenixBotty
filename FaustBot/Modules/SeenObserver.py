import datetime
import time

from FaustBot.Communication.Connection import Connection
from FaustBot.Model.UserProvider import UserProvider
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from ..Model.i18n import i18n


class SeenObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return [".seen"]

    @staticmethod
    def help():
        return ".seen <nick> - um abzufragen wann <nick> zuletzt hier war"

    def update_on_priv_msg(self, data, connection: Connection):
        if data['message'].find('.seen ') == -1:
            return
        if not self._is_idented_mod(data, connection):
            return
        who = data['message'].split(' ')[1]
        user_provider = UserProvider()
        activity = user_provider.get_activity(who)
        delta = time.gmtime(activity)
        i18n_server = i18n()
        td = datetime.timedelta(seconds=activity)
        print("Blotsch")
        print(str(activity)+"\n")
        print(datetime.datetime.fromtimestamp(activity).strftime("%m/%d/%Y, %H:%M:%S"))
        replacements = {'user': who, 'time': str(datetime.datetime.fromtimestamp(activity).strftime("%d.%m.%Y, %H:%M:%S")),'asker':data['nick']}
        output = i18n_server.get_text('seen', replacements=replacements,
                                      lang=self.config.lang)
        if not self._is_idented_mod(data, connection):
            connection.send_channel(output)
            return
        connection.send_back(output, data)

    def _is_idented_mod(self, data: dict, connection: Connection):
        return data['nick'] in self._config.mods and connection.is_idented(data['nick'])