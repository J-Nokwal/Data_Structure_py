#include <bits/stdc++.h>

using namespace std;

class MultiLinked {
	
	public:
	
	
	int VALUESTORED;
	
	map <MultiLinked*, int> a;
	
	map <int, MultiLinked*> z;
	
	MultiLinked *NEXT_POINTER;
	
	void insert_after(int y, int x, MultiLinked* startingpointer){
		
		
		MultiLinked* new_pointer = new MultiLinked, *TEMPORARY = startingpointer;
		
		
		new_pointer -> VALUESTORED = x;
		
		
		new_pointer -> NEXT_POINTER = NULL;
		
		
		while(TEMPORARY -> VALUESTORED != y){
			
			
			TEMPORARY = TEMPORARY -> NEXT_POINTER;
			
			
		}
		new_pointer -> NEXT_POINTER = TEMPORARY -> NEXT_POINTER;
		
		
		TEMPORARY -> NEXT_POINTER = new_pointer;
		
		
		a[new_pointer]++;
		
		
		z[x] = new_pointer;
	}
	
	
	
	
	void INSERTION_AT_BEGINNING(int x, MultiLinked*& startingpointer){
		
		
		MultiLinked* new_pointer = new MultiLinked;
		
		
		new_pointer -> NEXT_POINTER = NULL;
		
		
		new_pointer -> VALUESTORED = x;
		
		
		if(startingpointer == NULL){
			
			startingpointer = new_pointer;
			
			
			z[x] = new_pointer;
			
		}
		else{
			
			a[startingpointer]++;
			
			
			new_pointer -> NEXT_POINTER = startingpointer;
			
			
			z[x] = new_pointer;
		}
	}
	
	void ins_end(int x, MultiLinked*& startingpointer){
		
		
		MultiLinked* new_pointer = new MultiLinked, *TEMPORARY = startingpointer;
		
		
		new_pointer -> VALUESTORED = x;
		
		
		new_pointer -> NEXT_POINTER = NULL;
		
		
		if(startingpointer == NULL){
			
			
			z[x] = new_pointer;
			
			startingpointer = new_pointer;
			
			
		}
		
		else{
			while(TEMPORARY -> NEXT_POINTER != NULL){
				
				
				TEMPORARY = TEMPORARY -> NEXT_POINTER;
				
				
			}
			TEMPORARY -> NEXT_POINTER = new_pointer;
			
			
			a[new_pointer]++;
			
			
			z[x] = new_pointer;
		}
	}
	
	
	void INSERTION_BEFORE(int x, int y, MultiLinked* &startingpointer){
		
		
		MultiLinked* new_pointer = new MultiLinked, *TEMPORARY = startingpointer;
		
		
		new_pointer -> VALUESTORED = y;
		
		
		new_pointer -> NEXT_POINTER = NULL;
		
		
		if(startingpointer -> VALUESTORED == x){
			
			
			new_pointer -> NEXT_POINTER = startingpointer;
						
			
			startingpointer = new_pointer;
			
			
			z[y] = startingpointer;
			
			
			return;
		}
		while(TEMPORARY -> NEXT_POINTER -> VALUESTORED != x){
			
			TEMPORARY = TEMPORARY -> NEXT_POINTER;
			
		}
		new_pointer -> NEXT_POINTER = TEMPORARY -> NEXT_POINTER;
		
		
		TEMPORARY -> NEXT_POINTER = new_pointer;
		
		
		a[new_pointer]++;
		
		
		z[y] = new_pointer;
	}
	
	void middle_insert(int Z, int y, int x, MultiLinked* startingpointer){
		
		
		MultiLinked *Once, *Twice, *TEMPORARY;
		
		MultiLinked* new_pointer = new MultiLinked;
		
		
		new_pointer -> VALUESTORED = x;
		
		TEMPORARY = startingpointer;
		
		
		while(TEMPORARY -> VALUESTORED != Z){
			
			
			TEMPORARY = TEMPORARY -> NEXT_POINTER;
			
			
		}
		
		Once = TEMPORARY;
		
		Twice = TEMPORARY;
		
		
		while(Twice -> NEXT_POINTER && Twice -> NEXT_POINTER -> VALUESTORED != y){
			
			Twice = Twice -> NEXT_POINTER -> NEXT_POINTER;
			
			Once = Once -> NEXT_POINTER;
			
		}
		new_pointer -> NEXT_POINTER = Once -> NEXT_POINTER;
		
		
		Once -> NEXT_POINTER = new_pointer;
		
		
		a[new_pointer]++;
		
		
		z[x] = new_pointer;
	}
		
		void NodeAfterPPositions (int x, int positions, MultiLinked *fstartingpointer, MultiLinked *startingpointer){
	
			MultiLinked *TEMPORARY = fstartingpointer;
			
			
			if(TEMPORARY -> NEXT_POINTER){
				
				
				a[TEMPORARY -> NEXT_POINTER]--;
				
				
			}
			
			
		 MultiLinked *OriginalPointer = TEMPORARY;
		
				
				while(positions){
					
					
					if(TEMPORARY -> NEXT_POINTER == NULL){
						
						
						TEMPORARY -> NEXT_POINTER = startingpointer;
						
						
						TEMPORARY = startingpointer;
						
						
						a[startingpointer]++;
						
						
						positions--;
						
					}
			else{
				
				
				TEMPORARY = TEMPORARY -> NEXT_POINTER;
				
				
				positions--;
			}
		}
		a[TEMPORARY]++;
		
		
		OriginalPointer -> NEXT_POINTER = TEMPORARY;
	}
	
	void print_L(MultiLinked *startingpointer){
		while(startingpointer){
			
			
			cout << startingpointer -> VALUESTORED << " ";
			
			
			startingpointer = startingpointer -> NEXT_POINTER;
			
			
				}
				cout << "\n";
			}
			
			int check_circular(MultiLinked *startingpointer){
				
				
				MultiLinked *TEMPORARY = startingpointer;
				
				
				vector<int> S;
				
				int tempo = 0;
				
		
		while(TEMPORARY){
			
			
			if(find(S.begin(), S.end(), TEMPORARY -> VALUESTORED) == S.end()){
				
				
				S.push_back(TEMPORARY -> VALUESTORED);
				
				
			}
			else{
				
				
				tempo = 1;
							
							
							break;
							
							
						}
						
						
						TEMPORARY = TEMPORARY -> NEXT_POINTER;
						
					
					}
					
					return tempo;
		
	}
	
	
		int if_exists (int x, MultiLinked* startingpointer){
		
		
		MultiLinked *TEMPORARY = startingpointer;
		
		
				while(TEMPORARY){
					
					
					if(TEMPORARY -> VALUESTORED == x){
						
						
						return 1;
						
						
					}
					
					TEMPORARY = TEMPORARY -> NEXT_POINTER;
				
				}
				
				return 0;
			
			}
			
};

MultiLinked *startingpointer = NULL;

int main(){
	
			vector <int> elements_output;
			
			int multiplenodes = 0;
			
			
			startingpointer = NULL;
			
			
			int n;
			
			
			cin >> n;
			
			
			MultiLinked *O = new MultiLinked;
			
			
			while(n--){
				
		
		char UserCharacter;
		
			
			cin >> UserCharacter;
			
			
			if(UserCharacter == 'U'){
				
				int x, p;
				
				
				cin >> x >> p;
				
				
				O -> NodeAfterPPositions(x, p, O -> z[x], startingpointer);
			}
			else{
				int q;
				
				
				cin >> q;
				
				
				if(q == 0){
					
				int x;
				
				
				cin >> x;
				
				
				O -> ins_end(x, startingpointer);
				
				
			}
			else if(q == 1){
				
				
				int y, x;
				
				
				cin >> y >> x;
				
						
						if(O -> if_exists(y, startingpointer)){
							
							
							O -> insert_after(y, x, startingpointer);
							
							
						}
						else{
							
							
							O -> INSERTION_BEFORE(x, y, startingpointer);
					
					
				}
			}
			else{
				
				
				int z, y, x;
				
				
					cin >> z >> y >> x;
					
					
					O -> middle_insert(z, y, x, startingpointer);
			}
			
			
		}
		
		
	}
		
	cout << O -> check_circular(startingpointer) << "\n";
	
	

		sort(elements_output.begin(), elements_output.end());
		
	
	
	cout << multiplenodes << "\n";
	
	
			
			if(multiplenodes == 0){
				
				O -> print_L(startingpointer);		
		
	}
	else{
		for(int i = 0 ; i <  elements_output.size(); i++){
			
			cout << elements_output[i] << " ";
			
		}
		
		cout << "\n";
	}
	
	if(multiplenodes != 0){
				
				for(int i = 0 ; i <  elements_output.size(); i++){
					
					int elementsoutputment = elements_output[i];
			
							cout << O -> a[O -> z[elementsoutputment]] << " ";
			
		}
		
		cout << "\n";
		
	}
}