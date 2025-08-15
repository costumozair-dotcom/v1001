@@ .. @@
         # Gera relatório final limpo
         clean_report = comprehensive_report_generator.generate_clean_report(
-            final_results, session_id
+            {'report': final_results}, session_id
         )
         
         logger.info("✅ Relatório final limpo gerado")
         
         # Prepara resposta final
-        response_data = {
+        response_data = clean_report.get('report_sections', {
             'success': True,
             'session_id': session_id,
             'processing_time': processing_time,
             'analysis_result': final_results,
             'clean_report': clean_report,
             'quality_metrics': {
                 'components_completed': len(final_results.get('successful_components', {})),
                 'success_rate': final_results.get('execution_stats', {}).get('success_rate', 0),
                 'data_quality': 'REAL_DATA_ONLY'
             }
-        }
+        })
         
         return jsonify(response_data)