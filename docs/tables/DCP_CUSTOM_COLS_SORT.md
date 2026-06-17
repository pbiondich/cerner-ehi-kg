# DCP_CUSTOM_COLS_SORT

> This table holds the sort dialog informaiton that is used within PowerChart

**Description:** DCP CUSTOM COLS SORT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_CD` | DOUBLE | NOT NULL |  | This is the unique identifier to the column from codeset 6023Column |
| 2 | `COLUMN_DESCRIPTION` | VARCHAR(12) |  |  | displays the cdfMeaning of the column_cd if it is a custom sortColumn |
| 3 | `COLUMN_SORT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the table.Column |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | This is the code_value from codeset 88 for which the record is written.Column |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is an identifier that maps to the prsnl table for which this record is written. |
| 6 | `SORT_DIRECTION_IND` | DOUBLE |  |  | Tells whether the sort is ascending or descending |
| 7 | `SORT_LEVEL_FLAG` | DOUBLE |  |  | Tells if the sort is primary, secondary, or tertiaryColumn |
| 8 | `SORT_TYPE_FLAG` | DOUBLE |  |  | Tells if it is a default, rounds, or custom sortColumn |
| 9 | `SPREAD_TYPE_CD` | DOUBLE | NOT NULL |  | This maps to the value from codeset 6022 to identify which type of spreadsheet within PowerChart is going to use this sort information. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

