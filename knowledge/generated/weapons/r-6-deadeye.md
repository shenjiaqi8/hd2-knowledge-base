---
id: "r-6-deadeye"
name: "R-6 Deadeye"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/R-6_Deadeye"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/r-6-deadeye.json"
---

# R-6 Deadeye

**分类：** 武器 (`weapons`) · **ID：** `r-6-deadeye`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/R-6_Deadeye

## 简介

The R-6 Deadeye is a lever-action Primary Marksman Rifle that trades rate-of-fire for Medium armor penetration, high damage and stagger force, requiring users to aim well and hit their targets the first time.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | marksman_rifle |
| 特性 ID (`traitIds`) | rounds-reload, medium-armor-penetrating |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | other |
| 射速（RPM） (`fireRateRpm`) | 100 |
| `dps` | 500 |
| 容量 (`capacity`) | 8 |
| 备用弹匣 (`spareMagazines`) | 60 |
| 初始弹匣 (`startingMagazines`) | 32 |
| `magazinesFromSupply` | 60 |
| `magazinesFromAmmoBox` | 30 |
| 后坐力 (`recoil`) | 82.5 |
| `horizontalRecoil` | 45 |
| `verticalRecoil` | 120 |
| `spread.horizontal` | 0.1 |
| `spread.vertical` | 0.1 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | rounds |
| 装填时间（秒） (`reloadTimeS`) | 6.4 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. R-6 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 300 |
| `damage.durable` | 100 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 20 |
| `projectile.initialVelocityMps` | 850 |
| `projectile.dragFactorPct` | 30 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 35 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Borderline Justice P1 |
| 战争债券 ID (`warbondId`) | borderline-justice |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/r-6-deadeye.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/R-6_Deadeye
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

