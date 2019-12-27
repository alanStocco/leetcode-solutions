class Solution {
    public int reverse(int x) {
        String resString = "";
        // If negative number convert positive and save - in the resString string
        if(x < 0){ 
            x *= -1;
            resString = "-";
        }
        // Loop until x is not equal 0
        while(x != 0){
            resString += x%10;
            x=x/10;
        }
        int res;
        try {
            res = Integer.parseInt(resString);
        }
        catch (NumberFormatException e)
        {
            res = 0;
        }

        return res;
    }
}