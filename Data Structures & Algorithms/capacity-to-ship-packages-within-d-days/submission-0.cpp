class Solution {
public:

    bool canShip(vector<int>& weights, int capacity, int days) {

        int currentWeight = 0;
        int requiredDays = 1;

        for (int weight : weights) {

            if (weight + currentWeight > capacity) {
                requiredDays++;
                currentWeight = weight;
            }
            else {
                currentWeight += weight;
            }
        }

        return requiredDays <= days;
    }


    int shipWithinDays(vector<int>& weights, int days) {

        int left = 0;
        int right = 0;

        for (int weight : weights) {
            left = max(left, weight);
            right += weight;
        }

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (canShip(weights, mid, days)) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }

        return left;
    }
};