import tornado.web
import tornado.ioloop
from subprocess import Popen
import usefulFunctions

class runHandler(tornado.web.RequestHandler):
    def get(self):
        print("Hello world")
        self.write("Hello, world!!!!!!\n")

class wishHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            n = self.get_argument("n")
        except:
            n = 'User'
        self.write(f'Good morning {n}')
        print(f'Good morning {n}')

 

class fiboRecHandler(tornado.web.RequestHandler):

    def get(self):
        try:
            n = int(self.get_argument("n"))
            res = usefulFunctions.fiboRec(n)
        except Exception as e:
            print(e)
            print(f"Error occured: {e}")

        
        self.write(f'{n}th Fibonacci number is {res}')
        print(f'{n}th Fibonacci number is {res}')

class fiboHandler(tornado.web.RequestHandler):

    def get(self):
        try:
            n = int(self.get_argument("n"))
            res = usefulFunctions.fibo(n)
        except Exception as e:
            print(e)
            print(f"Error occured: {e}")

        
        self.write(f'{n}th Fibonacci number is {res}')
        print(f'{n}th Fibonacci number is {res}')


class factHandler(tornado.web.RequestHandler):

    def get(self):
        try:
            n = int(self.get_argument("n"))
            res = usefulFunctions.fact(n)
        except Exception as e:
            print(e)
            print(f"Error occured: {e}")

        
        self.write(f'{n} factorial is {res}')
        print(f'{n} factorial is {res}')


class factRecHandler(tornado.web.RequestHandler):

    def get(self):
        try:
            n = int(self.get_argument("n"))
            res = usefulFunctions.factRec(n)
        except Exception as e:
            print(e)
            print(f"Error occured: {e}")

        
        self.write(f'{n} factorial is {res}')
        print(f'{n} factorial is {res}')



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", runHandler),
        (r"/wish", wishHandler),
        (r"/fib", fiboHandler),
        (r"/fibRec", fiboRecHandler),
        (r"/fact", factHandler),
        (r"/factRec", factRecHandler),
    ])

    app.listen(8881)
    print("I'm listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
