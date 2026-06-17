# SN_RPT_SECT_REF

> Contains the section information for a report. This includes the section type, sequence, and default display.

**Description:** SN_RPT_SECT_REF  
**Table type:** REFERENCE  
**Primary key:** `RPT_SECT_REF_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The default display of this report section. |
| 2 | `ORDER_SEQ` | DOUBLE | NOT NULL |  | Contains the section sequence for this report and section type. |
| 3 | `RPT_SECT_REF_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 4 | `RPT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of report that this section belongs to. |
| 5 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of section. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_RPT_FIELD_REF](SN_RPT_FIELD_REF.md) | `RPT_SECT_REF_ID` |

