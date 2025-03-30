# variant 1
one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print(one_line_text)

# variant 2
one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")
print(one_line_text, "\n")



query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")
print(query)