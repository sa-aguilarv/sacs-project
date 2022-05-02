"""This program controls the general flow of the Sorting Algorithms Comparison System (SACS)
    This program performs a comparison of several sorting strategies
    
    Functions:
    main(): controls the general flow of SACS
"""

import input_output as io  # En general ya hay un IO en todos los lenguajes. Haz el tuyo

# import comparing_sorting


def main():
    """The main function
    Parameters:
    ----------

    Returns:
    ----------
    """
    config_setting = io.parsing_input()
    print(config_setting)
    # Cargas el archivo y validas los inputs. OJO: sin el -as io-, no funciona
    config = io.load_config_file(config_setting.input)
    # -> Preguntar cómo llamar archivos desde consola
    # comparison = comparing_sorting_methods(config)
    # output_table(comparison)


def load_config_file():
    pass


# NOTA: Esto era necesario antes de Python 3
if __name__ == "__main__":
    main()
