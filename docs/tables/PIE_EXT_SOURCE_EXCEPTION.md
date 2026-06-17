# PIE_EXT_SOURCE_EXCEPTION

> This table will store exceptions on sources

**Description:** PIE External Exception  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_EXT_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Child External Source info Identifier |
| 2 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Exception Type Code from code set |
| 3 | `PARENT_EXT_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Parent External Source Identifier |
| 4 | `PIE_EXT_SOURCE_EXCEPTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_EXT_SOURCE_ID` | [PIE_EXT_SOURCE](PIE_EXT_SOURCE.md) | `PIE_EXT_SOURCE_ID` |
| `PARENT_EXT_SOURCE_ID` | [PIE_EXT_SOURCE](PIE_EXT_SOURCE.md) | `PIE_EXT_SOURCE_ID` |

