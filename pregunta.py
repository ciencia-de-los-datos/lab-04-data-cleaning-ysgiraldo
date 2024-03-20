"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #
    # Inserte su código aquí
    #
    
    # Delete de NA values
    df.dropna(inplace=True)

    # All the str lower
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    # Delete regular expression that we do not need
    df = df.apply(lambda x: x.str.replace('_', '-') if x.dtype == "object" else x)
    df = df.apply(lambda x: x.str.replace('-', ' ') if x.dtype == "object" else x)

    # The format will be yyyy-mm-dd but if the date is already 
    # in the desired format, the function will not modify it
    def convert_date(date):
        try:
            return pd.to_datetime(date, format='%d/%m/%Y')
        except ValueError:
            return pd.to_datetime(date, errors='coerce')
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convert_date)

    # This will leave the format as float after removing the respective strings 
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '').str.replace('$', '').str.extract('(\d+)').astype(float)
    
    # Delete duplicates
    df.drop_duplicates(inplace=True)
    
    return df

# def main():
#     clean_df = clean_data()


# if __name__ == "__main__":
#     main()


# print(clean_data())