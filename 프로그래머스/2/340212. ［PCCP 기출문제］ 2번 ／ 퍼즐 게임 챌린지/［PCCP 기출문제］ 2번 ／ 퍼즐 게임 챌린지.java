import java.util.*;
import java.io.*;

class Solution {
    private static int[] diffs;
    private static int[] times;
    private static long limit;
    private static int N;
    
    public int solution(int[] diffs, int[] times, long limit) {
        this.diffs = diffs;
        this.times = times;
        this.limit = limit;
        this.N = diffs.length;
        
        int answer = 0;
        int left = Arrays.stream(diffs).min().getAsInt();
        int right = Arrays.stream(diffs).max().getAsInt();
        
        while (left <= right) {
            int mid = (int) (left + right) / 2;
            if (isPassed(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private static boolean isPassed(int level) {
        long totalTime = 0;
        for (int i = 0; i < N; i++) {
            if (diffs[i] <= level) {
                totalTime += times[i];
            } else {
                if (i == 0) {
                    totalTime += (diffs[i] - level) * (times[i]) + times[i];
                } else {
                    totalTime += (diffs[i] - level) * (times[i] + times[i-1]) + times[i];
                }
            }
        }
        if (totalTime <= limit) return true;
        else return false;
    }
}