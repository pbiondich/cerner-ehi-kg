# LH_CNT_WL_FACTOR

> This table stores the factors for the population rows found on the LH_CNT_WL_POP table.

**Description:** LH_CNT_WL_FACTOR  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_WL_FACTOR_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLOUD_IDENT` | VARCHAR(255) |  |  | Unique identifier for cloud payloads indicating a factor value. Used for troubleshooting. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FACTOR_TXT` | VARCHAR(255) |  |  | Factor text value. Not used by all risk factor types. |
| 6 | `FACTOR_TYPE_CD` | DOUBLE | NOT NULL |  | Factor type. Ex. AMI, PNEU, NEWS, PEWS, Sepsis, etc. |
| 7 | `FACTOR_VALUE` | DOUBLE | NOT NULL |  | Factor numeric value. Not used by all risk factor types. |
| 8 | `LH_CNT_WL_FACTOR_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `LH_CNT_WL_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key of the associated population member. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_WL_POP_ID` | [LH_CNT_WL_POP](LH_CNT_WL_POP.md) | `LH_CNT_WL_POP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_CNT_WL_FACTOR_DETAIL](LH_CNT_WL_FACTOR_DETAIL.md) | `LH_CNT_WL_FACTOR_ID` |
| [LH_CNT_WL_FACTOR_STATUS](LH_CNT_WL_FACTOR_STATUS.md) | `LH_CNT_WL_FACTOR_ID` |

