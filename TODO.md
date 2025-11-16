Fase 1: Análisis Exploratorio 📊
 Analizar distribución de buyer_d7 y revenue x
 Identificar features correlacionadas con compra
 Analizar distribución de revenue en compradores (percentiles, outliers)
 Crear visualizaciones de features vs revenue

Fase 2: Feature Engineering 🔧
 Crear features de engagement (clicks, impresiones, tiempo)
 Features temporales (hora del día, día semana, mes)
 Features de usuario (historial, demografía)
 Features de anuncio (categoría, formato, precio producto)
 Agregaciones por usuario/producto
 Encoding de variables categóricas

Fase 3: Modelado en Dos Etapas 🤖

Etapa 1 - Clasificación:
 Entrenar modelo clasificador (LightGBM/XGBoost)
 Ajustar scale_pos_weight para desbalanceo
 Probar threshold óptimo (favor a precision)
 Validación cruzada estratificada

Etapa 2 - Regresión:
 Entrenar solo con datos donde buyer_d7 = 1
 Probar modelos: LightGBM, XGBoost, CatBoost
 Implementar loss function asimétrica
 Validar con MAE y custom metric

Fase 4: Técnicas Avanzadas 🚀
 Quantile Regression: Predecir percentil 40-50 en vez de media
 Ensemble: Combinar múltiples modelos con pesos
 Calibración: Post-procesar predicciones (multiplicar por factor < 1)
 Clipping: Establecer límites máximos conservadores

Fase 5: Validación y Ajuste ✅
 Crear validación que simule métrica de Kaggle
 Analizar errores por segmentos
 Ajustar parámetros de penalización
 A/B testing de estrategias
 Feature importance analysis

Fase 6: Predicción Final 🎯
 Aplicar clasificador (threshold conservador)
 Aplicar regresor solo a casos positivos
 Post-procesamiento: multiplicar por 0.8-0.9 (reducir sobreestimación)
 Generar submission