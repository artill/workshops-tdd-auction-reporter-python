from auction_type import AuctionType
from bid import Bid


class Auction(object):
    def __init__(self, name, type, status, start_price, buy_now_price):
        self.name = name
        self.type = type
        self.status = status

        if AuctionType.BID == type:
            self.start_price = start_price
            self.bids = []

        if AuctionType.BUY_NOW == type:
            self.buy_now_price = buy_now_price

    def add_bid(self, price):
        self.bids.append(Bid(price))
