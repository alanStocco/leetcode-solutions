
/**
 * @param {number} n
 * @return {number}
 */
//Ricoursive
var climbStairs = function(n) {
    var map = new Map(); 
    map.set(0,1);
    map.set(1,1);
    if(n<2)  return 1;
    return climbStairsRecursive(n, map);    
  };
  
  var climbStairsRecursive = function(n, map) {
    var waysMin2, waysMin1 = 1;
    if(map.has(n-2))
      waysMin2 = map.get(n-2)
    else{
      waysMin2 = climbStairsRecursive(n-2, map);
      map.set(n-2,waysMin2);
      }
    if(map.has  (n-1)){
      waysMin1 = map.get(n-1)
    }else{
      waysMin1 = climbStairsRecursive(n-1, map);
      map.set(n-1,waysMin1);
    }
    
     
    return waysMin2 + waysMin1;
  };
  
    // To reach step n I can arrive from step n-1 and do a step or from step n-2 and do 2 steps 
    // ways(n) = ways(n-1) + ways(n-2)
    // ways(2) = ways(0)+ways(1)= 2
    // ways(3) = ways(2) + ways(1)= 2+1 = 3
    // ways(4) = ways(3)+ways(2) = 3+2 = 5
    // ways(5) = ways(4)+ways(3) = 5+3=8
    
  
    // n=1 ways is 1
    // example input 4
    // 1+1+1+1
    // 1+2+1
    // 1+1+2
    // 2+1+1
    // 2+2
    // for n=4 ways is  5
  
    //for n=5
    // 1+1+1+1+1
    // 1+1+1+2
    // 1+1+2+1
    // 1+2+2
    // 1+2+1+1
    // 2+1+1+1
    // 2+1+2
    // 2+2+1
    // ways is 8
  
    // for n=6
    /*
      1+1+1+1+1+1
      1+1+1+1+2
      1+1+1+2+1
      1+1+2+1+1
      1+2+1+1+1
      2+1+1+1+1
      2+2+2
      2+2+1+1
      2+1+2+1
      2+1+1+2
  
    */
  