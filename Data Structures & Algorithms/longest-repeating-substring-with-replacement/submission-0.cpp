class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char,int> count;
        int left = 0;
        int result=0;
        int max_frequency=0;
        for(int right=0;right<s.size();right++){
            count[s[right]]++;
            //right++;
            max_frequency = max(max_frequency, count[s[right]]);
            int replacements = (right-left+1)-max_frequency;
            // Agar allowed replacements se zyada hain
            while (replacements > k) {

                // Left wala character window se hatao
                count[s[left]]--;

                // Window ko left se chhota karo
                left++;

                // Nayi window ke replacements calculate karo
                replacements =
                    (right - left + 1) - max_frequency;
            }


            // Current window valid hai
            // Iski length answer se badi hai to answer update karo
            result = max(
                result,
                right - left + 1
            );

        }
        return result;
    }
};
