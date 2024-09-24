def count_vowels(text):
    vowels = 'aeiou'
    for char in text.lower(): 
        if char in vowels:
            count += 1
    return count
                
text = "Free Lung Implants in my AirBNB"

print(f"{count_vowels(text)}")