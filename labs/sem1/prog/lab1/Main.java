import java.util.Random;

public class Main {
    public static boolean check(short x) {
        short[] w = new short[]{4, 8, 10, 14, 16, 18};
        boolean f = false;
        for (short i : w) {
            if (i == x) {
                f = true;
            }
        }
        return f;
    }

    public static void beautifulOutput(double[][] z) {
        for (double[] j : z) {
            for (double i : j) {
                String s = String.format("%.3f", i);
                while (s.length() < 11) {
                    s = " " + s;
                }
                System.out.print(s + " ");
            }
            System.out.print('\n');
        }
    }

    public static void defaultOutput(double[][] z) {
        for (double[] j : z) {
            for (double i : j) {
                System.out.printf("%.3f ", i);
            }
            System.out.print('\n');
        }
    }

    public static void main(String[] args) {
        // Подсчёт массива w
        short[] w;
        w = new short[(24 - 2) / 2 + 1];
        int p = 0;
        for (short i = 24; i >= 2; i -= 2) {
            w[p] = i;
            p++;
        }
        // Подсчёт массива x
        Random rand = new Random();
        double[] x;
        x = new double[19];
        for (int i = 0; i < 19; i++) {
            x[i] = rand.nextDouble() * 11 - 6.0;
        }
        // Подсчёт массива z
        double[][] z = new double[12][19];
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 19; j++) {
                if (w[i] == 24) {
                    z[i][j] = Math.atan(Math.cos(Math.pow((1.0 / 4.0) / (0.25 - Math.pow(Math.E, x[j])), x[j] * (x[j] - 1.0 / 3.0))));
                } else if (check(w[i])) {
                    z[i][j] = Math.pow(x[j] * (x[j] + 1.0 / 4.0) - 1, 3) * (Math.pow(Math.cos(x[j]), (Math.pow(x[j], x[j] * (1.0 / 2.0 + x[j]))) / 2.0) + 1);
                } else {
                    z[i][j] = Math.pow(x[j] - (0.25 / 2.0) / (3.0 / 4.0), 3);
                }
            }
        }
        // Вывод
        beautifulOutput(z);
        // defaultOutput(z);
    }
}
