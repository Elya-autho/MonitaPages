import psycopg2

class DatabaseConnections:
    connect = psycopg2.connect(
        dbname="stage-kb-monita",
        user="filippova",
        password="w7TBAs3HCCw7wFmSFgtc",
        host="c-c9q6nqgic3cd8dpunlii.rw.mdb.yandexcloud.net",
        port="6432"
    )
    cursor = connect.cursor()

    sql = """
        SELECT s.id, s.sms_token FROM public.employees AS e
        JOIN public.sms_token_log AS s ON e.id = s.employee_id
        WHERE e.mobile_phone LIKE '%9085728301%'
        ORDER BY s.id DESC
        LIMIT 1;
        """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

