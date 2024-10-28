class Patterns:
    def square(self,n):

        for i in range(n):
            for j in range(n):
                print("*",end=" ")
            
            print("")
                
    def hollow_square(self,n):

        for i in range(n):

            for j in range(n):
                if i in [0,(n-1)]:
                    print("*",end=" ")
                
                else:
                    if j in [0,(n-1)]:
                        print("*",end=" ")
                    else:
                        print(" ",end = " ")
            
            print()

    def left_skewed_triangle(self,n):

        for i in range(n+1):

            for j in range(i):

                print("*",end= " ")

            print()

    def right_skewed_triangle(self,n):
        
        for i in range(n,0,-1):
            
            for  j in range(n+1):

                if j>=i:
                    print("*", end = " ")
                else:
                    print(" ",end= " ")

            print()

    def hollow_left_skewed_triangle(self,n):

        for i in range(1,n+1):
            
            for j in range(i):

                if i == n or j == 0 or j == (i-1):
                    print("*",end= " ")
                
                else:
                    print(" ",end = " ")

            print()

    def hollow_right_skewed_triangle(self,n):


        for i in range(1,n+1):

            for j in range(1,n+1):

                if i == n or j == n or j == (n-i+1):
                    print("*" ,end= " ")

                else:
                    print(" ",end= " ")
            
            print()

    def numbered_left_skewed_traingle(self,n):

        for i in range(1,n+1):
            num=1
            for j in range(1,n+1):

                if j <= i:
                    print(str(num),end = " ")

                else:
                    print(" ",end = " ")

            num+=1

            print()

    def down_left_traingle(self,n):

        for i in range(1,n+1):

            for j in range(1,n+1):

                if i == 1 or j == 1 or j == (n-i+1):

                    print("*",end = " ")
                else: 
                    print(" ",end = " ")
            print()

    def triangle(self,n):

        for i in range(n):

            for j in range(n-i-1):

                print(" ", end= "")


            for j in range((2*i)+1):
                print("*", end= "")


            for j in range(n-i-1):
                
                print(" ", end= "")


            print()

    def reverse_traingle(self,n):

           

        for i in range(n):

            for j in range(i):

                print(" ", end= "")


            for j in range((2*n)-((2*i)+1)):
                print("*", end= "")


            for j in range(i):
                
                print(" ", end= "")


            print()

    def side_triangle(self,n):

        for i in range(1,2*n):
            if i >n:

                for j in range(2*n-i):
                    print("*",end=" ")
            
            else:

                for j in range(i):
                    print("*",end=" ")


            
            print()

    def boolean_triangle(self,n):

        for i in range(n):
            
            start_num=0
            if i%2 == 0:
                start_num=1

            for j in range(i+1):
                
                print(start_num,end = " ")

                start_num = 1- start_num
                

            print()

    def hollow_v_numbers(self,n):
        space = 2*n-2
        for i in range(1,n+1):
            

            for j in range(i):
                
                print(j+1,end=" ")


            for j in range(space):
                print(" ",end=" ")

            for j in range(i,0,-1):
                
                print(j,end=" ")

                
            space-=2
            print()

    def numbered_triangle(self,n):
        start_num =1
        for i in range(1,n+1):

            for j in range(i):

                print(start_num,end= " ")
                start_num+=1

            print()

    def alphabet_triangle(self,n):

        for i in range(n):
            start_char = "A"

            for j in range(n-i):

                print(start_char,end= " ")

                start_char = chr(ord(start_char)+1)

            print()


        for i in range(n):

            for j in range(n-i-1):

                print(" ", end= "")


            for j in range((2*i)+1):
                print(start_char, end= "")

                


            for j in range(n-i-1):
                
                print(" ", end= "")

            
            print()

    def alphabet_triangle_2(self,n):

        for i in range(1,n+1):
            
            start_char = "A"
            for j in range(n-i):
                print(" ",end= " ")
            
            for j in range(2*i-1):
                print(start_char,end=" ")

                if j>=(i-1):

                    start_char = chr(ord(start_char)-1)
                else:
                    start_char = chr(ord(start_char)+1)

            for j in range(n-i):
                print(" ",end= " ")

            print()
            
    def alphabet_reverse_order_triangle(self,n):

        for i in range(n):

            start_char = chr(ord("E")-i)

            for j in range(1,n+1):

                if j <=(i+1):
                    print(start_char,end=" ")

                start_char = chr(ord(start_char)+1)

            print()

    def hollow_diamond(self,n):

        for i in range(n):
           
            for j in range(n-i):
               print("*",end=" ")
            
            for j in range(2*i):
               
               print(" ",end= " ")

            for j in range(n-i):
               print("*",end=" ")

            print()

        for i in range(n):
           
            for j in range(i+1):
               print("*",end=" ")

            for j in range(2*(n-i-1)):
               print(" ",end = " ")

            for j in range(i+1):
               print("*",end=" ")

            print()

    def butterfly(self,n):

        for i in range(n):

            for j in range(i+1):
                print("*",end=" ")

            for j in range(2*(n-i-1)):
                print(" ",end= " ")

            for j in range(i+1):
                print("*",end=" ")

            print()

        for i in range(n):
           
            for j in range(n-i):
               print("*",end=" ")
            
            for j in range(2*i):
               
               print(" ",end= " ")

            for j in range(n-i):
               print("*",end=" ")

            print()

    def matrix(self,n):

        for i in range(2*n-1):

            for j in range(2*n-1):

                top = i
                left = j
                right = (2*n-2)-j
                bottom = (2*n-2)-i

                print_val = n - min(left,right,top,bottom)

                print(print_val,end=" ")

            print()


if __name__ == "__main__":

    pattern_instance = Patterns()
    pattern_instance.square(15)
    pattern_instance.hollow_square(10)
    pattern_instance.left_skewed_triangle(5)
    pattern_instance.triangle(3)
    pattern_instance.butterfly(5)
    pattern_instance.matrix(4)



