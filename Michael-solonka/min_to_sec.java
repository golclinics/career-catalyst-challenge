class min_to_sec
{
    public static int  convert(int x)
    {
        int z=0;
        z=x*60;
        return z;
    }
   public static void main(String[] args) {
       
   
        int z;
        z=convert(5);
        System.out.println("5 minutes are " +z+" seconds");

        z=convert(3);
        System.out.println("3 minutes are " +z+" seconds");

        z=convert(2);
        System.out.println("2 minutes are " +z+" seconds");
    
       
    }

}
