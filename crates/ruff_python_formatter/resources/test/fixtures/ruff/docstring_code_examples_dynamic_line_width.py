def simple():
    """
    First line.

    ```py
    class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )
    ```

    Done.
    """
    pass


# Like simple, but we double everything up to ensure the indent level is
# tracked correctly.
def repeated():
    """
    First line.

    ```py
    class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )


    class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )

            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is just one character shy of
                # tripping the default line width of 88. So it should not be
                # wrapped.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
                return 5
            self.x = doit( 5 )
    ```

    Done.
    """
    pass


# Like simple, but we make one line exactly one character longer than the limit
# (for 4-space indents) and make sure it gets wrapped.
def barely_exceeds_limit():
    """
    First line.

    ```py
    class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
        def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
                # For 4 space indents, this is 89 columns, which is one
                # more than the limit. Therefore, it should get wrapped for
                # indent_width >= 4.
                print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a5678)
                return 5
            self.x = doit( 5 )
    ```

    Done.
    """
    pass


# This tests that if the code block is unindented, that it gets indented and
# the dynamic line width setting is applied correctly.
def unindented():
    """
    First line.

```py
class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
    def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
        def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            # For 4 space indents, this is just one character shy of
            # tripping the default line width of 88. So it should not be
            # wrapped.
            print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a567)
            return 5
        self.x = doit( 5 )
```

    Done.
    """
    pass


# Like unindented, but contains a `print` line where it just barely exceeds the
# globally configured line width *after* its indentation has been corrected.
def unindented_barely_exceeds_limit():
    """
    First line.

```py
class Abcdefghijklmopqrstuvwxyz(Abc, Def, Ghi, Jkl, Mno, Pqr, Stu, Vwx, Yz, A1, A2, A3, A4, A5):
    def abcdefghijklmnopqrstuvwxyz(self, abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
        def abcdefghijklmnopqrstuvwxyz(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4):
            # For 4 space indents, this is 89 columns, which is one
            # more than the limit. Therefore, it should get wrapped for
            # indent_width >= 4.
            print(abc, ddef, ghi, jkl, mno, pqr, stu, vwx, yz, a1, a2, a3, a4, a5678)
            return 5
        self.x = doit( 5 )
```

    Done.
    """
    pass