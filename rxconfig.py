import reflex as rx

config = rx.Config(
    app_name="orchard_endeavors",
    api_url="https://orchard-endeavors.com:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)