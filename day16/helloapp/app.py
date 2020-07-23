from controller.HelloController import Hello

class MyApp():

    def execute(self):
        h = Hello()
        h.hello_in_french()

app = MyApp()
app.execute()
