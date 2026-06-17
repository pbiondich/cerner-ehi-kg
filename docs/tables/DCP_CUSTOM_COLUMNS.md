# DCP_CUSTOM_COLUMNS

> This table holds the custom column informaiton that is used within PowerChart

**Description:** DCP CUSTOM COLUMNS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAPTION` | VARCHAR(40) | NOT NULL |  | This fields holds the custom defined caption for a column that has been changed by an end user. |
| 2 | `CUSTOM_COLUMN_CD` | DOUBLE | NOT NULL |  | This is the unique identifier to the column from codeset 6023 |
| 3 | `CUSTOM_COLUMN_MEANING` | VARCHAR(12) | NOT NULL |  | This is the meaning of the custom column code |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | This is the code_value from codeset 88 for which the record is written. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is an identifier that maps to the prsnl table for which this record is written. |
| 6 | `SEQUENCE_IND` | DOUBLE | NOT NULL |  | This is used to identify which order the columns listed on this table go when displaying the information on one of the PC spreadsheets. |
| 7 | `SPREAD_COLUMN_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the table. |
| 8 | `SPREAD_TYPE_CD` | DOUBLE | NOT NULL |  | This maps to the value from codeset 6022 to identify which type of spreadsheet within PowerChart is going to use this defined custom column information. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

