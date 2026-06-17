# RAD_WRKLST_CRIT

> This table models the criteria of a radiologists' reading worklist.

**Description:** Radiology Worklist Criteria  
**Table type:** REFERENCE  
**Primary key:** `RAD_WRKLST_CRIT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CRITERIA_CD` | DOUBLE | NOT NULL |  | The criteria that was specifically selected to be included or excluded on a worklist. |
| 3 | `INCLUDE_IND` | DOUBLE | NOT NULL |  | Used to indicate if the criteria values should be included or excluded. |
| 4 | `RAD_WRKLST_CRIT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RAD_WRKLST_CRIT table. |
| 5 | `RAD_WRKLST_DEF_ID` | DOUBLE | NOT NULL | FK→ | The radiology worklist that this criteria applies to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_WRKLST_DEF_ID` | [RAD_WRKLST_DEF](RAD_WRKLST_DEF.md) | `RAD_WRKLST_DEF_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_WRKLST_CRIT_VAL](RAD_WRKLST_CRIT_VAL.md) | `RAD_WRKLST_CRIT_ID` |

