Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/werkzeug/serving.py", line 362, in run_wsgi
    execute(self.server.app)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/werkzeug/serving.py", line 326, in execute
    write(data)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/werkzeug/serving.py", line 301, in write
    self.wfile.write(data)
  File "/usr/lib64/python3.12/socketserver.py", line 840, in write
    self._sock.sendall(b)
  File "/usr/lib64/python3.12/ssl.py", line 1211, in sendall
    v = self.send(byte_view[count:])
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.12/ssl.py", line 1180, in send
    return self._sslobj.write(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2406)
SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, coalesce(array_agg(brand_opl.product_portfolios.category_name), %(coalesce_1)s) AS portfolio_names, array_agg(distinct(brand_opl.product_types.product_type)) AS product_types 
FROM brand_opl.product LEFT OUTER JOIN brand_opl.product_portfolio_map ON brand_opl.product.product_id = brand_opl.product_portfolio_map.product_id LEFT OUTER JOIN brand_opl.product_portfolios ON brand_opl.product_portfolio_map.category_id = brand_opl.product_portfolios.category_id JOIN brand_opl.product_types_map ON brand_opl.product_types_map.product_id = brand_opl.product.product_id JOIN brand_opl.product_types ON brand_opl.product_types_map.type_id = brand_opl.product_types.type_id LEFT OUTER JOIN brand_opl.product_alias ON brand_opl.product_alias.product_id = brand_opl.product.product_id 
WHERE (brand_opl.product.product_name ILIKE %(product_name_1)s OR brand_opl.product_alias.alias_name ILIKE %(alias_name_1)s) AND brand_opl.product.product_name ILIKE %(product_name_2)s GROUP BY brand_opl.product.product_id, brand_opl.product.product_name, brand_opl.product.product_status, brand_opl.product.last_updated ORDER BY brand_opl.product.product_name
[]
127.0.0.1 - - [16/Apr/2024 21:05:24] "POST /opl/search-to-view-products HTTP/1.1" 200 -
127.0.0.1 - - [16/Apr/2024 21:05:24] "GET /static/css/main.css HTTP/1.1" 304 -
127.0.0.1 - - [16/Apr/2024 21:05:24] "GET /static/css/patternfly-addons.css HTTP/1.1" 304 -
127.0.0.1 - - [16/Apr/2024 21:05:24] "GET /static/css/patternfly.css HTTP/1.1" 304 -
127.0.0.1 - - [16/Apr/2024 21:05:24] "GET /static/images/red-hat-logo.png HTTP/1.1" 304 -
