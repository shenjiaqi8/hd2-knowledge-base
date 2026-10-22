---
id: "p-40-k-bolt-pistol"
name: "P/40-K Bolt Pistol"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/P/40-K_Bolt_Pistol"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/p-40-k-bolt-pistol.json"
---

# P/40-K Bolt Pistol

**分类：** 武器 (`weapons`) · **ID：** `p-40-k-bolt-pistol`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/P/40-K_Bolt_Pistol

## 简介

The P/40-K Bolt Pistol is a Secondary Pistol that fires large caliber rounds with massive recoil.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | secondary |
| 子类别 (`subcategory`) | special |
| 特性 ID (`traitIds`) | heavy-armor-penetrating, explosive, one-handed |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | semi |
| 射速（RPM） (`fireRateRpm`) | 150 |
| `dps` | 1250 |
| 容量 (`capacity`) | 6 |
| 备用弹匣 (`spareMagazines`) | 4 |
| 初始弹匣 (`startingMagazines`) | 3 |
| `magazinesFromSupply` | 6 |
| `magazinesFromAmmoBox` | 3 |
| 后坐力 (`recoil`) | 325 |
| `horizontalRecoil` | 150 |
| `verticalRecoil` | 500 |
| `spread.horizontal` | 2 |
| `spread.vertical` | 2 |
| `sway` | 1 |
| `ergonomics` | 30 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.45 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 1.3 |


## 攻击模式、伤害与穿甲

### 1. P/40-K P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 325 |
| `damage.durable` | 115 |
| `damage.type` | Ballistic |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 100 |
| `projectile.initialVelocityMps` | 350 |
| `projectile.dragFactorPct` | 0 |
| `projectile.gravityFactorPct` | 30 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 20 |
| `forces.stagger` | 35 |
| `forces.push` | 15 |


### 2. P/40-K P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 175 |
| `damage.durable` | 175 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 1 |
| `area.outerRadiusM` | 3.5 |
| `area.shockwaveRadiusM` | 5 |
| `forces.demolition` | 10 |
| `forces.stagger` | 35 |
| `forces.push` | 5 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Castellan’s Creed |
| 战争债券 ID (`warbondId`) | castellans-creed |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 50 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/p-40-k-bolt-pistol.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/P/40-K_Bolt_Pistol
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

