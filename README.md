# FinancialAutoTest

安享智慧理财 Web 自动化测试项目，基于 Python、Selenium、Page Object 和 Pytest 搭建，覆盖用户端及后台管理端的核心金融业务流程。

## 项目简介

安享智慧理财是线上金融管理系统，包含用户资金托管、信贷额度申请、额度审批等核心业务模块。本项目通过自动化测试验证主要业务流程及页面交互，辅助版本回归，减少重复手工测试工作。

## 业务覆盖

- 用户登录与注册
- 资金托管开户
- 信贷额度申请
- 后台管理端登录
- 信贷额度审核

## 技术栈

- Python
- Selenium WebDriver
- Page Object 设计模式
- Pytest
- Faker
- Allure
- Git / Jenkins

## 框架特点

- 使用 Page Object 分离页面定位、页面操作与测试用例
- 封装元素查找、输入、点击、窗口切换、Frame 切换和下拉框操作
- 使用 Pytest Fixture 管理浏览器生命周期及测试前置条件
- 支持 JSON 测试数据驱动和 Faker 动态测试数据
- 支持运行日志、失败场景截图及 Allure 测试报告
- 可通过 Jenkins 执行回归测试并归档测试结果

## 项目结构

```text
FinancialAutoTest/
├── base/               # 页面公共操作基类
├── data/               # 测试数据
├── img/                # 测试截图
├── page/               # Page Object 页面对象
├── script/             # 自动化测试用例
├── config.py           # 项目地址及动态测试数据配置
├── conftest.py         # Pytest Fixture 配置
├── tool.py             # 浏览器、日志和数据读取工具
├── pytest.ini          # Pytest 运行配置
└── cmd_allure.py       # Allure 报告生成脚本
```

## 环境准备

1. 安装 Python、Google Chrome，以及与 Chrome 版本匹配的 ChromeDriver。
2. 创建并激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. 安装项目依赖：

```powershell
pip install selenium pytest faker allure-pytest
```

4. 在 `config.py` 中配置用户端和后台管理端地址。
5. 在 `tool.py` 中将 ChromeDriver 路径修改为当前运行环境的实际路径。
6. 如需生成可视化测试报告，请安装 Allure Commandline 并将其加入系统 `PATH`。

## 执行测试

运行全部测试：

```powershell
pytest
```

运行指定测试文件：

```powershell
pytest script/test_01_login_json.py -v
```

`pytest.ini` 会将 Allure 原始结果输出到 `report/`。生成并查看报告：

```powershell
python cmd_allure.py
allure open new_report
```

## Jenkins 持续集成

Jenkins 任务可按以下顺序执行：拉取代码、创建运行环境、安装依赖、执行 `pytest`、生成 Allure 报告，并归档测试结果。建议将站点地址、浏览器驱动路径和测试账号配置为 Jenkins 参数或凭据，避免在代码中保存环境相关信息。

## 工作职责

- 搭建基于 Python、Selenium、Page Object 和 Pytest 的 Web 自动化测试框架，封装页面公共操作、浏览器管理、日志及数据读取能力。
- 编写登录、注册、资金托管开户、信贷额度申请、后台登录与额度审核等核心业务自动化测试脚本。
- 执行版本回归自动化测试，校验金融业务流程和页面交互逻辑，及时定位并反馈页面缺陷。
- 使用 Git 管理自动化脚本版本，对接 Jenkins 持续集成任务，降低重复手工测试成本并提升回归效率。

## 说明

本项目仅用于测试与学习场景。运行自动化测试前，请确认目标环境、测试账号及相关数据已准备就绪。
