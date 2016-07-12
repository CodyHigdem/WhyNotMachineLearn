#Octave

Prototyping languages tend to be easy to use octave,matlab, python, R
##Basic Operations
elementary math
5+6
returns 11
3-2
5*8
1/2
2^6

1 == 2 
returns 0 (false)
% comment

1 ~=2
returns 1 (true)


1 && 0 
%and

1 || 0
% or

xor(1,0)
% true

To Change the string in Octove
PS1('>> ');

###variables

a = 3
%a is not equal to 3

a = 3; %semi colon supressing output

b = 'hi';
%reutnrs hi

c  = (3>=1)
%returns true

a = pi;
just type a and it prints out
disp(a);
%'display a'
disp(sprintf('2 decimals: %0.2f', a))
%returns: 2 decimals: 3.24

dis(sprintf('6 decimals: %0.6f',a))
%returns 3.141593

format long

format short
these will alter decimal places

matrix
A = [1 2; 3 4; 56]
Returns

1 2
3 4
5 6

A = [1 2;
3 4;
5 6]
returns A same

v = [1 2 3]
returns 1 2 3

v = [1; 2; 3]
returns
1
2
3

To set the start number and iterate through. 

v = 1:0.1:2
returns:
Columns 1 through 7:
1.000 1.1000 1.2000 1.3000 1.4000 1.5000 1.6000

Columns 8 through 11:
1.7000 1.8000 1.9000 2.0000

v = 1:6
Returns:
1 2 3 4 5 6

ones(2,3)
Creates a two by three matrix that is a matrix of all ones
Returns:
1 1 1
1 1 1

C = 2*ones(2,3)
returns
2 2 2 
2 2 2

faster than c = [2 2 2; 2 2 2]

w = ones(1,3)
returns
1 1 1 
w = zeroes(1,3)
0 0 0

w = rand(1,3)

returns random numbers

Returns:
 .9000 .14569 .69858
 
 Same for 
 
 rand(3,3)
 
 Returns:
 .34 .25 .235
 .343 .343 .535
 .353 .75 .645
 
 w = randn(1,3)
 
 Three random numbers with a collision distrubtion
 
 Returns: -.353 1.35 -0.235235
 
 w = -6 + sqrt(10)*(randn(1,10000))
 Returns random matrix with 10,000 element vector
 
 hist(w)
 
 returns a histogram of w
 hist(w, 50) with more 'buckets' or bins
 
 
 eye(4)
 4x4 matrix
 
 returns: 
 
 1 0 0 0
 0 1 0 0
 0 0 1 0
 0 0 0 1
 
 Goes on for all of the differnet eye matrix types
 
 help eye 
 
 Returns help function info
 
 type the Q key to quit. 
 
 
