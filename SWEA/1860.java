// 진기의 최고급 붕어빵
// D3
package SWEA;

import java.util.*;
import java.io.FileInputStream;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();
            int[] arr = new int[N];
            String str = "Possible";
            for (int i = 0; i<N; i++) arr[i] = sc.nextInt();
            Arrays.sort(arr);
            System.out.printf("#%d ", test_case);
            for (int i = 0; i<N; i++) {
                int cnt;
                cnt = (arr[i] / M) * K - (i + 1);
                if (cnt < 0) {
                    str = "Impossible";
                    break;
                }
            }
            System.out.println(str);
        }
    }
}
