class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded="";
        for(string x:strs){
            encoded+=to_string(x.length())+"#"+x;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i<s.length()){
            int j=i;
            while(s[j]!='#'){
                j++;
            }
            //get length
            int len= stoi(s.substr(i,j-i));
            j++;
            string str=s.substr(j,len);
            result.push_back(str);
            i=j+len;
        }
        return result;
    }
};
