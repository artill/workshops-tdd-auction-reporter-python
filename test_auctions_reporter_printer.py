from auction import Auction
from auction_status import AuctionStatus
from auction_type import AuctionType
from auctions_reporter_printer import AuctionsReporterPrinter
from string_builder import StringBuilder


def test_ble():
    sut = AuctionsReporterPrinter()

    a1 = Auction("test", AuctionType.BUY_NOW, AuctionStatus.ACTIVE, 0, 5)
    a2 = Auction("test", AuctionType.BID, AuctionStatus.ACTIVE, 1, 0)
    a3 = Auction("test", AuctionType.BID, AuctionStatus.ACTIVE, 1, 0)
    a3.add_bid(2)

    result = sut.create_all_auctions_reporter([a1, a2, a3], StringBuilder())

    raise BaseException(result)
