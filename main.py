from opusfilter.filters import LengthFilter

with open('path', 'r', encoding='utf-8') as file:
    input_text = file.readlines()

filter_obj = LengthFilter(unit='word', max_length=10)
new_list = []
for senteces in input_text:
    if filter_obj.get_length(senteces, 0) <= 10:
        new_list.append(senteces)

with open('path', 'w', encoding='utf-8') as file:
    file.writelines(new_list)

print(len(input_text))
print(len(new_list))
