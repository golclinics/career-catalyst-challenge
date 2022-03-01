public class Summation{
  public double addition(double a, double b){
   double sum = 0;
   sum = a + b;
   
   return sum;
  }

  public static void main(String[] args){
    Summation summation = new Summation();
    System.out.println(summation.addition(3, 2));
    System.out.println(summation.addition(-3,-6));
    System.out.println(summation.addition(7, 3));
 }
}
