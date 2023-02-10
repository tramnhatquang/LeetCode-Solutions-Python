import java.util.*;

class Question1 {

    static String findDay(String day, int k) {
        String[] days = { "mon", "tue", "wed", "thu", "fri", "sat", "sun" };
        int current = 0;

        for (int i = 0; i < days.length; i++) {
            if (day.equals(days[i])) {
                current = i;
                break;
            }
        }
        int nextDay = (current + k) % 7;
        return days[nextDay];

    }

    public static void main(String[] args) {
        System.out.println(findDay("wed", 2)); // fri
        System.out.println(findDay("wed", 3)); // sat
        System.out.println(findDay("mon", 7)); // mon

    }
}