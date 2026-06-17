# LH_CNT_WL_FACTOR_H

> This table store historical data the from LH_CNT_WL_FACTOR table.

**Description:** LH_CNT_WL_FACTOR_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLOUD_IDENT` | VARCHAR(255) |  |  | Unique identifier for cloud payloads indicating a factor value. Used for troubleshooting |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FACTOR_TXT` | VARCHAR(255) |  |  | Factor text value. Not used by all risk factor types. |
| 6 | `FACTOR_TYPE_CD` | DOUBLE | NOT NULL |  | Factor type. Ex. AMI |
| 7 | `FACTOR_VALUE` | DOUBLE | NOT NULL |  | Factor numeric value. Not used by all risk factor types. |
| 8 | `LH_CNT_WL_FACTOR_H_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 9 | `LH_CNT_WL_FACTOR_ID` | DOUBLE | NOT NULL |  | FK to parent row. |
| 10 | `LH_CNT_WL_POP_ID` | DOUBLE | NOT NULL |  | Foreign key of the associated population member. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

