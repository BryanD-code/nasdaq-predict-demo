from pyspark.sql import SparkSession
from nasdaq_demo.features import calcular_retorno_diario

def test_calcular_retorno_diario():
    # Spark local
    spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()
    datos_falsos = [
       ("2026-09-01", 100.0),
        ("2026-09-02", 110.0),
        ("2026-09-03", 55.0)
    ]
    # Conversión y transformación de datos
    df_mock = spark.createDataFrame(datos_falsos, schema=["Date", "Close"])
    df_resultado = calcular_retorno_diario(df_mock)

    # Extracción 
    resultados = df_resultado.collect()
    retorno_dia_2 = resultados[1]["Retorno_diario"]
    retorno_dia_3 = resultados[2]["Retorno_diario"]

    # asserts
    assert round(retorno_dia_2, 2) == 0.10  
    assert round(retorno_dia_3, 2) == -0.50  