import reflex as rx

config = rx.Config(
    app_name="orchard_endeavors",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)