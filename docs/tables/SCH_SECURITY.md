# SCH_SECURITY

> Scheduling Security

**Description:** Scheduling Security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 44

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
| 7 | `DATA1_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling data source. |
| 8 | `DATA1_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 9 | `DATA2_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling data source. |
| 10 | `DATA2_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 11 | `DATA3_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling data source. |
| 12 | `DATA3_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 13 | `DISPLAY1_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 14 | `DISPLAY1_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID1 |
| 15 | `DISPLAY1_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID1 |
| 16 | `DISPLAY2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 17 | `DISPLAY2_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID2 |
| 18 | `DISPLAY2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID2 |
| 19 | `DISPLAY3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 20 | `DISPLAY3_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID3 |
| 21 | `DISPLAY3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID3 |
| 22 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 23 | `LOCK_ID` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling lock. |
| 24 | `LOCK_MEANING` | VARCHAR(12) |  |  | The 12-character meaning corresponding to the scheduling lock. |
| 25 | `LOCK_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the scheduling lock. This is the table on which the scheduling lock is defined. |
| 26 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 27 | `PARENT1_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 28 | `PARENT1_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT1_ID |
| 29 | `PARENT1_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT1_ID |
| 30 | `PARENT2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 31 | `PARENT2_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT2_ID |
| 32 | `PARENT2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT2_ID |
| 33 | `PARENT3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 34 | `PARENT3_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT3_ID |
| 35 | `PARENT3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT3_ID |
| 36 | `SECURITY_ID` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling security record. The record is used to secure an action for a object. |
| 37 | `SEC_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling security type. The types determines the type of object that is being secured. |
| 38 | `SEC_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-character description corresponding to scheduling security type. |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA1_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA2_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA3_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SEC_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

