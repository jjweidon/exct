import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        List<Robot> robots = new ArrayList<>();
        for (int[] rts : routes) {
            Pos pos = new Pos(points[rts[0]-1]);
            Robot robot = new Robot(pos);
            
            for (int j = 1; j < rts.length; j++) {
                Pos target = new Pos(points[rts[j]-1]);
                robot.move(target);
            }
            robots.add(robot);
        }
        
        int answer = 0;
        int maxSize = robots.stream()
            .mapToInt(r -> r.getPosList().size())
            .max()
            .orElse(0);
        
        for (int i = 0; i < maxSize; i++) {
            Set<String> visited = new HashSet<>();
            Set<String> duplicated = new HashSet<>();
            for (Robot robot : robots) {
                List<Pos> posList = robot.getPosList();
                if (i >= posList.size()) continue;
                Pos pos = posList.get(i);
                String key = pos.getY() + "," + pos.getX();
                if (!visited.add(key)) {
                    duplicated.add(key);
                }
            }
            answer += duplicated.size();
        }
        
        
        return answer;
    }
    
    class Robot {
        private Pos pos;
        private List<Pos> posList;
        
        public Robot(Pos pos) {
            this.pos = pos;
            posList = new ArrayList<>();
            posList.add(pos);
        }
        
        public Pos getPos() {
            return this.pos;
        }
        
        public List<Pos> getPosList() {
            return this.posList;
        }
        
        public void move(Pos target) {
            int cur_y = this.pos.getY();
            int cur_x = this.pos.getX();
            int tar_y = target.getY();
            int tar_x = target.getX();

            int step_y = Integer.compare(tar_y, cur_y);
            int step_x = Integer.compare(tar_x, cur_x);
            
            while (cur_y != tar_y || cur_x != tar_x) {
                if (cur_y != tar_y) cur_y += step_y;
                else if (cur_x != tar_x) cur_x += step_x;
                
                Pos new_pos = new Pos(cur_y, cur_x);
                posList.add(new_pos);
            }
            
            this.pos = new Pos(tar_y, tar_x);
        }
        
    }
    
    class Pos {
        private int y;
        private int x;
        
        public Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
        
        public Pos(int[] pos) {
            this.y = pos[0];
            this.x = pos[1];
        }
        
        public int getY() {
            return this.y;
        }
        
        public int getX() {
            return this.x;
        }
    }
}