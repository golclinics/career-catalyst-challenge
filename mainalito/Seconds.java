package mainalito;

public class Seconds{
    public static int convertToSeconds(int s){
        return s*60;
    }
    public static void main(String[] args){
        System.out.println(convertToSeconds(2));
    }
}