from ignis import widgets


def test_slider() -> widgets.Widget:

    slider = widgets.Scale(
        min=0,
        max=100,
        value=33,
        css_classes=["test-slider"],
        draw_value=False
    )

    return slider
