import java.util.HashMap;

public class SlidingWindows {

    public int lengthOfLongestSubstring(String s) {

        int left = 0;
        int right;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        int maxSubst = Integer.MIN_VALUE;

        if (s.isEmpty()) return 0;
        if (s.length() == 1) return 1;

        for (right=0; right<s.length(); right++){

            if (!hashMap.containsKey(s.charAt(right))) {
                hashMap.put(s.charAt(right), right);

            } else {

                if (hashMap.size() >= maxSubst){
                    maxSubst = hashMap.size();
                }

                while (s.charAt(left) != s.charAt(right)){
                    hashMap.remove(s.charAt(left));
                    left++;
                }
                hashMap.remove(s.charAt(left));
                hashMap.put(s.charAt(right), right);
                left++;
            }
        }
        return Math.max(maxSubst, hashMap.size());
    }

    public static void main(String[] args) {
        SlidingWindows SlidingWindows = new SlidingWindows();
        String test = "pwwkew";
        System.out.println(SlidingWindows.lengthOfLongestSubstring(test));
    }
}
