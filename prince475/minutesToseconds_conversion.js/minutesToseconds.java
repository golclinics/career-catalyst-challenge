import java.util.Scanner;
class minutesToSeconds
{
    public static void main(String[] arg)
    {
        int min,sec;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Minutes");
        min=sc.nextInt();
        sec=minToSec(min);
        System.out.println("Seconds: "+sec);
    }
    static int minToSec(int x)
    {
        return x*60;

    }
}