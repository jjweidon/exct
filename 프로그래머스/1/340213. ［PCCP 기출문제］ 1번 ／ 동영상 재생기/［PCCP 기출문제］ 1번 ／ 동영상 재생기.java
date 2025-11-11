import java.io.*;
import java.util.*;

class Solution {
    
    private static int curSecond;
    private static int startSecond;
    private static int endSecond;
    private static int videoLenSecond;
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) throws IOException {
        
        curSecond = msToSecond(sToMS(pos));
        startSecond = msToSecond(sToMS(op_start));
        endSecond = msToSecond(sToMS(op_end));
        videoLenSecond = msToSecond(sToMS(video_len));
        executeSkip();
        
        for (String cmd : commands) {
            if (cmd.equals("prev")) {
                executePrev();
            }
            if (cmd.equals("next")) {
                executeNext();
            }
            executeSkip();
        }
        
        return secondToS(curSecond);
    }
    
    private static int[] sToMS(String s) {
        String[] ms = s.split(":");
        int mm = Integer.parseInt(ms[0]);
        int ss = Integer.parseInt(ms[1]);
        return new int[] {mm, ss};
    }
    
    private static int msToSecond(int[] ms) {
        return ms[0] * 60 + ms[1];
    }
    
    private static String secondToS(int second) {
        int mm = second / 60;
        int ss = second % 60;
        return String.format("%02d:%02d", mm, ss);
    }
    
    private static void executeSkip() {
        if (curSecond >= startSecond && curSecond <= endSecond) {
            curSecond = endSecond;
        }
    }
    
    private static void executePrev() {
        curSecond -= 10;
        if (curSecond < 0) {
            curSecond = 0;
        }
    }
    
    private void executeNext() {
        curSecond += 10;
        if (curSecond > videoLenSecond) {
            curSecond = videoLenSecond;
        }
    }
}