import java.util.ArrayList;
public class static_and_dynamic{
    public static void main(String args[]){
        int v[]={1,2};  //declearing and initialising

        int[] arr;  //declearing  array or int arr[]
        arr=new int[3]; //instantiating or declaring memory

        System.out.println(arr.length);
        arr[0]=90;
        arr[1]=99;
        arr[2]=999;
     

        //Dynamic Array
        
        ArrayList<Integer> myArray = new ArrayList<Integer>();
        myArray.add(90); //add element in an array
        myArray.add(99);
        myArray.add(67);
        myArray.add(33);
        myArray.set(1,2000);//set the value of index 1 to 2000
        myArray.remove(0); //remove element at index 0 
        for (int number : myArray) {
            System.out.println(number);
        }
        

    }
}


