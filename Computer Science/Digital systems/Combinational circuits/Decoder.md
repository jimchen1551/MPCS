---
Created: [[2022-07-16]]
Aliases: 
Types: Card
Tags: 
- 
---
# Decoder
![[Pasted image 20220619022359.png]]
$$X'Y'Z'=m_0=D_0$$$$\dots$$$$XYZ=m_7=D_7$$
- turning binary codes into [[Minterm]]s
## Decoder expansion
- While the # of inputs increased, there were 2 solutions for the decoder. 
1. Enlarge each [[And]] gate
   - bringing about a high gate input count, which caused significant latency in the circuit
   - causing the huge area of the chip
![[slide_45.jpg]]
2. Use [[Hierarchical Design]] and collections of [[And]] gate
   - preventing the problems in solution 1
![[slide_46.jpg]]

### General algorithm
```C++
class ANDs{
	int num_AND; 
	vector inputs;
	vector outputs; 
	void in(vector in){
		inputs = in;
	}
	void out(vector out){
		outputs = out;
	}
	vector get_in(){
		return inputs;
	}
	vector get_out(){
		return outputs;
	}
	ANDs(int num){
		num_AND = num;
	}
};
int k = n; 
while (k!=1){
   ANDs K(2^k);
   if (k % 2 = 0) {
	   ANDs K_0(2^(k/2));
	   ANDs K_1(2^(k/2));
	   k = k/2;
   }
   else{
	   ANDs K_0(2^((k-1)/2));
	   ANDs K_1(2^((k+1)/2));
	   k = k+1/2;
   }
   K.in(K_0.get_out(), K_1.get_out());
}
```

## Decoder with enable input
![[slide_21.jpg]]