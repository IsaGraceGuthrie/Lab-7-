#the authors names are Ellen Kevin and isa grace
#part 1
def too_long(x):
    if len(x)>=139:
        print("Too long for a SMS message")
    else:
        print(x)

too_long("hello my name is isa grace and i am 19 years old i like computer programming asfjdklasdasdkjfa;slkdfjas asldfja;sdlkfja;lsdkjf kasasjkfa;slkdfj as")
too_long("Hello my name is isa grace and you are Ellen Kevin")

#The authors names are Isa Grace Guthrie and Ellen Kevin
#part 2
def number_of_o(x):
    total=0
    for w in x:
        if w=="o":
            total=total+1
    print(total)
number_of_o("bonono")
number_of_o("oboboobo")

#the authors names are Isa Grace Guthrie and Ellen Kevin
#part 3
def word_check(x):
    if x[0]=="k":
        print(True)
    else:
        print(False)

word_check("kiss")
word_check("kelp")
word_check("cop")
