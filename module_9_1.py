def apply_all_func(int_list, *functions):
    result = {}
    function_res_list = []
    function_name_list = []
    int_list = list(map(int, int_list))
    for function in functions:
        f_r_l = function(int_list)
        function_res_list.append(f_r_l )
        f_n_l = function.__name__
        function_name_list.append(f_n_l )
        result = dict(zip(function_name_list, function_res_list))
        # for i in range(len(function_name_list)):
        #     result[function_name_list[i]] = function_res_list[i]
    return  result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func(['6', '20', '15', '9'], len, sum, sorted))
