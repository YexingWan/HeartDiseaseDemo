import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.analysis.routes import app



if __name__ == '__main__' :
    app.run()


