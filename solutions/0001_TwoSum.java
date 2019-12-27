import java.util.HashMap;
import java.util.Map;
class Solution {
    public int[] twoSum(final int[] nums, final int target) {
        final int[] result = new int[2];
        // Loop the array, for each value exist one o 0 other value such
        // that they add up to target
        // I can create a dictionary with key the current number and value the position
        final Map<Integer, Integer> valAndPos = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            final Integer missToTarget = target - nums[i];
            if(valAndPos.get(missToTarget) != null){
                result[0] =  valAndPos.get(missToTarget);
                result[1] = i;
                return result;
            }
            else{
                valAndPos.put(new Integer(nums[i]), i);
            }
        }
        return result;
    }
}