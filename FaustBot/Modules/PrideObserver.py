from FaustBot.Communication import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype


class PrideObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return [".pride"]

    @staticmethod
    def help():
        return ".party - sorgt für Pride Flags"

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.pride') == -1:
            return
        connection.send_back('\001ACTION schmückt den Channel mit vielen großen Pride flags.\001', data)
