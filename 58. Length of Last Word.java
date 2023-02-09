class Solution {
    public int lengthOfLastWord(String s) {
        // Trimming the trailing spaces and count characters from the back
        int length = 0, n = s.length() - 1;
        while (n >= 0 && s.charAt(n) == ' ') {
            n--;
        }

        // count the last word
        while ( n >= 0  && s.charAt(n) != ' ') {
            length++;
            n--;
        }

        return length;
    }
}