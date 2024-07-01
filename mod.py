[2024-07-01 20:36:28 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 20:36:28 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
INFO:sqlalchemy.engine.Engine:select pg_catalog.version()
INFO:sqlalchemy.engine.Engine:[raw sql] ()
INFO:sqlalchemy.engine.Engine:select current_schema()
INFO:sqlalchemy.engine.Engine:[raw sql] ()
INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_description AS brand_opl_product_product_description, brand_opl.product.upcoming_change AS brand_opl_product_upcoming_change, brand_opl.product.deprecated AS brand_opl_product_deprecated, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, brand_opl.product.created AS brand_opl_product_created, brand_opl.product.product_status_detail AS brand_opl_product_product_status_detail 
FROM brand_opl.product 
WHERE brand_opl.product.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00012s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_types.type_id AS brand_opl_product_types_type_id, brand_opl.product_types.product_type AS brand_opl_product_types_product_type 
FROM brand_opl.product_types JOIN brand_opl.product_types_map ON brand_opl.product_types.type_id = brand_opl.product_types_map.type_id 
WHERE brand_opl.product_types_map.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00013s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_portfolio_map.product_id AS brand_opl_product_portfolio_map_product_id, brand_opl.product_portfolio_map.category_id AS brand_opl_product_portfolio_map_category_id 
FROM brand_opl.product_portfolio_map 
WHERE brand_opl.product_portfolio_map.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00018s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_portfolios.category_id AS brand_opl_product_portfolios_category_id, brand_opl.product_portfolios.category_name AS brand_opl_product_portfolios_category_name 
FROM brand_opl.product_portfolios 
WHERE brand_opl.product_portfolios.category_id IN (%s, %s)
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00016s] ('559799df-404e-4c36-872e-65015cadc06f', 'acbfe7c2-7801-41cb-8f8d-70c20ecb9d6c')
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.partners.partner_id AS brand_opl_partners_partner_id, brand_opl.partners.partner_name AS brand_opl_partners_partner_name 
FROM brand_opl.partners
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00013s] ()
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_description AS brand_opl_product_product_description, brand_opl.product.upcoming_change AS brand_opl_product_upcoming_change, brand_opl.product.deprecated AS brand_opl_product_deprecated, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, brand_opl.product.created AS brand_opl_product_created, brand_opl.product.product_status_detail AS brand_opl_product_product_status_detail 
FROM brand_opl.product
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00012s] ()
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_notes.product_id AS brand_opl_product_notes_product_id, brand_opl.product_notes.product_note AS brand_opl_product_notes_product_note 
FROM brand_opl.product_notes 
WHERE brand_opl.product_notes.product_id = %s 
 LIMIT 1
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00013s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_references.product_id AS brand_opl_product_references_product_id, brand_opl.product_references.product_link AS brand_opl_product_references_product_link, brand_opl.product_references.link_description AS brand_opl_product_references_link_description 
FROM brand_opl.product_references 
WHERE %s = brand_opl.product_references.product_id
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00026s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_alias.alias_id AS brand_opl_product_alias_alias_id, brand_opl.product_alias.product_id AS brand_opl_product_alias_product_id, brand_opl.product_alias.alias_name AS brand_opl_product_alias_alias_name, brand_opl.product_alias.alias_type AS brand_opl_product_alias_alias_type, brand_opl.product_alias.alias_approved AS brand_opl_product_alias_alias_approved, brand_opl.product_alias.previous_name AS brand_opl_product_alias_previous_name, brand_opl.product_alias.tech_docs AS brand_opl_product_alias_tech_docs, brand_opl.product_alias.tech_docs_cli AS brand_opl_product_alias_tech_docs_cli, brand_opl.product_alias.alias_notes AS brand_opl_product_alias_alias_notes 
FROM brand_opl.product_alias 
WHERE %s = brand_opl.product_alias.product_id
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00019s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_mkt_life.product_id AS brand_opl_product_mkt_life_product_id, brand_opl.product_mkt_life.product_release AS brand_opl_product_mkt_life_product_release, brand_opl.product_mkt_life.product_release_detail AS brand_opl_product_mkt_life_product_release_detail, brand_opl.product_mkt_life.product_release_link AS brand_opl_product_mkt_life_product_release_link, brand_opl.product_mkt_life.product_eol AS brand_opl_product_mkt_life_product_eol, brand_opl.product_mkt_life.product_eol_detail AS brand_opl_product_mkt_life_product_eol_detail, brand_opl.product_mkt_life.product_eol_link AS brand_opl_product_mkt_life_product_eol_link 
FROM brand_opl.product_mkt_life 
WHERE brand_opl.product_mkt_life.product_id = %s 
 LIMIT 1
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00016s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_partners.product_id AS brand_opl_product_partners_product_id, brand_opl.product_partners.partner_id AS brand_opl_product_partners_partner_id 
FROM brand_opl.product_partners 
WHERE brand_opl.product_partners.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00017s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_components.component_id AS brand_opl_product_components_component_id, brand_opl.product_components.product_id AS brand_opl_product_components_product_id, brand_opl.product_components.component_type AS brand_opl_product_components_component_type 
FROM brand_opl.product_components 
WHERE brand_opl.product_components.component_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00014s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_components.component_id AS brand_opl_product_components_component_id, brand_opl.product_components.product_id AS brand_opl_product_components_product_id, brand_opl.product_components.component_type AS brand_opl_product_components_component_type 
FROM brand_opl.product_components 
WHERE brand_opl.product_components.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00013s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_description AS brand_opl_product_product_description, brand_opl.product.upcoming_change AS brand_opl_product_upcoming_change, brand_opl.product.deprecated AS brand_opl_product_deprecated, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, brand_opl.product.created AS brand_opl_product_created, brand_opl.product.product_status_detail AS brand_opl_product_product_status_detail 
FROM brand_opl.product 
WHERE brand_opl.product.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00017s] ('4a491a3f-63c6-4a8f-ad08-21ac94848123',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_description AS brand_opl_product_product_description, brand_opl.product.upcoming_change AS brand_opl_product_upcoming_change, brand_opl.product.deprecated AS brand_opl_product_deprecated, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, brand_opl.product.created AS brand_opl_product_created, brand_opl.product.product_status_detail AS brand_opl_product_product_status_detail 
FROM brand_opl.product 
WHERE brand_opl.product.product_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00012s] ('d7964484-6198-4cf5-888b-cb35fa8a4507',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_log.log_id AS brand_opl_product_log_log_id, brand_opl.product_log.product_id AS brand_opl_product_log_product_id, brand_opl.product_log.edit_date AS brand_opl_product_log_edit_date, brand_opl.product_log.edit_notes AS brand_opl_product_log_edit_notes, brand_opl.product_log.username AS brand_opl_product_log_username 
FROM brand_opl.product_log 
WHERE brand_opl.product_log.product_id = %s ORDER BY brand_opl.product_log.edit_date DESC
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00014s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.product_notes.product_id AS brand_opl_product_notes_product_id, brand_opl.product_notes.product_note AS brand_opl_product_notes_product_note 
FROM brand_opl.product_notes 
WHERE %s = brand_opl.product_notes.product_id 
 LIMIT 1
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00020s] ('a5cc8b7f-bed7-4526-9c3b-7f343bfba0fc',)
INFO:sqlalchemy.engine.Engine:SELECT brand_opl.partners.partner_id AS brand_opl_partners_partner_id, brand_opl.partners.partner_name AS brand_opl_partners_partner_name 
FROM brand_opl.partners 
WHERE brand_opl.partners.partner_id = %s
INFO:sqlalchemy.engine.Engine:[dialect redshift+redshift_connector does not support caching 0.00020s] ('5698cbf4-c919-48cd-9158-227b98bd3218',)
INFO:sqlalchemy.engine.Engine:ROLLBACK
[2024-07-01 20:36:50 +0000] [7] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 20:36:50 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
