---
id: "smg-72-pummeler"
name: "SMG-72 Pummeler"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SMG-72_Pummeler"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/smg-72-pummeler.json"
---

# SMG-72 Pummeler

**分类：** 武器 (`weapons`) · **ID：** `smg-72-pummeler`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SMG-72_Pummeler

## 简介

The SMG-72 Pummeler is a Primary Submachine Gun that fires concussive rounds that can stun enemies.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | submachine_gun |
| 特性 ID (`traitIds`) | light-armor-penetrating, one-handed |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | auto, burst, semi |
| 射速（RPM） (`fireRateRpm`) | 475 |
| `dps` | 672.91 |
| 容量 (`capacity`) | 45 |
| 备用弹匣 (`spareMagazines`) | 7 |
| 初始弹匣 (`startingMagazines`) | 5 |
| `magazinesFromSupply` | 7 |
| `magazinesFromAmmoBox` | 3 |
| 后坐力 (`recoil`) | 8.75 |
| `horizontalRecoil` | 7.5 |
| `verticalRecoil` | 10 |
| `spread.horizontal` | 5 |
| `spread.vertical` | 5 |
| `sway` | 1 |
| `ergonomics` | 90 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.8 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. SMG-72 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 85 |
| `damage.durable` | 17 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 15 |
| `projectile.initialVelocityMps` | 210 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 15 |
| `forces.push` | 5 |


### 2. Stun Medium（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | — |
| `damage.durable` | — |
| `damage.type` | — |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | — |
| `forces.stagger` | — |
| `forces.push` | — |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Polar Patriots P2 |
| 战争债券 ID (`warbondId`) | polar-patriots |
| `page` | 2 |
| `cost.currency` | medals |
| `cost.amount` | 60 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/smg-72-pummeler.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SMG-72_Pummeler
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

