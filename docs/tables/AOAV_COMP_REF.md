# AOAV_COMP_REF

> Table contains the reference data for an AOAV Component

**Description:** AOAV_COMPONENT_REFERENCE  
**Table type:** REFERENCE  
**Primary key:** `AOAV_COMP_REF_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state |
| 2 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value of AOAV Component |
| 3 | `AOAV_COMP_REF_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 4 | `AOAV_COMP_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that defines the type of aoav component (for example- high, low, median ) |
| 5 | `CALC_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that defines the type of calculation (for example- PI ) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AOAV_COMP_POINTS_REF](AOAV_COMP_POINTS_REF.md) | `AOAV_COMP_REF_ID` |
| [AOAV_OUTCOME_COMP](AOAV_OUTCOME_COMP.md) | `AOAV_COMP_REF_ID` |

