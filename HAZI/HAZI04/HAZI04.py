# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladat által visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
def csv_to_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

#df = csv_to_df("StudentsPerformance.csv")
#df.head()

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(df_data: pd.DataFrame) -> pd.DataFrame:
    new_df = df_data.copy()
    new_df.columns = [column_name.upper() if 'e' not in column_name else column_name for column_name in new_df.columns]
    return new_df


#capitalize_columns(df)

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(old_df: pd.DataFrame) -> int:
    df = old_df.copy()
    return len(df[df['math score'] >= 50])


#print(math_passed_count(df))    

# %%
'''
Készíts egy függvényt, ahol Dataframe ként visszaadjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    return df[df['test preparation course'] == 'completed']


#print(did_pre_course(df))

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    return df.groupby('parental level of education').mean()


#print(average_scores(df))

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
def add_age(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    np.random.seed(42)
    ages = np.random.randint(18, 67, size=len(df))
    df['age'] = ages
    return df


#print(add_age(df))

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(input_df: pd.DataFrame) -> tuple:
    df = input_df.copy()
    subset = df[df['gender'] == 'female']
    subset.sort_values(by=['math score', 'reading score', 'writing score'], inplace=True, ascending=False)
    top_score = subset.head(1)
    tuple_of_tuple = tuple(top_score[['math score', 'reading score', 'writing score']].apply(tuple, axis=1))
    return tuple_of_tuple[0]


#print(female_top_score(df))


# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
def add_grade(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    points = ((df['math score'] + df['reading score'] + df['writing score']) / 300)
    df['point'] = points
    df['grade'] = ''
    for i in range(len(df)):
        if df['point'][i] >= 0.9:
            df['grade'][i] = 'A'
        elif df['point'][i] >= 0.8:
            df['grade'][i] = 'B'
        elif df['point'][i] >= 0.7:
            df['grade'][i] = 'C'
        elif df['point'][i] >= 0.6:
            df['grade'][i] = 'D'
        else:
            df['grade'][i] = 'F'
    df.drop(columns=['point'], inplace=True)
    return df


#print(add_grade(df))

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(input_df: pd.DataFrame) -> plt.Figure:
    df = input_df.copy()
    grouped = df.groupby('gender')['math score'].mean().plot(kind="bar")
    plt.xlabel('Gender')
    plt.ylabel('Math Score')
    plt.title('Average Math Score by Gender')
    grouped.plot()
    return plt.figure()


#math_bar_plot(df)
#print(type(math_bar_plot(df)))

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(input_df: pd.DataFrame) -> plt.Figure:
    df = input_df.copy()

    fig, ax = plt.subplots()
    ax.plot(df['writing score'], df.groupby(['writing score']).count())
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')
    return plt.figure()


#writing_hist(df)

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%



