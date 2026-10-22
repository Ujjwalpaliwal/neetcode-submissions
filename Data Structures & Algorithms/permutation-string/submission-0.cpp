class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n= s1.length();
        int m = s2.length();
        vector<int> count1(26,0);
        vector<int> count2(26,0);
        if(n>m) return false;
        for (char c :s1){
            count1[c-'a']++;
        }
        for(int i = 0; i<n;i++){
            count2[s2[i]-'a']++;
        }
        if(count1==count2){
            return true;
        }
        //sliding window
        for(int r = n;r<m;r++){
            count2[s2[r]-'a']++;
            count2[s2[r-n]-'a']--;
            if(count1 == count2){
                return true;
            }
        }
        return false;
    }
};
