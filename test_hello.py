from hello import hello

def test_hello():
    result = hello()
    print(f"hello() returned: {result}")
    assert result == "Hello World ~ Pratul"
    print("Test passed!")

# Call the test function
test_hello()