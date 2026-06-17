# EEM_ABN_INDEX

> This table is used to log the LMRP responses to an ABN check

**Description:** EEM_ABN_INDEX  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_CHECK_ID` | DOUBLE | NOT NULL | FK→ | ABN Check Identifier. A FK back tot he EEM_ABN_CHECK table. Part of the primary key of this table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HIGH_STATUS_CD` | DOUBLE | NOT NULL | FK→ | High Status Code |
| 9 | `HIGH_STATUS_MEANING` | VARCHAR(12) |  |  | High Status Meaning |
| 10 | `INDEX_SEQ_NBR` | DOUBLE | NOT NULL |  | A sequence number. Part of the primary key of this table. |
| 11 | `KEY_FIELD` | DOUBLE | NOT NULL |  | Key Field |
| 12 | `MED_STATUS_CD` | DOUBLE | NOT NULL | FK→ | Medium Status Code |
| 13 | `MED_STATUS_MEANING` | VARCHAR(12) |  |  | Medium Status Meaning |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABN_CHECK_ID` | [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `ABN_CHECK_ID` |
| `HIGH_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `MED_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

