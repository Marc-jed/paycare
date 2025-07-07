import pytest
import pandas as pd
from etl import extract_data, transform_data, load_data




def test_extract_data():
    #création d'un fichier temporaire csv
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp:
        tmp.write("col1,col2\n1,2\n3,4\n")
        tmp_path = tmp.name
    df = extract_data(tmp_path)
    # Nettoyage du fichier temporaire
    os.remove(tmp_path)
    # test de ce fichier
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    # Test du message d'erreur
    df = extract_data("non_existent_file.csv")
    assert df is None


# def test_transform_data():
#     df = pd.DataFrame({
#         'name': ['Alice', 'Bob', 'Charlie'],
#         'salary': [5000, 6000, 7000]
#     })

#     result = transform_data(df)

#     # Vérifications
#     assert result is not None
#     assert 'tax' in result.columns
#     assert 'net_salary' in result.columns
#     assert result.shape[0] == 3
#     assert result['tax'].iloc[0] == 500.0
#     assert result['net_salary'].iloc[1] == 5400.0

# def test_load_data():
#         # Crée un DataFrame de test
#     data = pd.DataFrame({
#         'name': ['Alice', 'Bob'],
#         'salary': [5000, 6000]
#     })

#     # Crée un fichier temporaire pour l’écriture
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
#         output_path = tmp.name

#     try:
#         # Appel de la fonction
#         load_data(data, output_path)

#         # Vérifie que le fichier a été créé et qu'il contient les bonnes données
#         assert os.path.exists(output_path)
#         df_loaded = pd.read_csv(output_path)

#         # Vérifie le contenu
#         assert df_loaded.equals(data)
#     finally:
#         # Nettoyage du fichier temporaire
#         os.remove(output_path)