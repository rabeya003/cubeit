from playwright.async_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_cube(page: Page):
    page.goto(BASE_URL)
    
    input =page.get_by_placeholder("Enter number.....")
    input.fill("5")

    page.get_by_role(
        "button",name="Cube"
    ).click()


    result=page.location("css=p#result")

    expect(result).to_have_text("1234")

    def test_empty_input(page:Page):
        page.goto(BASE_URL)
        input =page.get_by_placeholder("Enter number.....")
        input.fill("")

        page.get_by_role(
        "button",name="Cube"
        ).click()
        rasult=page.location("css=p#result")
        expect(result).to_have_text(
            "Enter Somethings!"
        )
