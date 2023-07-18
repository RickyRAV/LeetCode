public class Solution {
    public bool IsAnagram(string s, string t) 
    {
        bool output = true;
        char[] word1 = s.ToLower().ToCharArray();
        char[] word2 = t.ToLower().ToCharArray();
        Array.Sort(word1);
        Array.Sort(word2);
        string var1 = new string(word1);
        string var2 = new string(word2);
        if(var1==var2){
            output=true;
        }
        else{
            output=false;
        }
        return output;
    }
}