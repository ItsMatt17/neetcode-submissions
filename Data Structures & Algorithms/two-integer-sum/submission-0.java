class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        int[] arr = new int[2];


        for (int i = 0; i < nums.length; i++){ 
            if (hash.get(nums[i]) != null) {
                arr[0] = hash.get(nums[i]); 
                arr[1] = i;
                break;
            }

            hash.put(target - nums[i], i);
        }

        return arr;

    }
}
