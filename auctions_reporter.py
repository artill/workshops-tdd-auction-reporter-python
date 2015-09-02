class AuctionsReporter(object):
    def create_all_auctions_reporter(self, auctions, report):
        """
        :type auctions list[auction.Auction]
        :type report string_builder.StringBuilder
        :rtype str
        """
        return "Sample Total Auctions Report"

    def create_bid_auctions_report(self, auctions):
        """
        :type auctions list[auction.Auction]
        :rtype str
        """
        return "Sample Bid Auctions Report"

    def create_buy_now_auctions_report(self, auctions):
        """
        :type auctions list[auction.Auction]
        :rtype str
        """
        return "Sample Buy Now Auctions Report"
