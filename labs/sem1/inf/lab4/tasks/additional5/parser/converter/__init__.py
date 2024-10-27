def convert_to_csv(d: dict, tag="root"):
    csv = "title;group;teacher/name;teacher/id;date/day;date/weeks/0;date/weeks/1;date/weeks/2;date/weeks/3;date/weeks/4;date/weeks/5;date/weeks/6;date/weeks/7;date/weeks/8;date/weeks/9;date/weeks/10;date/weeks/11;date/weeks/12;date/weeks/13;date/weeks/14;date/weeks/15;time/lesson_number;time/start;time/end;room/name;room/id;campus/name;campus/id;lesson_type/type_name;lesson_type/type_id;lesson_format/format_name;lesson_format/format_id\n"

    for string in d["timetable"]:
        res = []
        res.append(string["title"])
        res.append(string["group"])
        res.append(string["teacher"]["name"])
        res.append(string["teacher"]["id"])
        res.append(string["date"]["day"])

        for i in string["date"]["weeks"]:
            res.append(str(i))
        for i in range(8 - len(string["date"]["weeks"])):
            res.append(";")

        res.append(string["time"]["lesson_number"])
        res.append(string["time"]["start"])
        res.append(string["time"]["end"])
        res.append(string["room"]["name"])
        res.append(string["room"]["id"])
        res.append(string["campus"]["name"])
        res.append(string["campus"]["id"])
        res.append(string["lesson_type"]["type_name"])
        res.append(string["lesson_type"]["type_id"])
        res.append(string["lesson_format"]["format_name"])
        res.append(string["lesson_format"]["format_id"])

        csv += ";".join(list(map(str, res))) + "\n"

    return csv
