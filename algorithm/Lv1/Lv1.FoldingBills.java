package Lv1;

import java.util.*;
import java.io.*;

class FoldingBills {
    public int main(int[] wallet, int[] bill) {
        int maxWallet = Arrays.stream(wallet).max().getAsInt();
        int minWallet = Arrays.stream(wallet).min().getAsInt();
        int maxBill = Arrays.stream(bill).max().getAsInt();
        int minBill = Arrays.stream(bill).min().getAsInt();
        
        int answer = 0;
        while (maxBill > maxWallet || minBill > minWallet){
            if (bill[0] > bill[1]){
                bill[0] = bill[0]/2;
            } else {
                bill[1] = bill[1]/2;
            };
            maxBill = Arrays.stream(bill).max().getAsInt();
            minBill = Arrays.stream(bill).min().getAsInt();
            answer++;
        }
            
        return answer;
    }
}