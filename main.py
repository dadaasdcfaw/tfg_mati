# This is a sample Python script.
from scripts.example_module import add_randint


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Lembra chamarlle en inglés ás cousas e engadir prints ao principio, medio e final dos módulos para que cando
# a execución se quede pillada, saber onde é que frenou

def run():
    # Use a breakpoint in the code line below to debug your script.
    # Esta é a parte ppal do código. Idealmente, non deberías empregar lóxica aquí. Simplemente executas os modulos
    # que xa tes creados noutros ficheiros de xeito secuencial. Por exemplo:

    # Aqui dentro importas a nube e fas tod0 o preprocesado que sexa necesario.
    # pointcloud = process_pointcloud()

    # Nesta parte exportas tod0 a imaxes
    # raster_pointcloud(pointcloud)

    # ... e así sucesivamente, cada un destes módulos terá o seu propio ficheiro onde fagas tod0 o relativo a ese
    # módulo


    add_randint(max_delta_val=10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
