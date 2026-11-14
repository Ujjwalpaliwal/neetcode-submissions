class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_buy = INT_MAX;
        int max_sell = 0;
        for(int price:prices){
            min_buy = min(min_buy,price);
            max_sell = max(max_sell,price-min_buy);
        }
        return max_sell;
    }
};
