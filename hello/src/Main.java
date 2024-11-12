public class Main {
    public static void main(String[] args) throws Exception {
        int n = 1260;
        int count = 0;

        int[] array = {500,100,50,10};
        
        for (int a : array){
            count += n / a;
            n %= a;
        }
        System.out.println(count);
    }
}
