# WORKLOAD_GROUP

> Holds the relationships between the standards, books, chapters, and sections within workload standards.

**Description:** Workload Group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BOOK_CD` | DOUBLE | NOT NULL |  | The code value from codeset 15230 that represents the book that this code is within. |
| 6 | `CHAPTER_CD` | DOUBLE | NOT NULL |  | The code value from codeset 15230 that represents the book that this code is within. |
| 7 | `SECTION_CD` | DOUBLE | NOT NULL |  | The code value from codeset 15230 that represents the book that this code is within. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WORKLOAD_CODE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the wrokload_code table. |
| 14 | `WORKLOAD_GROUP_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the workload_group table. It is an internal system assigned number. |
| 15 | `WORKLOAD_STANDARD_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the workload_standard table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLOAD_CODE_ID` | [WORKLOAD_CODE](WORKLOAD_CODE.md) | `WORKLOAD_CODE_ID` |
| `WORKLOAD_STANDARD_ID` | [WORKLOAD_STANDARD](WORKLOAD_STANDARD.md) | `WORKLOAD_STANDARD_ID` |

