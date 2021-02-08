class Solution {
    public String convert(String s, int numRows) {
        int sLen = s.length();
        String newS = "";
        int index = 0;
        int move = 0;
        Boolean zigzag = false;
        if (sLen <= numRows || numRows ==1) {
            return s;
        }
        int r = numRows;
        while (r > 1) {
            if (index > sLen-1) {
                index = 0;
                s = s.replace("*", "");
                zigzag = false;
                r = r-1;
                sLen = s.length();
            }
            move = (r-1)*2;
            newS = newS + s.charAt(index);
            if (index == sLen-1) {
                s = s.substring(0, index) + "*";
            }
            else {
                s = s.substring(0, index) + "*" + s.substring(index+1);
            }
            if (r == numRows) {
                index = index + move;
            }
            else {
                if (zigzag) {
                    index = index + 1;
                    zigzag = false;
                }
                else {
                    index = index + move;
                    zigzag = true;
                }
            }
        }
        return newS + s.replace("*", "");
    }
}