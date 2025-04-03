
#импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#создание класа
class GraphicStatistics:
    def __init__(self, df_path):
        
        self.df = pd.read_csv(df_path) #чтение данных из файла csv.

    def histogram(self): #определение метода для создания гистограммы
        
        grouped_df = self.df.groupby("STATE", as_index=False).mean() #группировка данных по колонке state

        #определение всех штатов
        selected_states = [ "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
            "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
            "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
            "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
            "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
            "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
            "West Virginia", "Wisconsin", "Wyoming" ]

        #фильтрация и упорядочивание данных 
        filtered_df = grouped_df[grouped_df["STATE"].isin(selected_states)]
        filtered_df = filtered_df.set_index("STATE").reindex(selected_states).reset_index()

        states = [ "Алабама", "Аляска", "Аризона", "Арканзас", "Калифорния", "Колорадо", "Коннектикут", "Делавэр", 
            "Округ Колумбия", "Флорида", "Джорджия", "Гавайи", "Айдахо", "Иллинойс", "Индиана", "Айова", "Канзас", 
            "Кентукки", "Луизиана", "Мэн", "Мэриленд", "Массачусетс", "Мичиган", "Миннесота", "Миссисипи", "Миссури", 
            "Монтана", "Небраска", "Невада", "Нью-Гэмпшир", "Нью-Джерси", "Нью-Мексико", "Нью-Йорк", "Северная Каролина", 
            "Северная Дакота", "Огайо", "Оклахома", "Орегон", "Пенсильвания", "Род-Айленд", "Южная Каролина", 
            "Южная Дакота", "Теннесси", "Техас", "Юта", "Вермонт", "Вирджиния", "Вашингтон", "Западная Вирджиния", 
            "Висконсин", "Вайоминг" ]  

        #извлечение данных
        federal_values = filtered_df["FEDERAL_REVENUE"].values
        state_values = filtered_df["STATE_REVENUE"].values
        local_values = filtered_df["LOCAL_REVENUE"].values

        total_revenue = federal_values + state_values + local_values #вычисление общего бюджета для каждого штата.
        federal_normalized = (federal_values / total_revenue) * 100
        state_normalized = (state_values / total_revenue) * 100
        local_normalized = (local_values / total_revenue) * 100

        x = np.arange(len(states))  #позиции для столбцов

        #создание графика
        fig, ax = plt.subplots(figsize=(15, 10))  # Увеличенные размеры графика для всех штатов
        bar_width = 0.8

        #построение нормализованных столбцов
        local_bars = ax.bar(x, local_normalized, color="green", width=bar_width, label="Местный бюджет")
        federal_bars = ax.bar(x, federal_normalized, bottom=local_normalized, color="blue", width=bar_width, label="Федеральный бюджет")
        state_bars = ax.bar(x, state_normalized, bottom=local_normalized + federal_normalized, color="gold", width=bar_width, label="Бюджет штата")

        #добавление значений внутри столбцов
        for i in range(len(states)):
            #местный бюджет
            ax.text(x[i], local_normalized[i] / 2, f"{local_values[i]:,.0f}", ha="center", va="center", color="white", fontsize=8)
            #федеральный бюджет
            ax.text(x[i], local_normalized[i] + federal_normalized[i] / 2, f"{federal_values[i]:,.0f}", ha="center", va="center", color="white", fontsize=8)
            #бюджет штата
            ax.text(x[i], local_normalized[i] + federal_normalized[i] + state_normalized[i] / 2, f"{state_values[i]:,.0f}", ha="center", va="center", color="white", fontsize=8)

            
        ax.set_xticks(x)
        ax.set_xticklabels(states, rotation=90)  # Поворот для длинных названий

        #настройка графика
        ax.set_ylabel("Сумма бюджета (нормализована до 100)")
        ax.set_title("Количество школ и их бюджет по штатам  ")
        ax.legend(loc="upper left")

        plt.subplots_adjust(bottom=0.5)
        plt.tight_layout()
        plt.show()

def main():
    df_path = 'states.csv'  
    stats = GraphicStatistics(df_path)
    stats.histogram()
    
if __name__ == "__main__":
    main()