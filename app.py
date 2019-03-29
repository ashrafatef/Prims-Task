import functools 

def get_all_prime_numbers_in_list (prime_numbers):

    p = 2 
    limit = prime_numbers[-1] + 1
    while p*p < limit:

        if prime_numbers[p] != 0 :
            for i in range(p*p , limit , p):
                prime_numbers[i] = 0 
            
        p+=1

    return prime_numbers

def get_max_prime_sum_previous_prims(prims):
    prims_sum =[0] * len(prims)
    total = 0
    target = 0
    for i in range(len(prims)):
        total+=prims[i]
        prims_sum[i] = total

    
    for i in range(len(prims_sum)):
        single_prim_sum = prims_sum[i]
        target = search_for_prim_number(prims , single_prim_sum) or target
    return target
   

def search_for_prim_number(list_of_prims , number):
    start = 0
    end = len(list_of_prims) -1 
    while start <= end :
        mid = int((end + start) /2)
        if (list_of_prims[mid] == number):
            return list_of_prims[mid]
        elif (list_of_prims[mid] > number):
            end = mid - 1
        elif (list_of_prims[mid] < number):
            start = mid + 1
    return False

def main():
    limit  = int(input())
    all_numbers = list(range(limit))

    prime_numbers = get_all_prime_numbers_in_list(all_numbers)

    filtered_prim_numbers = list(filter(lambda x : x != 0 and x != 1 , prime_numbers))
    print(filtered_prim_numbers)
    print ("sum of all prims" , functools.reduce(lambda a,b : a+b,filtered_prim_numbers))
    
    prim_of_all_sum_of_prims = get_max_prime_sum_previous_prims(filtered_prim_numbers)
    print ("THE Prime" , prim_of_all_sum_of_prims)

    
main()
