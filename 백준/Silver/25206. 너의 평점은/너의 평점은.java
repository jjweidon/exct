import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        double A = 0; // (학점 × 과목평점)의 합
        double B = 0; // 학점의 총합
        Map<String, Double> grades = Map.of(
            "A+", 4.5,
            "A0", 4.0,
            "B+", 3.5,
            "B0", 3.0,
            "C+", 2.5,
            "C0", 2.0,
            "D+", 1.5,
            "D0", 1.0,
            "F", 0.0,
            "P", 0.0
        );

        for (int i = 0; i < 20; i++) {
            String[] ss = br.readLine().split(" ");
            double score = Double.parseDouble(ss[1]);
            double grade = grades.get(ss[2]);
            if (ss[2].equals("P")) {
                continue;
            }
            A += score * grade;
            B += score;
        }

        bw.write(String.format("%.6f", A / B) + "\n");
        
        bw.flush();
        br.close();
        bw.close();
    }
}