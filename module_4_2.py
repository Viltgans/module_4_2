def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


# inner_function() - Существует только в локальном пространстве имен функции test_function
test_function()