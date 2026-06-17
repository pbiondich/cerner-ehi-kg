# SN_RPT

> Contains all SurgiNet client built reports. This stores various information about paper size, orientation, margins, surgical area, and the name of the report.

**Description:** Contains all SurgiNet client built reports.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUTTON_SEQ` | DOUBLE |  |  | identifies the report as having a shortcut button and in which sequence to display the up to five definable buttons. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was first inserted. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that caused the row to be created in the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The display name of the report. |
| 7 | `FORMAT_FLAG` | DOUBLE | NOT NULL |  | FUTURE:: Will indicate the type of file format that is generated for this report. |
| 8 | `LANDSCAPE_IND` | DOUBLE | NOT NULL |  | Determines if the report prints in landscape mode or not. |
| 9 | `NUM_COLS` | DOUBLE | NOT NULL |  | The number of printable columns that are on the report's paper. |
| 10 | `NUM_ROWS` | DOUBLE | NOT NULL |  | The number of printable rows that are on the report's paper. |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization id refers to the ID of the organization to which the report belongs to |
| 12 | `OWNER_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) assigned to own the report. |
| 13 | `PAPER_SOURCE` | VARCHAR(20) | NOT NULL |  | The display value of the paper source used to default the number of rows and columns for this report. |
| 14 | `PRINT_BARCODE_IND` | DOUBLE | NOT NULL |  | ** NOT USED - Logically Obsolete ** Indicates whether the barcode should be printed to case picklist report or not |
| 15 | `RPT_ID` | DOUBLE | NOT NULL |  | Primary KeyColumn |
| 16 | `RPT_KEY` | VARCHAR(32) | NOT NULL |  | The unique area key for this report. Used primarily for operations jobs to determine which report to run. |
| 17 | `RPT_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of report this is. |
| 18 | `START_COL` | DOUBLE | NOT NULL |  | The column number on the page to start printing on. |
| 19 | `START_ROW` | DOUBLE | NOT NULL |  | The row number on the page to start printing on. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OWNER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

