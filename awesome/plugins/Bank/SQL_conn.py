import pymysql
from awesome.plugins.Bank.SQL_config import CONFIG


class SQL:
    def __init__(self):
        print("---SQL:开始连接---")
        self.start_conn()
        self.__check_init_status()

    # 加载配置
    def __load_config(self) -> dict:
        return CONFIG

    # 开始连接
    def start_conn(self) -> None:
        try:
            config: dict = self.__load_config()
            self.BankBash = pymysql.connect(config['host'],
                                            config['user'],
                                            config['password'],
                                            config['databash'],
                                            config['port'])
            print("---SQL:连接成功---")
        except pymysql.err.ProgrammingError:
            print("---SQL:连接失败---")

    # 关闭连接
    def close_conn(self) -> None:
        print("---SQL:关闭连接---")
        self.BankBash.close()

    # 重启连接
    def restart_conn(self) -> None:
        print("---SQL:重新连接---")
        self.BankBash.close()
        self.start_conn()

    # 新建游标
    def new_cursor(self):
        return self.BankBash.cursor()

    # 检查初始化状态
    def __check_init_status(self):
        c = self.new_cursor()
        print("---SQL:检查初始化---")
        try:
            c.execute("SELECT * FROM qq_bot.Bank")
            print("---SQL:检测到已初始化---")
            return True
        except pymysql.err.ProgrammingError:
            print("---SQL:检测到未初始化---")
            self.initialization()
            return False
        finally:
            c.close()

    # 执行初始化
    def initialization(self):
        c = self.new_cursor()
        with open("iNIT.sql") as f:
            sql = f.read()
        try:
            c.execute(sql)
            self.BankBash.commit()
            print("---SQL:成功初始化---")
        except pymysql.err.ProgrammingError:
            self.BankBash.rollback()
            print("---SQL:初始化失败，加群：866912510 获取帮助---")
        finally:
            c.close()

    # 注册新用户
    def Registered_User(self, qq):
        c = self.new_cursor()
        try:
            c.execute(f"INSERT INTO qq_bot.Bank (QQ) VALUES({qq})")
            self.BankBash.commit()
            return True
        except pymysql.err.ProgrammingError:
            self.BankBash.rollback()
            return False
        finally:
            c.close()

    # BAN用户
    def BAN_User(self, qq):
        c = self.new_cursor()
        try:
            c.execute(f"UPDATE Bank SET BAN=1 WHERE QQ={qq}")
            self.BankBash.commit()
            return True
        except pymysql.err.ProgrammingError:
            self.BankBash.rollback()
            return False
        finally:
            c.close()

    # 注销用户
    def Delete_user(self, qq):
        c = self.new_cursor()
        try:
            c.execute(f"DELETE FROM Bank WHERE QQ={qq}")
            self.BankBash.commit()
            return True
        except pymysql.err.ProgrammingError:
            self.BankBash.rollback()
            return False
        finally:
            c.close()

    # 存款
    def Deposit(self, qq, deposit):
        c = self.new_cursor()
        try:
            c.execute(f"UPDATE qq_bot.Bank SET Balance = {deposit} WHERE QQ = {qq}")
            self.BankBash.commit()
            return True
        except pymysql.err.ProgrammingError:
            self.BankBash.rollback()
            return False
        finally:
            c.close()

    # 检查用户是否存在
    def check_user(self, qq):
        c = self.new_cursor()
        c.execute(f"SELECT * FROM Bank WHERE QQ={qq}")
        data = c.fetchone()
        if data == '':
            return False
        else:
            return True
