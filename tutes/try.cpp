#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;


struct Node
{
  short int data;
  Node *next;
  public :
    Node(short int initialData){
        data=initialData;
        next=NULL;
    }
};
class LinkedList
{
  Node *head;
public:
    LinkedList ()
  {
    head = NULL;
  }
    Node* getHead(){
        return head;
    }
  void print(){
    Node *itr=head;

        while(itr != NULL){
            cout<<itr->data<<" ";
            itr=itr->next;

            /*
            if(itr == NULL  || itr == head)
                break;
                */
        }

        cout<<endl;



  }

  void insertAtEnd (short int data)
  {
     Node* itr=head;
     Node* newNode=new Node(data);

     if(itr!=NULL){
        while(itr->next != NULL && itr->next != head){
            itr=itr->next;
        }
        if(itr->next==head){
            newNode->next=head;
        }
        itr->next=newNode;

     }else{
        head=newNode;
     }
  }

  void middleInsert(short int startValue,short int endValue,short int midValue){
    Node* itr=head;
    Node* startPtr=isExist(startValue);
    short int diff=0;
    bool flag=false;

    while(itr->data!=endValue){
        if(itr->data==startValue  &&  flag==false){
            flag=true;
            startPtr=itr;
        }
        if(flag){
            diff++;
        }
        itr=itr->next;
    }

    for(int i=0;i<(diff-1)/2;i++){
        startPtr=startPtr->next;
    }
    Node *newNode=new Node(midValue);
    newNode->next=startPtr->next;
    startPtr->next=newNode;
  }


  void interchangeInsert(short int arg1 , short int arg2){
    Node *arg1Ptr=isExist(arg1);
    Node *itr=head;
    if(arg1Ptr!=NULL){
        Node* newNode=new Node(arg2);
        newNode->next=arg1Ptr->next;
        arg1Ptr->next=newNode;
    }else{
    //assuming arg2 exists
     Node* newNode=new Node(arg1);


        if(itr == NULL)
            return;

        if(head->data == arg2){
            newNode->next=head;
            head=newNode;
            return;
        }

        while(itr->next != NULL && itr->next->data != arg2){
            itr=itr->next;
        }


                newNode->next=itr->next;
                itr->next=newNode;

      /*
        if(itr != NULL){
        while(itr->next != NULL && itr->next->data!=arg2){
            itr=itr->next;
        }
        }
    */


    }
    }



  Node* isExist(short int value){
        Node *returnPtr=NULL;
        Node *itr=head;
        while(itr != NULL){
            if(itr->data == value){
                returnPtr=itr;
                break;
            }
            if(itr->next == NULL || itr->next == head){
                break;
            }
            itr=itr->next;
        }
        return returnPtr;
  }
};

class Processor
{
  bool isCircular;
  vector<short int> addr;
  LinkedList linkedList;
  short int numOperations;


public:
    Processor ()
  {
    isCircular = false;
    cin >> numOperations;
  }
  void start ()
  {

    char opCode;
    short int numCode;
    short int arg[3];

    for (int i = 0; i < numOperations; i++)
      {
	cin >> opCode;
	cin >> numCode;
	cin >> arg[0];
	if (opCode == 'U')
	  {
	    linkingOperation(numCode,arg[0]);
	    //linkedList.print();
	    //linkedList.print();
	  }
	else
	  {
	    switch (numCode)
	      {
            case 1:
                cin >> arg[1];
                linkedList.interchangeInsert(arg[0],arg[1]);
                //linkedList.print();
                break;
            case 2:
                cin >> arg[1];
                cin >> arg[2];
                linkedList.middleInsert(arg[0],arg[1],arg[2]);
                //linkedList.print();
                break;
            case 0:
                linkedList.insertAtEnd(arg[0]);
                //linkedList.print();
                break;
	      }
	  }
      }
  }
  void output(){
        if(isCircular){
            cout<<"1"<<endl;
        }else{
            cout<<"0"<<endl;
        }

        vector<short int> uniqueElements;
        uniqueElements.reserve(addr.size());
        vector<short int> frequency;
        frequency.reserve(addr.size());
            //contents
            for(auto i=addr.begin();i != addr.end(); i++){
                if(count(uniqueElements.begin(),uniqueElements.end(),*i)){
                }
                else{
                    //if(linkedList.isExist(*i) != NULL)
                     uniqueElements.push_back(*i);
                }

            }


        if(uniqueElements.size() == 0){
            cout<<"0"<<endl;
        }else{
            cout<<uniqueElements.size()<<endl;
        }


        if(addr.size() == 0){
            linkedList.print();
        }else{

            for( auto i=uniqueElements.begin(); i != uniqueElements.end() ; i++){
                cout<<*i<<" ";
                frequency.push_back(count(addr.begin(),addr.end(),*i));
            }
            cout<<endl;
            //frequency
             for( auto i=frequency.begin(); i != frequency.end() ; i++){
                cout<<*i+1<<" ";
            }
            cout<<endl;

        }




  }

  void linkingOperation(short int a,short int b){
    Node* head=linkedList.getHead();
    Node* startPtr=linkedList.isExist(a);

    //a must exist
    if(startPtr != NULL  && b!=0){
        Node* itrPtr=startPtr;
        //bool isLinkedAlready=false;



        for(int i=0;i<b;i++){
            if(itrPtr->next == NULL){
                isCircular=true;
                //itrPtr=head;
                itrPtr->next=head;
            }
            //else{
                itrPtr=itrPtr->next;
            //}
        }

        if(startPtr->next == itrPtr){
            return;
        }



        int occurence=count(addr.begin(),addr.end(),startPtr->next->data);
        if(occurence){
              auto deleteItr = find(addr.begin(),addr.end(),startPtr->next->data);
              addr.erase(deleteItr);
        }

        startPtr->next=itrPtr;

        addr.push_back(itrPtr->data);
    }

  }

};

int main ()
{
  // your code goes here
  ios_base::sync_with_stdio (false);
  cin.tie(NULL);


  Processor p;
  p.start();
  p.output();

  return 0;
}

