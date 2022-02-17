package com.company;

public class conversion {

    //Function to convert to seconds
    private static void convertSeconds(int n){
        int seconds;

        seconds = n * 60;

        System.out.println("convert(" + n + ")->" + seconds);
    }

    public static void main(String[] args){
        int n = 5;
        convertSeconds(n);
    }

}
