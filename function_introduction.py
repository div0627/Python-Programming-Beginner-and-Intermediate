''' This program Write a summary_statistics() function that will take movie_data as input, and output a dictionary that will give useful numbers from the data.
Define summary_statistics() with one argument, an input list.
Use the feature_counter() with the relevant arguments to count the following properties and make them equal to the corresponding variables.
Assign the number of movies made in Japan to num_japan_films.
Assign the number of movies in color to num_color_films.
Assign the number of movies in English to num_films_in_english.
Create a dictionary that associates the keys (japan_films,color_films,films_in_english) with the corresponding variables.
Return the dictionary.
Call the function with movie_data as its input, and store its value in summary.
'''

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    summary_dict = {"japan_films" : num_japan_films, "color_films" : num_color_films, "films_in_english" : num_films_in_english}
    return summary_dict
summary = summary_statistics(movie_data)
