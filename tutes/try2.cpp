#include <iostream>

using namespace std;
class nd
{
    int data;
    nd* next;
    nd* head=NULL;
    bool isCircular=false;
    int *table=new int[1001];
    nd* ndTable[1001];
    int N=0;
    public:
    int* getTable()
    {
        return table;
    }
    nd()
    {
        for(int i=0;i<1001;i++) {table[i]=0;};
        for(int i=0;i<1001;i++){ndTable[i]=NULL;}
    }
    
    void i0(int x)
    {
        nd* temp2=new nd;
        temp2->data=x;
        temp2->next=NULL;
        ndTable[x]=temp2;
        N++;
    
        if(head==NULL)
        {
            head=temp2;
            table[head->data]=0;
            return;
        }
    
        nd* temp=head;
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=temp2;
    }

    void srch(int y,int x)
    {
        N++;
        if(Search(y))
            insert_after(y,x);
        else
            insert_before(y,x);
    }
    
    void i2(int x,int y,int z)
    {
       nd* temp2=new nd;
       temp2->data=z;
       temp2->next=NULL;
       ndTable[z]=temp2;
       int distance=0;
       nd* temp=head;
       while(temp->data!=x)
       {
        temp=temp->next;
       }
       nd* Initial=temp;
       while(temp->data!=y)
       {
        temp=temp->next;
        distance++;
       }
       distance/=2;
       while(distance!=0)
       {
        Initial=Initial->next;
        distance--;
       }
       temp2->next=Initial->next;
       Initial->next=temp2;
       N++;
    }

    bool Search(int x)
    {
        nd* temp=head;
        while(temp!=NULL)
        {
            if(temp->data==x)
            {
                return true;
            }
            temp=temp->next;
        }
        if(temp==NULL) 
            return false;
    
    }

    void print()
    {
        nd* temp=head;
        while(temp!=NULL)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
    }

    void u(int x,int p)
    {
        if(Search(x)==false)
        {
            return;
        }
        
        nd* temp=ndTable[x];
    	while(p!=0)
    	{
    		if(temp->next==NULL)
    		{ 
    		    temp->next=head;
    		    temp=head;
        	    isCircular=true;
        	    p--;
    		}
    		else
    		{ 
    		    temp=temp->next; 
    		    p--;
    		}
        }
    	ndTable[x]->next=temp;
    }
    
    void insert_before(int y,int x)
    {
        nd* temp=new nd;
        temp->data=y;
        temp->next=NULL;
        ndTable[y]=temp;
    	if(head->data==x)
    	{
            temp->next=head;
            head=temp;
            return;
        }
        nd* temp2=head;
        while(temp2->next->data!=x)
        {
            temp2=temp2->next;
        }
        temp->next=temp2->next;
        temp2->next=temp;
    }

    void insert_after(int y,int x)
    {
        nd* temp=new nd;
        temp->data=x;
        temp->next=NULL;
        ndTable[x]=temp;
        nd* temp2=head;
        while(temp2->data!=y)
        {
            temp2=temp2->next;
        }
        temp->next=temp2->next;
        temp2->next=temp;
    }
    
    void Genratetable()
    {
        for(int i=1;i<1001;i++)
        {
           if(ndTable[i]!=NULL)
           {
                if(ndTable[i]->next!=NULL)
                {
                    table[ndTable[i]->next->data]++;
                }
           }
        }
    }

    void printtable()
    {
        for(int i=1;i<10;i++)
        {
            cout<<i<<" "<<table[i]<<endl;
        }
    }
    bool circular()
    {
        return isCircular;
    }
    int len()
    {
        return N;
    }
};
int main()
{
    nd A;
    int N;
    cin>>N;
    char a;
    int b;
    for(int i=0;i<N;i++)
    {
        cin>>a;
        cin>>b;
        if(a=='I' && b==0)
        {
            int x;
            cin>>x;
            A.i0(x);
        }
        else if(a=='I' && b==1)
        {
            int x,y;
            cin>>x>>y;
            A.srch(x,y);
        }

        else if(a=='I' && b==2)
        {
            int x,y,z;
            cin>>x>>y>>z;
            A.i2(x,y,z);
        }
        else if(a=='U')
        {
            int p;
            cin>>p;
            A.u(b,p);
        }
    }
    A.Genratetable();
    int* ansTable=A.getTable();
    int countMultiple=0;
    if(A.circular())
        cout<<1<<endl;
    else
        cout<<0<<endl;
    for(int i=1;i<=1000;i++)
    {
        if(ansTable[i]>=2) 
        {
            countMultiple++;
        }
    }
    if(countMultiple==0) 
    { 
        cout<<"0"<<endl; A.print();
    }
    else 
    {
            cout<<countMultiple<<endl;
        for(int i=1;i<=1000;i++)
        {
            if(ansTable[i]>=2) cout<<i<<" ";
        }
        cout<<endl;
        for(int i=1;i<=1000;i++)
        {
            if(ansTable[i]>=2) cout<<ansTable[i]<<" ";
        }
    }
    cout<<endl;
}