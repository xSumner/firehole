import firehole as fh

converter = fh.ConvertID()

# ID number of 18 digits
test_id1 = "130701199310302288"
# ID number of 15 digits
test_id2 = "320311770706001"

# convert from 15 digits to 18 digits
new_18 = converter.up_to_eighteen(test_id2)
print("Convered to 18 digits: ", new_18)

# convert from 18 digits to 15 digits
new_15 = converter.down_to_fifteen(test_id1)
print("Convered to 15 digits: ", new_15)

# ID list of 18 digits
test_list = ["130701199310302288", "52030219891209794X"]
# Covert an ID list
new_15_list = list(map(converter.down_to_fifteen, test_list))
print(new_15_list)