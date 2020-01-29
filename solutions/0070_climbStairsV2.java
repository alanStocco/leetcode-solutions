/**
* You are climbing a stair case. It takes n steps to reach to the top.
* Each time you can either climb 1 or 2 steps. 
* In how many distinct ways can you climb to the top?
* Note: Given n will be a positive integer.
* @author  Alan Stocco
* @version 1.0
* @since   29-01-2020 
 */
class Solution {
  public static   void main(final String[] args){
      final TopDownWithMemoization_v1 topDownWithMemoization_v1 = new TopDownWithMemoization_v1();
      final TopDownWithMemoization_v2 topDownWithMemoization_v2 = new TopDownWithMemoization_v2();
      
      final int num = 44;
      long startTimeV1 = System.nanoTime();
      int sol = topDownWithMemoization_v1.climbStairs(num);
      long stopTimeV1 = System.nanoTime();
      int sol2 = topDownWithMemoization_v2.climbStairs(num);
      long stopTimeV2 = System.nanoTime();

      if(sol == sol2){
        System.out.println("Solution: "+sol); 
        System.out.println("Time V1: "+ (stopTimeV1 - startTimeV1)); 
        System.out.println("Time V2: "+ (stopTimeV2 - stopTimeV1)); 

      }else{
        System.out.println("Different solutions.");  
      }
   }
}

class TopDownWithMemoization_v1 {
  public int climbStairs(int n) {
    int memo[] = new int[n+1];
    return climbStairsRecursive(0, n, memo);  
  }

  public int climbStairsRecursive(int i, int n, int memo[]){
    if(i > n){
      return 0;
    }
    if(i == n){
      return 1;
    }    
    if(memo[i] > 0){
      return memo[i];
    }
    memo[i] = climbStairsRecursive(i+1, n, memo) + climbStairsRecursive(i+2, n, memo);
    return memo[i];
  }
}

class TopDownWithMemoization_v2 {
  public int climbStairs(int n) {
    int memo[] = new int[n+1];
    return climbStairsRecursive(n, memo);  
  }

  public int climbStairsRecursive(int n, int memo[]){
    if(n < 0){
      return 0;
    }
    if(n == 0){
      return 1;
    }    
    if(memo[n] > 0){
      return memo[n];
    }
    return climbStairsRecursive(n-2, memo) + climbStairsRecursive(n-1, memo);
  }
}