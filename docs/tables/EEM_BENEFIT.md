# EEM_BENEFIT

> EEM Benefits

**Description:** EEM Benefit  
**Table type:** REFERENCE  
**Primary key:** `EEM_BENEFIT_ID`  
**Columns:** 32  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Benefit Type Code |
| 7 | `COST_PER_BED_DAY` | DOUBLE |  |  | Cost per bed day |
| 8 | `COST_PER_CASE` | DOUBLE |  |  | Cost per case |
| 9 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Data Type Code. |
| 10 | `DATE_VALUE` | DATETIME |  |  | Date Value |
| 11 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 12 | `DOUBLE_VALUE` | DOUBLE | NOT NULL |  | Double Value |
| 13 | `EEM_BENEFIT_ID` | DOUBLE | NOT NULL | PK | EEM Benefit Identifier |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `INFO_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary Key to LONG_TEXT_REFERENCE table |
| 16 | `LOCAL_RVU` | DOUBLE |  |  | Local Relative Value Unit stored against HRG |
| 17 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary Key to LONG_TEXT_REFERENCE table |
| 18 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 19 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 20 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 21 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 22 | `NATIONAL_RVU` | DOUBLE |  |  | National Relative Value Unit stored against HRG |
| 23 | `NBR_PAT_AGREED` | DOUBLE |  |  | Number of patients agreed |
| 24 | `RVU_AMNT` | DOUBLE |  |  | Relative Value Unit stored against HRG |
| 25 | `STRING_VALUE` | VARCHAR(255) |  |  | String Value |
| 26 | `UNITS_CD` | DOUBLE | NOT NULL | FK→ | Units Of Measure Code |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VARIANCE_LEVEL` | DOUBLE |  |  | Variance Level |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EEM_BENEFIT_ALLOC](EEM_BENEFIT_ALLOC.md) | `EEM_BENEFIT_ID` |
| [EEM_BENEFIT_QUAL](EEM_BENEFIT_QUAL.md) | `BENEFIT_ID` |
| [EEM_BENEFIT_RELTN](EEM_BENEFIT_RELTN.md) | `EEM_BENEFIT_ID` |

