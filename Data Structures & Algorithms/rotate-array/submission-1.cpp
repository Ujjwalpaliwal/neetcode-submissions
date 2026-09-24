class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n= nums.size();
        k%=n;
        vector<int> sub(n);
        for(int i=0;i<n;i++){
            sub[(i+k)%n]=nums[i];
        }
        nums=sub;
    }
};