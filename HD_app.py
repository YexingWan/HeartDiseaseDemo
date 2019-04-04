from app.analysis.routes import app
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
if __name__ == '__main__' :
    app.run()


