# OMF_GRID_COLUMN

> Columns to display on a PowerVision grid

**Description:** Columns to display on a PowerVision grid.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRID_CD` | DOUBLE | NOT NULL | FK→ | Code value for an indicator. The cdf_meaning is 'GRID'. Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `GRID_COLUMN_CD` | DOUBLE | NOT NULL |  | Code value for an indicator or vo_type_cd. The cdf_meaning is 'INDICATOR'. Other codesets can be used besides 14265 depending on the team defining the value. |
| 3 | `GRID_COLUMN_HDG` | VARCHAR(50) |  |  | Column heading to display in grid. |
| 4 | `GRID_COLUMN_SEQ` | DOUBLE | NOT NULL |  | The order in which columns appear in the grid. |
| 5 | `GRID_VO_IND` | DOUBLE |  |  | Is the grid_column_cd a view option? |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GRID_CD` | [OMF_GRID](OMF_GRID.md) | `GRID_CD` |

