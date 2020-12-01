package Java.Easy;

// ne pas modifier Monnaie
class Monnaie {
    long piece2 = 0;
    long billet5 = 0;
    long billet10 = 0;
}

class monnaieOptimale {
    
    // ne pas modifier la signature de cette​​​​​​‌​​​‌‌‌‌​​​‌‌​​​‌​‌‌‌​‌​​ méthode
    static Monnaie monnaieOptimale(long s)
    {
        Monnaie c = new Monnaie();
        if(s==1 || s==3){return null;}
        if(s>=10)
        {
            c.billet10=(long) s/10;
            if((s%10)%5!=0)
            {
                c.billet5 = (long) (s%10)/5;
                if(((s%10)%5)%2==0)
                {
                    c.piece2=(long) ((s%10)%5)/2;
                }
                else
                {
                    if((s%10)%2==0)
                    {
                        c.billet5 = 0;
                        c.piece2 = (s%10)/2;
                    }
                }
            }
            else
            {
                if((s%10)%5==0)
                {
                    c.billet5=(long) (s%10)/5;
                }
                else
                {
                    if((s%10)%2 ==0)
                    {
                        c.piece2 = (long) (s%10)/2;
                    }
                }
            }

        }
        else
        {
            if(s>=5)
            {
                c.billet5 = (long) s/5;
                if((s%5)%2 == 0)
                {
                    c.piece2 = (long) (s%5)/2;
                }
                else
                {
                    if(s%2==0)
                    {
                        c.billet5=0;
                        c.piece2= s/2;
                    }
                }

            }
            else
            {
                if(s>=2)
                {
                    c.piece2 = (long) s/2;
                }
            }
        }
        return c;

    }
}