from abc import ABC, abstractmethod


class AbstractStrategy(ABC):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def set_settings(self, short_term, long_term, client):
        pass

    @abstractmethod
    def run_strategy(self, interval, stream_id):
        pass

    @abstractmethod
    def signal_buy(self, price_data, step):
        pass

    @abstractmethod
    def signal_sell(self, price_data, step):
        pass

    @abstractmethod
    def send_order(self, price_data, wallet_data, step, recv_window):
        pass

    @abstractmethod
    def compute(self, price_data, step):
        pass

    @abstractmethod
    def stop_strategy(self, price_data, wallet_data, recv_window):
        pass
