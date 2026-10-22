---
id: "smg-flam-34-stoker"
name: "SMG/FLAM-34 Stoker"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/SMG/FLAM-34_Stoker"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/smg-flam-34-stoker.json"
---

# SMG/FLAM-34 Stoker

**分类：** 武器 (`weapons`) · **ID：** `smg-flam-34-stoker`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/SMG/FLAM-34_Stoker

## 简介

The SMG/FLAM-34 Stoker is a Primary Submachine Gun that comes equipped with an under-barrel flamethrower.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | submachine_gun |
| 特性 ID (`traitIds`) | light-armor-penetrating, one-handed, incendiary |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | — |
| 射速（RPM） (`fireRateRpm`) | 420 |
| `dps` | 910 |
| 容量 (`capacity`) | 45 |
| 备用弹匣 (`spareMagazines`) | 5 |
| 初始弹匣 (`startingMagazines`) | 3 |
| `magazinesFromSupply` | 5 |
| `magazinesFromAmmoBox` | 2 |
| 后坐力 (`recoil`) | 8.75 |
| `horizontalRecoil` | 7.5 |
| `verticalRecoil` | 10 |
| `spread.horizontal` | 5 |
| `spread.vertical` | 5 |
| `sway` | 1 |
| `ergonomics` | 60 |
| `reloadKind` | magazine |
| 装填时间（秒） (`reloadTimeS`) | 2.8 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | 1.73 |


## 攻击模式、伤害与穿甲

### 1. SMG/FLAM-34 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 130 |
| `damage.durable` | 30 |
| `damage.type` | Ballistic |
| `penetration.direct` | light |
| `penetration.slightAngle` | light |
| `penetration.largeAngle` | light |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 15 |
| `projectile.initialVelocityMps` | 285 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 15 |
| `forces.push` | 10 |


### 2. Underbarrel SMG/FLAM-34 STOKER 0 S（spray）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 2 |
| `damage.durable` | 2 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 5 |
| `forces.push` | 5 |


### 3. Fire（status）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 100 |
| `damage.durable` | 100 |
| `damage.type` | Fire |
| `penetration.direct` | heavy |
| `penetration.slightAngle` | heavy |
| `penetration.largeAngle` | heavy |
| `penetration.extremeAngle` | unarmored |
| `projectile` | — |
| `area` | — |
| `forces.demolition` | 0 |
| `forces.stagger` | 0 |
| `forces.push` | 0 |


### 4. Fire Panic（status）

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


### 5. FlamerSlowed（status）

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
| `label` | Entrenched Division P1 |
| 战争债券 ID (`warbondId`) | entrenched-division |
| `page` | 1 |
| `cost.currency` | medals |
| `cost.amount` | 35 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/smg-flam-34-stoker.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/SMG/FLAM-34_Stoker
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

