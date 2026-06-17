# SN_ACUITY_LEVEL

> The times associated with acuity levels, i.e. acuity 1, 2,3,4 Start/Stop Time etc.

**Description:** SurgiNet Acuity Levels  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACUITY_LEVEL_CD` | DOUBLE | NOT NULL |  | Indicates the Acuity Level such as ACUITY Level I, II etc? |
| 3 | `ACUITY_LEVEL_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table. This value is unique for all versions of a given acuity level for a case. |
| 4 | `ACUITY_START_DT_TM` | DATETIME |  |  | The date and time associated with this Acuity start date and time. |
| 5 | `ACUITY_STOP_DT_TM` | DATETIME |  |  | The date and time associated with this Acuity stop date and time. |
| 6 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the segment_header table indicating the status of this segment, i.e. Accessed, Discontinued, etc. |
| 7 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case Identifier |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

