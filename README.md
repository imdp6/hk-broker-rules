# 香港券商 Surge 分流规则

以香港券商用户为主的保守域名规则，初版审查日期：2026-10-04。
覆盖富途、长桥、老虎、华盛及盈透的已核实官网和部分服务域名，共 18 条。

这些规则用于选择网络出口，不是防钓鱼白名单，也不证明某个域名下所有内容安全。
域名后缀规则会匹配该域名及全部子域名；集团域名也可能涵盖香港以外的业务。

## 使用

在 Surge 的 `[Rule]` 中加入下面一行。`香港券商` 必须替换为你的实际策略或策略组名称。
按需放在通用直连/代理规则及 `FINAL` 前面；已有安全拦截规则应保持在前。

推荐固定版本，后续更新先查看差异：

```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/imdp6/hk-broker-rules/v1.0.0/rule/Surge/HK-Broker.list,香港券商,update-interval=-1
```

固定提交 SHA 比版本标签更严格（标签可移动）：将 URL 中的 `v1.0.0` 替换为你审查过的完整提交 SHA。
Surge 会下载并缓存规则；上述配置关闭规则文件的自动更新。

若希望跟随仓库更新，可改用以下订阅：

```ini
RULE-SET,https://raw.githubusercontent.com/imdp6/hk-broker-rules/main/rule/Surge/HK-Broker.list,香港券商
```

Surge 外部规则默认每 24 小时重新下载，采用动态订阅即信任未来的仓库修改。

## 单独订阅

仅使用某家券商时，建议只订阅对应文件。将上述 URL 的文件名替换为：

| 券商 | 文件 |
| --- | --- |
| 富途香港 / 富途牛牛 | `Futu.list` |
| 长桥香港 / LongPort | `Longbridge.list` |
| 老虎证券香港 | `Tiger.list` |
| 华盛证券 / 华盛通 | `Huasheng.list` |
| 盈透证券香港 | `IBKR.list` |

## 收录范围和限制

- 只允许 `DOMAIN`、`DOMAIN-SUFFIX`，无 IP 网段、共享分析/广告服务、脚本、MITM、证书或重写配置。
- 每条规则的官方依据和纳入理由见 [sources.json](sources.json)。未确认的域名不凭名称猜测收录。
- 这是保守初版，不是完整的 App 网络端点清单。App 的裸 IP、第三方验证、支付及其他未收录域名会继续匹配你原配置的后续规则，可能走不同出口。
- 没有对真实账户登录、行情和下单做运行测试。使用前在 Surge 请求记录中核对相关连接的最终策略及出口。
- 出口地区由你的策略决定；规则不保证香港出口、访问成功或免除券商风控。请选择可信且稳定的出口，保持 TLS 校验；无需为此启用 MITM。
- 未收录银行、TradingView、嘉信、全球券商合集或不明 `futu0`–`futu9` 等域名。

## 维护与验证

修改 `sources.json`，记录新的官方依据，再执行：

```sh
python3 scripts/build.py
python3 scripts/build.py --check
```

构建脚本检查规则类型、域名格式、来源字段、重复项及输出一致性。CI 仅验证，不联网自动扩充规则。
新增 IP 规则或第三方服务需另行审查，不属于本仓库当前范围。

## 官方参考

- [富途香港](https://www.futuhk.com/hans)
- [长桥香港](https://longbridge.com/hk/zh-CN) · [LongPort 官方应用页面](https://play.google.com/store/apps/details?id=global.longport.app.android) · [长桥 Socket 端点](https://open.longbridge.com/docs/socket/hosts)
- [老虎香港](https://www.itiger.com/hk/hans/) · [机构业务登录入口](https://www-web.itiger.com/hk/inst)
- [华盛通](https://www.hstong.com/hk/about) · [华盛证券](https://www.vbkr.com/promotions/open-account-en)
- [盈透香港](https://www.interactivebrokers.com.hk/cn/)
- [Surge RULE-SET 文档](https://manual.nssurge.com/rules/ruleset.html)
