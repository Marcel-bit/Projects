from compounding import Compounding

def main():
    initial = 1000
    recurring = 100
    years = 5
    ann_percent = 0.1
    test = Compounding(initial, recurring, years, ann_percent)
    test.string_part()
    

if __name__ == '__main__':
    main()