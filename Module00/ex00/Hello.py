ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#My code---------------

ft_list.append("World!")

tuple_france = ("France!",)
ft_tuple = (ft_tuple[0],  (tuple_france[0]))

ft_set.remove("tutu!")
ft_set.add("Perpignan!")

ft_dict.update({"Hello" : "42Perpignan!"})

#----------------------

# print(ft_tuple[:1])
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)