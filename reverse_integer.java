class Solution {
    public int reverse(int x) {
        int z = x;
        String s = "";

        if(x == 0) return x;

        while(z != 0) {
            s += Math.abs(z % 10);
            z = z / 10;
        }

        long y = Long.parseLong(s);

        if(x < 0) y = y * -1;

        if(y < Integer.MIN_VALUE || y > Integer.MAX_VALUE) return 0;
        
        else return (int)y;
    }
}
