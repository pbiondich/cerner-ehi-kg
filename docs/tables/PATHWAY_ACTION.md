# PATHWAY_ACTION

> Pathway action Table

**Description:** Pathway action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_COMMENT` | VARCHAR(255) |  |  | Comments about the Action |
| 2 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time the action occurred |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who performed the action |
| 4 | `ACTION_REASON_CD` | DOUBLE | NOT NULL |  | Plan action reason |
| 5 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action code |
| 6 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 7 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the communication type of the order, e.g., written, verbal, etc. |
| 8 | `DURATION_QTY` | DOUBLE |  |  | Duration quantity before the action was applied. |
| 9 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Duration unit before the action was applied. |
| 10 | `END_DT_TM` | DATETIME |  |  | Pathway end date and time before the action was applied. |
| 11 | `END_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the phase end date time is estimated or precise. |
| 12 | `END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 13 | `PATHWAY_ACTION_ID` | DOUBLE | NOT NULL |  | Add as 3rd column of Primary Key. Can be 0 for rows prior to being added. This column, when populated, will be unique by itself. |
| 14 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the PATHWAY_CATALOG the action is associated with. |
| 15 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway the action is associated with |
| 16 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The Id of the ordering provider. |
| 17 | `PW_ACTION_SEQ` | DOUBLE | NOT NULL |  | Sequence of the action |
| 18 | `PW_STATUS_CD` | DOUBLE | NOT NULL |  | Status code of the pathway |
| 19 | `START_DT_TM` | DATETIME |  |  | Pathway start date and time before the action was applied. |
| 20 | `START_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the phase start date time is estimated or precise. |
| 21 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

