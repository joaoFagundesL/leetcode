int maxProfit(int* prices, int pricesSize){
    int r = 1, l = 0, max = 0;

    for(int i = 0; i < pricesSize - 1; i++) {
        if(prices[r] < prices[l]) {
            l = r;
            r += 1;
        } else {
            int profit = prices[r] - prices[l];
            if(profit > max) max = profit;
            r += 1;
        }
    }

    return max;
}
