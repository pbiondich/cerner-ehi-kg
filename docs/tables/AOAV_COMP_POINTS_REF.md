# AOAV_COMP_POINTS_REF

> This table stores the points for different ranges for each component contributing to a score

**Description:** AOAV_COMPONENT_POINTS_REFERENCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AOAV_COMP_POINTS_REF_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `AOAV_COMP_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique number that identifies an AOAV Component |
| 4 | `COMP_POINTS` | DOUBLE |  |  | Points for the component that contribute to a score |
| 5 | `LIMIT_FLAG` | DOUBLE | NOT NULL |  | Flag values for the type of limit (0-None, 1-Upper only, 2-lower only, 3-both) |
| 6 | `LOWER_LIMIT` | DOUBLE | NOT NULL |  | Lower limit for the value range |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPPER_LIMIT` | DOUBLE | NOT NULL |  | Upper limit for the value range |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AOAV_COMP_REF_ID` | [AOAV_COMP_REF](AOAV_COMP_REF.md) | `AOAV_COMP_REF_ID` |

