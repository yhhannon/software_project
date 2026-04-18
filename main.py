import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import csv
import datetime
import ctypes
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 高清适配
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

LANG = {
    "zh": {
        "title": "个人记账本",
        "lang_text": "语言",
        "currency_text": "默认币种",
        "btn_record": "记账",
        "btn_history": "记录",
        "btn_stats": "统计",
        "btn_exchange": "汇率",
        "btn_clear": "清空数据",
        "btn_show_pie": "显示饼状图",
        "type": "类型",
        "expense": "支出",
        "income": "收入",
        "amount": "金额",
        "category": "分类",
        "note": "备注",
        "date": "日期",
        "time": "时间",
        "save": "保存记录",
        "filter_cat": "分类",
        "filter_min": "最小金额",
        "filter_max": "最大金额",
        "filter_btn": "筛选",
        "export_csv": "导出CSV",
        "sort_time": "按时间",
        "sort_amount": "按金额",
        "asc": "升序",
        "today": "今日支出",
        "week": "本周支出",
        "month": "本月支出",
        "chart_title": "分类消费占比",
        "mop": "澳门元(MOP)",
        "cny": "人民币(CNY)",
        "hkd": "港币(HKD)",
        "day": "日",
        "week": "周",
        "month": "月",
        "time_col": "时间",
        "type_col": "类型",
        "amount_col": "金额",
        "category_col": "分类",
        "note_col": "备注",
        "hour": "时",
        "minute": "分",
        "confirm_date": "确认日期",
        "clear_date": "清除日期",
        "tip_empty": "金额和分类不能为空",
        "tip_num": "请输入有效正数",
        "tip_save": "保存成功",
        "tip_export": "导出成功",
        "tip_invalid": "请输入数字",
        "tip_date": "日期无效",
        "clear_all": "清空全部数据",
        "clear_range": "按日期区间清空",
        "start_date": "开始日期 (YYYY-MM-DD)",
        "end_date": "结束日期 (YYYY-MM-DD)",
        "confirm_clear": "确定删除？此操作不可恢复！",
        "clear_success": "清空成功",
        "date_format_err": "日期格式错误",
        "delete_selected": "删除选中记录",
        "no_selection": "请先选择一条记录"
    },
    "en": {
        "title": "Finance Tracker",
        "lang_text": "Language",
        "currency_text": "Currency",
        "btn_record": "Record",
        "btn_history": "History",
        "btn_stats": "Stats",
        "btn_exchange": "Exchange",
        "btn_clear": "Clear Data",
        "btn_show_pie": "Show Pie Chart",
        "type": "Type",
        "expense": "Expense",
        "income": "Income",
        "amount": "Amount",
        "category": "Category",
        "note": "Note",
        "date": "Date",
        "time": "Time",
        "save": "Save",
        "filter_cat": "Category",
        "filter_min": "Min",
        "filter_max": "Max",
        "filter_btn": "Filter",
        "export_csv": "Export CSV",
        "sort_time": "Time",
        "sort_amount": "Amount",
        "asc": "Asc",
        "today": "Today",
        "week": "Week",
        "month": "Month",
        "chart_title": "Category Ratio",
        "mop": "MOP",
        "cny": "CNY",
        "hkd": "HKD",
        "day": "Day",
        "week": "Week",
        "month": "Month",
        "time_col": "Time",
        "type_col": "Type",
        "amount_col": "Amount",
        "category_col": "Category",
        "note_col": "Note",
        "hour": "Hour",
        "minute": "Minute",
        "confirm_date": "Confirm Date",
        "clear_date": "Clear Date",
        "tip_empty": "Amount & Category required",
        "tip_num": "Enter positive number",
        "tip_save": "Saved",
        "tip_export": "Exported",
        "tip_invalid": "Invalid number",
        "tip_date": "Invalid date",
        "clear_all": "Clear All",
        "clear_range": "Clear Range",
        "start_date": "Start Date (YYYY-MM-DD)",
        "end_date": "End Date (YYYY-MM-DD)",
        "confirm_clear": "Confirm delete? Cannot be undone!",
        "clear_success": "Cleared",
        "date_format_err": "Date format error",
        "delete_selected": "Delete Selected",
        "no_selection": "Please select an item first"
    },
    "ko": {
        "title": "가계부",
        "lang_text": "언어",
        "currency_text": "통화",
        "btn_record": "기록",
        "btn_history": "내역",
        "btn_stats": "통계",
        "btn_exchange": "환율",
        "btn_clear": "데이터 지우기",
        "btn_show_pie": "파이 차트 보기",
        "type": "유형",
        "expense": "지출",
        "income": "수입",
        "amount": "금액",
        "category": "분류",
        "note": "비고",
        "date": "날짜",
        "time": "시간",
        "save": "저장",
        "filter_cat": "분류",
        "filter_min": "최소",
        "filter_max": "최대",
        "filter_btn": "필터",
        "export_csv": "CSV 내보내기",
        "sort_time": "시간순",
        "sort_amount": "금액순",
        "asc": "오름차순",
        "today": "오늘",
        "week": "이번주",
        "month": "이번달",
        "chart_title": "분류 비율",
        "mop": "마카오 파타카",
        "cny": "위안",
        "hkd": "홍콩 달러",
        "day": "일",
        "week": "주",
        "month": "월",
        "time_col": "시간",
        "type_col": "유형",
        "amount_col": "금액",
        "category_col": "분류",
        "note_col": "비고",
        "hour": "시",
        "minute": "분",
        "confirm_date": "날짜 확인",
        "clear_date": "날짜 지우기",
        "tip_empty": "금액과 분류 필요",
        "tip_num": "양수 입력",
        "tip_save": "저장됨",
        "tip_export": "내보냄",
        "tip_invalid": "숫자 아님",
        "tip_date": "잘못된 날짜",
        "clear_all": "전체 지우기",
        "clear_range": "기간별 지우기",
        "start_date": "시작일 (YYYY-MM-DD)",
        "end_date": "종료일 (YYYY-MM-DD)",
        "confirm_clear": "삭제할까요? 복구할 수 없습니다!",
        "clear_success": "삭제됨",
        "date_format_err": "날짜 형식 오류",
        "delete_selected": "선택 삭제",
        "no_selection": "항목을 선택하세요"
    }
}

class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("个人记账本")
        self.geometry("1000x700")
        self.resizable(True, True)

        self.lang = tk.StringVar(value="zh")
        self.currency = tk.StringVar(value="MOP")
        self.rates = {"CNY": 0.79, "HKD": 0.96, "MOP": 1.0}
        self.records = []
        self.chart_period = tk.StringVar(value="month")
        self.selected_date = None

        self.load_exchange()
        self.load_csv()
        self.build_layout()
        self.apply_lang()
        self.reset_pie_to_button()

    def load_exchange(self):
        try:
            r = requests.get("https://api.exchangerate-api.com/v4/latest/MOP", timeout=2)
            d = r.json()
            self.rates["CNY"] = d["rates"]["CNY"]
            self.rates["HKD"] = d["rates"]["HKD"]
        except:
            pass

    def cv(self, amt, fcur):
        amt = float(amt)
        if fcur == self.currency.get():
            return round(amt, 2)
        mop = amt / self.rates[fcur]
        return round(mop * self.rates[self.currency.get()], 2)

    def build_layout(self):
        top_frame = ttk.Frame(self, height=260)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        top_frame.pack_propagate(False)

        left_top = ttk.Frame(top_frame, width=480)
        left_top.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        left_top.pack_propagate(False)

        ttk.Label(left_top, textvariable=self.t("lang_text")).grid(row=0, column=0, sticky="w", pady=4)
        self.lang_cb = ttk.Combobox(left_top, state="readonly", width=12)
        self.lang_cb["values"] = ["中文", "English", "한국어"]
        self.lang_cb.set("中文")
        self.lang_cb.grid(row=0, column=1, padx=5)
        self.lang_cb.bind("<<ComboboxSelected>>", self._set_lang_code)

        ttk.Label(left_top, textvariable=self.t("currency_text")).grid(row=1, column=0, sticky="w", pady=4)
        self.cur_cb = ttk.Combobox(left_top, textvariable=self.currency, state="readonly", width=10)
        self.cur_cb["values"] = ["MOP", "CNY", "HKD"]
        self.cur_cb.grid(row=1, column=1, padx=5)
        self.cur_cb.bind("<<ComboboxSelected>>", self.on_cur_change)

        ttk.Label(left_top, text="周期：").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Radiobutton(left_top, textvariable=self.t("day"), variable=self.chart_period, value="day", command=self.reset_pie_to_button).grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(left_top, textvariable=self.t("week"), variable=self.chart_period, value="week", command=self.reset_pie_to_button).grid(row=2, column=2, sticky="w")
        ttk.Radiobutton(left_top, textvariable=self.t("month"), variable=self.chart_period, value="month", command=self.reset_pie_to_button).grid(row=2, column=3, sticky="w")

        btn_frame = ttk.Frame(left_top)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=15)
        self.b1 = ttk.Button(btn_frame, textvariable=self.t("btn_record"), width=10, command=lambda: self.show(0))
        self.b2 = ttk.Button(btn_frame, textvariable=self.t("btn_history"), width=10, command=lambda: self.show(1))
        self.b3 = ttk.Button(btn_frame, textvariable=self.t("btn_stats"), width=10, command=lambda: self.show(2))
        self.b4 = ttk.Button(btn_frame, textvariable=self.t("btn_exchange"), width=10, command=lambda: self.show(3))
        self.b5 = ttk.Button(btn_frame, textvariable=self.t("btn_clear"), width=10, command=self.open_clear_window)
        self.b1.pack(side=tk.LEFT, padx=4)
        self.b2.pack(side=tk.LEFT, padx=4)
        self.b3.pack(side=tk.LEFT, padx=4)
        self.b4.pack(side=tk.LEFT, padx=4)
        self.b5.pack(side=tk.LEFT, padx=4)

        right_top = ttk.Frame(top_frame, width=480, height=240)
        right_top.pack(side=tk.RIGHT, padx=5)
        right_top.pack_propagate(False)
        self.pie_frame = right_top

        self.notebook_frame = ttk.Frame(self)
        self.notebook_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.nb = ttk.Notebook(self.notebook_frame)
        self.t1 = ttk.Frame(self.nb)
        self.t2 = ttk.Frame(self.nb)
        self.t3 = ttk.Frame(self.nb)
        self.t4 = ttk.Frame(self.nb)
        self.nb.add(self.t1)
        self.nb.add(self.t2)
        self.nb.add(self.t3)
        self.nb.add(self.t4)
        self.nb.pack(fill=tk.BOTH, expand=True)

        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()

    def t(self, key):
        v = tk.StringVar()
        def upd(*_): v.set(LANG[self.lang.get()][key])
        upd()
        self.lang.trace_add("write", upd)
        return v

    def _set_lang_code(self, *_):
        s = self.lang_cb.get()
        if s == "中文": self.lang.set("zh")
        elif s == "English": self.lang.set("en")
        elif s == "한국어": self.lang.set("ko")
        self.apply_lang()

    def apply_lang(self):
        self.title(LANG[self.lang.get()]["title"])
        self.reset_pie_to_button()
        self.refresh_list()
        self.refresh_stats()
        self.update_tree_headers()

    def show(self, i):
        self.nb.select(i)
        self.reset_pie_to_button()
        if i == 1: self.refresh_list()
        if i == 2: self.refresh_stats()

    def on_cur_change(self, *_):
        self.reset_pie_to_button()
        self.refresh_list()
        self.refresh_stats()

    # ====================== 饼图改为按钮 + 点击显示
    def reset_pie_to_button(self):
        for w in self.pie_frame.winfo_children():
            w.destroy()
        self.pie_btn = ttk.Button(
            self.pie_frame,
            textvariable=self.t("btn_show_pie"),
            command=self.draw_pie
        )
        self.pie_btn.pack(expand=True, ipadx=20, ipady=10)

    def draw_pie(self):
        for w in self.pie_frame.winfo_children():
            w.destroy()
        L = LANG[self.lang.get()]
        period = self.chart_period.get()
        today = datetime.date.today()

        cat_sum = {}
        for r in self.records:
            if len(r) < 7: continue
            s = r[6]
            try:
                if " " in s:
                    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
                else:
                    dt = datetime.datetime.strptime(s, "%Y-%m-%d")
            except:
                continue

            ok = False
            if period == "day":
                ok = (dt.date() == today)
            elif period == "week":
                ok = (dt.isocalendar()[:2] == today.isocalendar()[:2])
            else:
                ok = (dt.strftime("%Y-%m") == today.strftime("%Y-%m"))
            if not ok: continue

            if r[1] in [L["expense"], "支出", "Expense", "지출"]:
                amt = self.cv(r[2], r[5])
                cat_sum[r[3]] = cat_sum.get(r[3], 0) + amt

        if not cat_sum:
            ttk.Label(self.pie_frame, text=L["chart_title"] + " — 暂无记录").pack(expand=True)
            return

        fig = Figure(figsize=(4.0, 4.0), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(
            cat_sum.values(),
            labels=cat_sum.keys(),
            autopct="%.0f%%",
            radius=0.8,
            textprops={"size":9},
            pctdistance=0.75,
            labeldistance=1.05
        )
        ax.set_aspect("equal")
        fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
        canvas = FigureCanvasTkAgg(fig, self.pie_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # ====================== 清空数据
    def open_clear_window(self):
        L = LANG[self.lang.get()]
        top = tk.Toplevel(self)
        top.title(L["btn_clear"])
        top.geometry("300x180")
        top.grab_set()
        ttk.Button(top, text=L["clear_all"], command=lambda: [top.destroy(), self.do_clear_all()]).pack(pady=12)
        ttk.Button(top, text=L["clear_range"], command=lambda: [top.destroy(), self.do_clear_range()]).pack(pady=12)

    def do_clear_all(self):
        L = LANG[self.lang.get()]
        if messagebox.askokcancel(L["btn_clear"], L["confirm_clear"]):
            self.records.clear()
            self.save_csv()
            self.reset_pie_to_button()
            self.refresh_list()
            messagebox.showinfo(L["btn_clear"], L["clear_success"])

    def do_clear_range(self):
        L = LANG[self.lang.get()]
        start = simpledialog.askstring(L["btn_clear"], L["start_date"])
        end = simpledialog.askstring(L["btn_clear"], L["end_date"])
        if not start or not end: return

        try:
            datetime.date.fromisoformat(start)
            datetime.date.fromisoformat(end)
        except ValueError:
            messagebox.showerror(L["btn_clear"], L["date_format_err"])
            return

        if messagebox.askokcancel(L["btn_clear"], L["confirm_clear"]):
            new_rec = []
            for r in self.records:
                if len(r) <7:
                    new_rec.append(r)
                    continue
                s = r[6].split(" ")[0]
                if not (start <= s <= end):
                    new_rec.append(r)
            self.records = new_rec
            self.save_csv()
            self.reset_pie_to_button()
            self.refresh_list()
            messagebox.showinfo(L["btn_clear"], L["clear_success"])

    # ====================== 单条删除
    def delete_selected_row(self, event=None):
        L = LANG[self.lang.get()]
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(L["btn_clear"], L["no_selection"])
            return

        if messagebox.askokcancel(L["delete_selected"], L["confirm_clear"]):
            for item in selected:
                idx = self.tree.index(item)
                if 0 <= idx < len(self.records):
                    self.records.pop(idx)
            self.save_csv()
            self.reset_pie_to_button()
            self.refresh_list()

    # ====================== 记账
    def init_tab1(self):
        f = ttk.Frame(self.t1, padding=20)
        f.pack(fill=tk.BOTH, expand=1)
        ttk.Label(f, textvariable=self.t("type")).grid(row=0, column=0, sticky="w", pady=8)
        self.tp = tk.StringVar(value=LANG[self.lang.get()]["expense"])
        ttk.Radiobutton(f, textvariable=self.t("expense"), variable=self.tp, value=LANG[self.lang.get()]["expense"]).grid(row=0, column=1)
        ttk.Radiobutton(f, textvariable=self.t("income"), variable=self.tp, value=LANG[self.lang.get()]["income"]).grid(row=0, column=2)

        ttk.Label(f, textvariable=self.t("amount")).grid(row=1, column=0, sticky="w", pady=8)
        self.amt = ttk.Entry(f)
        self.amt.grid(row=1, column=1, columnspan=2, sticky="ew", pady=3)

        ttk.Label(f, textvariable=self.t("category")).grid(row=2, column=0, sticky="w", pady=8)
        self.cat = ttk.Entry(f)
        self.cat.grid(row=2, column=1, columnspan=2, sticky="ew", pady=3)

        ttk.Label(f, textvariable=self.t("note")).grid(row=3, column=0, sticky="w", pady=8)
        self.note = ttk.Entry(f)
        self.note.grid(row=3, column=1, columnspan=2, sticky="ew", pady=3)

        ttk.Label(f, textvariable=self.t("date")).grid(row=4, column=0, sticky="w", pady=8)
        years = [str(y) for y in range(2000, 2100)]
        months = [f"{m:02d}" for m in range(1,13)]
        days = [f"{d:02d}" for d in range(1,32)]
        self.y = ttk.Combobox(f, values=years, width=6)
        self.m = ttk.Combobox(f, values=months, width=4)
        self.d = ttk.Combobox(f, values=days, width=4)
        self.y.grid(row=4, column=1, padx=2)
        self.m.grid(row=4, column=2, padx=2)
        self.d.grid(row=4, column=3, padx=2)
        self.y.set(""); self.m.set(""); self.d.set("")

        ttk.Button(f, textvariable=self.t("confirm_date"), command=self.confirm_date).grid(row=4, column=4, padx=2)
        ttk.Button(f, textvariable=self.t("clear_date"), command=self.clear_date).grid(row=4, column=5, padx=2)

        ttk.Label(f, textvariable=self.t("time")).grid(row=5, column=0, sticky="w", pady=8)
        self.hh = ttk.Entry(f, width=5)
        self.hh.grid(row=5, column=1, padx=2)
        ttk.Label(f, textvariable=self.t("hour")).grid(row=5, column=2)
        self.mm = ttk.Entry(f, width=5)
        self.mm.grid(row=5, column=3, padx=2)
        ttk.Label(f, textvariable=self.t("minute")).grid(row=5, column=4)

        ttk.Button(f, textvariable=self.t("save"), command=self.add_rec).grid(row=6, column=1, pady=12)

    def confirm_date(self):
        L = LANG[self.lang.get()]
        try:
            y = int(self.y.get())
            m = int(self.m.get())
            d = int(self.d.get())
            if m == 2:
                leap = (y%4==0 and y%100!=0) or (y%400==0)
                if (leap and d>29) or (not leap and d>28):
                    raise Exception()
            self.selected_date = datetime.date(y,m,d)
        except:
            messagebox.showwarning("", L["tip_date"])

    def clear_date(self):
        self.y.set("")
        self.m.set("")
        self.d.set("")
        self.selected_date = None

    def add_rec(self):
        L = LANG[self.lang.get()]
        a = self.amt.get().strip()
        c = self.cat.get().strip()
        if not a or not c:
            messagebox.showwarning("", L["tip_empty"])
            return
        try:
            a = float(a)
            if a <= 0:
                messagebox.showwarning("", L["tip_num"])
                return
        except:
            messagebox.showwarning("", L["tip_num"])
            return

        dt = self.selected_date or datetime.date.today()
        hh = self.hh.get().strip()
        mm = self.mm.get().strip()
        dt_str = f"{dt} {hh}:{mm}" if (hh and mm) else str(dt)

        self.records.append([dt_str, self.tp.get(), a, c, self.note.get(), self.currency.get(), dt_str])
        self.save_csv()
        self.reset_pie_to_button()
        self.amt.delete(0,tk.END)
        self.cat.delete(0,tk.END)
        self.note.delete(0,tk.END)
        self.hh.delete(0,tk.END)
        self.mm.delete(0,tk.END)
        messagebox.showinfo("", L["tip_save"])

    # ====================== 记录列表
    def init_tab2(self):
        f = ttk.Frame(self.t2)
        f.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(f, textvariable=self.t("filter_cat")).grid(row=0, column=0)
        self.fc = ttk.Entry(f, width=10)
        self.fc.grid(row=0, column=1, padx=3)
        ttk.Label(f, textvariable=self.t("filter_min")).grid(row=0, column=2)
        self.fm = ttk.Entry(f, width=6)
        self.fm.grid(row=0, column=3, padx=3)
        ttk.Label(f, textvariable=self.t("filter_max")).grid(row=0, column=4)
        self.fx = ttk.Entry(f, width=6)
        self.fx.grid(row=0, column=5, padx=3)
        ttk.Button(f, textvariable=self.t("filter_btn"), command=self.refresh_list).grid(row=0, column=6, padx=3)
        ttk.Button(f, textvariable=self.t("export_csv"), command=self.export_csv).grid(row=0, column=7, padx=3)

        f2 = ttk.Frame(self.t2)
        f2.pack(fill=tk.X, padx=5)
        self.sby = tk.StringVar(value="time")
        ttk.Radiobutton(f2, textvariable=self.t("sort_time"), variable=self.sby, value="time").pack(side=tk.LEFT)
        ttk.Radiobutton(f2, textvariable=self.t("sort_amount"), variable=self.sby, value="amt").pack(side=tk.LEFT)
        self.sasc = tk.BooleanVar()
        ttk.Checkbutton(f2, textvariable=self.t("asc"), variable=self.sasc).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(self.t2, columns=["a","b","c","d","e"], show="headings", height=12)
        style = ttk.Style()
        style.configure("Treeview", rowheight=24)
        self.tree.pack(fill=tk.BOTH, expand=1, padx=5, pady=8)

        self.tree.bind("<Delete>", self.delete_selected_row)
        self.menu = tk.Menu(self.tree, tearoff=0)
        self.update_right_click_menu()

    def update_right_click_menu(self):
        self.menu.delete(0, tk.END)
        L = LANG[self.lang.get()]
        self.menu.add_command(label=L["delete_selected"], command=self.delete_selected_row)
        self.tree.bind("<Button-3>", lambda e: self.menu.post(e.x_root, e.y_root))

    def update_tree_headers(self):
        L = LANG[self.lang.get()]
        cols = [L["time_col"], L["type_col"], L["amount_col"], L["category_col"], L["note_col"]]
        for i, t in enumerate(cols):
            self.tree.heading(i, text=t)
            self.tree.column(i, width=160, anchor="center")

    def refresh_list(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        L = LANG[self.lang.get()]
        for r in self.records:
            if len(r) <7: continue
            amt = self.cv(r[2], r[5])
            tp = r[1]
            if tp in ["支出", "Expense", "지출"]: tp = L["expense"]
            if tp in ["收入", "Income", "수입"]: tp = L["income"]
            self.tree.insert("", "end", values=[r[6], tp, f"{amt:.2f}", r[3], r[4]])
        self.update_right_click_menu()

    # ====================== 统计
    def init_tab3(self):
        f = ttk.Frame(self.t3, padding=15)
        f.pack(fill=tk.BOTH, expand=1)
        self.st = tk.Text(f, height=12)
        self.st.pack(fill=tk.BOTH, expand=True)

    def refresh_stats(self):
        self.st.delete(1.0, tk.END)
        L = LANG[self.lang.get()]
        c = self.currency.get()
        today_sum = 0
        today = str(datetime.date.today())
        for r in self.records:
            if len(r)>=7 and today in r[6] and r[1] in [L["expense"],"支出","Expense","지출"]:
                today_sum += self.cv(r[2], r[5])
        self.st.insert("end", f"{L['today']} {today_sum:.2f} {c}\n")

    # ====================== 汇率
    def init_tab4(self):
        f = ttk.Frame(self.t4, padding=25)
        f.pack(fill=tk.BOTH, expand=1)
        ttk.Label(f, textvariable=self.t("mop")).grid(row=0, column=0, sticky="w", pady=10)
        self.em = ttk.Entry(f)
        self.em.grid(row=0, column=1, sticky="ew", pady=5)
        self.em.bind("<KeyRelease>", lambda _: self.ex("m"))
        ttk.Label(f, textvariable=self.t("cny")).grid(row=1, column=0, sticky="w", pady=10)
        self.ec = ttk.Entry(f)
        self.ec.grid(row=1, column=1, sticky="ew", pady=5)
        ttk.Label(f, textvariable=self.t("hkd")).grid(row=2, column=0, sticky="w", pady=10)
        self.eh = ttk.Entry(f)
        self.eh.grid(row=2, column=1, sticky="ew", pady=5)
        f.grid_columnconfigure(1, weight=1)

    def ex(self, s):
        try:
            if s == "m":
                m = float(self.em.get())
                self.ec.delete(0,tk.END)
                self.eh.delete(0,tk.END)
                self.ec.insert(0, f"{m*self.rates['CNY']:.2f}")
                self.eh.insert(0, f"{m*self.rates['HKD']:.2f}")
        except:
            pass

    # ====================== CSV
    def save_csv(self):
        with open("records.csv","w",encoding="utf-8",newline="") as f:
            csv.writer(f).writerows(self.records)

    def load_csv(self):
        try:
            with open("records.csv","r",encoding="utf-8") as f:
                self.records = list(csv.reader(f))
        except FileNotFoundError:
            self.records = []

    def export_csv(self):
        p = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV","*.csv")])
        if p:
            with open(p,"w",encoding="utf-8-sig",newline="") as f:
                csv.writer(f).writerows(self.records)
            messagebox.showinfo("", LANG[self.lang.get()]["tip_export"])

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
