from flask.ext.script import Manager, Server
import main

manager = Manager(main.app)

manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=main.app)

if __name__=='__main__':
    manager.run()
