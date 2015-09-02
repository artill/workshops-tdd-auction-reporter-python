from auction_status import AuctionStatus
from auction_type import AuctionType
from auctions_reporter import AuctionsReporter
from request_context import RequestContext


class AuctionsReporterPrinter(AuctionsReporter):
    def __init__(self):
        self.total_bid = 0
        self.total_bid_price = 0
        self.total_buy_now = 0
        self.total_buy_now_price = 0
        self.total_new_auctions = 0
        self.total_active_auctions = 0
        self.total_finished_auctions = 0

    def create_all_auctions_reporter(self, auctions, report):
        """
        :type auctions list[auction.Auction]
        :type report string_builder.StringBuilder
        :rtype str
        """
        c = self._get_request_context()

        report.append("ANNUAL SUMMARY OF ALL AUCTIONS.\n")
        report.append("*******************************\n\n")

        now = c.now
        month = now.month

        print "\r\nMonth -> " + str(month) + "\r\n"

        if 0 < month <= 2:
            report.append("Report period: 01/01/2015 and 31/03/2015\n")
        elif 3 < month <= 6:
            report.append("Report period: 01/04/2015 and 30/06/2015\n")
        elif 6 < month <= 9:
            report.append("Report period: 01/07/2015 and 30/09/2015\n")
        elif 9 < month <= 12:
            report.append("Report period: 01/10/2015 and 31/12/2015\n")
        else:
            raise Exception("Critical issue")

        report.append("Total number of auctions: " + str(len(auctions)))
        report.append("\n")

        for auction in auctions:
            self._data(auction)

        report.append("Including ")
        report.append(self.total_bid)
        report.append(" bid auctions and ")
        report.append(self.total_buy_now)
        report.append(" buy now auctions\n")

        report.append(self.total_new_auctions)
        report.append(" auctions are ")
        report.append(self._get_description(AuctionStatus.NEW))
        report.append("\n")

        report.append(self.total_active_auctions)
        report.append(" auctions are ")
        report.append(self._get_description(AuctionStatus.ACTIVE))
        report.append("\n")

        report.append(self.total_finished_auctions)
        report.append(" auctions are ")
        report.append(self._get_description(AuctionStatus.FINISHED))
        report.append("\n")

        report.append("Total buy now price: ")
        report.append(self.total_buy_now_price)
        report.append(" zl\n")

        report.append("Total bid price: ")
        report.append(self.total_bid_price)
        report.append(" zl\n")

        return report.string

    def _get_request_context(self):
        return RequestContext(None)

    def _data(self, auction):
        if AuctionType.BID == auction.type:
            self.total_bid += 1
            if len(auction.bids) == 0:
                self.total_bid_price += auction.start_price
            else:
                self.total_bid_price += auction.bids[-1].price
        elif AuctionType.BUY_NOW == auction.type:
            self.total_buy_now += 1
            self.total_buy_now_price += auction.buy_now_price
        else:
            raise Exception("Not recognized auction type")

        if AuctionStatus.NEW == auction.status:
            self.total_new_auctions += 1
        elif AuctionStatus.ACTIVE == auction.status:
            self.total_active_auctions += 1
        elif AuctionStatus.FINISHED == auction.status:
            self.total_finished_auctions += 1
        else:
            raise Exception("Not recognized auction status")

    def _get_description(self, status):
        if AuctionStatus.NEW == status:
            return "new"
        elif AuctionStatus.ACTIVE == status:
            return "active"
        else:
            return "finished"

    def create_bid_auctions_report(self, auctions):
        raise Exception("Report type not supported")

    def create_buy_now_auctions_report(self, auctions):
        raise Exception("Report type not supported")
