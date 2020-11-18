package Java.Moyen;

import java.util.*;

class Huffman implements Comparable<Huffman>{
    private String data;
    private int Hz;
    private Huffman right;
    private Huffman left;
    public Huffman(String dt,int frequency) {
        this.data = dt;
        this.Hz = frequency;
        this.right = null;
        this.left = null;
    }
    
    public String getData() {
        return data;
    }
    public int getHz() {
        return Hz;
    }
    public Huffman getLeft() {
        return left;
    }
    public Huffman getRight() {
        return right;
    }
    public void setLeft(Huffman left) {
        this.left = left;
    }
    public void setRight(Huffman right) {
        this.right = right;
    }

    @Override
    public int compareTo(Huffman o) {
        if(this.getHz()>o.getHz()){ return 1;}
        else if(this.getHz()<o.getHz()) {return -1;}
        else{return 0;}
    }
    public String toString()
    {
        if(this.left == null && this.right!=null){return "data : "+this.getData()+" Frequence: "+this.getHz()+ "\n\tnoeud droit:\n\t"+this.right.toString();}
        else if(this.left!=null && this.right==null){return "data : "+this.getData()+" Frequence: "+this.getHz()+ "\n\tnoeud gauche:\n\t"+this.left.toString();}
        else if(this.left==null && this.right == null){return "data : "+this.getData()+" Frequence: "+this.getHz();}
        return "data : "+this.getData()+" Frequence: "+this.getHz()+ "\n\tnoeud droit:\n\t"+this.right.toString()+"\n\tnoeud gauche:\n\t" + this.left.toString();
    }
}

public class HuffmanCode
{
    public static ArrayList<Integer> goThroughNode(Huffman node, String s,ArrayList<Integer>tmp)
    {
        if(node.getRight() == null && node.getLeft() == null)
        { 
            tmp.add(node.getHz()*(s.length()-1));
            return tmp; 
        }
        goThroughNode(node.getLeft(),s+ "0",tmp); 
        goThroughNode(node.getRight(), s + "1",tmp);

        return tmp;
    }
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in); 
        List<Huffman> ls = new ArrayList<Huffman>();
        for(int i=0;i<in.nextInt();i++)
        {
            ls.add(new Huffman(Integer.toString(i),in.nextInt()));
        }
        if(ls.size()==1)
        {
            System.out.println(ls.get(0).getHz());
            in.close();
            return;
        }
        while(ls.size()!=1)
        {
            Collections.sort(ls);
            try{
                Huffman o1 = ls.get(0);
                Huffman o2 = ls.get(1);
                Huffman tmp = new Huffman(o1.getData()+o2.getData(),o1.getHz()+o2.getHz());
                tmp.setRight(o1);
                tmp.setLeft(o2);
                ls.remove(o1);
                ls.remove(o2);
                ls.add(tmp);
            }
            catch(Exception e)
            {
                System.out.println("error in the index");
                continue;
            }

        }
        in.close();
        ArrayList<Integer> tab = goThroughNode(ls.get(0), " ",new ArrayList<Integer>());
        int my_sum = 0;
        for(int i=0;i<tab.size();i++){my_sum+=tab.get(i);}
        System.out.print(my_sum);
    }
}
