from datetime import datetime      
#get_days_from_today = input("введіть дату-  " )
def get_days_from_today(date):
    try:
        
        input_date = datetime.strptime(date, '%Y-%m-%d').date() # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        #-------------------------------------------------------------------------
        current_date = datetime.today().date() # Отримання поточної дати
        #-------------------------------------------------------------------------
        delta = current_date - input_date # Розрахунок різниці у днях
        #-------------------------------------------------------------------------
        return delta.days # Повернення різниці у днях як цілого числа
    #-----------------------------------------------------------------------------
    except ValueError:
        # Обробка винятку, якщо введена неправильна дата
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

 
print(get_days_from_today(input("введіть дату --> ")))