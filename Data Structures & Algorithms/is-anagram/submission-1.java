class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] n = new int[26];

        for (int i = 0; i < s.length(); i++){ 
            char subChar = s.charAt(i); 
            n[subChar - 'a' ] += 1;
        }

        for (int i = 0; i < t.length(); i++) { 
            char subChar = t.charAt(i);
            if (n[subChar - 'a'] == 0) return false;
            n[subChar - 'a'] -= 1;
        }
        return true;
    }
}
