from flask.ext.script import Manager, Server
import main
import models

manager = Manager(main.app)

manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app对象
    return dict(app=main.app,db=models,User=models.User)

if __name__=='__main__':
    manager.run()
