try:
    def main():

            fulltankCapacity = 0

            #Price of fuels

            PetrolPrice = 165.5
            PremiumPetrol = 165.6
            DieselPrice = 2458.06
            PremiumDieselPrice = 459.19
            Gas = 750.0
            Kerosene = 200.0

            print(f'1 - Petrol:   {PetrolPrice}  Per Litre')
            print(f'2 - PremiumPetrol: {PremiumPetrol} Per Litre')
            print(f'3 - Diesel:  {DieselPrice} Per Litre')
            print(f'4 - PremiumDiesel:  {PremiumDieselPrice} Per Litre')
            print(f'5 - Gas: {Gas} Per KG')
            print(f'6 - Kerosene: {Kerosene} Per Litre')

            pricePerLitre = 0

            try:
                output = input('Which fuel do you need?\n'
                               '1,2,3,4,5,6\n')
                if output in ('1','2','3','4','5','6'):
                    if output == '1':
                        pricePerLitre = PetrolPrice
                    elif output == '2':
                        pricePerLitre = PremiumPetrol
                    elif output == '3':
                        pricePerLitre = DieselPrice
                    elif output == '4':
                        pricePerLitre = PremiumDieselPrice
                    elif output == '5':
                        pricePerLitre = Gas
                    elif output == '6':
                        pricePerLitre = Kerosene
                else:
                    print('INVALID INPUT')
                    exit()

                def kok():
                    fulltank = str(input('In cash or litres?\n'
                                         '1- Cash ,2- Litres\n'))
                    if fulltank in ('1','2'):
                        if fulltank == '1':
                            quantity = int(input('Amount\n'))
                            if quantity > 0:
                                quantity = quantity / pricePerLitre
                        if fulltank == '2':
                            quantity = int(input('How many litres do ou want?\n'))
                            lik = quantity * pricePerLitre
                    else:
                        print('INVALID INPUT')
                        exit()
                    cost = quantity * pricePerLitre

                    print('Fuel Choice:' + output)
                    print(f'Quantity:  {quantity}  Litres')
                    print(f'Total Cost: {cost} Naira')
                    print('Thanks for your patronage ')
                    return main()
                kok()
            except Exception as e:
                    print(e)

    main()
except Exception as e:
    print(e)