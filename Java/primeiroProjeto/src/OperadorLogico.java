public class OperadorLogico {
    public static void main(String[] args) {
        int n1, n2, n3;
        n1 = 3;
        n2 = 4;
        n3 = 5;
        boolean res;
        res = (n1 <= n2 && n2 <= n3)?true:false;
        System.out.println(res);
    }
}
