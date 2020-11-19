using System;
namespace CShap
{
    class Change{
        public long coin2 = 0;
        public long bill5=0;
        public long bill10 = 0;
        public Change()
        {
            this.coin2 = 0;
            this.bill5 = 0;
            this.bill10=0;
        }
    }

    class MoneyBack{
        public static Change ChangeOptimal(long s)
        {
            Change c = new Change();
            if(s==1 || s==3){return null;}
            if(s>=10)
            {
                c.bill10=(long) s/10;
                if((s%10)%5!=0)
                {
                    c.bill5 = (long) (s%10)/5;
                    if(((s%10)%5)%2==0)
                    {
                        c.coin2=(long) ((s%10)%5)/2;
                    }
                    else
                    {
                        if((s%10)%2==0)
                        {
                            c.bill5 = 0;
                            c.coin2 = (s%10)/2;
                        }
                    }
                }
                else
                {
                    if((s%10)%5==0)
                    {
                        c.bill5=(long) (s%10)/5;
                    }
                    else
                    {
                        if((s%10)%2 ==0)
                        {
                            c.coin2 = (long) (s%10)/2;
                        }
                    }
                }

            }
            else{
                if(s>=5)
                {
                    c.bill5 = (long) s/5;
                    if((s%5)%2 == 0)
                    {
                        c.coin2 = (long) (s%5)/2;
                    }
                    else
                    {
                        if(s%2==0)
                        {
                            c.bill5=0;
                            c.coin2= s/2;
                        }
                    }

                }
                else
                {
                    if(s>=2)
                    {
                        c.coin2 = (long) s/2;
                    }
                }
            }
            return c;

        }
        public static void Main(String[] args)
        {
            Change c = ChangeOptimal(159);
            Console.WriteLine("Coin(s) 2€ : "+c.coin2);
            Console.WriteLine("Bill(s)) 5€ : "+c.bill5);
            Console.WriteLine("Bill(s) 10€ : "+c.bill10);
            Console.WriteLine("Total amount : "+(long) ((c.coin2*2)+(c.bill5*5)+(c.bill10*10)));
        }
    }
}
