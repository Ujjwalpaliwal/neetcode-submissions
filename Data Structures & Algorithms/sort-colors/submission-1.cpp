class Solution {
public:
    void sortColors(vector<int>& nums) {
        int freq[3]={0};
        for(int x:nums){
            freq[x]++;
        }
        int index=0;
        for( int i=0;i<freq[0];i++){
            nums[index]=0;
            index++;
        }
        for(int i =0;i<freq[1];i++){
            nums[index]=1;
            index++;
        }
        for(int i =0;i<freq[2];i++){
            nums[index]=2;
            index++;
        }
    }
};