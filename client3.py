################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    stock = quote['stock']
    bid_price_a = float(quote['top_bid']['price'])
    ask_price_a = float(quote['top_ask']['price'])
    price_a = (bid_price_a + ask_price_a) / 2
    bid_price_b = float(quote['top_bid_b']['price'])  # Assuming there's a 'top_bid_b' key
    ask_price_b = float(quote['top_ask_b']['price'])  # Assuming there's a 'top_ask_b' key
    price_b = (bid_price_b + ask_price_b) / 2
    return stock, price_a, price_b


def getRatio(price_a, price_b):
    return price_a / price_b if price_b != 0 else None


if __name__ == "__main__":
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, price_a, price_b = getDataPoint(quote)
            print("Quoted %s at (price_a:%s, price_b:%s)" % (stock, price_a, price_b))

            ratio = getRatio(price_a, price_b)
            print("Ratio %s" % ratio)

