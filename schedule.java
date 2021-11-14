import java.util.Scanner;
public class schedule{
    public static void main(String[] argv){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        String[] nameList = new String[n];
        String[] timeList = new String[n];
        int[] numList = new int[n];
        String[] total = new String[3];
        System.out.println("1");
        for (int i = 0;i < n;i++){
            total = input.next().split("");
            print(total);
            for (int j = 0;j < 3;j++){
                if (j == 0)
                    nameList[i] = total[0];
                if (j == 1)
                    timeList[i] = total[1];
                if (j == 2)
                    numList[i] = total[2];
            }
        }
        print(nameList,timeList,numList);
    }
    
    public static void print(String[] nameList,String[] timeList,int[] numList){
        for (int i = 0;i < nameList.length;i++)
            System.out.println(nameList[i]+" "+timeList[i]+" "+numList[i]);
    }
}
    
    