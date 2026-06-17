# AOAV_COMP_CHILD_REF

> This table stores the reference data build for a child component (such as SBP, DBP)

**Description:** AOAV_COMPONENT_CHILD_REFERENCE  
**Table type:** REFERENCE  
**Primary key:** `AOAV_COMP_CHILD_REF_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state |
| 2 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value of the child component (for e.g. SBP, DBP) |
| 3 | `AOAV_COMP_CHILD_REF_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `AOAV_COMP_PARENT_CD` | DOUBLE | NOT NULL |  | Code value of the parent component (for e.g. MAP) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AOAV_EVENT_CHILD](AOAV_EVENT_CHILD.md) | `AOAV_COMP_CHILD_REF_ID` |

