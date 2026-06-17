# SN_RPT_SECT

> Contains the descriptions, types, order, and sizes of sections in a report.

**Description:** SN RPT SECT  
**Table type:** REFERENCE  
**Primary key:** `RPT_SECT_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was first inserted. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the row to be created in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `DISPLAY_COLS` | DOUBLE | NOT NULL |  | The number of columns that are displayed in the section. |
| 6 | `DISPLAY_ROWS` | DOUBLE | NOT NULL |  | The number of rows that are displayed in the section. |
| 7 | `LINE_FLAG` | DOUBLE | NOT NULL |  | Determines what type of line is surrounding this section. |
| 8 | `ORDER_SEQ` | DOUBLE | NOT NULL |  | Contains the section sequence for this report and section type. |
| 9 | `RPT_ID` | DOUBLE | NOT NULL |  | Foreign key into the SN_RPT table to indicate which report this section belongs in. |
| 10 | `RPT_SECT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 11 | `RPT_SECT_REF_ID` | DOUBLE | NOT NULL |  | Foreign key into the SN_RPT_SECT_REF table to link to the reference section for this section. |
| 12 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of section. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_RPT_FIELD](SN_RPT_FIELD.md) | `RPT_SECT_ID` |

