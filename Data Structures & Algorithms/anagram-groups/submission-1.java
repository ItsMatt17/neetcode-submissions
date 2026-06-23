class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<List<String>>();
        if (strs.length == 1){ 
            ans.add(Arrays.asList(strs));
            return ans;
        }
        for (int i = 0; i < strs.length; i++) { 
            String word = strs[i]; 
            if (word == " ") continue; 

            List<String> subList = new ArrayList<String>();
            subList.add(word);
            for (int j = i + 1; j < strs.length; j++){
                String iterWord = strs[j];
                if (iterWord == " ") continue; 
                if (word.length() != iterWord.length()) continue;
                if (!isAnagram(word, iterWord)) continue;

                subList.add(iterWord);
                strs[j] = " ";
                
            }
            ans.add(subList);

        }
        return ans;

    }

    public boolean isAnagram(String s1, String s2) { 
        if (s1.length() != s2.length()) return false;
        int[] key = new int[26];

        for (int i = 0; i < s1.length(); i++){
            char letter = s1.charAt(i);
            key[letter - 'a']++;
        }

        for (int i = 0; i < s2.length(); i++) { 
            char letter = s2.charAt(i);
            if(key[letter - 'a'] == 0) return false;
            key[letter - 'a']--;
        }

        return true;
    }
}
