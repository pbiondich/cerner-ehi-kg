# SN_RPT_DEST

> This table holds the printer queue and number of copies that should be printed of each report.

**Description:** This table holds the printer information for each of SurgiNet's reports.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was first inserted. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the row to be created in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The display name of the print queue. |
| 6 | `NUM_COPIES` | DOUBLE | NOT NULL |  | The number of copies that is to printed to this print queue for this report. |
| 7 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key into the OUTPUT_DEST table to indicate which printer queue this row belongs to. |
| 8 | `RPT_DEST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 9 | `RPT_FILTER_GRP_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key into the SN_RPT_FILTER_GRP table. |
| 10 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of output destination this is. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `RPT_FILTER_GRP_ID` | [SN_RPT_FILTER_GRP](SN_RPT_FILTER_GRP.md) | `RPT_FILTER_GRP_ID` |

