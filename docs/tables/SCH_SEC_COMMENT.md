# SCH_SEC_COMMENT

> Scheduling Security Comments

**Description:** Scheduling Security Comments  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 9 | `SEC_ACTION_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Security Action |
| 10 | `SEC_ACTION_MEANING` | VARCHAR(12) |  |  | Security Action Meaning |
| 11 | `SEC_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Security Types |
| 12 | `SEC_TYPE_MEANING` | VARCHAR(12) |  |  | Scheduling Security Type Meaning |
| 13 | `SUB_TEXT_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text sub-type. |
| 14 | `SUB_TEXT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text sub-type. |
| 15 | `TEXT_ID` | DOUBLE | NOT NULL | FK→ | Text Identifier |
| 16 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text type. |
| 17 | `TEXT_TYPE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text type. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEC_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SEC_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SUB_TEXT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `TEXT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

