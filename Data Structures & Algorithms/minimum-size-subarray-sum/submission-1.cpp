class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        long long sum = 0;
        int ans=INT_MAX;
        for(int r = 0;r<n;r++){
            sum +=nums[r];
            while(sum>=target){
                ans =min(ans,r-left+1);
                sum-=nums[left];
                left++;
            }
        }
        return ans == INT_MAX?0 :ans;
    }
};