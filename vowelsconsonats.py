def count_vc(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return f"Vowels={v_count}, Consonants={c_count}"
str=input()
print(count_vc(str))


