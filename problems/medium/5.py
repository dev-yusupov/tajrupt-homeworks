n = int(input())

def generate_fibonacci(limit):
    fi_list = [0, 1]

    while True:
        next_fi = fi_list[-1] + fi_list[-2]
        if next_fi > limit:
            break
        
        fi_list.append(next_fi)
    
    return fi_list

print(generate_fibonacci(n))