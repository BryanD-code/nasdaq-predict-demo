from pyspark.sql import functions as F, Window
from loguru import logger
import typer

app = typer.Typer()

# --- 1. AQUÍ VA TU LÓGICA DE NEGOCIO (Pura y testeable) ---
def calcular_retorno_diario(df):
    """
    Recibe un DataFrame de Spark, calcula el retorno diario y devuelve el DataFrame transformado.
    """
    ventana_cronologica = Window.orderBy("Date")
    
    df_transformado = (df
        .withColumn("Precio_dia_Anterior", F.lag("Close", 1).over(ventana_cronologica))
        .withColumn("Retorno_diario", (F.col("Close") - F.col("Precio_dia_Anterior")) / F.col("Precio_dia_Anterior"))
    )
    return df_transformado


# --- 2. AQUÍ VA LA EJECUCIÓN (Lo que usarías en producción) ---
@app.command()
def main():
    logger.info("Iniciando generación de features con PySpark...")
    
    # IMPORTANTE: En producción, aquí inicializarías Spark y leerías de la Capa Bronce
    # spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()
    # df_raw = spark.table("nasdaq_raw")
    
    # df_silver = calcular_retorno_diario(df_raw)
    
    # df_silver.write.format("delta").mode("overwrite").saveAsTable("nasdaq_silver")
    logger.success("Features generadas y guardadas en Capa Plata.")

if __name__ == "__main__":
    app()