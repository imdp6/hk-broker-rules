# Longbridge Pro 用户实测补充

证据：用户于 2026-10-04 提供的 Surge 请求记录截图（截屏2026-10-04 21.14.37.png）。
截图将以下请求归于 Longbridge Pro 或其 Helper。此记录证明应用发起过这些连接，
不证明主机所有权、业务必要性或连接成功。仅记录域名，不上传截图及其他连接详情。
用户明确要求将截图中的主机加入分流规则。

| 主机 | 规则覆盖 |
| --- | --- |
| api-status.longbridgeapp.com | 新增精确 DOMAIN |
| geotest.lbkrs.com | 已有 lbkrs.com 后缀 |
| o333560.ingest.us.sentry.io | 新增精确 DOMAIN；第三方 Sentry 遥测 |
| api-gl.lbkrs.com | 已有 lbkrs.com 后缀 |
| event-tracking.lbctrl.com | 新增精确 DOMAIN；事件遥测 |
| assets.lbctrl.com | 已有精确 DOMAIN |
| mr.lbkrs.com | 已有 lbkrs.com 后缀 |
| quote-gl.lbkrs.com | 已有 lbkrs.com 后缀 |
| download.wbrks.com | 新增精确 DOMAIN |
| lb-desktop.lbctrl.com | 新增精确 DOMAIN |
| ws-gl.lbkrs.com | 已有 lbkrs.com 后缀 |
| admin-ws.lbkrs.com | 已有 lbkrs.com 后缀 |
| performance-data.lbkrs.com | 已有 lbkrs.com 后缀 |
| lb-hk-desktop.oss-cn-hongkong.aliyuncs.com | Dashboard 后续观察补充，精确 DOMAIN |
| sg.app.wbrks.com | Dashboard 后续观察补充，精确 DOMAIN |
| papertrading.app.wbrks.com | Dashboard 后续观察补充，精确 DOMAIN |

规则不包含端口后缀；截图中的 :443 不属于域名。
Sentry 使用精确主机匹配，不添加 sentry.io、ingest.us.sentry.io 等共享后缀。
新增匹配只改变出口选择，不启用、关闭或拦截应用遥测。

后续补充：2026-10-04 通过 Surge Dashboard 核对到上述 OSS 主机由 Longbridge Pro 发起。用户明确要求将其加入规则，以便手机端按域名选择香港出口。桌面记录不能证明手机端全部服务已覆盖。

再次核对：2026-10-04 Dashboard 的 Longbridge Pro 经典版请求记录显示，
Longbridge Pro Helper 于 21:31:41、21:33:06 访问 `sg.app.wbrks.com:443`，
于 21:31:44 访问 `papertrading.app.wbrks.com:443`，策略栏均为 `🇭🇰`。
按用户要求补入两个精确 DOMAIN，不扩展为整个 `wbrks.com` 后缀。
同批出现的 `assets.lbkrs.com`、`m.lbkrs.com`、`event-tracking.lbkrs.com`、
`performance-data.lbkrs.com` 已由 `lbkrs.com` 后缀规则覆盖。
这两条新增规则收录于 `v1.0.3`，旧版本 `v1.0.2` 不包含；尚未在手机端验证。
