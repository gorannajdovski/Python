from name_function import get_formatted_name # import f-je za test

def test_first_last_name():  # definišemo test f-ju 
    formatted_name = get_formatted_name("taylor","swift") # poziv f-je 
    assert formatted_name == "Taylor Swift" 
