import functools 

def get_all_prime_numbers_in_list (prime_numbers):

    p = 2 
    limit = prime_numbers[-1] + 1
    # total  = 0
    while p*p < limit:

        if prime_numbers[p] != 0 :
            for i in range(p*p , limit , p):
                prime_numbers[i] = 0 
            
        p+=1
    # for p in range(2, limit): 
    #     if prime_numbers[p]: 
    #         total += prime_numbers[p]
    # print(total)
    return prime_numbers

def get_max_prime_sum_previous_prims(prims):
    prims_sum =[0] * len(prims)
    total = 0
    target = 0
    for i in range(len(prims)):
        total+=prims[i]
        prims_sum[i] = total

    
    for i in range(len(prims_sum)):
        x = prims_sum[i]
        start = 0
        end = len(prims) -1 
        while start <= end :
            mid = int((end + start) /2)
            if (prims[mid] == x):
                target = prims[mid]
                break
            elif (prims[mid] > x):
                end = mid - 1
            elif (prims[mid] < x):
                start = mid + 1
    print(target)    


def main():
    limit  = int(input())
    prime_numbers = list(range(limit))
    # prime_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    prime_numbers = get_all_prime_numbers_in_list(prime_numbers)
    filtered_prim_numbers = list(filter(lambda x : x != 0 and x != 1 , prime_numbers))
    print(filtered_prim_numbers)
    print ("sum of all prims" , functools.reduce(lambda a,b : a+b,filtered_prim_numbers))
    get_max_prime_sum_previous_prims(filtered_prim_numbers)

    
main()
