import tkinter as tk
from tkinter import ttk, filedialog
import traceback
import os
from dotenv import load_dotenv, set_key
import threading
from manager.main_manager import MainManager
from util.db_relate import check_tables_exist, init_tables, test_connection, delete_tables 
from util.constants import CHANGE_SETTING, TEST_CONNECTION, CREATE_TABLES, CHECK_EXIST_TABLES, RESET_DATABASE
from util.helper import get_root_dir
class DatabaseFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        root_dir = get_root_dir()
        # Find the .env file (assuming it's in the project root)
        self.env_path = root_dir / '.env'
        print(self.env_path)
        load_dotenv(dotenv_path=self.env_path)

        # Labels and Entries for Configuration
        self.host_label = tk.Label(self, text="HOST")
        self.host_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.host_entry = tk.Entry(self, width=30)
        self.host_entry.insert(0, os.environ.get('DB_HOST', ''))
        self.host_entry.grid(row=0, column=1, sticky="we", padx=5, pady=5)

        self.port_label = tk.Label(self, text="PORT")
        self.port_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.port_entry = tk.Entry(self, width=30)
        self.port_entry.insert(0, os.environ.get('DB_PORT', ''))
        self.port_entry.grid(row=1, column=1, sticky="we", padx=5, pady=5)

        self.db_name_label = tk.Label(self, text="DB_NAME")
        self.db_name_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.db_name_entry = tk.Entry(self, width=30)
        self.db_name_entry.insert(0, os.environ.get('DB_DATABASE', ''))
        self.db_name_entry.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        self.user_label = tk.Label(self, text="USER")
        self.user_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.user_entry = tk.Entry(self, width=30)
        self.user_entry.insert(0, os.environ.get('DB_USER', ''))
        self.user_entry.grid(row=3, column=1, sticky="we", padx=5, pady=5)

        self.password_label = tk.Label(self, text="PASSWORD")
        self.password_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.insert(0, os.environ.get('DB_PASSWORD', ''))
        self.password_entry.grid(row=4, column=1, sticky="we", padx=5, pady=5)

        # Operation Selection
        self.operation_label = tk.Label(self, text="操作を選択")
        self.operation_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.operation_choices = [
            CHANGE_SETTING,
            TEST_CONNECTION,
            CREATE_TABLES,
            CHECK_EXIST_TABLES,
            RESET_DATABASE
        ]
        self.operation_var = tk.StringVar(value=self.operation_choices[0])
        self.operation_dropdown = ttk.Combobox(self, textvariable=self.operation_var, 
                                             values=self.operation_choices, state="readonly")
        self.operation_dropdown.grid(row=5, column=1, sticky="we", padx=5, pady=5)

        # Execute Button (Unified)
        self.execute_button = tk.Button(self, text="実行", command=self.execute_operation)
        self.execute_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Status Label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Make Columns Expandable
        self.grid_columnconfigure(1, weight=1)

    def save_settings(self): # Move to execute Operations
        """Save settings to the .env file."""
        new_config = {
            "DB_HOST": self.host_entry.get(),
            "DB_PORT": self.port_entry.get(),
            "DB_DATABASE": self.db_name_entry.get(),
            "DB_USER": self.user_entry.get(),
            "DB_PASSWORD": self.password_entry.get()
        }

        try:
            # Run in Separate Thread
            threading.Thread(target=self._write_dotenv, args=(new_config,)).start()

        except Exception as e:
            self.show_status(f"設定を保存できませんでした: {e}", "red") 
            traceback.print_exc()

    def _write_dotenv(self, new_config):
        try:
            for key, value in new_config.items():
                set_key(self.env_path, key, value)  # set_key only accepts str values
            self.show_status("設定を保存しました", "green")  # Success
        except Exception as e:
            self.show_status(f"設定ファイルの書き込みエラー: {e}", "red")
            traceback.print_exc()

    def test_connection(self):
        try:
            connect = test_connection() # Get connect info from .evn from test connection

            if connect:
                self.show_status("データベースに接続成功", "green") # Connect to database
            else:
                self.show_status("データベースへの接続に失敗しました", "red") # Connect failed

        except KeyError as e:
            self.show_status(f"必要な環境変数が不足しています: {e}", "red")  # Check environment
        except ValueError as e:
            self.show_status(f"ポートは整数でなければなりません", "red")  # Port must be integer
        except Exception as e:
            self.show_status(f"接続テスト中にエラーが発生しました: {e}", "red")
            traceback.print_exc()

    def init_db(self):
        try:
            init_tables()
            self.show_status("データベースを初期化しました", "green") # Init database
        except Exception as e:
            self.show_status(f"データベースの初期化に失敗しました: {e}", "red") # Init database failed
            traceback.print_exc()

    def reset_db(self):
        try:
            delete_tables()
            self.show_status("データベースをリセットしました", "green")
        except Exception as e:
            self.show_status(f"データベースのリセットに失敗しました: {e}", "red") 
            traceback.print_exc()

    def check_exist_table(self): # Check is exist
        try:
            tables = check_tables_exist() # get tables is exist from check table exist.

            # Implement Your Table Name display Logic
            table_names = ", ".join(tables)
            self.show_status(f"テーブルが存在します: {table_names}", "green") # Table is Exist

        except Exception as e:
            self.show_status(f"テーブルの存在確認に失敗しました: {e}", "red") # Table is Exist failed
            traceback.print_exc()


    def execute_operation(self):
        selected_operation = self.operation_var.get() #get operation name

        if selected_operation == CHANGE_SETTING: #save config
            self.save_settings()
        elif selected_operation == TEST_CONNECTION: # test connect
            self.test_connection()
        elif selected_operation == CREATE_TABLES: # init data
            self.init_db()
        elif selected_operation == RESET_DATABASE: # reset database
            self.reset_db()
        elif selected_operation ==CHECK_EXIST_TABLES: # check is exist
            self.check_exist_table()
        else:
            self.show_status("無効な操作", "red")  # Invalid Operation

    def show_status(self, message, color):
        self.status_label.config(text=message, fg=color)
        self.master.update()




class CSVInputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.path_label = tk.Label(self, text="CSVファイルが格納されているフォルダのパスを入力してください")
        self.path_label.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)
        self.csv_input_label = tk.Label(self, text="CSVフォルダ")
        self.csv_input_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)  
        # Entry for path input
        self.path_entry = tk.Entry(self, width=50)
        self.path_entry.grid(row=3, column=1, sticky="we", padx=5, pady=5)  

        # Browse button
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=3, column=1, sticky="e", padx=5, pady=5)

        # Execute button
        self.execute_button = tk.Button(self, text="実行", command=self.execute)
        self.execute_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Error message label (initially hidden)
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.program_running_label = tk.Label(self, text="", fg="green")  
        self.program_running_label.grid(row=5, column=0, padx=5, pady=5,columnspan=2)  
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(1, weight=0)

    def browse_folder(self):
        
        folder_selected = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END) 
        self.path_entry.insert(0, folder_selected)


    def execute(self):
        path = self.path_entry.get()
        if not path:
            self.show_error("パスを入力してください") 
            return

        if not os.path.exists(path):
            self.show_error("指定されたパスが存在しません") 
            return

        if not os.path.isdir(path):
            self.show_error("指定されたパスはディレクトリではありません")  
            return

        # Simulate program execution (replace with your actual logic)
        self.program_running_label.config(text="プログラムが実行中です")
        self.master.update() 
        try:
            main_app = MainManager(path)
            main_app.main()
         
        except Exception as e:
            self.show_error(f"エラーが発生しました: {e}") 
            self.program_running_label.config(text="")  



    def show_error(self, message):
        self.error_label.config(text=message)  # Set the error message
        self.error_label.config(fg="red") 
        self.master.update()
        
    def show_status(self, message, color):
        self.status_label.config(text=message, fg=color)
        self.master.update()
        
        def clear_error(self):
          self.error_label.config(text="") 
          self.master.update()
