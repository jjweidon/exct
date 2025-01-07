import java.io.*;
import java.util.Arrays;

public class p2063 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(bf.readLine());
        Integer[] arr = Arrays.stream(bf.readLine().split(" "))
                .map(Integer::parseInt)
                .toArray(Integer[]::new);

        Arrays.sort(arr);

        int median = arr[N / 2];
        bw.write(median + "\n");
        bw.flush();
        bw.close();
    }
}