---
id: "gl-15-evictor"
name: "GL-15 Evictor"
collection: "weapons"
aliases: []
status: "released"
data_version: "2026-10-21.fb36bb01"
wiki_flags: ["potentially_outdated"]
wiki_url: "https://helldivers.wiki.gg/wiki/GL-15_Evictor"
source_api_url: "https://helldivers-api.dionatha.com.br/v1/weapons/gl-15-evictor.json"
---

# GL-15 Evictor

**分类：** 武器 (`weapons`) · **ID：** `gl-15-evictor`

> ⚠️ 原始 Wiki 数据被标记为 `potentially_outdated`，数值请结合最新补丁核对。

**Wiki 原始词条：** https://helldivers.wiki.gg/wiki/GL-15_Evictor

## 简介

GL-15 Evictor is a Explosive primary weapon that fires high-damaging grenades that explode upon impact. The pump handle chambers each round, similar to a pump-action shotgun.

## 主要属性

| 字段 | 数值 |
|---|---|
| 类别 (`category`) | primary |
| 子类别 (`subcategory`) | explosive |
| 特性 ID (`traitIds`) | medium-armor-penetrating, explosive, rounds-reload |


## 枪械属性

| 字段 | 数值 |
|---|---|
| `firingModes` | other |
| 射速（RPM） (`fireRateRpm`) | 60 |
| `dps` | 490 |
| 容量 (`capacity`) | 4 |
| 备用弹匣 (`spareMagazines`) | 32 |
| 初始弹匣 (`startingMagazines`) | 24 |
| `magazinesFromSupply` | 32 |
| `magazinesFromAmmoBox` | 16 |
| 后坐力 (`recoil`) | 82.5 |
| `horizontalRecoil` | 45 |
| `verticalRecoil` | 120 |
| `spread.horizontal` | 15 |
| `spread.vertical` | 12 |
| `sway` | 1 |
| `ergonomics` | 65 |
| `reloadKind` | rounds |
| 装填时间（秒） (`reloadTimeS`) | 2.67 |
| `reloadTimeUpgradedS` | — |
| `tacticalReloadTimeS` | — |


## 攻击模式、伤害与穿甲

### 1. GL-15 P（projectile）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 50 |
| `damage.durable` | 2 |
| `damage.type` | Ballistic |
| `penetration.direct` | medium |
| `penetration.slightAngle` | medium |
| `penetration.largeAngle` | medium |
| `penetration.extremeAngle` | unarmored |
| `projectile.pellets` | — |
| `projectile.massG` | 50 |
| `projectile.initialVelocityMps` | 100 |
| `projectile.dragFactorPct` | 120 |
| `projectile.gravityFactorPct` | 100 |
| `projectile.penetrationSlowdownPct` | 25 |
| `area` | — |
| `forces.demolition` | 10 |
| `forces.stagger` | 30 |
| `forces.push` | 10 |


### 2. GL-15 P IE（explosion）

| 字段 | 数值 |
|---|---|
| `damage.standard` | 440 |
| `damage.durable` | 440 |
| `damage.type` | Explosion |
| `penetration.direct` | — |
| `penetration.slightAngle` | — |
| `penetration.largeAngle` | — |
| `penetration.extremeAngle` | — |
| `projectile` | — |
| `area.innerRadiusM` | 2.25 |
| `area.outerRadiusM` | 5.5 |
| `area.shockwaveRadiusM` | 8 |
| `forces.demolition` | 30 |
| `forces.stagger` | 25 |
| `forces.push` | 30 |


## 获取方式

| 字段 | 数值 |
|---|---|
| `type` | warbond |
| `label` | Ironclad Democracy P3 |
| 战争债券 ID (`warbondId`) | ironclad-democracy |
| `page` | 3 |
| `cost.currency` | medals |
| `cost.amount` | 65 |
| `rotating` | — |


## 数据来源与许可

- 来源数据：[https://github.com/DionathaGoulart/Helldivers-api](https://github.com/DionathaGoulart/Helldivers-api)（基于 [The Helldivers Wiki](https://helldivers.wiki.gg/)）
- API 记录：https://helldivers-api.dionatha.com.br/v1/weapons/gl-15-evictor.json
- Wiki 词条：https://helldivers.wiki.gg/wiki/GL-15_Evictor
- 数据版本：`2026-10-21.fb36bb01`
- 许可：CC BY-NC-SA 4.0（以原项目和各 Wiki 页面实际许可为准）；非官方社区数据。

