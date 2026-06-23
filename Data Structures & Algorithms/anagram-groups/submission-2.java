class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> ans = new HashMap<>();

        for (String word : strs){ 
            int[] alpha = new int[26];
            for (char c : word.toCharArray()) { 
                alpha[c - 'a']++;
            }
            String key = Arrays.toString(alpha);
            ans.putIfAbsent(key, new ArrayList<>());
            ans.get(key).add(word);
        }
        return new ArrayList<>(ans.values());
    }
}
