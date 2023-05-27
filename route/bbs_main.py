from .tool.func import *


def bbs_main():
    with get_db_connect() as conn:
        curs = conn.cursor()

        curs.execute(
            db_change(
                'select set_data, set_id from bbs_set where set_name = "bbs_name"'
            )
        )
        db_data = curs.fetchall()

        data = ""

        if db_data:
            data += '<ul class="opennamu_ul">'
            for for_a in db_data:
                curs.execute(
                    db_change(
                        'select set_data from bbs_set where set_name = "bbs_type" and set_id = ?'
                    ),
                    [for_a[1]],
                )
                db_data_2 = curs.fetchall()
                bbs_type = db_data_2[0][0] if db_data_2 else "comment"

                data += (
                    '<li><a href="/bbs/w/'
                    + for_a[1]
                    + '">'
                    + for_a[0]
                    + " ("
                    + bbs_type
                    + ")</a></li>"
                )

            data += "</ul>"

        if admin_check() == 1:
            menu = [["bbs/make", load_lang("add")]]
        else:
            menu = []

        return easy_minify(
            flask.render_template(
                skin_check(),
                imp=[
                    load_lang("bbs_main"),
                    wiki_set(),
                    wiki_custom(),
                    wiki_css([0, 0]),
                ],
                data=data,
                menu=[["other", load_lang("return")]] + menu,
            )
        )
