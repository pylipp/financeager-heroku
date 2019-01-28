from financeager import fflask

app = fflask.create_app({"debug": True})

if __name__ == "__main__":
    app.run()
