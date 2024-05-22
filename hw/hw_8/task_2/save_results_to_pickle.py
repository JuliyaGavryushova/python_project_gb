import pickle


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(results, file)